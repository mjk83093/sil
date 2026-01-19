"""
NEC 110.26 Working Space Validation
====================================
Deterministic validation of electrical equipment working space clearances.
All validation logic is pure Python - NO LLM involvement.

Reference: NEC 2023 Article 110.26
"""

from typing import List
from .validation_result import ValidationResult

WORKING_SPACE_DEPTH_TABLE: dict[str, dict[int, float]] = {
    "0-150V": {1: 3.0, 2: 3.0, 3: 3.0},
    "151-600V": {1: 3.0, 2: 3.5, 3: 4.0},
    "601-2500V": {1: 3.0, 2: 4.0, 3: 5.0},
}

def _get_voltage_category(voltage: int) -> str:
    """
    Determine voltage category for Table 110.26(A)(1) lookup.

    Args:
        voltage: Nominal voltage in volts

    Returns:
        Voltage category string for table lookup

    Raises:
        ValueError: If voltage is out of supported range
    """
    if voltage <= 0:
        raise ValueError(f"Voltage must be positive, got {voltage}")
    elif voltage <= 150:
        return "0-150V"
    elif voltage <= 600:
        return "151-600V"
    elif voltage <= 2500:
        return "601-2500V"
    else:
        raise ValueError(
            f"Voltage {voltage}V exceeds Table 110.26(A)(1) range (max 2500V)"
        )

def validate_working_space_depth(
    voltage: int, condition: int, actual_depth_ft: float
) -> ValidationResult:
    """
    Validate working space depth per NEC 110.26(A)(1).

    Working space depth is measured from the exposed live parts or from the
    enclosure front if live parts are enclosed.

    Args:
        voltage: Nominal voltage of equipment in volts
        condition: Working space condition (1, 2, or 3)
        actual_depth_ft: Actual working space depth in feet

    Returns:
        ValidationResult with PASS/FAIL status

    Example:
        >>> result = validate_working_space_depth(480, 2, 3.5)
        >>> result.status
        'PASS'
    """
    if condition not in (1, 2, 3):
        return ValidationResult(
            status="FAIL",
            message=f"Invalid condition {condition}. Must be 1, 2, or 3.",
            nec_reference="NEC 110.26(A)(1)",
            details={"condition": condition},
        )

    try:
        voltage_category = _get_voltage_category(voltage)
    except ValueError as e:
        return ValidationResult(
            status="FAIL",
            message=str(e),
            nec_reference="NEC 110.26(A)(1)",
            details={"voltage": voltage},
        )

    required_depth_ft = WORKING_SPACE_DEPTH_TABLE[voltage_category][condition]

    details = {
        "voltage": voltage,
        "voltage_category": voltage_category,
        "condition": condition,
        "required_depth_ft": required_depth_ft,
        "actual_depth_ft": actual_depth_ft,
    }

    if actual_depth_ft >= required_depth_ft:
        return ValidationResult(
            status="PASS",
            message=f"Working space depth {actual_depth_ft}' meets minimum {required_depth_ft}' "
            f"for {voltage_category} Condition {condition}",
            nec_reference="NEC 110.26(A)(1), Table 110.26(A)(1)",
            details=details,
        )
    else:
        return ValidationResult(
            status="FAIL",
            message=f"Working space depth {actual_depth_ft}' is less than required {required_depth_ft}' "
            f"for {voltage_category} Condition {condition}",
            nec_reference="NEC 110.26(A)(1), Table 110.26(A)(1)",
            details=details,
        )

def validate_working_space_width(
    equipment_width_in: float, actual_width_in: float
) -> ValidationResult:
    """
    Validate working space width per NEC 110.26(A)(2).

    Width of working space must be at least 30 inches or the width of the
    equipment, whichever is greater.

    Args:
        equipment_width_in: Width of equipment in inches
        actual_width_in: Actual working space width in inches

    Returns:
        ValidationResult with PASS/FAIL status

    Example:
        >>> result = validate_working_space_width(42, 48)
        >>> result.status
        'PASS'
    """
    MIN_WIDTH_IN = 30.0
    required_width_in = max(MIN_WIDTH_IN, equipment_width_in)

    details = {
        "equipment_width_in": equipment_width_in,
        "minimum_code_width_in": MIN_WIDTH_IN,
        "required_width_in": required_width_in,
        "actual_width_in": actual_width_in,
    }

    if actual_width_in >= required_width_in:
        return ValidationResult(
            status="PASS",
            message=f'Working space width {actual_width_in}" meets minimum {required_width_in}" '
            f'(equipment width: {equipment_width_in}", code minimum: {MIN_WIDTH_IN}")',
            nec_reference="NEC 110.26(A)(2)",
            details=details,
        )
    else:
        return ValidationResult(
            status="FAIL",
            message=f'Working space width {actual_width_in}" is less than required {required_width_in}" '
            f'(equipment width: {equipment_width_in}", code minimum: {MIN_WIDTH_IN}")',
            nec_reference="NEC 110.26(A)(2)",
            details=details,
        )

def validate_working_space_height(
    equipment_height_ft: float, actual_height_ft: float
) -> ValidationResult:
    """
    Validate working space height per NEC 110.26(A)(3).

    Height of working space must be at least 6.5 feet or the height of the
    equipment, whichever is greater.

    Args:
        equipment_height_ft: Height of equipment in feet
        actual_height_ft: Actual working space height (floor to ceiling) in feet

    Returns:
        ValidationResult with PASS/FAIL status

    Example:
        >>> result = validate_working_space_height(5.0, 8.0)
        >>> result.status
        'PASS'
    """
    MIN_HEIGHT_FT = 6.5
    required_height_ft = max(MIN_HEIGHT_FT, equipment_height_ft)

    details = {
        "equipment_height_ft": equipment_height_ft,
        "minimum_code_height_ft": MIN_HEIGHT_FT,
        "required_height_ft": required_height_ft,
        "actual_height_ft": actual_height_ft,
    }

    if actual_height_ft >= required_height_ft:
        return ValidationResult(
            status="PASS",
            message=f"Working space height {actual_height_ft}' meets minimum {required_height_ft}' "
            f"(equipment height: {equipment_height_ft}', code minimum: {MIN_HEIGHT_FT}')",
            nec_reference="NEC 110.26(A)(3)",
            details=details,
        )
    else:
        return ValidationResult(
            status="FAIL",
            message=f"Working space height {actual_height_ft}' is less than required {required_height_ft}' "
            f"(equipment height: {equipment_height_ft}', code minimum: {MIN_HEIGHT_FT}')",
            nec_reference="NEC 110.26(A)(3)",
            details=details,
        )

PROHIBITED_OBSTRUCTIONS = {
    "duct",
    "hvac_duct",
    "supply_duct",
    "return_duct",
    "pipe",
    "water_pipe",
    "gas_pipe",
    "drain_pipe",
    "sprinkler",
    "sprinkler_pipe",
    "cable_tray_non_electrical",
    "pneumatic_tube",
    "steam_pipe",
}

def validate_dedicated_space(obstructions: List[str]) -> ValidationResult:
    """
    Validate dedicated equipment space per NEC 110.26(E).

    The space above electrical equipment extending to the structural ceiling
    must be dedicated to the electrical installation. Foreign systems (piping,
    ducts, etc.) are not permitted in this space.

    Exception: Sprinkler protection is permitted if installed to protect the
    electrical equipment.

    Args:
        obstructions: List of obstruction types found in dedicated space
                     (e.g., ["duct", "pipe", "sprinkler"])

    Returns:
        ValidationResult with PASS/FAIL/WARN status

    Example:
        >>> result = validate_dedicated_space([])
        >>> result.status
        'PASS'
        >>> result = validate_dedicated_space(["hvac_duct"])
        >>> result.status
        'FAIL'
    """
    if not obstructions:
        return ValidationResult(
            status="PASS",
            message="Dedicated equipment space is clear of obstructions",
            nec_reference="NEC 110.26(E)(1)(a)",
            details={"obstructions": []},
        )

    normalized_obstructions = [obs.lower().strip() for obs in obstructions]

    violations = []
    warnings = []

    for obs in normalized_obstructions:
        if obs in PROHIBITED_OBSTRUCTIONS:
            if "sprinkler" in obs:
                warnings.append(obs)
            else:
                violations.append(obs)
        else:
            warnings.append(obs)

    details = {
        "obstructions": obstructions,
        "violations": violations,
        "warnings": warnings,
    }

    if violations:
        return ValidationResult(
            status="FAIL",
            message=f"Dedicated equipment space contains prohibited obstructions: {', '.join(violations)}. "
            f"Foreign systems not permitted per NEC 110.26(E)(1)(a).",
            nec_reference="NEC 110.26(E)(1)(a)",
            details=details,
        )
    elif warnings:
        return ValidationResult(
            status="WARN",
            message=f"Dedicated equipment space contains items requiring review: {', '.join(warnings)}. "
            f"Verify compliance with NEC 110.26(E) exceptions.",
            nec_reference="NEC 110.26(E)(1)(a)",
            details=details,
        )
    else:
        return ValidationResult(
            status="PASS",
            message="Dedicated equipment space is clear of prohibited obstructions",
            nec_reference="NEC 110.26(E)(1)(a)",
            details=details,
        )
