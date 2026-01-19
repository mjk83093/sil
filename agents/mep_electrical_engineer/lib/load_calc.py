"""
Load Calculator
===============
Deterministic load calculations per NEC Article 220.
All calculations are pure Python - NO LLM involvement.
"""

import math
from typing import Dict, Optional, List, Any

from lib.nec_tables import (
    LIGHTING_DEMAND_FACTORS_220_42,
    RECEPTACLE_DEMAND_FACTORS_220_44,
    get_lighting_load,
)

def calculate(
    area_sqft: float,
    occupancy: str,
    voltage: int = 120,
    additional_loads: Optional[List[Dict[str, Any]]] = None,
    apply_demand_factors: bool = True,
) -> Dict:
    """
    Calculate electrical load per NEC Article 220.

    This function calculates:
    1. General lighting load per Table 220.12
    2. Receptacle loads per 220.14
    3. Demand factors per 220.42 and 220.44

    Args:
        area_sqft: Building/space area in square feet
        occupancy: Occupancy type (office, retail, warehouse, residential, etc.)
        voltage: System voltage (default 120V for load calculations)
        additional_loads: List of additional loads, each with:
            - name: str - Load description
            - va: float - Load in VA
            - type: str - "lighting", "receptacle", "motor", "hvac", "other"
            - demand_factor: float - Optional override demand factor (0.0-1.0)
        apply_demand_factors: Whether to apply NEC demand factors (default True)

    Returns:
        Dictionary with:
        - calculated_load_va: Total connected load in VA
        - demand_load_va: Load after demand factors in VA
        - demand_factor: Overall demand factor applied
        - load_amps: Load current in amps
        - work_shown: Step-by-step calculation
        - nec_citations: List of NEC references
    """
    work_steps = []
    nec_citations = []

    work_steps.append("=" * 60)
    work_steps.append("LOAD CALCULATION PER NEC ARTICLE 220")
    work_steps.append("=" * 60)
    work_steps.append("\nInput Parameters:")
    work_steps.append(f"  Area: {area_sqft:,.0f} sq ft")
    work_steps.append(f"  Occupancy: {occupancy}")
    work_steps.append(f"  Voltage: {voltage} V")

    lighting_load_va = 0.0
    receptacle_load_va = 0.0
    other_loads_va = 0.0

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: General Lighting Load (NEC Table 220.12)")
    work_steps.append("─" * 60)

    va_per_sqft = get_lighting_load(occupancy)
    lighting_load_va = area_sqft * va_per_sqft

    work_steps.append(f"  Occupancy type: {occupancy}")
    work_steps.append(f"  VA per sq ft (Table 220.12): {va_per_sqft} VA/sq ft")
    work_steps.append(
        f"  General lighting load = {area_sqft:,.0f} × {va_per_sqft} = {lighting_load_va:,.0f} VA"
    )
    nec_citations.append("NEC Table 220.12 - General Lighting Loads by Occupancy")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Receptacle Load (NEC 220.14)")
    work_steps.append("─" * 60)

    if occupancy.lower() in ["dwelling", "residential"]:
        work_steps.append("  For dwelling units, receptacle load is included in")
        work_steps.append("  general lighting load per NEC 220.14(J)")
        receptacle_load_va = 0
    else:
        estimated_receptacles = max(1, int(area_sqft / 100))
        receptacle_load_va = estimated_receptacles * 180
        work_steps.append("  Per NEC 220.14(I): 180 VA per general-use receptacle")
        work_steps.append(
            f"  Estimated receptacles (1 per 100 sq ft): {estimated_receptacles}"
        )
        work_steps.append(
            f"  Receptacle load = {estimated_receptacles} × 180 VA = {receptacle_load_va:,.0f} VA"
        )

    nec_citations.append("NEC 220.14 - Other Loads — All Occupancies")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Additional Loads")
    work_steps.append("─" * 60)

    additional_lighting_va = 0.0
    additional_receptacle_va = 0.0
    motor_loads_va = 0.0
    hvac_loads_va = 0.0
    other_additional_va = 0.0

    if additional_loads:
        for load in additional_loads:
            name = load.get("name", "Unnamed load")
            va = load.get("va", 0)
            load_type = load.get("type", "other").lower()

            work_steps.append(f"  {name}: {va:,.0f} VA ({load_type})")

            if load_type == "lighting":
                additional_lighting_va += va
            elif load_type == "receptacle":
                additional_receptacle_va += va
            elif load_type == "motor":
                motor_loads_va += va
            elif load_type == "hvac":
                hvac_loads_va += va
            else:
                other_additional_va += va
    else:
        work_steps.append("  No additional loads specified")

    lighting_load_va += additional_lighting_va
    receptacle_load_va += additional_receptacle_va
    other_loads_va = motor_loads_va + hvac_loads_va + other_additional_va

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Total Connected Load")
    work_steps.append("─" * 60)

    total_connected_va = lighting_load_va + receptacle_load_va + other_loads_va

    work_steps.append(f"  Lighting load: {lighting_load_va:,.0f} VA")
    work_steps.append(f"  Receptacle load: {receptacle_load_va:,.0f} VA")
    work_steps.append(f"  Other loads: {other_loads_va:,.0f} VA")
    work_steps.append("  ─────────────────────────")
    work_steps.append(f"  Total connected load: {total_connected_va:,.0f} VA")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Apply Demand Factors")
    work_steps.append("─" * 60)

    if not apply_demand_factors:
        demand_lighting_va = lighting_load_va
        demand_receptacle_va = receptacle_load_va
        demand_other_va = other_loads_va
        work_steps.append("  Demand factors not applied (per user request)")
    else:
        demand_lighting_va = apply_lighting_demand_factor(
            lighting_load_va, occupancy, work_steps
        )
        nec_citations.append("NEC Table 220.42 - Lighting Load Demand Factors")

        demand_receptacle_va = apply_receptacle_demand_factor(
            receptacle_load_va, work_steps
        )
        nec_citations.append("NEC Table 220.44 - Receptacle Load Demand Factors")

        demand_other_va = other_loads_va
        if other_loads_va > 0:
            work_steps.append(
                f"\n  Other loads (motors, HVAC, etc.): {other_loads_va:,.0f} VA at 100%"
            )
            work_steps.append(
                "  Note: Motor loads may require additional calculations per NEC 430"
            )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 6: Total Demand Load")
    work_steps.append("─" * 60)

    total_demand_va = demand_lighting_va + demand_receptacle_va + demand_other_va

    work_steps.append(f"  Lighting demand: {demand_lighting_va:,.0f} VA")
    work_steps.append(f"  Receptacle demand: {demand_receptacle_va:,.0f} VA")
    work_steps.append(f"  Other demand: {demand_other_va:,.0f} VA")
    work_steps.append("  ─────────────────────────")
    work_steps.append(f"  Total demand load: {total_demand_va:,.0f} VA")

    overall_demand_factor = (
        total_demand_va / total_connected_va if total_connected_va > 0 else 1.0
    )
    work_steps.append(
        f"\n  Overall demand factor: {total_demand_va:,.0f} / {total_connected_va:,.0f} = {overall_demand_factor:.2%}"
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 7: Calculate Load Current")
    work_steps.append("─" * 60)

    load_amps = total_demand_va / voltage

    work_steps.append("  I = VA / V")
    work_steps.append(f"  I = {total_demand_va:,.0f} / {voltage}")
    work_steps.append(f"  I = {load_amps:.1f} A")

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("LOAD CALCULATION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(f"  Total Connected Load: {total_connected_va:,.0f} VA")
    work_steps.append(f"  Total Demand Load: {total_demand_va:,.0f} VA")
    work_steps.append(f"  Demand Factor: {overall_demand_factor:.1%}")
    work_steps.append(f"  Load Current: {load_amps:.1f} A @ {voltage}V")
    work_steps.append("=" * 60)

    return {
        "area_sqft": area_sqft,
        "occupancy": occupancy,
        "voltage": voltage,
        "lighting_load_va": round(lighting_load_va, 0),
        "receptacle_load_va": round(receptacle_load_va, 0),
        "other_loads_va": round(other_loads_va, 0),
        "calculated_load_va": round(total_connected_va, 0),
        "demand_lighting_va": round(demand_lighting_va, 0),
        "demand_receptacle_va": round(demand_receptacle_va, 0),
        "demand_other_va": round(demand_other_va, 0),
        "demand_load_va": round(total_demand_va, 0),
        "demand_factor": round(overall_demand_factor, 3),
        "load_amps": round(load_amps, 1),
        "va_per_sqft": va_per_sqft,
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }

def apply_lighting_demand_factor(
    lighting_va: float, occupancy: str, work_steps: List[str]
) -> float:
    """
    Apply lighting load demand factors per NEC Table 220.42.

    Args:
        lighting_va: Total lighting load in VA
        occupancy: Occupancy type
        work_steps: List to append calculation steps

    Returns:
        Demand lighting load in VA
    """
    work_steps.append("\n  Lighting Demand Factor (NEC Table 220.42):")

    occupancy_lower = occupancy.lower()
    if occupancy_lower in LIGHTING_DEMAND_FACTORS_220_42:
        demand_schedule = LIGHTING_DEMAND_FACTORS_220_42[occupancy_lower]
    else:
        demand_schedule = LIGHTING_DEMAND_FACTORS_220_42["default"]
        work_steps.append(f"    Occupancy '{occupancy}' not in table, using 100%")

    remaining_va = lighting_va
    demand_va = 0.0
    previous_threshold = 0.0

    for threshold, factor in demand_schedule:
        if remaining_va <= 0:
            break

        if threshold == float("inf"):
            portion = remaining_va
        else:
            portion = min(remaining_va, threshold - previous_threshold)

        demand_portion = portion * factor
        demand_va += demand_portion

        if portion > 0:
            work_steps.append(
                f"    {portion:,.0f} VA × {factor:.0%} = {demand_portion:,.0f} VA"
            )

        remaining_va -= portion
        previous_threshold = threshold

    work_steps.append(f"    Total lighting demand: {demand_va:,.0f} VA")

    return demand_va

def apply_receptacle_demand_factor(
    receptacle_va: float, work_steps: List[str]
) -> float:
    """
    Apply receptacle load demand factors per NEC Table 220.44.

    Args:
        receptacle_va: Total receptacle load in VA
        work_steps: List to append calculation steps

    Returns:
        Demand receptacle load in VA
    """
    work_steps.append("\n  Receptacle Demand Factor (NEC Table 220.44):")

    if receptacle_va == 0:
        work_steps.append("    No receptacle load")
        return 0.0

    remaining_va = receptacle_va
    demand_va = 0.0
    previous_threshold = 0.0

    for threshold, factor in RECEPTACLE_DEMAND_FACTORS_220_44:
        if remaining_va <= 0:
            break

        if threshold == float("inf"):
            portion = remaining_va
        else:
            portion = min(remaining_va, threshold - previous_threshold)

        demand_portion = portion * factor
        demand_va += demand_portion

        if portion > 0:
            work_steps.append(
                f"    {portion:,.0f} VA × {factor:.0%} = {demand_portion:,.0f} VA"
            )

        remaining_va -= portion
        previous_threshold = threshold

    work_steps.append(f"    Total receptacle demand: {demand_va:,.0f} VA")

    return demand_va

def calculate_dwelling_unit(
    area_sqft: float,
    num_small_appliance_circuits: int = 2,
    num_laundry_circuits: int = 1,
    electric_range_kw: float = 0.0,
    electric_dryer_kw: float = 0.0,
    hvac_load_va: float = 0.0,
    water_heater_kw: float = 0.0,
    other_loads: Optional[List[Dict[str, Any]]] = None,
    voltage: int = 240,
) -> Dict:
    """
    Calculate dwelling unit service load per NEC Article 220.

    This implements the standard calculation method for dwelling units
    per NEC 220.40 through 220.54.

    Args:
        area_sqft: Dwelling unit area in square feet
        num_small_appliance_circuits: Number of 20A small appliance circuits (min 2)
        num_laundry_circuits: Number of laundry circuits (min 1)
        electric_range_kw: Electric range/oven nameplate rating in kW
        electric_dryer_kw: Electric dryer nameplate rating in kW
        hvac_load_va: HVAC load in VA
        water_heater_kw: Water heater rating in kW
        other_loads: List of other fixed loads
        voltage: Service voltage (typically 240V for residential)

    Returns:
        Dictionary with dwelling unit load calculation results
    """
    work_steps = []
    nec_citations = []

    work_steps.append("=" * 60)
    work_steps.append("DWELLING UNIT LOAD CALCULATION")
    work_steps.append("NEC Article 220 - Standard Calculation Method")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: General Lighting Load (NEC 220.12)")
    work_steps.append("─" * 60)

    lighting_va = area_sqft * 3.0
    work_steps.append(
        f"  Area: {area_sqft:,.0f} sq ft × 3 VA/sq ft = {lighting_va:,.0f} VA"
    )
    nec_citations.append("NEC Table 220.12 - Dwelling units: 3 VA per sq ft")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Small Appliance Circuits (NEC 220.52(A))")
    work_steps.append("─" * 60)

    small_appliance_va = num_small_appliance_circuits * 1500
    work_steps.append(
        f"  {num_small_appliance_circuits} circuits × 1500 VA = {small_appliance_va:,.0f} VA"
    )
    nec_citations.append("NEC 220.52(A) - Small appliance circuits: 1500 VA each")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Laundry Circuit (NEC 220.52(B))")
    work_steps.append("─" * 60)

    laundry_va = num_laundry_circuits * 1500
    work_steps.append(
        f"  {num_laundry_circuits} circuit × 1500 VA = {laundry_va:,.0f} VA"
    )
    nec_citations.append("NEC 220.52(B) - Laundry circuit: 1500 VA")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Apply Demand Factor (NEC Table 220.42)")
    work_steps.append("─" * 60)

    combined_load = lighting_va + small_appliance_va + laundry_va
    work_steps.append(
        f"  Combined load: {lighting_va:,.0f} + {small_appliance_va:,.0f} + {laundry_va:,.0f} = {combined_load:,.0f} VA"
    )

    if combined_load <= 3000:
        demand_combined = combined_load * 1.0
        work_steps.append(
            f"  First 3000 VA at 100%: {min(combined_load, 3000):,.0f} VA"
        )
    else:
        demand_combined = 3000 * 1.0
        work_steps.append("  First 3000 VA at 100%: 3,000 VA")

        remaining = combined_load - 3000
        if remaining <= 117000:
            demand_combined += remaining * 0.35
            work_steps.append(
                f"  Remaining {remaining:,.0f} VA at 35%: {remaining * 0.35:,.0f} VA"
            )
        else:
            demand_combined += 117000 * 0.35
            work_steps.append(f"  Next 117,000 VA at 35%: {117000 * 0.35:,.0f} VA")
            over_120k = remaining - 117000
            demand_combined += over_120k * 0.25
            work_steps.append(f"  Over 120,000 VA at 25%: {over_120k * 0.25:,.0f} VA")

    work_steps.append(f"  Demand load: {demand_combined:,.0f} VA")
    nec_citations.append("NEC Table 220.42 - Lighting load demand factors")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Electric Range (NEC Table 220.55)")
    work_steps.append("─" * 60)

    if electric_range_kw > 0:
        if electric_range_kw <= 12:
            range_demand_va = 8000
            work_steps.append(f"  Range: {electric_range_kw} kW (≤12 kW)")
            work_steps.append("  Per Table 220.55 Column C: 8,000 VA")
        else:
            excess_kw = electric_range_kw - 12
            range_demand_va = 8000 * (1 + 0.05 * excess_kw)
            work_steps.append(f"  Range: {electric_range_kw} kW (>12 kW)")
            work_steps.append(
                f"  Base 8 kW + 5% per kW over 12: {range_demand_va:,.0f} VA"
            )
        nec_citations.append("NEC Table 220.55 - Electric ranges demand factors")
    else:
        range_demand_va = 0
        work_steps.append("  No electric range")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 6: Electric Dryer (NEC 220.54)")
    work_steps.append("─" * 60)

    if electric_dryer_kw > 0:
        dryer_va = max(5000, electric_dryer_kw * 1000)
        work_steps.append(f"  Dryer: {electric_dryer_kw} kW")
        work_steps.append(
            "  Per NEC 220.54: Use 5000 VA or nameplate, whichever is larger"
        )
        work_steps.append(f"  Dryer demand: {dryer_va:,.0f} VA")
        nec_citations.append("NEC 220.54 - Electric dryer load")
    else:
        dryer_va = 0
        work_steps.append("  No electric dryer")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 7: HVAC Load (NEC 220.60)")
    work_steps.append("─" * 60)

    if hvac_load_va > 0:
        work_steps.append(f"  HVAC load: {hvac_load_va:,.0f} VA")
        work_steps.append("  Note: Per NEC 220.60, use larger of heating or cooling")
        nec_citations.append("NEC 220.60 - Noncoincident loads")
    else:
        work_steps.append("  No HVAC load specified")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 8: Water Heater")
    work_steps.append("─" * 60)

    water_heater_va = water_heater_kw * 1000
    if water_heater_va > 0:
        work_steps.append(
            f"  Water heater: {water_heater_kw} kW = {water_heater_va:,.0f} VA"
        )
    else:
        work_steps.append("  No electric water heater")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 9: Other Fixed Loads")
    work_steps.append("─" * 60)

    other_va = 0.0
    if other_loads:
        for load in other_loads:
            name = load.get("name", "Unnamed")
            va = load.get("va", 0)
            other_va += va
            work_steps.append(f"  {name}: {va:,.0f} VA")
    else:
        work_steps.append("  No other fixed loads")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 10: Total Service Load")
    work_steps.append("─" * 60)

    total_demand_va = (
        demand_combined
        + range_demand_va
        + dryer_va
        + hvac_load_va
        + water_heater_va
        + other_va
    )

    work_steps.append(f"  Lighting/appliance demand: {demand_combined:,.0f} VA")
    work_steps.append(f"  Range demand: {range_demand_va:,.0f} VA")
    work_steps.append(f"  Dryer demand: {dryer_va:,.0f} VA")
    work_steps.append(f"  HVAC: {hvac_load_va:,.0f} VA")
    work_steps.append(f"  Water heater: {water_heater_va:,.0f} VA")
    work_steps.append(f"  Other loads: {other_va:,.0f} VA")
    work_steps.append("  ─────────────────────────")
    work_steps.append(f"  Total demand: {total_demand_va:,.0f} VA")

    service_amps = total_demand_va / voltage
    work_steps.append(
        f"\n  Service current: {total_demand_va:,.0f} VA / {voltage} V = {service_amps:.1f} A"
    )

    if service_amps <= 100:
        recommended_service = 100
    elif service_amps <= 150:
        recommended_service = 150
    elif service_amps <= 200:
        recommended_service = 200
    elif service_amps <= 400:
        recommended_service = 400
    else:
        recommended_service = int(math.ceil(service_amps / 100) * 100)

    work_steps.append(f"  Recommended service size: {recommended_service} A")

    work_steps.append(f"\n{'=' * 60}")

    return {
        "area_sqft": area_sqft,
        "lighting_load_va": round(lighting_va, 0),
        "small_appliance_va": round(small_appliance_va, 0),
        "laundry_va": round(laundry_va, 0),
        "combined_load_va": round(combined_load, 0),
        "demand_combined_va": round(demand_combined, 0),
        "range_demand_va": round(range_demand_va, 0),
        "dryer_demand_va": round(dryer_va, 0),
        "hvac_load_va": round(hvac_load_va, 0),
        "water_heater_va": round(water_heater_va, 0),
        "other_loads_va": round(other_va, 0),
        "total_demand_va": round(total_demand_va, 0),
        "service_amps": round(service_amps, 1),
        "recommended_service_amps": recommended_service,
        "voltage": voltage,
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }
