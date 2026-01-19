"""
Conduit Fill Calculator
=======================
Deterministic conduit fill calculations per NEC Chapter 9.
All calculations are pure Python - NO LLM involvement.
"""

from typing import Dict, Optional, List, Any

from lib.nec_tables import (
    CONDUIT_AREA,
)

CONDUCTOR_AREAS = {
    "THHN": {
        "14": 0.0097,
        "12": 0.0133,
        "10": 0.0211,
        "8": 0.0366,
        "6": 0.0507,
        "4": 0.0824,
        "3": 0.0973,
        "2": 0.1158,
        "1": 0.1562,
        "1/0": 0.1855,
        "2/0": 0.2223,
        "3/0": 0.2679,
        "4/0": 0.3237,
        "250": 0.3970,
        "300": 0.4608,
        "350": 0.5242,
        "400": 0.5863,
        "500": 0.7073,
        "600": 0.8676,
        "700": 0.9887,
        "750": 1.0496,
    },
    "THWN": {
        "14": 0.0097,
        "12": 0.0133,
        "10": 0.0211,
        "8": 0.0366,
        "6": 0.0507,
        "4": 0.0824,
        "3": 0.0973,
        "2": 0.1158,
        "1": 0.1562,
        "1/0": 0.1855,
        "2/0": 0.2223,
        "3/0": 0.2679,
        "4/0": 0.3237,
        "250": 0.3970,
        "300": 0.4608,
        "350": 0.5242,
        "400": 0.5863,
        "500": 0.7073,
    },
    "XHHW": {
        "14": 0.0139,
        "12": 0.0181,
        "10": 0.0243,
        "8": 0.0437,
        "6": 0.0590,
        "4": 0.0814,
        "3": 0.0962,
        "2": 0.1146,
        "1": 0.1534,
        "1/0": 0.1825,
        "2/0": 0.2190,
        "3/0": 0.2642,
        "4/0": 0.3197,
        "250": 0.3904,
        "300": 0.4536,
        "350": 0.5166,
        "400": 0.5782,
        "500": 0.6984,
    },
    "RHH": {
        "14": 0.0293,
        "12": 0.0353,
        "10": 0.0437,
        "8": 0.0835,
        "6": 0.1041,
        "4": 0.1333,
        "3": 0.1521,
        "2": 0.1750,
        "1": 0.2660,
        "1/0": 0.3039,
        "2/0": 0.3505,
        "3/0": 0.4072,
        "4/0": 0.4754,
        "250": 0.6291,
        "300": 0.7088,
        "350": 0.7870,
        "400": 0.8626,
        "500": 1.0082,
    },
}

GROUND_WIRE_AREAS = {
    "14": 0.0097,
    "12": 0.0133,
    "10": 0.0211,
    "8": 0.0366,
    "6": 0.0507,
    "4": 0.0824,
    "3": 0.0973,
    "2": 0.1158,
    "1": 0.1562,
    "1/0": 0.1855,
    "2/0": 0.2223,
    "3/0": 0.2679,
    "4/0": 0.3237,
}

CONDUIT_SIZES = ["1/2", "3/4", "1", "1-1/4", "1-1/2", "2", "2-1/2", "3", "3-1/2", "4"]

def calculate(
    conductors: List[Dict[str, Any]],
    conduit_type: str = "EMT",
    include_ground: bool = True,
    ground_size: Optional[str] = None,
    conduit_size: Optional[str] = None,
) -> Dict:
    """
    Calculate conduit fill and recommend conduit size.

    Per NEC Chapter 9 Table 1:
    - 1 conductor: 53% fill
    - 2 conductors: 31% fill
    - 3+ conductors: 40% fill

    Args:
        conductors: List of conductor specifications, each with:
            - size: str - AWG or kcmil (e.g., "10", "1/0", "250")
            - insulation: str - Insulation type (THHN, THWN, XHHW, RHH)
            - quantity: int - Number of conductors of this type
        conduit_type: Type of conduit (EMT, RMC, PVC)
        include_ground: Whether to include equipment grounding conductor
        ground_size: Size of ground wire (if None, calculated per NEC 250.122)
        conduit_size: Optional specific conduit size to check (e.g., "1", "2")

    Returns:
        Dictionary with:
        - total_conductor_area: Total area of all conductors (sq in)
        - recommended_conduit_size: Minimum conduit trade size (or checked size)
        - fill_percent: Actual fill percentage
        - max_fill_percent: Maximum allowed fill percentage
        - nec_compliant: True if fill is within limits
        - work_shown: Step-by-step calculation
        - nec_citations: List of NEC references
    """
    work_steps = []
    nec_citations = []

    work_steps.append("=" * 60)
    work_steps.append("CONDUIT FILL CALCULATION")
    work_steps.append("NEC Chapter 9")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Calculate Conductor Areas")
    work_steps.append("─" * 60)

    total_area = 0.0
    total_conductors = 0
    conductor_details = []

    for cond in conductors:
        size = cond.get("size", "12")
        insulation = cond.get("insulation", "THHN").upper()
        quantity = cond.get("quantity", cond.get("count", 1))

        if insulation in CONDUCTOR_AREAS:
            area_table = CONDUCTOR_AREAS[insulation]
        else:
            area_table = CONDUCTOR_AREAS["THHN"]
            work_steps.append(f"  Note: {insulation} not in tables, using THHN values")

        if size in area_table:
            single_area = area_table[size]
            total_cond_area = single_area * quantity
            total_area += total_cond_area
            total_conductors += quantity

            work_steps.append(
                f"  {quantity}× #{size} {insulation}: {single_area:.4f} sq in × {quantity} = {total_cond_area:.4f} sq in"
            )
            conductor_details.append(
                {
                    "size": size,
                    "insulation": insulation,
                    "quantity": quantity,
                    "area_each": single_area,
                    "area_total": total_cond_area,
                }
            )
        else:
            work_steps.append(f"  Warning: Size {size} not found in {insulation} table")

    if include_ground:
        if ground_size is None:
            largest_size = max(
                (c.get("size", "12") for c in conductors),
                key=lambda s: _size_to_numeric(s),
            )
            ground_size = _get_ground_size(largest_size)

        if ground_size in GROUND_WIRE_AREAS:
            ground_area = GROUND_WIRE_AREAS[ground_size]
            total_area += ground_area
            total_conductors += 1
            work_steps.append(
                f"  1× #{ground_size} EGC (ground): {ground_area:.4f} sq in"
            )
            conductor_details.append(
                {
                    "size": ground_size,
                    "insulation": "EGC",
                    "quantity": 1,
                    "area_each": ground_area,
                    "area_total": ground_area,
                }
            )
            nec_citations.append("NEC 250.122 - Size of Equipment Grounding Conductors")

    work_steps.append(f"\n  Total conductor area: {total_area:.4f} sq in")
    work_steps.append(f"  Total number of conductors: {total_conductors}")

    nec_citations.append("NEC Chapter 9 Table 5 - Dimensions of Insulated Conductors")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Determine Maximum Fill Percentage")
    work_steps.append("─" * 60)

    if total_conductors == 1:
        max_fill_percent = 53
        work_steps.append("  1 conductor: 53% maximum fill")
    elif total_conductors == 2:
        max_fill_percent = 31
        work_steps.append("  2 conductors: 31% maximum fill")
    else:
        max_fill_percent = 40
        work_steps.append(f"  {total_conductors} conductors (3+): 40% maximum fill")

    nec_citations.append("NEC Chapter 9 Table 1 - Percent of Cross Section of Conduit")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Calculate Required Conduit Area")
    work_steps.append("─" * 60)

    required_area = total_area / (max_fill_percent / 100)
    work_steps.append("  Required conduit area = Total conductor area / Max fill %")
    work_steps.append(
        f"  Required conduit area = {total_area:.4f} / {max_fill_percent / 100:.2f}"
    )
    work_steps.append(f"  Required conduit area = {required_area:.4f} sq in")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Select Conduit Size")
    work_steps.append("─" * 60)

    conduit_type_upper = conduit_type.upper()
    if conduit_type_upper not in ["EMT", "RMC", "PVC"]:
        conduit_type_upper = "EMT"
        work_steps.append(f"  Note: {conduit_type} not recognized, using EMT")

    selected_size = None
    selected_area = 0.0
    actual_fill_percent = 0.0

    if conduit_size:
        work_steps.append(
            f'  Checking provided size: {conduit_size}" {conduit_type_upper}'
        )
        if conduit_size in CONDUIT_AREA:
            conduit_area = CONDUIT_AREA[conduit_size].get(conduit_type_upper)
            if conduit_area:
                selected_size = conduit_size
                selected_area = conduit_area
                actual_fill_percent = (total_area / conduit_area) * 100
                work_steps.append(f"  Conduit area: {conduit_area:.4f} sq in")
            else:
                work_steps.append(
                    f"  Error: Conduit type {conduit_type_upper} not available in size {conduit_size}"
                )
        else:
            work_steps.append(
                f"  Error: Conduit size {conduit_size} not found in tables"
            )
    else:
        work_steps.append(f"  Conduit type: {conduit_type_upper}")
        work_steps.append("  Checking available sizes:")

        for size in CONDUIT_SIZES:
            if size in CONDUIT_AREA:
                conduit_area = CONDUIT_AREA[size].get(conduit_type_upper)
                if conduit_area:
                    fill_pct = (total_area / conduit_area) * 100
                    status = "✓" if conduit_area >= required_area else "✗"
                    work_steps.append(
                        f'    {size}": {conduit_area:.4f} sq in, fill = {fill_pct:.1f}% {status}'
                    )

                    if conduit_area >= required_area and selected_size is None:
                        selected_size = size
                        selected_area = conduit_area
                        actual_fill_percent = fill_pct

    nec_citations.append(
        "NEC Chapter 9 Table 4 - Dimensions and Percent Area of Conduit"
    )

    if selected_size is None:
        return {
            "error": "No standard conduit size is large enough"
            if not conduit_size
            else f"Provided size {conduit_size} not found or invalid",
            "total_conductor_area": round(total_area, 4),
            "required_conduit_area": round(required_area, 4),
            "suggestion": "Consider multiple conduit runs or larger conductors",
            "work_shown": "\n".join(work_steps),
            "nec_citations": nec_citations,
        }

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Verify Compliance")
    work_steps.append("─" * 60)

    nec_compliant = actual_fill_percent <= max_fill_percent

    work_steps.append(f'  Selected conduit: {selected_size}" {conduit_type_upper}')
    work_steps.append(f"  Conduit area: {selected_area:.4f} sq in")
    work_steps.append(f"  Actual fill: {actual_fill_percent:.1f}%")
    work_steps.append(f"  Maximum fill: {max_fill_percent}%")
    work_steps.append(f"  Compliance: {'✓ PASS' if nec_compliant else '✗ FAIL'}")

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("CONDUIT FILL SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(f"  Conductors: {total_conductors}")
    work_steps.append(f"  Total conductor area: {total_area:.4f} sq in")
    work_steps.append(f'  Recommended conduit: {selected_size}" {conduit_type_upper}')
    work_steps.append(f"  Fill: {actual_fill_percent:.1f}% (max {max_fill_percent}%)")
    work_steps.append("=" * 60)

    return {
        "conductors": conductor_details,
        "total_conductors": total_conductors,
        "total_conductor_area_sqin": round(total_area, 4),
        "conduit_type": conduit_type_upper,
        "recommended_conduit_size": selected_size,
        "conduit_area_sqin": round(selected_area, 4),
        "fill_percent": round(actual_fill_percent, 1),
        "max_fill_percent": max_fill_percent,
        "nec_compliant": nec_compliant,
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }

def _size_to_numeric(size: str) -> float:
    """Convert conductor size to numeric value for comparison."""
    if "/" in size and "0" in size:
        return 0 - int(size.split("/")[0])
    elif size.isdigit():
        return -int(size)  # Negative so larger AWG numbers are smaller
    else:
        return float(size)  # kcmil sizes

def _get_ground_size(conductor_size: str) -> str:
    """
    Get equipment grounding conductor size per NEC 250.122.
    Simplified table - actual sizing depends on overcurrent device rating.
    """
    ground_map = {
        "14": "14",
        "12": "12",
        "10": "10",
        "8": "10",
        "6": "10",
        "4": "10",
        "3": "10",
        "2": "10",
        "1": "8",
        "1/0": "8",
        "2/0": "6",
        "3/0": "6",
        "4/0": "4",
        "250": "4",
        "300": "4",
        "350": "3",
        "400": "3",
        "500": "2",
    }
    return ground_map.get(conductor_size, "10")

def calculate_nipple_fill(
    conductors: List[Dict[str, Any]],
    conduit_type: str = "EMT",
) -> Dict:
    """
    Calculate conduit fill for nipples (≤24 inches).

    Per NEC Chapter 9 Note 4, conduit nipples not exceeding 24 inches
    may be filled to 60% of their total cross-sectional area.

    Args:
        conductors: List of conductor specifications
        conduit_type: Type of conduit (EMT, RMC, PVC)

    Returns:
        Dictionary with nipple fill calculations
    """
    result = calculate(conductors, conduit_type, include_ground=False)

    if "error" in result:
        return result

    total_area = result["total_conductor_area_sqin"]
    required_area = total_area / 0.60

    work_steps = [
        "=" * 60,
        "CONDUIT NIPPLE FILL CALCULATION",
        "NEC Chapter 9 Note 4 (≤24 inches)",
        "=" * 60,
        f"\nTotal conductor area: {total_area:.4f} sq in",
        "Maximum fill for nipples: 60%",
        f"Required conduit area: {total_area:.4f} / 0.60 = {required_area:.4f} sq in",
    ]

    conduit_type_upper = conduit_type.upper()
    selected_size = None
    selected_area = None

    for size in CONDUIT_SIZES:
        if size in CONDUIT_AREA:
            conduit_area = CONDUIT_AREA[size].get(conduit_type_upper)
            if conduit_area and conduit_area >= required_area:
                selected_size = size
                selected_area = conduit_area
                break

    if selected_size:
        actual_fill = (total_area / selected_area) * 100
        work_steps.append(
            f'\nRecommended nipple size: {selected_size}" {conduit_type_upper}'
        )
        work_steps.append(f"Actual fill: {actual_fill:.1f}%")

        return {
            "total_conductor_area_sqin": round(total_area, 4),
            "recommended_conduit_size": selected_size,
            "conduit_area_sqin": round(selected_area, 4),
            "fill_percent": round(actual_fill, 1),
            "max_fill_percent": 60,
            "nec_compliant": actual_fill <= 60,
            "work_shown": "\n".join(work_steps),
            "nec_citations": ["NEC Chapter 9 Note 4 - Nipple fill allowance (60%)"],
        }

    return {
        "error": "No standard conduit size is large enough for nipple",
        "work_shown": "\n".join(work_steps),
        "nec_citations": ["NEC Chapter 9 Note 4"],
    }
