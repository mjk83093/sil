"""
NEC 240.4 Conductor Protection Validation
==========================================
Deterministic validation of overcurrent protection for conductors.
All validation logic is pure Python - NO LLM involvement.

Reference: NEC 2023 Article 240.4
"""

from typing import List, Optional
from .validation_result import ValidationResult

STANDARD_OCPD_SIZES: List[int] = [
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    125,
    150,
    175,
    200,
    225,
    250,
    300,
    350,
    400,
    450,
    500,
    600,
    700,
    800,
    1000,
    1200,
    1600,
    2000,
    2500,
    3000,
    4000,
    5000,
    6000,
]

SMALL_CONDUCTOR_LIMITS: dict[str, int] = {
    "14": 15,  # 14 AWG max 15A
    "12": 20,  # 12 AWG max 20A
    "10": 30,  # 10 AWG max 30A
}

def get_next_standard_ocpd_size(ampacity: float) -> int:
    """
    Get the next standard OCPD size at or above the given ampacity.

    Per NEC 240.6(A), standard ampere ratings for fuses and inverse time
    circuit breakers are: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90,
    100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600,
    700, 800, 1000, 1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000.

    Args:
        ampacity: Required ampacity in amps

    Returns:
        Next standard OCPD size at or above the ampacity

    Raises:
        ValueError: If ampacity exceeds maximum standard size (6000A)

    Example:
        >>> get_next_standard_ocpd_size(18)
        20
        >>> get_next_standard_ocpd_size(100)
        100
        >>> get_next_standard_ocpd_size(85)
        90
    """
    if ampacity <= 0:
        raise ValueError(f"Ampacity must be positive, got {ampacity}")

    for size in STANDARD_OCPD_SIZES:
        if size >= ampacity:
            return size

    raise ValueError(f"Ampacity {ampacity}A exceeds maximum standard OCPD size (6000A)")

def get_next_lower_standard_ocpd_size(ampacity: float) -> Optional[int]:
    """
    Get the next standard OCPD size at or below the given ampacity.

    Args:
        ampacity: Ampacity in amps

    Returns:
        Next standard OCPD size at or below the ampacity, or None if below minimum

    Example:
        >>> get_next_lower_standard_ocpd_size(18)
        15
        >>> get_next_lower_standard_ocpd_size(100)
        100
    """
    if ampacity < STANDARD_OCPD_SIZES[0]:
        return None

    result = STANDARD_OCPD_SIZES[0]
    for size in STANDARD_OCPD_SIZES:
        if size <= ampacity:
            result = size
        else:
            break

    return result

def validate_conductor_protection(
    conductor_ampacity: float,
    ocpd_rating: int,
    conductor_size: Optional[str] = None,
    allow_next_size_up: bool = True,
) -> ValidationResult:
    """
    Validate that conductor is properly protected per NEC 240.4.

    NEC 240.4(B) allows the next higher standard overcurrent device rating
    (above the ampacity of the conductors being protected) when:
    - The ampacity does not correspond to a standard rating
    - The next higher standard rating does not exceed 800A

    NEC 240.4(D) limits protection for small conductors:
    - 14 AWG: Maximum 15A
    - 12 AWG: Maximum 20A
    - 10 AWG: Maximum 30A

    Args:
        conductor_ampacity: Ampacity of conductor in amps
        ocpd_rating: Rating of overcurrent protective device in amps
        conductor_size: Optional conductor size (e.g., "14", "12", "10") for
                       small conductor rule checking
        allow_next_size_up: Whether to allow next-size-up rule per 240.4(B)

    Returns:
        ValidationResult with PASS/FAIL status

    Example:
        >>> result = validate_conductor_protection(20, 20)
        >>> result.status
        'PASS'
        >>> result = validate_conductor_protection(20, 30)
        >>> result.status
        'FAIL'
    """
    if ocpd_rating not in STANDARD_OCPD_SIZES:
        return ValidationResult(
            status="WARN",
            message=f"OCPD rating {ocpd_rating}A is not a standard size per NEC 240.6(A)",
            nec_reference="NEC 240.6(A)",
            details={
                "ocpd_rating": ocpd_rating,
                "standard_sizes": STANDARD_OCPD_SIZES,
            },
        )

    details = {
        "conductor_ampacity": conductor_ampacity,
        "ocpd_rating": ocpd_rating,
        "conductor_size": conductor_size,
    }

    if conductor_size and conductor_size in SMALL_CONDUCTOR_LIMITS:
        max_ocpd = SMALL_CONDUCTOR_LIMITS[conductor_size]
        details["small_conductor_max_ocpd"] = max_ocpd

        if ocpd_rating > max_ocpd:
            return ValidationResult(
                status="FAIL",
                message=f"{conductor_size} AWG conductor limited to {max_ocpd}A OCPD maximum "
                f"per NEC 240.4(D). Actual OCPD: {ocpd_rating}A",
                nec_reference="NEC 240.4(D)",
                details=details,
            )

    if ocpd_rating <= conductor_ampacity:
        return ValidationResult(
            status="PASS",
            message=f"OCPD rating {ocpd_rating}A does not exceed conductor ampacity {conductor_ampacity}A",
            nec_reference="NEC 240.4(B)",
            details=details,
        )

    if allow_next_size_up and ocpd_rating <= 800:
        try:
            next_size_up = get_next_standard_ocpd_size(conductor_ampacity)
        except ValueError:
            next_size_up = None

        details["next_standard_size_up"] = next_size_up

        if next_size_up and ocpd_rating == next_size_up:
            lower_size = get_next_lower_standard_ocpd_size(conductor_ampacity)

            if lower_size is None or conductor_ampacity > lower_size:
                return ValidationResult(
                    status="PASS",
                    message=f"OCPD rating {ocpd_rating}A permitted as next standard size above "
                    f"conductor ampacity {conductor_ampacity}A per NEC 240.4(B)",
                    nec_reference="NEC 240.4(B)",
                    details=details,
                )

    return ValidationResult(
        status="FAIL",
        message=f"OCPD rating {ocpd_rating}A exceeds conductor ampacity {conductor_ampacity}A. "
        f"Conductor not adequately protected.",
        nec_reference="NEC 240.4(B)",
        details=details,
    )

def validate_small_conductor_protection(
    conductor_size: str, ocpd_rating: int
) -> ValidationResult:
    """
    Validate small conductor protection per NEC 240.4(D).

    Small conductors (14, 12, 10 AWG) have specific maximum OCPD ratings
    regardless of their actual ampacity under specific conditions.

    Args:
        conductor_size: Conductor size ("14", "12", or "10")
        ocpd_rating: Rating of overcurrent protective device in amps

    Returns:
        ValidationResult with PASS/FAIL status

    Example:
        >>> result = validate_small_conductor_protection("14", 15)
        >>> result.status
        'PASS'
        >>> result = validate_small_conductor_protection("14", 20)
        >>> result.status
        'FAIL'
    """
    normalized_size = conductor_size.strip().upper().replace("AWG", "").strip()

    if normalized_size not in SMALL_CONDUCTOR_LIMITS:
        return ValidationResult(
            status="PASS",
            message=f"Conductor size {conductor_size} is not subject to NEC 240.4(D) limits",
            nec_reference="NEC 240.4(D)",
            details={
                "conductor_size": conductor_size,
                "ocpd_rating": ocpd_rating,
            },
        )

    max_ocpd = SMALL_CONDUCTOR_LIMITS[normalized_size]

    details = {
        "conductor_size": conductor_size,
        "ocpd_rating": ocpd_rating,
        "max_ocpd_per_240_4_d": max_ocpd,
    }

    if ocpd_rating <= max_ocpd:
        return ValidationResult(
            status="PASS",
            message=f"{conductor_size} AWG conductor with {ocpd_rating}A OCPD meets "
            f"NEC 240.4(D) limit of {max_ocpd}A maximum",
            nec_reference="NEC 240.4(D)",
            details=details,
        )
    else:
        return ValidationResult(
            status="FAIL",
            message=f"{conductor_size} AWG conductor limited to {max_ocpd}A OCPD maximum "
            f"per NEC 240.4(D). Actual OCPD: {ocpd_rating}A exceeds limit.",
            nec_reference="NEC 240.4(D)",
            details=details,
        )
