"""
Validation Result Data Class
============================
Standard result type for all NEC compliance validation functions.
"""

from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class ValidationResult:
    """
    Result of a NEC compliance validation check.

    Attributes:
        status: "PASS", "FAIL", or "WARN"
        message: Human-readable description of the result
        nec_reference: NEC article/section reference (e.g., "NEC 110.26(A)(1)")
        details: Additional context (values checked, thresholds, etc.)
    """

    status: str  # "PASS", "FAIL", "WARN"
    message: str
    nec_reference: str
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """Validate status is one of the allowed values."""
        valid_statuses = {"PASS", "FAIL", "WARN"}
        if self.status not in valid_statuses:
            raise ValueError(
                f"status must be one of {valid_statuses}, got '{self.status}'"
            )
