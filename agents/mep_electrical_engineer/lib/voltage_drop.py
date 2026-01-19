"""
Voltage Drop Calculator
=======================
Deterministic voltage drop calculations per NEC requirements.
All calculations are pure Python - NO LLM involvement.
"""

import math
from typing import Dict

from lib.nec_tables import (
    get_resistance,
    CONDUCTOR_RESISTANCE_COPPER,
    CONDUCTOR_RESISTANCE_ALUMINUM,
)

def calculate(
    conductor_size: str,
    length_feet: float,
    current_amps: float,
    voltage: int,
    phases: int = 3,
    power_factor: float = 0.85,
    conductor_material: str = "copper",
) -> Dict:
    """
    Calculate voltage drop for a conductor run.

    Formulas:
    - Single-phase: VD = 2 * I * L * R / 1000
    - Three-phase: VD = √3 * I * L * R / 1000

    Where:
    - I = current in amps
    - L = one-way length in feet
    - R = resistance in ohms per 1000 feet

    Args:
        conductor_size: AWG or kcmil size (e.g., "10", "1/0", "250")
        length_feet: One-way conductor length in feet
        current_amps: Load current in amps
        voltage: System voltage (e.g., 120, 208, 277, 480)
        phases: 1 for single-phase, 3 for three-phase
        power_factor: Power factor (0.0 to 1.0), default 0.85
        conductor_material: "copper" or "aluminum"

    Returns:
        Dictionary with:
        - voltage_drop_volts: Voltage drop in volts
        - voltage_drop_percent: Voltage drop as percentage
        - receiving_end_voltage: Voltage at load end
        - nec_compliant_branch: True if < 3% (branch circuit limit)
        - nec_compliant_feeder: True if < 3% (feeder limit)
        - nec_compliant_total: True if < 5% (total system limit)
        - work_shown: Step-by-step calculation
        - nec_citations: List of NEC references
    """
    work_steps = []
    nec_citations = []

    resistance = get_resistance(conductor_size, conductor_material)

    if resistance is None:
        return {
            "error": f"Conductor size '{conductor_size}' not found in NEC tables",
            "valid_sizes": list(CONDUCTOR_RESISTANCE_COPPER.keys()),
            "work_shown": "",
            "nec_citations": ["NEC Chapter 9 Table 8"],
        }

    work_steps.append("Step 1: Look up conductor resistance from NEC Chapter 9 Table 8")
    work_steps.append(f"  Conductor: {conductor_size} AWG/kcmil {conductor_material}")
    work_steps.append(f"  Resistance (R) = {resistance} Ω per 1000 ft")
    nec_citations.append("NEC Chapter 9 Table 8 - Conductor Properties")

    work_steps.append("\nStep 2: Calculate voltage drop")
    work_steps.append(f"  Current (I) = {current_amps} A")
    work_steps.append(f"  Length (L) = {length_feet} ft (one-way)")
    work_steps.append(f"  Power Factor (PF) = {power_factor}")

    if phases == 1:
        voltage_drop = (
            2 * current_amps * length_feet * resistance * power_factor
        ) / 1000
        work_steps.append("\n  Single-phase voltage drop formula:")
        work_steps.append("  VD = 2 × I × L × R × PF / 1000")
        work_steps.append(
            f"  VD = 2 × {current_amps} × {length_feet} × {resistance} × {power_factor} / 1000"
        )
        work_steps.append(
            f"  VD = {2 * current_amps * length_feet * resistance * power_factor:.4f} / 1000"
        )
    else:
        sqrt3 = math.sqrt(3)
        voltage_drop = (
            sqrt3 * current_amps * length_feet * resistance * power_factor
        ) / 1000
        work_steps.append("\n  Three-phase voltage drop formula:")
        work_steps.append("  VD = √3 × I × L × R × PF / 1000")
        work_steps.append(
            f"  VD = {sqrt3:.4f} × {current_amps} × {length_feet} × {resistance} × {power_factor} / 1000"
        )
        work_steps.append(
            f"  VD = {sqrt3 * current_amps * length_feet * resistance * power_factor:.4f} / 1000"
        )

    work_steps.append(f"  VD = {voltage_drop:.2f} V")

    voltage_drop_percent = (voltage_drop / voltage) * 100
    receiving_end_voltage = voltage - voltage_drop

    work_steps.append("\nStep 3: Calculate voltage drop percentage")
    work_steps.append(f"  System voltage = {voltage} V")
    work_steps.append("  VD% = (VD / V) × 100")
    work_steps.append(f"  VD% = ({voltage_drop:.2f} / {voltage}) × 100")
    work_steps.append(f"  VD% = {voltage_drop_percent:.2f}%")
    work_steps.append(
        f"\n  Receiving end voltage = {voltage} - {voltage_drop:.2f} = {receiving_end_voltage:.2f} V"
    )

    nec_compliant_branch = voltage_drop_percent <= 3.0
    nec_compliant_feeder = voltage_drop_percent <= 3.0
    nec_compliant_total = voltage_drop_percent <= 5.0

    work_steps.append("\nStep 4: NEC Compliance Check")
    work_steps.append("  NEC 210.19(A)(1) Informational Note No. 4:")
    work_steps.append("    Branch circuit voltage drop limit: 3%")
    work_steps.append(
        f"    Result: {voltage_drop_percent:.2f}% {'≤' if nec_compliant_branch else '>'} 3% → {'COMPLIANT' if nec_compliant_branch else 'NON-COMPLIANT'}"
    )
    work_steps.append("  NEC 215.2(A)(4) Informational Note No. 2:")
    work_steps.append("    Feeder voltage drop limit: 3%")
    work_steps.append(
        f"    Result: {voltage_drop_percent:.2f}% {'≤' if nec_compliant_feeder else '>'} 3% → {'COMPLIANT' if nec_compliant_feeder else 'NON-COMPLIANT'}"
    )
    work_steps.append("  Total system voltage drop limit: 5%")
    work_steps.append(
        f"    Result: {voltage_drop_percent:.2f}% {'≤' if nec_compliant_total else '>'} 5% → {'COMPLIANT' if nec_compliant_total else 'NON-COMPLIANT'}"
    )

    nec_citations.extend(
        [
            "NEC 210.19(A)(1) Informational Note No. 4 - Branch circuit voltage drop",
            "NEC 215.2(A)(4) Informational Note No. 2 - Feeder voltage drop",
        ]
    )

    return {
        "conductor_size": conductor_size,
        "conductor_material": conductor_material,
        "resistance_per_1000ft": resistance,
        "length_feet": length_feet,
        "current_amps": current_amps,
        "voltage": voltage,
        "phases": phases,
        "power_factor": power_factor,
        "voltage_drop_volts": round(voltage_drop, 2),
        "voltage_drop_percent": round(voltage_drop_percent, 2),
        "receiving_end_voltage": round(receiving_end_voltage, 2),
        "nec_compliant_branch": nec_compliant_branch,
        "nec_compliant_feeder": nec_compliant_feeder,
        "nec_compliant_total": nec_compliant_total,
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }

def calculate_required_size(
    length_feet: float,
    current_amps: float,
    voltage: int,
    max_voltage_drop_percent: float = 3.0,
    phases: int = 3,
    power_factor: float = 0.85,
    conductor_material: str = "copper",
) -> Dict:
    """
    Calculate the minimum conductor size required to meet voltage drop limits.

    Args:
        length_feet: One-way conductor length in feet
        current_amps: Load current in amps
        voltage: System voltage
        max_voltage_drop_percent: Maximum allowable voltage drop (default 3%)
        phases: 1 for single-phase, 3 for three-phase
        power_factor: Power factor (default 0.85)
        conductor_material: "copper" or "aluminum"

    Returns:
        Dictionary with recommended conductor size and calculations
    """
    work_steps = []
    nec_citations = ["NEC Chapter 9 Table 8 - Conductor Properties"]

    max_vd_volts = (max_voltage_drop_percent / 100) * voltage

    work_steps.append("Step 1: Calculate maximum allowable voltage drop")
    work_steps.append(f"  Max VD% = {max_voltage_drop_percent}%")
    work_steps.append(
        f"  Max VD = {max_voltage_drop_percent}% × {voltage}V = {max_vd_volts:.2f}V"
    )

    work_steps.append("\nStep 2: Calculate required maximum resistance")

    if phases == 1:
        max_resistance = (max_vd_volts * 1000) / (
            2 * current_amps * length_feet * power_factor
        )
        work_steps.append("  Single-phase: R_max = VD × 1000 / (2 × I × L × PF)")
        work_steps.append(
            f"  R_max = {max_vd_volts:.2f} × 1000 / (2 × {current_amps} × {length_feet} × {power_factor})"
        )
    else:
        sqrt3 = math.sqrt(3)
        max_resistance = (max_vd_volts * 1000) / (
            sqrt3 * current_amps * length_feet * power_factor
        )
        work_steps.append("  Three-phase: R_max = VD × 1000 / (√3 × I × L × PF)")
        work_steps.append(
            f"  R_max = {max_vd_volts:.2f} × 1000 / ({sqrt3:.4f} × {current_amps} × {length_feet} × {power_factor})"
        )

    work_steps.append(f"  R_max = {max_resistance:.4f} Ω per 1000 ft")

    work_steps.append("\nStep 3: Select conductor from NEC Chapter 9 Table 8")

    if conductor_material.lower() == "copper":
        resistance_table = CONDUCTOR_RESISTANCE_COPPER
    else:
        resistance_table = CONDUCTOR_RESISTANCE_ALUMINUM

    sorted_sizes = sorted(resistance_table.items(), key=lambda x: x[1], reverse=True)

    selected_size = None
    selected_resistance = None

    for size, resistance in sorted_sizes:
        if resistance <= max_resistance:
            selected_size = size
            selected_resistance = resistance
            work_steps.append(
                f"  {size} AWG/kcmil: R = {resistance} Ω/1000ft {'≤' if resistance <= max_resistance else '>'} {max_resistance:.4f} → {'SELECTED' if size == selected_size else 'OK'}"
            )
            break
        else:
            work_steps.append(
                f"  {size} AWG/kcmil: R = {resistance} Ω/1000ft > {max_resistance:.4f} → Too small"
            )

    if selected_size is None:
        return {
            "error": "No standard conductor size meets the voltage drop requirement",
            "max_resistance_required": round(max_resistance, 4),
            "suggestion": "Consider parallel conductors or shorter run length",
            "work_shown": "\n".join(work_steps),
            "nec_citations": nec_citations,
        }

    verification = calculate(
        conductor_size=selected_size,
        length_feet=length_feet,
        current_amps=current_amps,
        voltage=voltage,
        phases=phases,
        power_factor=power_factor,
        conductor_material=conductor_material,
    )

    work_steps.append("\nStep 4: Verify selection")
    work_steps.append(f"  Selected: {selected_size} AWG/kcmil {conductor_material}")
    work_steps.append(
        f"  Actual VD = {verification['voltage_drop_volts']}V ({verification['voltage_drop_percent']}%)"
    )
    work_steps.append(f"  Limit = {max_vd_volts:.2f}V ({max_voltage_drop_percent}%)")
    work_steps.append(
        f"  Result: {'COMPLIANT' if verification['voltage_drop_percent'] <= max_voltage_drop_percent else 'NON-COMPLIANT'}"
    )

    return {
        "recommended_size": selected_size,
        "conductor_material": conductor_material,
        "resistance_per_1000ft": selected_resistance,
        "calculated_voltage_drop_volts": verification["voltage_drop_volts"],
        "calculated_voltage_drop_percent": verification["voltage_drop_percent"],
        "max_voltage_drop_percent": max_voltage_drop_percent,
        "compliant": verification["voltage_drop_percent"] <= max_voltage_drop_percent,
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }
