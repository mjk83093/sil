#!/usr/bin/env bash
# name: validator.sh
# Purpose: Read-only safety validator for forked repo setup (origin/upstream protection).
# Usage:
#   ./validator.sh [--expected-origin-url git@github.com:USER/REPO.git] [--expected-origin-user USER] [--expected-repo REPO]
# Examples:
#   ./validator.sh
#   ./validator.sh --expected-origin-user=mjk83093 --expected-repo=sil
# Notes: This script is read-only and will not modify remotes or hooks.

set -euo pipefail

EXPECTED_ORIGIN_URL=""
EXPECTED_ORIGIN_USER=""
EXPECTED_REPO=""
ALLOW_UPSTREAM_PUSH=0

while [ $# -gt 0 ]; do
  case "$1" in
    --expected-origin-url) EXPECTED_ORIGIN_URL="$2"; shift 2;;
    --expected-origin-user) EXPECTED_ORIGIN_USER="$2"; shift 2;;
    --expected-repo) EXPECTED_REPO="$2"; shift 2;;
    --allow-upstream-push) ALLOW_UPSTREAM_PUSH=1; shift ;;
    -h|--help) echo "Usage: $0 [--expected-origin-url URL] [--expected-origin-user USER] [--expected-repo REPO]"; exit 0;;
    *) echo "Unknown arg: $1"; exit 2;;
  esac
done

err() { printf "  [FAIL] %s\n" "$1"; }
ok()  { printf "  [PASS] %s\n" "$1"; }
info(){ printf "  [INFO] %s\n" "$1"; }

# Ensure we're inside a git repo
if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Error: not inside a git repository."
  exit 2
fi

echo "Validator: checking repository safety (read-only checks)"
echo

# 1) remotes
echo "1) Remotes"
REMOTE_LIST="$(git remote -v)"
echo "$REMOTE_LIST" | sed 's/^/    /'
echo

# Check origin present
if git remote | grep -q '^origin$'; then
  ok "origin remote exists"
  ORIGIN_FETCH=$(git remote get-url origin 2>/dev/null || true)
  ORIGIN_PUSH=$(git remote get-url --push origin 2>/dev/null || true)
  info "origin fetch: $ORIGIN_FETCH"
  info "origin push:  $ORIGIN_PUSH"
else
  err "origin remote is missing"
fi
echo

# Check upstream present
if git remote | grep -q '^upstream$'; then
  ok "upstream remote exists"
  UPSTREAM_FETCH=$(git remote get-url upstream 2>/dev/null || true)
  # some git versions support get-url --push
  if UPSTREAM_PUSH=$(git remote get-url --push upstream 2>/dev/null || true); then :; fi
  # fallback parse remote -v
  if [ -z "${UPSTREAM_PUSH:-}" ]; then
    UPSTREAM_PUSH=$(git remote -v | awk '/^upstream[[:space:]]/ && /push/ {print $2; exit}')
  fi
  info "upstream fetch: $UPSTREAM_FETCH"
  info "upstream push:  ${UPSTREAM_PUSH:-<none>}"
else
  err "upstream remote is missing"
fi
echo

# 2) upstream push safety
echo "2) Upstream push-url safety"
unsafe_upstream=0
if [ -n "${UPSTREAM_PUSH:-}" ]; then
  # If upstream push URL contains the original repo address (common unsafe case)
  if printf "%s" "${UPSTREAM_PUSH}" | grep -qE 'agent0ai/agent-zero|github.com[:/].*agent0ai'; then
    unsafe_upstream=1
    err "upstream push URL appears to point to the original repo: ${UPSTREAM_PUSH}"
  else
    # acceptable values include 'no_push' or blank or some invalid URL
    if [ "$UPSTREAM_PUSH" = "no_push" ] || [ -z "$UPSTREAM_PUSH" ]; then
      ok "upstream push URL is non-writable (set to '$UPSTREAM_PUSH')"
    else
      if [ $ALLOW_UPSTREAM_PUSH -eq 1 ]; then
        ok "upstream push URL is set (but allow flag enabled): ${UPSTREAM_PUSH}"
      else
        info "upstream push URL is set to: ${UPSTREAM_PUSH}"
        info "This may allow accidental pushes to upstream unless set to a harmless value (e.g. 'no_push')."
      fi
    fi
  fi
else
  ok "no upstream push URL detected (safe)"
fi
echo

# 3) current branch and tracking
echo "3) Current branch & tracking"
CURRENT_BRANCH=$(git symbolic-ref --quiet --short HEAD 2>/dev/null || git rev-parse --short HEAD)
info "current branch: $CURRENT_BRANCH"

# Does branch have an upstream?
if git rev-parse --abbrev-ref --symbolic-full-name "@{u}" >/dev/null 2>&1; then
  BR_UPSTREAM=$(git rev-parse --abbrev-ref --symbolic-full-name "@{u}" 2>/dev/null || true)
  ok "current branch tracks $BR_UPSTREAM"
else
  warn_msg="current branch does not have an upstream (no tracking branch configured)"
  err "$warn_msg"
fi

