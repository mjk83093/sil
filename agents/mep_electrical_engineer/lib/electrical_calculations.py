import math

def calculate_voltage_drop(voltage, current, length, circular_mils, factor_k=12.9, phases=3):
    """
    Calculates voltage drop for a circuit.
    K = 12.9 for Copper, 21.2 for Aluminum
    Phases factor: 1.732 (sqrt 3) for 3-phase, 2 for single-phase
    """
    phase_multiplier = 1.732 if phases == 3 else 2
    vd = (phase_multiplier * factor_k * current * length) / circular_mils
    vd_percent = (vd / voltage) * 100
    return {
        "voltage_drop": round(vd, 2),
        "percent_drop": round(vd_percent, 2)
    }

def get_motor_flc(hp, voltage, phases=3):
    """
    Returns FLC from NEC Table 430.250/430.248 (Simplified lookup)
    """
    # Simplified lookup for common 460V 3PH motors
    flc_table_460v_3ph = {
        1: 2.1, 2: 3.4, 3: 4.8, 5: 7.6, 7.5: 11, 10: 14, 15: 21, 
        20: 27, 25: 34, 30: 40, 40: 52, 50: 65, 60: 77, 75: 96, 100: 124
    }
    if phases == 3 and voltage in [460, 480]:
        return flc_table_460v_3ph.get(hp)
    return None

def size_grounding_conductor(ocpd_rating, material="copper"):
    """
    Sizing per NEC Table 250.122
    """
    table_250_122 = [
        (15, "14 AWG"), (20, "12 AWG"), (30, "10 AWG"), (60, "10 AWG"),
        (100, "8 AWG"), (200, "6 AWG"), (300, "4 AWG"), (400, "3 AWG"),
        (500, "2 AWG"), (600, "1 AWG"), (800, "1/0 AWG"), (1000, "2/0 AWG")
    ]
    for rating, size in table_250_122:
        if ocpd_rating <= rating:
            return size
    return "Special Calculation Required"
