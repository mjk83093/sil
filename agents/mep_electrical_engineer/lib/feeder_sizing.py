"""
Feeder/Conductor Sizing Calculator
==================================
Deterministic feeder and conductor sizing per NEC requirements.
All calculations are pure Python - NO LLM involvement.
"""

from typing import Dict

from lib.nec_tables import (
    get_temp_correction_factor,
    get_insulation_temp_rating,
    CONDUCTOR_SIZES,
    AMPACITY_TABLE_310_15_B_16_COPPER,
    AMPACITY_TABLE_310_15_B_16_ALUMINUM,
)
from lib.voltage_drop import calculate as calculate_voltage_drop

def calculate(
    load_amps: float,
    voltage: int,
    phases: int,
    distance_feet: float,
    conductor_type: str = "THHN",
    conduit_type: str = "EMT",
    temperature: float = 30.0,
    conductor_material: str = "copper",
    max_voltage_drop_percent: float = 3.0,
    power_factor: float = 0.85,
    continuous_load: bool = True,
    num_current_carrying: int = 3,
) -> Dict:
    """
    Calculate feeder/conductor sizing per NEC requirements.

    This function determines the appropriate conductor size based on:
    1. Ampacity requirements (NEC 310.15)
    2. Temperature correction factors (NEC Table 310.15(B)(1))
    3. Conductor adjustment factors (NEC Table 310.15(C)(1))
    4. Voltage drop limits (NEC 210.19, 215.2)
    5. Continuous load requirements (NEC 215.2(A)(1))

    Args:
        load_amps: Load current in amps
        voltage: System voltage (e.g., 120, 208, 277, 480)
        phases: Number of phases (1 or 3)
        distance_feet: One-way conductor length in feet
        conductor_type: Insulation type (THHN, THWN, XHHW, etc.)
        conduit_type: Conduit type (EMT, RMC, PVC)
        temperature: Ambient temperature in Celsius (default 30°C)
        conductor_material: "copper" or "aluminum"
        max_voltage_drop_percent: Maximum voltage drop (default 3%)
        power_factor: Power factor (default 0.85)
        continuous_load: True if load operates 3+ hours (default True)
        num_current_carrying: Number of current-carrying conductors (default 3)

    Returns:
        Dictionary with:
        - conductor_size: Recommended conductor size (e.g., "3/0 AWG")
        - ampacity: Derated ampacity of selected conductor
        - voltage_drop_volts: Calculated voltage drop
        - voltage_drop_percent: Voltage drop as percentage
        - nec_compliant: True if all requirements met
        - work_shown: Step-by-step calculation
        - nec_citations: List of NEC references
    """
    work_steps = []
    nec_citations = []

    work_steps.append("=" * 60)
    work_steps.append("FEEDER/CONDUCTOR SIZING CALCULATION")
    work_steps.append("=" * 60)
    work_steps.append("\nInput Parameters:")
    work_steps.append(f"  Load: {load_amps} A")
    work_steps.append(f"  Voltage: {voltage} V, {phases}-phase")
    work_steps.append(f"  Distance: {distance_feet} ft (one-way)")
    work_steps.append(f"  Conductor: {conductor_material.title()}, {conductor_type}")
    work_steps.append(f"  Conduit: {conduit_type}")
    work_steps.append(f"  Ambient Temperature: {temperature}°C")
    work_steps.append(f"  Continuous Load: {'Yes' if continuous_load else 'No'}")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Calculate Required Ampacity")
    work_steps.append("─" * 60)

    if continuous_load:
        required_ampacity = load_amps * 1.25
        work_steps.append(
            "  Per NEC 215.2(A)(1), continuous loads require 125% factor:"
        )
        work_steps.append(
            f"  Required Ampacity = {load_amps} A × 1.25 = {required_ampacity:.1f} A"
        )
        nec_citations.append("NEC 215.2(A)(1) - Continuous load factor (125%)")
    else:
        required_ampacity = load_amps
        work_steps.append("  Non-continuous load, no multiplier required:")
        work_steps.append(f"  Required Ampacity = {load_amps} A")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Determine Insulation Temperature Rating")
    work_steps.append("─" * 60)

    temp_rating = get_insulation_temp_rating(conductor_type)
    work_steps.append(f"  Conductor type: {conductor_type}")
    work_steps.append(f"  Temperature rating: {temp_rating}°C")
    nec_citations.append(f"NEC Table 310.15(B)(16) - Ampacities at {temp_rating}°C")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Temperature Correction Factor")
    work_steps.append("─" * 60)

    temp_correction = get_temp_correction_factor(temperature, temp_rating)
    work_steps.append(f"  Ambient temperature: {temperature}°C")
    work_steps.append("  Per NEC Table 310.15(B)(1):")
    work_steps.append(f"  Temperature correction factor = {temp_correction}")
    nec_citations.append("NEC Table 310.15(B)(1) - Temperature correction factors")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Conductor Adjustment Factor")
    work_steps.append("─" * 60)

    if num_current_carrying <= 3:
        conductor_adjustment = 1.0
        work_steps.append(
            f"  Number of current-carrying conductors: {num_current_carrying}"
        )
        work_steps.append("  3 or fewer conductors - no adjustment required")
        work_steps.append("  Conductor adjustment factor = 1.0")
    else:
        if num_current_carrying <= 6:
            conductor_adjustment = 0.80
        elif num_current_carrying <= 9:
            conductor_adjustment = 0.70
        elif num_current_carrying <= 20:
            conductor_adjustment = 0.50
        elif num_current_carrying <= 30:
            conductor_adjustment = 0.45
        elif num_current_carrying <= 40:
            conductor_adjustment = 0.40
        else:
            conductor_adjustment = 0.35

        work_steps.append(
            f"  Number of current-carrying conductors: {num_current_carrying}"
        )
        work_steps.append("  Per NEC Table 310.15(C)(1):")
        work_steps.append(f"  Conductor adjustment factor = {conductor_adjustment}")
        nec_citations.append(
            "NEC Table 310.15(C)(1) - Adjustment factors for more than 3 conductors"
        )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Calculate Minimum Table Ampacity")
    work_steps.append("─" * 60)

    combined_factor = temp_correction * conductor_adjustment
    min_table_ampacity = required_ampacity / combined_factor

    work_steps.append(
        f"  Combined derating factor = {temp_correction} × {conductor_adjustment} = {combined_factor:.3f}"
    )
    work_steps.append(
        f"  Minimum table ampacity = {required_ampacity:.1f} A / {combined_factor:.3f} = {min_table_ampacity:.1f} A"
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 6: Select Conductor Size (Ampacity)")
    work_steps.append("─" * 60)

    if conductor_material.lower() == "copper":
        ampacity_table = AMPACITY_TABLE_310_15_B_16_COPPER
    else:
        ampacity_table = AMPACITY_TABLE_310_15_B_16_ALUMINUM

    ampacity_selected_size = None
    ampacity_selected_value = None

    for size in CONDUCTOR_SIZES:
        if size in ampacity_table:
            table_ampacity = ampacity_table[size].get(temp_rating)
            if table_ampacity and table_ampacity >= min_table_ampacity:
                ampacity_selected_size = size
                ampacity_selected_value = table_ampacity
                work_steps.append(
                    f"  Checking {size}: {table_ampacity} A >= {min_table_ampacity:.1f} A ✓ SELECTED"
                )
                break
            else:
                if table_ampacity:
                    work_steps.append(
                        f"  Checking {size}: {table_ampacity} A < {min_table_ampacity:.1f} A ✗"
                    )

    if ampacity_selected_size is None:
        return {
            "error": "No standard conductor size meets ampacity requirements",
            "required_ampacity": round(min_table_ampacity, 1),
            "suggestion": "Consider parallel conductors",
            "work_shown": "\n".join(work_steps),
            "nec_citations": nec_citations,
        }

    derated_ampacity = ampacity_selected_value * combined_factor
    work_steps.append(f"\n  Selected for ampacity: {ampacity_selected_size}")
    work_steps.append(f"  Table ampacity: {ampacity_selected_value} A")
    work_steps.append(
        f"  Derated ampacity: {ampacity_selected_value} × {combined_factor:.3f} = {derated_ampacity:.1f} A"
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 7: Voltage Drop Check")
    work_steps.append("─" * 60)

    current_size = ampacity_selected_size
    current_size_index = CONDUCTOR_SIZES.index(current_size)

    vd_result = calculate_voltage_drop(
        conductor_size=current_size,
        length_feet=distance_feet,
        current_amps=load_amps,
        voltage=voltage,
        phases=phases,
        power_factor=power_factor,
        conductor_material=conductor_material,
    )

    work_steps.append(f"  Checking {current_size} for voltage drop:")
    work_steps.append(
        f"  VD = {vd_result['voltage_drop_volts']} V ({vd_result['voltage_drop_percent']}%)"
    )
    work_steps.append(f"  Limit = {max_voltage_drop_percent}%")

    vd_selected_size = current_size
    iterations = 0
    max_iterations = 10

    while (
        vd_result["voltage_drop_percent"] > max_voltage_drop_percent
        and iterations < max_iterations
    ):
        current_size_index += 1
        if current_size_index >= len(CONDUCTOR_SIZES):
            work_steps.append("  ✗ No larger conductor available")
            break

        current_size = CONDUCTOR_SIZES[current_size_index]

        if current_size not in ampacity_table:
            continue

        vd_result = calculate_voltage_drop(
            conductor_size=current_size,
            length_feet=distance_feet,
            current_amps=load_amps,
            voltage=voltage,
            phases=phases,
            power_factor=power_factor,
            conductor_material=conductor_material,
        )

        work_steps.append(
            f"  Upsizing to {current_size}: VD = {vd_result['voltage_drop_percent']}%"
        )
        iterations += 1

    if vd_result["voltage_drop_percent"] <= max_voltage_drop_percent:
        vd_selected_size = current_size
        work_steps.append(f"  ✓ {vd_selected_size} meets voltage drop requirement")
    else:
        work_steps.append(
            f"  ⚠ Voltage drop exceeds {max_voltage_drop_percent}% even with largest conductor"
        )

    nec_citations.extend(
        [
            "NEC 210.19(A)(1) Informational Note No. 4 - Branch circuit voltage drop",
            "NEC 215.2(A)(4) Informational Note No. 2 - Feeder voltage drop",
        ]
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 8: Final Conductor Selection")
    work_steps.append("─" * 60)

    ampacity_index = CONDUCTOR_SIZES.index(ampacity_selected_size)
    vd_index = CONDUCTOR_SIZES.index(vd_selected_size)

    if vd_index > ampacity_index:
        final_size = vd_selected_size
        governing_factor = "voltage drop"
        work_steps.append(f"  Ampacity requires: {ampacity_selected_size}")
        work_steps.append(f"  Voltage drop requires: {vd_selected_size}")
        work_steps.append(f"  FINAL SELECTION: {final_size} (governed by voltage drop)")
    else:
        final_size = ampacity_selected_size
        governing_factor = "ampacity"
        work_steps.append(f"  Ampacity requires: {ampacity_selected_size}")
        work_steps.append(f"  Voltage drop requires: {vd_selected_size}")
        work_steps.append(f"  FINAL SELECTION: {final_size} (governed by ampacity)")

    final_table_ampacity = ampacity_table[final_size].get(temp_rating, 0)
    final_derated_ampacity = final_table_ampacity * combined_factor

    final_vd = calculate_voltage_drop(
        conductor_size=final_size,
        length_feet=distance_feet,
        current_amps=load_amps,
        voltage=voltage,
        phases=phases,
        power_factor=power_factor,
        conductor_material=conductor_material,
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 9: Compliance Summary")
    work_steps.append("─" * 60)

    ampacity_compliant = final_derated_ampacity >= required_ampacity
    vd_compliant = final_vd["voltage_drop_percent"] <= max_voltage_drop_percent
    nec_compliant = ampacity_compliant and vd_compliant

    work_steps.append(
        f"  Conductor: {final_size} AWG/kcmil {conductor_material.title()} {conductor_type}"
    )
    work_steps.append(f"  Table Ampacity: {final_table_ampacity} A")
    work_steps.append(f"  Derated Ampacity: {final_derated_ampacity:.1f} A")
    work_steps.append(f"  Required Ampacity: {required_ampacity:.1f} A")
    work_steps.append(
        f"  Ampacity Check: {'✓ PASS' if ampacity_compliant else '✗ FAIL'}"
    )
    work_steps.append(f"  Voltage Drop: {final_vd['voltage_drop_percent']}%")
    work_steps.append(f"  VD Limit: {max_voltage_drop_percent}%")
    work_steps.append(f"  Voltage Drop Check: {'✓ PASS' if vd_compliant else '✗ FAIL'}")
    work_steps.append(
        f"\n  OVERALL: {'✓ NEC COMPLIANT' if nec_compliant else '✗ NON-COMPLIANT'}"
    )

    work_steps.append(f"\n{'=' * 60}")

    if final_size in ["1/0", "2/0", "3/0", "4/0"]:
        display_size = f"{final_size} AWG"
    elif final_size.isdigit() and int(final_size) <= 4:
        display_size = f"#{final_size} AWG"
    elif final_size.isdigit():
        display_size = f"#{final_size} AWG"
    else:
        display_size = f"{final_size} kcmil"

    return {
        "conductor_size": final_size,
        "conductor_size_display": display_size,
        "conductor_material": conductor_material,
        "conductor_type": conductor_type,
        "table_ampacity": final_table_ampacity,
        "derated_ampacity": round(final_derated_ampacity, 1),
        "required_ampacity": round(required_ampacity, 1),
        "load_amps": load_amps,
        "temperature_correction_factor": temp_correction,
        "conductor_adjustment_factor": conductor_adjustment,
        "combined_derating_factor": round(combined_factor, 3),
        "voltage_drop_volts": final_vd["voltage_drop_volts"],
        "voltage_drop_percent": final_vd["voltage_drop_percent"],
        "max_voltage_drop_percent": max_voltage_drop_percent,
        "receiving_end_voltage": final_vd["receiving_end_voltage"],
        "governing_factor": governing_factor,
        "ampacity_compliant": ampacity_compliant,
        "voltage_drop_compliant": vd_compliant,
        "nec_compliant": nec_compliant,
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }

def calculate_parallel_conductors(
    load_amps: float,
    voltage: int,
    phases: int,
    distance_feet: float,
    conductor_type: str = "THHN",
    conductor_material: str = "copper",
    max_voltage_drop_percent: float = 3.0,
    power_factor: float = 0.85,
) -> Dict:
    """
    Calculate parallel conductor requirements when single conductors are insufficient.

    Per NEC 310.10(G), parallel conductors must be:
    - 1/0 AWG or larger
    - Same length, material, size, insulation, and termination method

    Args:
        load_amps: Total load current in amps
        voltage: System voltage
        phases: Number of phases
        distance_feet: One-way conductor length
        conductor_type: Insulation type
        conductor_material: "copper" or "aluminum"
        max_voltage_drop_percent: Maximum voltage drop
        power_factor: Power factor

    Returns:
        Dictionary with parallel conductor recommendations
    """
    work_steps = []
    nec_citations = ["NEC 310.10(G) - Parallel conductor requirements"]

    work_steps.append("=" * 60)
    work_steps.append("PARALLEL CONDUCTOR CALCULATION")
    work_steps.append("=" * 60)
    work_steps.append(f"\nTotal load: {load_amps} A")

    min_parallel_size = "1/0"
    min_parallel_index = CONDUCTOR_SIZES.index(min_parallel_size)

    work_steps.append(
        f"Per NEC 310.10(G), minimum size for parallel conductors: {min_parallel_size} AWG"
    )

    for num_sets in range(2, 7):  # 2 to 6 parallel sets
        amps_per_conductor = load_amps / num_sets
        work_steps.append(f"\n--- Trying {num_sets} parallel sets ---")
        work_steps.append(
            f"Current per conductor: {load_amps} / {num_sets} = {amps_per_conductor:.1f} A"
        )

        result = calculate(
            load_amps=amps_per_conductor,
            voltage=voltage,
            phases=phases,
            distance_feet=distance_feet,
            conductor_type=conductor_type,
            conductor_material=conductor_material,
            max_voltage_drop_percent=max_voltage_drop_percent,
            power_factor=power_factor,
            continuous_load=True,
        )

        if "error" in result:
            work_steps.append("  No suitable size found")
            continue

        selected_size = result["conductor_size"]
        selected_index = CONDUCTOR_SIZES.index(selected_size)

        if selected_index >= min_parallel_index:
            work_steps.append(f"  Selected size: {selected_size}")
            work_steps.append("  Meets minimum parallel size requirement: ✓")
            work_steps.append(f"  Voltage drop: {result['voltage_drop_percent']}%")

            if result["nec_compliant"]:
                work_steps.append(
                    f"\n✓ SOLUTION FOUND: {num_sets} sets of {selected_size}"
                )

                return {
                    "num_parallel_sets": num_sets,
                    "conductor_size": selected_size,
                    "conductor_material": conductor_material,
                    "conductor_type": conductor_type,
                    "amps_per_conductor": round(amps_per_conductor, 1),
                    "total_load_amps": load_amps,
                    "voltage_drop_percent": result["voltage_drop_percent"],
                    "nec_compliant": True,
                    "work_shown": "\n".join(work_steps),
                    "nec_citations": nec_citations,
                }
        else:
            work_steps.append(
                f"  Selected size {selected_size} < {min_parallel_size} minimum"
            )

    return {
        "error": "Could not find suitable parallel conductor configuration",
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }
