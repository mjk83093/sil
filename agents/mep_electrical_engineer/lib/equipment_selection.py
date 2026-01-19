"""
Equipment Selection Tools
=========================
Deterministic equipment selection based on load requirements and NEC compliance.
All calculations are pure Python - NO LLM involvement.

These tools help engineers select appropriate electrical equipment:
- Panelboards
- Transformers
- Disconnect switches
- Conduit
- Conductors/cables
"""

import math
from typing import Dict, List, Optional, Tuple

from lib.nec_tables import (
    get_resistance,
    get_temp_correction_factor,
    get_conductor_adjustment_factor,
    get_insulation_temp_rating,
    CONDUCTOR_SIZES,
    CONDUIT_AREA,
    AMPACITY_TABLE_310_15_B_16_COPPER,
    AMPACITY_TABLE_310_15_B_16_ALUMINUM,
)

STANDARD_PANEL_SIZES = [100, 125, 150, 200, 225, 400, 600, 800, 1200]
STANDARD_TRANSFORMER_KVA = [
    15,
    25,
    37.5,
    45,
    75,
    112.5,
    150,
    225,
    300,
    500,
    750,
    1000,
    1500,
    2000,
    2500,
]
STANDARD_DISCONNECT_SIZES = [30, 60, 100, 200, 400, 600, 800, 1200]
STANDARD_CONDUIT_SIZES = [
    "1/2",
    "3/4",
    "1",
    "1-1/4",
    "1-1/2",
    "2",
    "2-1/2",
    "3",
    "3-1/2",
    "4",
]
STANDARD_BREAKER_SIZES = [
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
]

STANDARD_PANEL_SPACES = [12, 18, 24, 30, 42, 54, 60, 72, 84]

TRANSFORMER_IMPEDANCE = {
    15: 3.0,
    25: 3.5,
    37.5: 4.0,
    45: 4.0,
    75: 4.5,
    112.5: 4.5,
    150: 5.0,
    225: 5.0,
    300: 5.5,
    500: 5.75,
    750: 5.75,
    1000: 5.75,
    1500: 5.75,
    2000: 5.75,
    2500: 6.0,
}

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

def select_panelboard(
    total_load_va: float,
    voltage: int,
    phases: int,
    num_circuits: int,
    main_breaker: bool = True,
    aic_rating: int = 10000,
) -> Dict:
    """
    Select appropriate panelboard based on load requirements.

    Per NEC 408.36, panelboards must be protected by an overcurrent device
    having a rating not greater than that of the panelboard.

    Args:
        total_load_va: Total connected load in VA
        voltage: System voltage (120, 208, 240, 277, 480)
        phases: Number of phases (1 or 3)
        num_circuits: Number of branch circuits required
        main_breaker: True for main breaker panel, False for main lug only
        aic_rating: Required AIC (Ampere Interrupting Capacity) rating

    Returns:
        Dictionary with:
        - recommended_panel_amps: Standard panel size
        - main_breaker_amps: Main breaker size
        - bus_rating: Bus ampacity
        - spaces_required: Number of circuit spaces needed
        - recommended_spaces: Standard panel spaces
        - aic_rating: Required AIC rating
        - nec_references: List of applicable NEC articles
    """
    work_steps = []
    nec_references = []

    work_steps.append("=" * 60)
    work_steps.append("PANELBOARD SELECTION")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Calculate Load Current")
    work_steps.append("─" * 60)

    if phases == 1:
        load_amps = total_load_va / voltage
        work_steps.append("  Single-phase calculation:")
        work_steps.append(
            f"  I = VA / V = {total_load_va:,.0f} / {voltage} = {load_amps:.1f} A"
        )
    else:
        sqrt3 = math.sqrt(3)
        load_amps = total_load_va / (voltage * sqrt3)
        work_steps.append("  Three-phase calculation:")
        work_steps.append(
            f"  I = VA / (V × √3) = {total_load_va:,.0f} / ({voltage} × {sqrt3:.3f})"
        )
        work_steps.append(f"  I = {load_amps:.1f} A")

    nec_references.append(
        "NEC 220 - Branch-Circuit, Feeder, and Service Load Calculations"
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Apply Continuous Load Factor")
    work_steps.append("─" * 60)

    design_amps = load_amps * 1.25
    work_steps.append("  Per NEC 408.36, assuming continuous load:")
    work_steps.append(
        f"  Design current = {load_amps:.1f} × 1.25 = {design_amps:.1f} A"
    )
    nec_references.append("NEC 408.36 - Overcurrent Protection")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Select Panel Size")
    work_steps.append("─" * 60)

    recommended_panel_amps = None
    for size in STANDARD_PANEL_SIZES:
        if size >= design_amps:
            recommended_panel_amps = size
            work_steps.append(
                f"  Checking {size}A panel: {size} >= {design_amps:.1f} ✓"
            )
            break
        else:
            work_steps.append(f"  Checking {size}A panel: {size} < {design_amps:.1f} ✗")

    if recommended_panel_amps is None:
        recommended_panel_amps = STANDARD_PANEL_SIZES[-1]
        work_steps.append(
            f"  Load exceeds standard sizes, using maximum: {recommended_panel_amps}A"
        )
        work_steps.append("  Consider using switchboard or multiple panels")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Determine Main Breaker Size")
    work_steps.append("─" * 60)

    if main_breaker:
        main_breaker_amps = None
        for size in STANDARD_BREAKER_SIZES:
            if size >= design_amps and size <= recommended_panel_amps:
                main_breaker_amps = size
                break

        if main_breaker_amps is None:
            main_breaker_amps = recommended_panel_amps

        work_steps.append("  Main breaker panel selected")
        work_steps.append(f"  Main breaker size: {main_breaker_amps}A")
    else:
        main_breaker_amps = None
        work_steps.append("  Main lug only (MLO) panel selected")
        work_steps.append("  Upstream protection required per NEC 408.36(A)")

    nec_references.append("NEC 408.36(A) - Panelboard Protection")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Calculate Panel Spaces")
    work_steps.append("─" * 60)

    if phases == 1:
        spaces_required = int(num_circuits * 1.2)  # 20% buffer for 2-pole
    else:
        spaces_required = int(num_circuits * 1.5)  # 50% buffer for multi-pole

    spaces_with_spare = int(spaces_required * 1.2)

    work_steps.append(f"  Circuits required: {num_circuits}")
    work_steps.append(f"  Spaces for multi-pole breakers: {spaces_required}")
    work_steps.append(f"  With 20% spare capacity: {spaces_with_spare}")

    recommended_spaces = None
    for spaces in STANDARD_PANEL_SPACES:
        if spaces >= spaces_with_spare:
            recommended_spaces = spaces
            break

    if recommended_spaces is None:
        recommended_spaces = STANDARD_PANEL_SPACES[-1]

    work_steps.append(f"  Recommended panel spaces: {recommended_spaces}")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 6: Verify AIC Rating")
    work_steps.append("─" * 60)

    standard_aic_ratings = [
        10000,
        14000,
        18000,
        22000,
        25000,
        35000,
        42000,
        65000,
        100000,
    ]
    recommended_aic = None
    for aic in standard_aic_ratings:
        if aic >= aic_rating:
            recommended_aic = aic
            break

    if recommended_aic is None:
        recommended_aic = standard_aic_ratings[-1]

    work_steps.append(f"  Required AIC: {aic_rating:,} A")
    work_steps.append(f"  Recommended AIC: {recommended_aic:,} A")
    work_steps.append(
        "  Per NEC 110.9, equipment must have adequate interrupting rating"
    )
    nec_references.append("NEC 110.9 - Interrupting Rating")

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("PANELBOARD SELECTION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(
        f"  Panel Rating: {recommended_panel_amps}A, {phases}-phase, {voltage}V"
    )
    work_steps.append(
        f"  Main Breaker: {main_breaker_amps}A"
        if main_breaker
        else "  Main Lug Only (MLO)"
    )
    work_steps.append(f"  Bus Rating: {recommended_panel_amps}A")
    work_steps.append(f"  Panel Spaces: {recommended_spaces}")
    work_steps.append(f"  AIC Rating: {recommended_aic:,}A")

    return {
        "recommended_panel_amps": recommended_panel_amps,
        "main_breaker_amps": main_breaker_amps,
        "bus_rating": recommended_panel_amps,
        "spaces_required": spaces_required,
        "recommended_spaces": recommended_spaces,
        "aic_rating": recommended_aic,
        "load_amps": round(load_amps, 1),
        "design_amps": round(design_amps, 1),
        "voltage": voltage,
        "phases": phases,
        "work_shown": "\n".join(work_steps),
        "nec_references": nec_references,
    }

def select_transformer(
    load_kva: float,
    primary_voltage: int,
    secondary_voltage: int,
    phases: int = 3,
    application: str = "general",  # "general", "k-rated", "drive-isolation"
) -> Dict:
    """
    Select appropriate transformer based on load.

    Per NEC 450.3, transformer overcurrent protection is based on
    primary and secondary current ratings.

    Args:
        load_kva: Connected load in kVA
        primary_voltage: Primary voltage (e.g., 480, 4160, 13800)
        secondary_voltage: Secondary voltage (e.g., 208, 480)
        phases: Number of phases (1 or 3)
        application: "general", "k-rated" (for harmonics), "drive-isolation"

    Returns:
        Dictionary with:
        - recommended_kva: Standard transformer size
        - primary_fla: Primary full load amps
        - secondary_fla: Secondary full load amps
        - typical_impedance: Typical %Z for this size
        - primary_ocpd: Primary overcurrent protection size
        - secondary_ocpd: Secondary overcurrent protection size
        - nec_references: List of applicable NEC articles
    """
    work_steps = []
    nec_references = []

    work_steps.append("=" * 60)
    work_steps.append("TRANSFORMER SELECTION")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Determine Sizing Factor")
    work_steps.append("─" * 60)

    if application == "k-rated":
        sizing_factor = 1.15  # 15% derating for harmonics
        work_steps.append("  Application: K-rated (harmonic loads)")
        work_steps.append("  Sizing factor: 1.15 (15% derating for harmonics)")
    elif application == "drive-isolation":
        sizing_factor = 1.25  # 25% for drive applications
        work_steps.append("  Application: Drive isolation")
        work_steps.append("  Sizing factor: 1.25 (25% for VFD applications)")
    else:
        sizing_factor = 1.0
        work_steps.append("  Application: General purpose")
        work_steps.append("  Sizing factor: 1.0")

    design_kva = load_kva * sizing_factor
    work_steps.append(
        f"  Design kVA = {load_kva} × {sizing_factor} = {design_kva:.1f} kVA"
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Select Standard Transformer Size")
    work_steps.append("─" * 60)

    recommended_kva = None
    for kva in STANDARD_TRANSFORMER_KVA:
        if kva >= design_kva:
            recommended_kva = kva
            work_steps.append(f"  Checking {kva} kVA: {kva} >= {design_kva:.1f} ✓")
            break
        else:
            work_steps.append(f"  Checking {kva} kVA: {kva} < {design_kva:.1f} ✗")

    if recommended_kva is None:
        recommended_kva = STANDARD_TRANSFORMER_KVA[-1]
        work_steps.append(
            f"  Load exceeds standard sizes, using maximum: {recommended_kva} kVA"
        )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Calculate Full Load Currents")
    work_steps.append("─" * 60)

    if phases == 1:
        primary_fla = (recommended_kva * 1000) / primary_voltage
        secondary_fla = (recommended_kva * 1000) / secondary_voltage
        work_steps.append("  Single-phase transformer")
        work_steps.append(
            f"  Primary FLA = {recommended_kva} × 1000 / {primary_voltage} = {primary_fla:.1f} A"
        )
        work_steps.append(
            f"  Secondary FLA = {recommended_kva} × 1000 / {secondary_voltage} = {secondary_fla:.1f} A"
        )
    else:
        sqrt3 = math.sqrt(3)
        primary_fla = (recommended_kva * 1000) / (primary_voltage * sqrt3)
        secondary_fla = (recommended_kva * 1000) / (secondary_voltage * sqrt3)
        work_steps.append("  Three-phase transformer")
        work_steps.append(
            f"  Primary FLA = {recommended_kva} × 1000 / ({primary_voltage} × √3) = {primary_fla:.1f} A"
        )
        work_steps.append(
            f"  Secondary FLA = {recommended_kva} × 1000 / ({secondary_voltage} × √3) = {secondary_fla:.1f} A"
        )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Typical Impedance")
    work_steps.append("─" * 60)

    typical_impedance = TRANSFORMER_IMPEDANCE.get(recommended_kva, 5.75)
    work_steps.append(f"  Typical %Z for {recommended_kva} kVA: {typical_impedance}%")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Overcurrent Protection (NEC 450.3)")
    work_steps.append("─" * 60)

    nec_references.append("NEC 450.3 - Overcurrent Protection")

    if primary_voltage <= 600:
        work_steps.append("  Per NEC Table 450.3(B) (≤600V):")

        primary_ocpd_calc = primary_fla * 1.25
        primary_ocpd = _select_standard_ocpd(primary_ocpd_calc)

        if primary_ocpd > primary_fla * 1.25:
            max_primary = primary_fla * 2.50
            if primary_ocpd > max_primary:
                primary_ocpd = _select_standard_ocpd(max_primary, round_down=True)

        work_steps.append(
            f"  Primary OCPD: {primary_fla:.1f} × 125% = {primary_ocpd_calc:.1f}A → {primary_ocpd}A"
        )

        secondary_ocpd_calc = secondary_fla * 1.25
        secondary_ocpd = _select_standard_ocpd(secondary_ocpd_calc)
        work_steps.append(
            f"  Secondary OCPD: {secondary_fla:.1f} × 125% = {secondary_ocpd_calc:.1f}A → {secondary_ocpd}A"
        )

        nec_references.append(
            "NEC Table 450.3(B) - Maximum Rating for Transformers 600V or Less"
        )
    else:
        work_steps.append("  Per NEC Table 450.3(A) (>600V):")

        if typical_impedance <= 6:
            primary_multiplier = 3.0  # 300% for impedance ≤6%
        else:
            primary_multiplier = 2.5  # 250% for impedance >6%

        primary_ocpd_calc = primary_fla * primary_multiplier
        primary_ocpd = _select_standard_ocpd(primary_ocpd_calc, round_down=True)
        work_steps.append(
            f"  Primary OCPD: {primary_fla:.1f} × {primary_multiplier * 100:.0f}% = {primary_ocpd}A"
        )

        secondary_ocpd_calc = secondary_fla * 1.25
        secondary_ocpd = _select_standard_ocpd(secondary_ocpd_calc)
        work_steps.append(
            f"  Secondary OCPD: {secondary_fla:.1f} × 125% = {secondary_ocpd}A"
        )

        nec_references.append(
            "NEC Table 450.3(A) - Maximum Rating for Transformers Over 600V"
        )

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("TRANSFORMER SELECTION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(f"  Recommended Size: {recommended_kva} kVA")
    work_steps.append(f"  Primary: {primary_voltage}V, {primary_fla:.1f}A FLA")
    work_steps.append(f"  Secondary: {secondary_voltage}V, {secondary_fla:.1f}A FLA")
    work_steps.append(f"  Typical Impedance: {typical_impedance}%")
    work_steps.append(f"  Primary OCPD: {primary_ocpd}A")
    work_steps.append(f"  Secondary OCPD: {secondary_ocpd}A")

    return {
        "recommended_kva": recommended_kva,
        "load_kva": load_kva,
        "design_kva": round(design_kva, 1),
        "primary_voltage": primary_voltage,
        "secondary_voltage": secondary_voltage,
        "phases": phases,
        "primary_fla": round(primary_fla, 1),
        "secondary_fla": round(secondary_fla, 1),
        "typical_impedance": typical_impedance,
        "primary_ocpd": primary_ocpd,
        "secondary_ocpd": secondary_ocpd,
        "application": application,
        "work_shown": "\n".join(work_steps),
        "nec_references": nec_references,
    }

def select_disconnect(
    load_amps: float,
    voltage: int,
    phases: int,
    motor_load: bool = False,
    fused: bool = True,
    nema_rating: str = "1",  # "1", "3R", "4", "4X", "12"
) -> Dict:
    """
    Select appropriate disconnect switch.

    Per NEC 430.109 and 430.110, motor disconnects must be rated
    for at least 115% of motor FLA.

    Args:
        load_amps: Load current in amps
        voltage: System voltage
        phases: Number of phases (1 or 3)
        motor_load: True if disconnecting motor load
        fused: True for fusible disconnect, False for non-fusible
        nema_rating: NEMA enclosure type ("1", "3R", "4", "4X", "12")

    Returns:
        Dictionary with:
        - recommended_amps: Standard disconnect size
        - switch_type: "fusible" or "non-fusible"
        - hp_rating: Horsepower rating (if motor load)
        - nema_enclosure: NEMA enclosure type
        - nec_references: List of applicable NEC articles
    """
    work_steps = []
    nec_references = []

    work_steps.append("=" * 60)
    work_steps.append("DISCONNECT SWITCH SELECTION")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Determine Minimum Rating")
    work_steps.append("─" * 60)

    if motor_load:
        min_rating = load_amps * 1.15
        work_steps.append("  Motor load disconnect per NEC 430.110(A):")
        work_steps.append(f"  Minimum rating = {load_amps} × 115% = {min_rating:.1f}A")
        nec_references.append("NEC 430.110(A) - Ampere Rating of Disconnecting Means")
        nec_references.append("NEC 430.109 - Type of Disconnecting Means")
    else:
        min_rating = load_amps
        work_steps.append("  General load disconnect:")
        work_steps.append(f"  Minimum rating = {load_amps}A")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Select Standard Size")
    work_steps.append("─" * 60)

    recommended_amps = None
    for size in STANDARD_DISCONNECT_SIZES:
        if size >= min_rating:
            recommended_amps = size
            work_steps.append(f"  Checking {size}A: {size} >= {min_rating:.1f} ✓")
            break
        else:
            work_steps.append(f"  Checking {size}A: {size} < {min_rating:.1f} ✗")

    if recommended_amps is None:
        recommended_amps = STANDARD_DISCONNECT_SIZES[-1]
        work_steps.append(
            f"  Load exceeds standard sizes, using maximum: {recommended_amps}A"
        )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Switch Type")
    work_steps.append("─" * 60)

    switch_type = "fusible" if fused else "non-fusible"
    work_steps.append(f"  Switch type: {switch_type}")

    if fused:
        work_steps.append("  Fusible disconnect provides overcurrent protection")
        work_steps.append("  Fuse size should be selected per load requirements")
    else:
        work_steps.append("  Non-fusible disconnect requires separate OCPD")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Horsepower Rating")
    work_steps.append("─" * 60)

    hp_rating = None
    if motor_load:
        if phases == 1:
            if voltage == 115:
                hp_rating = _estimate_hp_from_fla_1ph_115v(load_amps)
            elif voltage == 230:
                hp_rating = _estimate_hp_from_fla_1ph_230v(load_amps)
            else:
                hp_rating = _estimate_hp_from_fla_1ph_230v(load_amps)
        else:
            if voltage == 208:
                hp_rating = _estimate_hp_from_fla_3ph_208v(load_amps)
            elif voltage == 230:
                hp_rating = _estimate_hp_from_fla_3ph_230v(load_amps)
            elif voltage == 460:
                hp_rating = _estimate_hp_from_fla_3ph_460v(load_amps)
            elif voltage == 480:
                hp_rating = _estimate_hp_from_fla_3ph_460v(load_amps)  # Similar to 460V
            else:
                hp_rating = _estimate_hp_from_fla_3ph_460v(load_amps)

        work_steps.append(f"  Estimated motor HP: {hp_rating} HP")
        work_steps.append("  (Verify with motor nameplate)")
        nec_references.append("NEC Table 430.248 - Single-Phase Motor FLA")
        nec_references.append("NEC Table 430.250 - Three-Phase Motor FLA")
    else:
        work_steps.append("  Non-motor load - HP rating not applicable")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: NEMA Enclosure")
    work_steps.append("─" * 60)

    nema_descriptions = {
        "1": "Indoor, general purpose",
        "3R": "Outdoor, rainproof",
        "4": "Watertight, indoor/outdoor",
        "4X": "Watertight, corrosion resistant",
        "12": "Industrial, dust-tight",
    }

    nema_description = nema_descriptions.get(nema_rating, "General purpose")
    work_steps.append(f"  NEMA {nema_rating}: {nema_description}")
    nec_references.append("NEC 430.14 - Location of Disconnecting Means")

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("DISCONNECT SELECTION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(f"  Disconnect Rating: {recommended_amps}A")
    work_steps.append(f"  Switch Type: {switch_type.title()}")
    work_steps.append(f"  Voltage: {voltage}V, {phases}-phase")
    work_steps.append(f"  NEMA Enclosure: Type {nema_rating}")
    if hp_rating:
        work_steps.append(f"  HP Rating: {hp_rating} HP")

    return {
        "recommended_amps": recommended_amps,
        "switch_type": switch_type,
        "hp_rating": hp_rating,
        "nema_enclosure": nema_rating,
        "nema_description": nema_description,
        "load_amps": load_amps,
        "min_rating": round(min_rating, 1),
        "voltage": voltage,
        "phases": phases,
        "motor_load": motor_load,
        "work_shown": "\n".join(work_steps),
        "nec_references": nec_references,
    }

def select_conduit(
    conductors: List[Dict],  # [{"size": "10", "type": "THHN", "quantity": 3}, ...]
    conduit_type: str = "EMT",  # "EMT", "RMC", "PVC"
    max_fill_percent: float = 40.0,
) -> Dict:
    """
    Select appropriate conduit size based on conductor fill.

    Uses NEC Chapter 9 Tables 4 and 5 for fill calculations.

    Per NEC Chapter 9 Table 1:
    - 1 conductor: 53% fill
    - 2 conductors: 31% fill
    - 3+ conductors: 40% fill

    Args:
        conductors: List of conductor specifications with:
            - size: AWG or kcmil (e.g., "10", "1/0", "250")
            - type: Insulation type (THHN, THWN, XHHW)
            - quantity: Number of conductors
        conduit_type: Type of conduit (EMT, RMC, PVC)
        max_fill_percent: Maximum fill percentage (default 40%)

    Returns:
        Dictionary with:
        - recommended_size: Trade size
        - actual_fill_percent: Calculated fill percentage
        - conductor_area_sqin: Total conductor area
        - conduit_area_sqin: Conduit internal area
        - nec_references: List of applicable NEC articles
    """
    work_steps = []
    nec_references = []

    work_steps.append("=" * 60)
    work_steps.append("CONDUIT SELECTION")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Calculate Conductor Areas")
    work_steps.append("─" * 60)

    total_area = 0.0
    total_conductors = 0
    conductor_details = []

    for cond in conductors:
        size = str(cond.get("size", "12"))
        insulation = cond.get("type", "THHN").upper()
        quantity = cond.get("quantity", 1)

        if insulation in CONDUCTOR_AREAS:
            area_table = CONDUCTOR_AREAS[insulation]
        else:
            area_table = CONDUCTOR_AREAS["THHN"]
            work_steps.append(f"  Note: {insulation} not in tables, using THHN")

        if size in area_table:
            single_area = area_table[size]
            cond_total_area = single_area * quantity
            total_area += cond_total_area
            total_conductors += quantity

            work_steps.append(
                f"  {quantity}× #{size} {insulation}: {single_area:.4f} × {quantity} = {cond_total_area:.4f} sq in"
            )
            conductor_details.append(
                {
                    "size": size,
                    "type": insulation,
                    "quantity": quantity,
                    "area_each": single_area,
                    "area_total": round(cond_total_area, 4),
                }
            )
        else:
            work_steps.append(f"  Warning: Size {size} not found in tables")

    work_steps.append(f"\n  Total conductor area: {total_area:.4f} sq in")
    work_steps.append(f"  Total conductors: {total_conductors}")

    nec_references.append("NEC Chapter 9 Table 5 - Dimensions of Insulated Conductors")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Determine Maximum Fill")
    work_steps.append("─" * 60)

    if total_conductors == 1:
        nec_max_fill = 53.0
        work_steps.append("  1 conductor: 53% maximum fill per NEC")
    elif total_conductors == 2:
        nec_max_fill = 31.0
        work_steps.append("  2 conductors: 31% maximum fill per NEC")
    else:
        nec_max_fill = 40.0
        work_steps.append(f"  {total_conductors} conductors: 40% maximum fill per NEC")

    effective_max_fill = min(nec_max_fill, max_fill_percent)
    if max_fill_percent < nec_max_fill:
        work_steps.append(f"  User-specified limit: {max_fill_percent}%")
    work_steps.append(f"  Effective maximum fill: {effective_max_fill}%")

    nec_references.append("NEC Chapter 9 Table 1 - Percent of Cross Section of Conduit")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Calculate Required Conduit Area")
    work_steps.append("─" * 60)

    required_area = total_area / (effective_max_fill / 100)
    work_steps.append(
        f"  Required area = {total_area:.4f} / {effective_max_fill / 100:.2f}"
    )
    work_steps.append(f"  Required area = {required_area:.4f} sq in")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Select Conduit Size")
    work_steps.append("─" * 60)

    conduit_type_upper = conduit_type.upper()
    if conduit_type_upper not in ["EMT", "RMC", "PVC"]:
        conduit_type_upper = "EMT"
        work_steps.append(f"  Note: {conduit_type} not recognized, using EMT")

    work_steps.append(f"  Conduit type: {conduit_type_upper}")

    recommended_size: Optional[str] = None
    conduit_area: float = 0.0
    actual_fill: float = 0.0

    for size in STANDARD_CONDUIT_SIZES:
        if size in CONDUIT_AREA:
            area = CONDUIT_AREA[size].get(conduit_type_upper)
            if area:
                fill_pct = (total_area / area) * 100
                status = "✓" if area >= required_area else "✗"
                work_steps.append(
                    f'    {size}": {area:.4f} sq in, fill = {fill_pct:.1f}% {status}'
                )

                if area >= required_area and recommended_size is None:
                    recommended_size = size
                    conduit_area = area
                    actual_fill = fill_pct

    nec_references.append(
        "NEC Chapter 9 Table 4 - Dimensions and Percent Area of Conduit"
    )

    if recommended_size is None:
        return {
            "error": "No standard conduit size is large enough",
            "conductor_area_sqin": round(total_area, 4),
            "required_area_sqin": round(required_area, 4),
            "suggestion": "Consider multiple conduit runs",
            "work_shown": "\n".join(work_steps),
            "nec_references": nec_references,
        }

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("CONDUIT SELECTION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(
        f'  Recommended Conduit: {recommended_size}" {conduit_type_upper}'
    )
    work_steps.append(f"  Conduit Area: {conduit_area:.4f} sq in")
    work_steps.append(f"  Conductor Area: {total_area:.4f} sq in")
    work_steps.append(f"  Fill: {actual_fill:.1f}% (max {effective_max_fill}%)")

    return {
        "recommended_size": recommended_size,
        "conduit_type": conduit_type_upper,
        "actual_fill_percent": round(actual_fill, 1),
        "max_fill_percent": effective_max_fill,
        "conductor_area_sqin": round(total_area, 4),
        "conduit_area_sqin": round(conduit_area, 4),
        "total_conductors": total_conductors,
        "conductor_details": conductor_details,
        "nec_compliant": actual_fill <= effective_max_fill,
        "work_shown": "\n".join(work_steps),
        "nec_references": nec_references,
    }

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("CONDUIT SELECTION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(
        f'  Recommended Conduit: {recommended_size}" {conduit_type_upper}'
    )
    work_steps.append(f"  Conduit Area: {conduit_area:.4f} sq in")
    work_steps.append(f"  Conductor Area: {total_area:.4f} sq in")
    work_steps.append(f"  Fill: {actual_fill:.1f}% (max {effective_max_fill}%)")

    return {
        "recommended_size": recommended_size,
        "conduit_type": conduit_type_upper,
        "actual_fill_percent": round(actual_fill, 1),
        "max_fill_percent": effective_max_fill,
        "conductor_area_sqin": round(total_area, 4),
        "conduit_area_sqin": round(conduit_area, 4),
        "total_conductors": total_conductors,
        "conductor_details": conductor_details,
        "nec_compliant": actual_fill <= effective_max_fill,
        "work_shown": "\n".join(work_steps),
        "nec_references": nec_references,
    }

def select_conductor(
    load_amps: float,
    voltage: int,
    length_feet: float,
    phases: int = 3,
    material: str = "copper",
    insulation: str = "THHN",
    ambient_temp_c: float = 30.0,
    num_current_carrying: int = 3,
    max_voltage_drop_percent: float = 3.0,
) -> Dict:
    """
    Select appropriate conductor size for ampacity and voltage drop.

    Per NEC 310.15, conductor ampacity must be derated for:
    - Temperature (Table 310.15(B)(1))
    - Number of conductors (Table 310.15(C)(1))

    Args:
        load_amps: Load current in amps
        voltage: System voltage
        length_feet: One-way conductor length in feet
        phases: Number of phases (1 or 3)
        material: "copper" or "aluminum"
        insulation: Insulation type (THHN, THWN, XHHW)
        ambient_temp_c: Ambient temperature in Celsius
        num_current_carrying: Number of current-carrying conductors
        max_voltage_drop_percent: Maximum allowable voltage drop

    Returns:
        Dictionary with:
        - recommended_size: Conductor size (AWG or kcmil)
        - ampacity: Derated ampacity
        - voltage_drop_percent: Calculated voltage drop
        - sizing_factor: "ampacity" or "voltage_drop" (which governed)
        - adjustment_factor: Bundling adjustment applied
        - correction_factor: Temperature correction applied
        - nec_references: List of applicable NEC articles
    """
    work_steps = []
    nec_references = []

    work_steps.append("=" * 60)
    work_steps.append("CONDUCTOR SELECTION")
    work_steps.append("=" * 60)

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 1: Insulation Temperature Rating")
    work_steps.append("─" * 60)

    temp_rating = get_insulation_temp_rating(insulation)
    work_steps.append(f"  Insulation: {insulation}")
    work_steps.append(f"  Temperature rating: {temp_rating}°C")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 2: Temperature Correction Factor")
    work_steps.append("─" * 60)

    correction_factor = get_temp_correction_factor(ambient_temp_c, temp_rating)
    work_steps.append(f"  Ambient temperature: {ambient_temp_c}°C")
    work_steps.append(f"  Correction factor: {correction_factor}")
    nec_references.append("NEC Table 310.15(B)(1) - Temperature Correction Factors")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 3: Conductor Adjustment Factor")
    work_steps.append("─" * 60)

    adjustment_factor = get_conductor_adjustment_factor(num_current_carrying)
    work_steps.append(f"  Current-carrying conductors: {num_current_carrying}")
    work_steps.append(f"  Adjustment factor: {adjustment_factor}")

    if num_current_carrying > 3:
        nec_references.append("NEC Table 310.15(C)(1) - Adjustment Factors")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 4: Combined Derating Factor")
    work_steps.append("─" * 60)

    combined_factor = correction_factor * adjustment_factor
    work_steps.append(
        f"  Combined factor = {correction_factor} × {adjustment_factor} = {combined_factor:.3f}"
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 5: Minimum Table Ampacity")
    work_steps.append("─" * 60)

    design_amps = load_amps * 1.25
    min_table_ampacity = design_amps / combined_factor

    work_steps.append(f"  Load: {load_amps}A × 1.25 (continuous) = {design_amps:.1f}A")
    work_steps.append(
        f"  Min table ampacity = {design_amps:.1f} / {combined_factor:.3f} = {min_table_ampacity:.1f}A"
    )
    nec_references.append("NEC 215.2(A)(1) - Continuous Load Factor (125%)")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 6: Select Conductor for Ampacity")
    work_steps.append("─" * 60)

    if material.lower() == "copper":
        ampacity_table = AMPACITY_TABLE_310_15_B_16_COPPER
    else:
        ampacity_table = AMPACITY_TABLE_310_15_B_16_ALUMINUM

    ampacity_size = None
    ampacity_value = None

    for size in CONDUCTOR_SIZES:
        if size in ampacity_table:
            table_amp = ampacity_table[size].get(temp_rating)
            if table_amp and table_amp >= min_table_ampacity:
                ampacity_size = size
                ampacity_value = table_amp
                work_steps.append(
                    f"  {size}: {table_amp}A >= {min_table_ampacity:.1f}A ✓"
                )
                break
            elif table_amp:
                work_steps.append(
                    f"  {size}: {table_amp}A < {min_table_ampacity:.1f}A ✗"
                )

    if ampacity_size is None:
        return {
            "error": "No standard conductor meets ampacity requirements",
            "required_ampacity": round(min_table_ampacity, 1),
            "suggestion": "Consider parallel conductors",
            "work_shown": "\n".join(work_steps),
            "nec_references": nec_references,
        }

    nec_references.append("NEC Table 310.15(B)(16) - Conductor Ampacities")

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 7: Voltage Drop Check")
    work_steps.append("─" * 60)

    vd_size = ampacity_size
    vd_size_index = CONDUCTOR_SIZES.index(vd_size)

    vd_percent = _calculate_voltage_drop(
        vd_size, length_feet, load_amps, voltage, phases, material
    )

    work_steps.append(f"  Checking {vd_size}: VD = {vd_percent:.2f}%")

    while (
        vd_percent > max_voltage_drop_percent
        and vd_size_index < len(CONDUCTOR_SIZES) - 1
    ):
        vd_size_index += 1
        vd_size = CONDUCTOR_SIZES[vd_size_index]

        if vd_size not in ampacity_table:
            continue

        vd_percent = _calculate_voltage_drop(
            vd_size, length_feet, load_amps, voltage, phases, material
        )
        work_steps.append(f"  Upsizing to {vd_size}: VD = {vd_percent:.2f}%")

    nec_references.append("NEC 210.19(A)(1) Informational Note No. 4 - Voltage Drop")
    nec_references.append(
        "NEC 215.2(A)(4) Informational Note No. 2 - Feeder Voltage Drop"
    )

    work_steps.append(f"\n{'─' * 60}")
    work_steps.append("Step 8: Final Selection")
    work_steps.append("─" * 60)

    ampacity_index = CONDUCTOR_SIZES.index(ampacity_size)
    vd_index = CONDUCTOR_SIZES.index(vd_size)

    if vd_index > ampacity_index:
        recommended_size = vd_size
        sizing_factor = "voltage_drop"
        work_steps.append(f"  Ampacity requires: {ampacity_size}")
        work_steps.append(f"  Voltage drop requires: {vd_size}")
        work_steps.append(f"  SELECTED: {recommended_size} (governed by voltage drop)")
    else:
        recommended_size = ampacity_size
        sizing_factor = "ampacity"
        work_steps.append(f"  Ampacity requires: {ampacity_size}")
        work_steps.append(f"  Voltage drop requires: {vd_size}")
        work_steps.append(f"  SELECTED: {recommended_size} (governed by ampacity)")

    final_table_ampacity = ampacity_table[recommended_size].get(temp_rating, 0)
    final_derated_ampacity = final_table_ampacity * combined_factor
    final_vd_percent = _calculate_voltage_drop(
        recommended_size, length_feet, load_amps, voltage, phases, material
    )

    work_steps.append(f"\n{'=' * 60}")
    work_steps.append("CONDUCTOR SELECTION SUMMARY")
    work_steps.append("=" * 60)
    work_steps.append(f"  Recommended Size: {recommended_size} {material.title()}")
    work_steps.append(f"  Insulation: {insulation}")
    work_steps.append(f"  Table Ampacity: {final_table_ampacity}A")
    work_steps.append(f"  Derated Ampacity: {final_derated_ampacity:.1f}A")
    work_steps.append(f"  Voltage Drop: {final_vd_percent:.2f}%")
    work_steps.append(f"  Sizing Factor: {sizing_factor}")

    return {
        "recommended_size": recommended_size,
        "material": material,
        "insulation": insulation,
        "ampacity": round(final_derated_ampacity, 1),
        "table_ampacity": final_table_ampacity,
        "voltage_drop_percent": round(final_vd_percent, 2),
        "max_voltage_drop_percent": max_voltage_drop_percent,
        "sizing_factor": sizing_factor,
        "adjustment_factor": adjustment_factor,
        "correction_factor": correction_factor,
        "combined_factor": round(combined_factor, 3),
        "load_amps": load_amps,
        "design_amps": round(design_amps, 1),
        "length_feet": length_feet,
        "voltage": voltage,
        "phases": phases,
        "ambient_temp_c": ambient_temp_c,
        "num_current_carrying": num_current_carrying,
        "work_shown": "\n".join(work_steps),
        "nec_references": nec_references,
    }

def _select_standard_ocpd(amps: float, round_down: bool = False) -> int:
    """Select standard OCPD size for given amperage."""
    if round_down:
        selected = STANDARD_BREAKER_SIZES[0]
        for size in STANDARD_BREAKER_SIZES:
            if size <= amps:
                selected = size
            else:
                break
        return selected
    else:
        for size in STANDARD_BREAKER_SIZES:
            if size >= amps:
                return size
        return STANDARD_BREAKER_SIZES[-1]

def _calculate_voltage_drop(
    conductor_size: str,
    length_feet: float,
    current_amps: float,
    voltage: int,
    phases: int,
    material: str,
) -> float:
    """Calculate voltage drop percentage for given conductor."""
    resistance = get_resistance(conductor_size, material)
    if resistance is None:
        return 999.0  # Return high value if size not found

    if phases == 1:
        vd_volts = (2 * current_amps * length_feet * resistance) / 1000
    else:
        vd_volts = (math.sqrt(3) * current_amps * length_feet * resistance) / 1000

    return (vd_volts / voltage) * 100

def _estimate_hp_from_fla_1ph_115v(fla: float) -> float:
    """Estimate single-phase 115V motor HP from FLA (NEC Table 430.248)."""
    hp_fla_map = [
        (0.5, 9.8),
        (0.75, 13.8),
        (1, 16),
        (1.5, 20),
        (2, 24),
        (3, 34),
        (5, 56),
        (7.5, 80),
        (10, 100),
    ]
    for hp, table_fla in hp_fla_map:
        if fla <= table_fla * 1.1:  # 10% tolerance
            return hp
    return 10  # Default to 10 HP for larger

def _estimate_hp_from_fla_1ph_230v(fla: float) -> float:
    """Estimate single-phase 230V motor HP from FLA (NEC Table 430.248)."""
    hp_fla_map = [
        (0.5, 4.9),
        (0.75, 6.9),
        (1, 8),
        (1.5, 10),
        (2, 12),
        (3, 17),
        (5, 28),
        (7.5, 40),
        (10, 50),
    ]
    for hp, table_fla in hp_fla_map:
        if fla <= table_fla * 1.1:
            return hp
    return 10

def _estimate_hp_from_fla_3ph_208v(fla: float) -> float:
    """Estimate three-phase 208V motor HP from FLA (NEC Table 430.250)."""
    hp_fla_map = [
        (0.5, 2.4),
        (0.75, 3.5),
        (1, 4.6),
        (1.5, 6.6),
        (2, 7.5),
        (3, 10.6),
        (5, 16.7),
        (7.5, 24.2),
        (10, 30.8),
        (15, 46.2),
        (20, 59.4),
        (25, 74.8),
        (30, 88),
        (40, 114),
        (50, 143),
        (60, 169),
        (75, 211),
        (100, 273),
        (125, 343),
        (150, 396),
        (200, 528),
    ]
    for hp, table_fla in hp_fla_map:
        if fla <= table_fla * 1.1:
            return hp
    return 200

def _estimate_hp_from_fla_3ph_230v(fla: float) -> float:
    """Estimate three-phase 230V motor HP from FLA (NEC Table 430.250)."""
    hp_fla_map = [
        (0.5, 2.2),
        (0.75, 3.2),
        (1, 4.2),
        (1.5, 6),
        (2, 6.8),
        (3, 9.6),
        (5, 15.2),
        (7.5, 22),
        (10, 28),
        (15, 42),
        (20, 54),
        (25, 68),
        (30, 80),
        (40, 104),
        (50, 130),
        (60, 154),
        (75, 192),
        (100, 248),
        (125, 312),
        (150, 360),
        (200, 480),
    ]
    for hp, table_fla in hp_fla_map:
        if fla <= table_fla * 1.1:
            return hp
    return 200

def _estimate_hp_from_fla_3ph_460v(fla: float) -> float:
    """Estimate three-phase 460V motor HP from FLA (NEC Table 430.250)."""
    hp_fla_map = [
        (0.5, 1.1),
        (0.75, 1.6),
        (1, 2.1),
        (1.5, 3),
        (2, 3.4),
        (3, 4.8),
        (5, 7.6),
        (7.5, 11),
        (10, 14),
        (15, 21),
        (20, 27),
        (25, 34),
        (30, 40),
        (40, 52),
        (50, 65),
        (60, 77),
        (75, 96),
        (100, 124),
        (125, 156),
        (150, 180),
        (200, 240),
        (250, 302),
        (300, 361),
        (350, 414),
        (400, 477),
        (450, 515),
        (500, 590),
    ]
    for hp, table_fla in hp_fla_map:
        if fla <= table_fla * 1.1:
            return hp
    return 500