# If expected origin user/repo provided, check branch tracks origin/<branch>
if [ -n "$EXPECTED_ORIGIN_USER" ] && [ -n "$EXPECTED_REPO" ]; then
  expected_origin_url_ssh="git@github.com:${EXPECTED_ORIGIN_USER}/${EXPECTED_REPO}.git"
  expected_origin_url_https="https://github.com/${EXPECTED_ORIGIN_USER}/${EXPECTED_REPO}.git"
  if [ "$ORIGIN_PUSH" = "$expected_origin_url_ssh" ] || [ "$ORIGIN_FETCH" = "$expected_origin_url_ssh" ] || \
     [ "$ORIGIN_PUSH" = "$expected_origin_url_https" ] || [ "$ORIGIN_FETCH" = "$expected_origin_url_https" ]; then
    ok "origin matches expected ${EXPECTED_ORIGIN_USER}/${EXPECTED_REPO}"
  else
    info "origin does not match expected ${EXPECTED_ORIGIN_USER}/${EXPECTED_REPO} (origin: ${ORIGIN_FETCH})"
  fi
elif [ -n "$EXPECTED_ORIGIN_URL" ]; then
  if [ "$ORIGIN_PUSH" = "$EXPECTED_ORIGIN_URL" ] || [ "$ORIGIN_FETCH" = "$EXPECTED_ORIGIN_URL" ]; then
    ok "origin matches expected URL"
  else
    info "origin does not match expected URL (origin: ${ORIGIN_FETCH})"
  fi
fi
echo

# 4) push.default
echo "4) push.default"
LOCAL_PUSH_DEFAULT=$(git config --local push.default || true)
GLOBAL_PUSH_DEFAULT=$(git config --global push.default || true)
if [ -n "$LOCAL_PUSH_DEFAULT" ]; then
  info "local push.default = $LOCAL_PUSH_DEFAULT"
else
  info "local push.default is not set"
fi
if [ "$LOCAL_PUSH_DEFAULT" = "simple" ]; then
  ok "local push.default is 'simple' (recommended)"
else
  if [ -z "$LOCAL_PUSH_DEFAULT" ]; then
    info "consider setting local push.default to 'simple' to avoid accidental pushes (git config --local push.default simple)"
  else
    info "local push.default is '$LOCAL_PUSH_DEFAULT' (consider 'simple')"
  fi
fi
echo

# 5) hooks: check for pre-push hook in .git/hooks or core.hooksPath
echo "5) Hooks"
HOOKS_PATH="$(git config core.hooksPath || echo .git/hooks)"
info "hooks path: $HOOKS_PATH"

PREPUSH_FOUND=0
if [ -f "$HOOKS_PATH/pre-push" ]; then
  PREPUSH_FOUND=1
  ok "pre-push hook exists at $HOOKS_PATH/pre-push"
  # Light content check for safety patterns
  if grep -qiE 'agent0ai/agent-zero|upstream' "$HOOKS_PATH/pre-push"; then
    ok "pre-push hook mentions upstream or agent0ai (likely blocks upstream pushes)"
  else
    info "pre-push hook exists but does not obviously reference upstream or the original repo"
  fi
else
  if [ -f ".git/hooks/pre-push" ]; then
    PREPUSH_FOUND=1
    ok "pre-push hook exists at .git/hooks/pre-push"
    if grep -qiE 'agent0ai/agent-zero|upstream' ".git/hooks/pre-push"; then
      ok "pre-push hook mentions upstream or agent0ai (likely blocks upstream pushes)"
    else
      info "pre-push hook exists but does not obviously reference upstream or the original repo"
    fi
  else
    err "no pre-push hook found in $HOOKS_PATH or .git/hooks"
  fi
fi
echo

# 6) Summary
echo "SUMMARY"
PASS=0
WARN=0
FAIL=0

# Evaluate states
if git remote | grep -q '^origin$'; then PASS=$((PASS+1)); else FAIL=$((FAIL+1)); fi
if git remote | grep -q '^upstream$'; then PASS=$((PASS+1)); else WARN=$((WARN+1)); fi

if [ "${unsafe_upstream:-0}" -eq 1 ]; then
  FAIL=$((FAIL+1))
else
  PASS=$((PASS+1))
fi

if git rev-parse --abbrev-ref --symbolic-full-name "@{u}" >/dev/null 2>&1; then PASS=$((PASS+1)); else WARN=$((WARN+1)); fi

if [ "$LOCAL_PUSH_DEFAULT" = "simple" ]; then PASS=$((PASS+1)); else WARN=$((WARN+1)); fi

if [ "$PREPUSH_FOUND" -eq 1 ]; then PASS=$((PASS+1)); else WARN=$((WARN+1)); fi

echo "  pass: $PASS, warn: $WARN, fail: $FAIL"
echo

if [ $FAIL -gt 0 ]; then
  echo "ACTION: Some critical checks failed. Fix the items marked [FAIL] before pushing to be safe."
  exit 3
elif [ $WARN -gt 0 ]; then
  echo "ACTION: Some checks need attention (warnings). Review the [INFO]/[FAIL] messages above and consider fixes."
  exit 1
else
  echo "ACTION: All checks passed. Your repo appears safely configured for the 'fork + upstream (fetch-only)' workflow."
  exit 0
fi