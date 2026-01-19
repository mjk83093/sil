"""
NEC 250 Grounding Validation
============================
Deterministic validation of grounding electrode conductor (GEC) and
equipment grounding conductor (EGC) sizing.
All validation logic is pure Python - NO LLM involvement.

Reference: NEC 2023 Article 250, Tables 250.66 and 250.122
"""

from typing import Dict, Optional
from .validation_result import ValidationResult

AWG_TO_CMIL: Dict[str, int] = {
    "18": 1620,
    "16": 2580,
    "14": 4110,
    "12": 6530,
    "10": 10380,
    "8": 16510,
    "6": 26240,
    "4": 41740,
    "3": 52620,
    "2": 66360,
    "1": 83690,
    "1/0": 105600,
    "2/0": 133100,
    "3/0": 167800,
    "4/0": 211600,
    "250": 250000,
    "300": 300000,
    "350": 350000,
    "400": 400000,
    "500": 500000,
    "600": 600000,
    "700": 700000,
    "750": 750000,
    "800": 800000,
    "900": 900000,
    "1000": 1000000,
    "1100": 1100000,
    "1200": 1200000,
    "1500": 1500000,
    "1750": 1750000,
    "2000": 2000000,
}

TABLE_250_66_COPPER: Dict[str, str] = {
    "2_or_smaller": "8",
    "1_or_1/0": "6",
    "2/0_or_3/0": "4",
    "over_3/0_through_350": "2",
    "over_350_through_600": "1/0",
    "over_600_through_1100": "2/0",
    "over_1100": "3/0",
}

TABLE_250_66_ALUMINUM: Dict[str, str] = {
    "1/0_or_smaller": "6",
    "2/0_or_3/0": "4",
    "4/0_or_250": "2",
    "over_250_through_500": "1/0",
    "over_500_through_900": "2/0",
    "over_900_through_1750": "3/0",
    "over_1750": "250",
}

TABLE_250_122_COPPER: Dict[int, str] = {
    15: "14",
    20: "12",
    30: "10",
    40: "10",
    60: "10",
    100: "8",
    200: "6",
    300: "4",
    400: "3",
    500: "2",
    600: "1",
    800: "1/0",
    1000: "2/0",
    1200: "3/0",
    1600: "4/0",
    2000: "250",
    2500: "350",
    3000: "400",
    4000: "500",
    5000: "700",
    6000: "800",
}

TABLE_250_122_ALUMINUM: Dict[int, str] = {
    15: "12",
    20: "10",
    30: "8",
    40: "8",
    60: "8",
    100: "6",
    200: "4",
    300: "2",
    400: "1",
    500: "1/0",
    600: "2/0",
    800: "3/0",
    1000: "4/0",
    1200: "250",
    1600: "350",
    2000: "400",
    2500: "600",
    3000: "600",
    4000: "750",
    5000: "1000",
    6000: "1200",
}

def _normalize_conductor_size(size: str) -> str:
    """Normalize conductor size string for comparison."""
    return size.strip().upper().replace(" ", "").replace("AWG", "").replace("KCMIL", "")

def _get_cmil(size: str) -> Optional[int]:
    """Get circular mils for a conductor size."""
    normalized = _normalize_conductor_size(size)
    return AWG_TO_CMIL.get(normalized)

def _compare_conductor_sizes(size1: str, size2: str) -> int:
    """
    Compare two conductor sizes.

    Returns:
        -1 if size1 < size2 (size1 is smaller)
         0 if size1 == size2
         1 if size1 > size2 (size1 is larger)
    """
    cmil1 = _get_cmil(size1)
    cmil2 = _get_cmil(size2)

    if cmil1 is None or cmil2 is None:
        raise ValueError(f"Unknown conductor size: {size1 if cmil1 is None else size2}")

    if cmil1 < cmil2:
        return -1
    elif cmil1 > cmil2:
        return 1
    else:
        return 0

def _get_required_gec_size_copper(service_conductor_size: str) -> str:
    """
    Get required GEC size for copper service conductors per Table 250.66.

    Args:
        service_conductor_size: Service conductor size (e.g., "4/0", "500")

    Returns:
        Required GEC size
    """
    cmil = _get_cmil(service_conductor_size)
    if cmil is None:
        raise ValueError(f"Unknown service conductor size: {service_conductor_size}")

    if cmil <= AWG_TO_CMIL["2"]:  # 2 AWG or smaller
        return "8"
    elif cmil <= AWG_TO_CMIL["1/0"]:  # 1 or 1/0
        return "6"
    elif cmil <= AWG_TO_CMIL["3/0"]:  # 2/0 or 3/0
        return "4"
    elif cmil <= 350000:  # Over 3/0 through 350 kcmil
        return "2"
    elif cmil <= 600000:  # Over 350 through 600 kcmil
        return "1/0"
    elif cmil <= 1100000:  # Over 600 through 1100 kcmil
        return "2/0"
    else:  # Over 1100 kcmil
        return "3/0"

def _get_required_gec_size_aluminum(service_conductor_size: str) -> str:
    """
    Get required GEC size for aluminum service conductors per Table 250.66.

    Args:
        service_conductor_size: Service conductor size (e.g., "4/0", "500")

    Returns:
        Required GEC size (aluminum)
    """
    cmil = _get_cmil(service_conductor_size)
    if cmil is None:
        raise ValueError(f"Unknown service conductor size: {service_conductor_size}")

    if cmil <= AWG_TO_CMIL["1/0"]:  # 1/0 or smaller
        return "6"
    elif cmil <= AWG_TO_CMIL["3/0"]:  # 2/0 or 3/0
        return "4"
    elif cmil <= 250000:  # 4/0 or 250 kcmil
        return "2"
    elif cmil <= 500000:  # Over 250 through 500 kcmil
        return "1/0"
    elif cmil <= 900000:  # Over 500 through 900 kcmil
        return "2/0"
    elif cmil <= 1750000:  # Over 900 through 1750 kcmil
        return "3/0"
    else:  # Over 1750 kcmil
        return "250"

def validate_gec_size(
    service_conductor_size: str, gec_size: str, material: str = "copper"
) -> ValidationResult:
    """
    Validate grounding electrode conductor (GEC) sizing per NEC 250.66.

    The GEC connects the grounding electrode system to the service equipment
    grounding terminal. Size is based on the largest ungrounded service
    conductor or equivalent area for parallel conductors.

    Args:
        service_conductor_size: Size of service entrance conductors (e.g., "4/0", "500")
        gec_size: Actual GEC size installed (e.g., "2", "1/0")
        material: Conductor material ("copper" or "aluminum")

    Returns:
        ValidationResult with PASS/FAIL status

    Example:
        >>> result = validate_gec_size("4/0", "2", "copper")
        >>> result.status
        'PASS'
    """
    material_normalized = material.lower().strip()

    try:
        if material_normalized == "copper":
            required_gec = _get_required_gec_size_copper(service_conductor_size)
        elif material_normalized == "aluminum":
            required_gec = _get_required_gec_size_aluminum(service_conductor_size)
        else:
            return ValidationResult(
                status="FAIL",
                message=f"Invalid material '{material}'. Must be 'copper' or 'aluminum'.",
                nec_reference="NEC 250.66",
                details={"material": material},
            )
    except ValueError as e:
        return ValidationResult(
            status="FAIL",
            message=str(e),
            nec_reference="NEC 250.66, Table 250.66",
            details={"service_conductor_size": service_conductor_size},
        )

    try:
        comparison = _compare_conductor_sizes(gec_size, required_gec)
    except ValueError as e:
        return ValidationResult(
            status="FAIL",
            message=str(e),
            nec_reference="NEC 250.66, Table 250.66",
            details={"gec_size": gec_size},
        )

    details = {
        "service_conductor_size": service_conductor_size,
        "gec_size": gec_size,
        "required_gec_size": required_gec,
        "material": material_normalized,
    }

    if comparison >= 0:  # GEC is equal to or larger than required
        return ValidationResult(
            status="PASS",
            message=f"GEC size {gec_size} AWG meets minimum {required_gec} AWG "
            f"for {service_conductor_size} service conductors ({material_normalized})",
            nec_reference="NEC 250.66, Table 250.66",
            details=details,
        )
    else:
        return ValidationResult(
            status="FAIL",
            message=f"GEC size {gec_size} AWG is undersized. Minimum {required_gec} AWG required "
            f"for {service_conductor_size} service conductors ({material_normalized})",
            nec_reference="NEC 250.66, Table 250.66",
            details=details,
        )

def _get_required_egc_size(ocpd_rating: int, material: str) -> Optional[str]:
    """
    Get required EGC size from Table 250.122.

    Args:
        ocpd_rating: OCPD rating in amps
        material: "copper" or "aluminum"

    Returns:
        Required EGC size, or None if OCPD rating not in table
    """
    table = TABLE_250_122_COPPER if material == "copper" else TABLE_250_122_ALUMINUM

    applicable_ratings = sorted(table.keys())

    for rating in applicable_ratings:
        if ocpd_rating <= rating:
            return table[rating]

    return table[applicable_ratings[-1]]

def validate_egc_size(
    ocpd_rating: int, egc_size: str, material: str = "copper"
) -> ValidationResult:
    """
    Validate equipment grounding conductor (EGC) sizing per NEC 250.122.

    The EGC provides a low-impedance path for fault current to facilitate
    operation of overcurrent protective devices. Size is based on the
    rating of the overcurrent device protecting the circuit.

    Args:
        ocpd_rating: Rating of overcurrent protective device in amps
        egc_size: Actual EGC size installed (e.g., "10", "6")
        material: Conductor material ("copper" or "aluminum")

    Returns:
        ValidationResult with PASS/FAIL status

    Example:
        >>> result = validate_egc_size(100, "8", "copper")
        >>> result.status
        'PASS'
    """
    material_normalized = material.lower().strip()

    if material_normalized not in ("copper", "aluminum"):
        return ValidationResult(
            status="FAIL",
            message=f"Invalid material '{material}'. Must be 'copper' or 'aluminum'.",
            nec_reference="NEC 250.122",
            details={"material": material},
        )

    required_egc = _get_required_egc_size(ocpd_rating, material_normalized)

    if required_egc is None:
        return ValidationResult(
            status="FAIL",
            message=f"OCPD rating {ocpd_rating}A not found in Table 250.122",
            nec_reference="NEC 250.122, Table 250.122",
            details={"ocpd_rating": ocpd_rating},
        )

    try:
        comparison = _compare_conductor_sizes(egc_size, required_egc)
    except ValueError as e:
        return ValidationResult(
            status="FAIL",
            message=str(e),
            nec_reference="NEC 250.122, Table 250.122",
            details={"egc_size": egc_size},
        )

    details = {
        "ocpd_rating": ocpd_rating,
        "egc_size": egc_size,
        "required_egc_size": required_egc,
        "material": material_normalized,
    }

    if comparison >= 0:  # EGC is equal to or larger than required
        return ValidationResult(
            status="PASS",
            message=f"EGC size {egc_size} AWG meets minimum {required_egc} AWG "
            f"for {ocpd_rating}A OCPD ({material_normalized})",
            nec_reference="NEC 250.122, Table 250.122",
            details=details,
        )
    else:
        return ValidationResult(
            status="FAIL",
            message=f"EGC size {egc_size} AWG is undersized. Minimum {required_egc} AWG required "
            f"for {ocpd_rating}A OCPD ({material_normalized})",
            nec_reference="NEC 250.122, Table 250.122",
            details=details,
        )
