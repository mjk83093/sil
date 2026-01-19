"""
Short Circuit Calculator
========================
Deterministic short circuit analysis calculations.
All calculations are pure Python - NO LLM involvement.
"""

import math
from typing import Dict, Optional

from lib.nec_tables import (
    get_resistance,
)

TRANSFORMER_IMPEDANCE_TYPICAL = {
    15: 2.0,
    25: 2.0,
    37.5: 2.5,
    50: 2.5,
    75: 2.5,
    100: 2.5,
    112.5: 2.5,
    150: 3.0,
    225: 3.5,
    300: 4.0,
    500: 4.5,
    750: 5.0,
    1000: 5.5,
    1500: 5.75,
    2000: 5.75,
    2500: 5.75,
}

def calculate(
    transformer_kva: float,
    transformer_impedance_percent: Optional[float] = None,
    primary_voltage: int = 480,
    secondary_voltage: int = 208,
    conductor_size: str = "500",
    conductor_length_feet: float = 100,
    conductor_material: str = "copper",
    phases: int = 3,
    utility_sca: Optional[float] = None,
) -> Dict:
    """
    Calculate available short circuit current at a point in the system.

    This uses the point-to-point method for calculating short circuit
    currents, which is suitable for most industrial and commercial
    applications.

    Args:
        transformer_kva: Transformer kVA rating
        transformer_impedance_percent: Transformer %Z (if None, uses typical)
        primary_voltage: Primary voltage (V)
        secondary_voltage: Secondary voltage (V)
        conductor_size: Conductor size (AWG or kcmil)
        conductor_length_feet: One-way conductor length (feet)
        conductor_material: "copper" or "aluminum"
        phases: Number of phases (1 or 3)
        utility_sca: Utility available short circuit amps (if known)

    Returns:
        Dictionary with:
        - transformer_fla: Transformer full load amps
        - transformer_sca: Short circuit amps at transformer secondary
        - point_sca: Short circuit amps at calculated point
        - work_shown: Step-by-step calculation
        - nec_citations: List of NEC references
    """
    work_steps = []
    nec_citations = []

    work_steps.append("=" * 60)
    work_steps.append("SHORT CIRCUIT CALCULATION")
    work_steps.append("Point-to-Point Method")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Transformer Parameters")
    work_steps.append("─" * 60)

    if transformer_impedance_percent is None:
        for kva, z in sorted(TRANSFORMER_IMPEDANCE_TYPICAL.items()):
            if transformer_kva <= kva:
                transformer_impedance_percent = z
                break
        else:
            transformer_impedance_percent = 5.75  # Default for large transformers
        work_steps.append(f"  Transformer: {transformer_kva} kVA")
        work_steps.append(
            f"  %Z not specified, using typical value: {transformer_impedance_percent}%"
        )
    else:
        work_steps.append(f"  Transformer: {transformer_kva} kVA")
        work_steps.append(f"  %Z (specified): {transformer_impedance_percent}%")

    work_steps.append(f"  Primary voltage: {primary_voltage} V")
    work_steps.append(f"  Secondary voltage: {secondary_voltage} V")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Transformer Full Load Amps (FLA)")
    work_steps.append("─" * 60)

    if phases == 3:
        sqrt3 = math.sqrt(3)
        transformer_fla = (transformer_kva * 1000) / (sqrt3 * secondary_voltage)
        work_steps.append("  Three-phase formula: FLA = kVA × 1000 / (√3 × V)")
        work_steps.append(
            f"  FLA = {transformer_kva} × 1000 / ({sqrt3:.4f} × {secondary_voltage})"
        )
    else:
        transformer_fla = (transformer_kva * 1000) / secondary_voltage
        work_steps.append("  Single-phase formula: FLA = kVA × 1000 / V")
        work_steps.append(f"  FLA = {transformer_kva} × 1000 / {secondary_voltage}")

    work_steps.append(f"  FLA = {transformer_fla:.1f} A")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Short Circuit Current at Transformer Secondary")
    work_steps.append("─" * 60)

    transformer_sca = transformer_fla * 100 / transformer_impedance_percent

    work_steps.append("  Formula: SCA = FLA × 100 / %Z")
    work_steps.append(
        f"  SCA = {transformer_fla:.1f} × 100 / {transformer_impedance_percent}"
    )
    work_steps.append(f"  SCA = {transformer_sca:,.0f} A")

    if utility_sca is not None:
        work_steps.append(f"\n  Utility available SCA: {utility_sca:,.0f} A")
        combined_sca = 1 / (1 / transformer_sca + 1 / utility_sca)
        work_steps.append(
            f"  Combined SCA = 1 / (1/{transformer_sca:,.0f} + 1/{utility_sca:,.0f})"
        )
        work_steps.append(f"  Combined SCA = {combined_sca:,.0f} A")
        transformer_sca = combined_sca

    nec_citations.append("IEEE 141 (Red Book) - Short circuit calculations")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Conductor Impedance")
    work_steps.append("─" * 60)

    resistance_per_1000ft = get_resistance(conductor_size, conductor_material)

    if resistance_per_1000ft is None:
        return {
            "error": f"Conductor size '{conductor_size}' not found",
            "work_shown": "\n".join(work_steps),
            "nec_citations": nec_citations,
        }

    total_resistance = 2 * conductor_length_feet * resistance_per_1000ft / 1000

    work_steps.append(f"  Conductor: {conductor_size} {conductor_material}")
    work_steps.append(f"  Length: {conductor_length_feet} ft (one-way)")
    work_steps.append(f"  Resistance: {resistance_per_1000ft} Ω/1000 ft")
    work_steps.append(
        f"  Total R = 2 × {conductor_length_feet} × {resistance_per_1000ft} / 1000"
    )
    work_steps.append(f"  Total R = {total_resistance:.6f} Ω")

    reactance_per_1000ft = 0.05
    total_reactance = 2 * conductor_length_feet * reactance_per_1000ft / 1000
    work_steps.append(
        f"  Estimated X = {total_reactance:.6f} Ω (typical for steel conduit)"
    )

    total_impedance = math.sqrt(total_resistance**2 + total_reactance**2)
    work_steps.append(
        f"  Total Z = √(R² + X²) = √({total_resistance:.6f}² + {total_reactance:.6f}²)"
    )
    work_steps.append(f"  Total Z = {total_impedance:.6f} Ω")

    nec_citations.append("NEC Chapter 9 Table 8 - Conductor Properties")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Short Circuit Current at Point")
    work_steps.append("─" * 60)

    if phases == 3:
        voltage_ln = secondary_voltage / math.sqrt(3)
        work_steps.append(
            f"  Line-to-neutral voltage: {secondary_voltage} / √3 = {voltage_ln:.1f} V"
        )
    else:
        voltage_ln = secondary_voltage / 2  # For 120/240V single-phase
        work_steps.append(f"  Line-to-neutral voltage: {voltage_ln:.1f} V")

    transformer_z_ohms = voltage_ln / transformer_sca
    work_steps.append(
        f"  Transformer Z = V_LN / SCA = {voltage_ln:.1f} / {transformer_sca:,.0f}"
    )
    work_steps.append(f"  Transformer Z = {transformer_z_ohms:.6f} Ω")

    total_system_z = transformer_z_ohms + total_impedance
    work_steps.append(
        f"  Total system Z = {transformer_z_ohms:.6f} + {total_impedance:.6f}"
    )
    work_steps.append(f"  Total system Z = {total_system_z:.6f} Ω")

    point_sca = voltage_ln / total_system_z
    work_steps.append("\n  SCA at point = V_LN / Z_total")
    work_steps.append(f"  SCA at point = {voltage_ln:.1f} / {total_system_z:.6f}")
    work_steps.append(f"  SCA at point = {point_sca:,.0f} A")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 6: M Factor (Reduction from Transformer)")
    work_steps.append("─" * 60)

    m_factor = point_sca / transformer_sca
    work_steps.append("  M = SCA_point / SCA_transformer")
    work_steps.append(f"  M = {point_sca:,.0f} / {transformer_sca:,.0f}")
    work_steps.append(f"  M = {m_factor:.3f} ({m_factor * 100:.1f}%)")

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("SHORT CIRCUIT CALCULATION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(
        f"  Transformer: {transformer_kva} kVA, {transformer_impedance_percent}%Z"
    )
    work_steps.append(f"  Transformer FLA: {transformer_fla:.1f} A")
    work_steps.append(f"  SCA at transformer: {transformer_sca:,.0f} A")
    work_steps.append(
        f"  Conductor: {conductor_size} {conductor_material}, {conductor_length_feet} ft"
    )
    work_steps.append(f"  SCA at point: {point_sca:,.0f} A")
    work_steps.append(f"  Reduction factor: {m_factor:.1%}")
    work_steps.append("=" * 60)

    work_steps.append("\n  Equipment AIC Rating Guidance:")
    if point_sca <= 10000:
        work_steps.append("  Standard 10 kAIC equipment is adequate")
    elif point_sca <= 14000:
        work_steps.append("  Minimum 14 kAIC equipment required")
    elif point_sca <= 22000:
        work_steps.append("  Minimum 22 kAIC equipment required")
    elif point_sca <= 42000:
        work_steps.append("  Minimum 42 kAIC equipment required")
    elif point_sca <= 65000:
        work_steps.append("  Minimum 65 kAIC equipment required")
    else:
        work_steps.append("  High AIC equipment required (>65 kAIC)")

    nec_citations.append("NEC 110.9 - Interrupting Rating")
    nec_citations.append(
        "NEC 110.10 - Circuit Impedance, Short-Circuit Current Ratings"
    )

    return {
        "transformer_kva": transformer_kva,
        "transformer_impedance_percent": transformer_impedance_percent,
        "primary_voltage": primary_voltage,
        "secondary_voltage": secondary_voltage,
        "phases": phases,
        "transformer_fla": round(transformer_fla, 1),
        "transformer_sca": round(transformer_sca, 0),
        "conductor_size": conductor_size,
        "conductor_material": conductor_material,
        "conductor_length_feet": conductor_length_feet,
        "conductor_resistance_ohms": round(total_resistance, 6),
        "conductor_impedance_ohms": round(total_impedance, 6),
        "point_sca": round(point_sca, 0),
        "m_factor": round(m_factor, 3),
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }

def calculate_motor_contribution(
    motor_hp: float,
    motor_voltage: int = 480,
    motor_efficiency: float = 0.90,
    motor_power_factor: float = 0.85,
    phases: int = 3,
) -> Dict:
    """
    Calculate motor contribution to short circuit current.

    Motors contribute to fault current during the first few cycles
    of a fault. This is typically 4-6 times the motor FLA.

    Args:
        motor_hp: Motor horsepower
        motor_voltage: Motor voltage
        motor_efficiency: Motor efficiency (decimal)
        motor_power_factor: Motor power factor (decimal)
        phases: Number of phases

    Returns:
        Dictionary with motor contribution calculations
    """
    work_steps = []
    nec_citations = []

    work_steps.append("=" * 60)
    work_steps.append("MOTOR SHORT CIRCUIT CONTRIBUTION")
    work_steps.append("=" * 60)

    if phases == 3:
        sqrt3 = math.sqrt(3)
        motor_fla = (motor_hp * 746) / (
            sqrt3 * motor_voltage * motor_efficiency * motor_power_factor
        )
        work_steps.append(f"  Motor: {motor_hp} HP, {motor_voltage}V, 3-phase")
        work_steps.append("  FLA = HP × 746 / (√3 × V × eff × pf)")
        work_steps.append(
            f"  FLA = {motor_hp} × 746 / ({sqrt3:.4f} × {motor_voltage} × {motor_efficiency} × {motor_power_factor})"
        )
    else:
        motor_fla = (motor_hp * 746) / (
            motor_voltage * motor_efficiency * motor_power_factor
        )
        work_steps.append(f"  Motor: {motor_hp} HP, {motor_voltage}V, 1-phase")
        work_steps.append("  FLA = HP × 746 / (V × eff × pf)")

    work_steps.append(f"  FLA = {motor_fla:.1f} A")

    motor_contribution_multiplier = 4.0
    motor_sca_contribution = motor_fla * motor_contribution_multiplier

    work_steps.append(
        f"\n  Motor contribution multiplier: {motor_contribution_multiplier}×"
    )
    work_steps.append(
        f"  Motor SCA contribution = {motor_fla:.1f} × {motor_contribution_multiplier}"
    )
    work_steps.append(f"  Motor SCA contribution = {motor_sca_contribution:.0f} A")

    nec_citations.append("IEEE 141 - Motor contribution to short circuit")

    return {
        "motor_hp": motor_hp,
        "motor_voltage": motor_voltage,
        "motor_fla": round(motor_fla, 1),
        "contribution_multiplier": motor_contribution_multiplier,
        "motor_sca_contribution": round(motor_sca_contribution, 0),
        "work_shown": "\n".join(work_steps),
        "nec_citations": nec_citations,
    }
