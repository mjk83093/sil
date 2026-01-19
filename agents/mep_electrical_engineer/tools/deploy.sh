#!/bin/bash
# PAI Agent Deployment Script - MEP Electrical Engineer
# Ensures modular structure is synced to global agents directory

AGENT_NAME="mep_electrical_engineer"
SRC_DIR="/home/mjk83/._proj/UB_BEB/agents/$AGENT_NAME"
DEST_DIR="/home/mjk83/sil/agents/$AGENT_NAME"

echo "Deploying $AGENT_NAME to PAI System..."

# Create structure
mkdir -p "$DEST_DIR"/{lib,tools,data,prompts}

# Sync files
cp -rv "$SRC_DIR"/* "$DEST_DIR"/

echo "Deployment complete."
ls -R "$DEST_DIR"
