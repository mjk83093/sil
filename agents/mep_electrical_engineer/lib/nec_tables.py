"""
NEC Reference Tables
====================
Deterministic lookup tables from the National Electrical Code.
All values are from NEC 2023 edition.
"""

from typing import Dict, Optional, List, Tuple

AMPACITY_TABLE_310_15_B_16_COPPER: Dict[str, Dict[str, int]] = {
    "14": {"60": 15, "75": 20, "90": 25},
    "12": {"60": 20, "75": 25, "90": 30},
    "10": {"60": 30, "75": 35, "90": 40},
    "8": {"60": 40, "75": 50, "90": 55},
    "6": {"60": 55, "75": 65, "90": 75},
    "4": {"60": 70, "75": 85, "90": 95},
    "3": {"60": 85, "75": 100, "90": 115},
    "2": {"60": 95, "75": 115, "90": 130},
    "1": {"60": 110, "75": 130, "90": 145},
    "1/0": {"60": 125, "75": 150, "90": 170},
    "2/0": {"60": 145, "75": 175, "90": 195},
    "3/0": {"60": 165, "75": 200, "90": 225},
    "4/0": {"60": 195, "75": 230, "90": 260},
    "250": {"60": 215, "75": 255, "90": 290},
    "300": {"60": 240, "75": 285, "90": 320},
    "350": {"60": 260, "75": 310, "90": 350},
    "400": {"60": 280, "75": 335, "90": 380},
    "500": {"60": 320, "75": 380, "90": 430},
    "600": {"60": 350, "75": 420, "90": 475},
    "700": {"60": 385, "75": 460, "90": 520},
    "750": {"60": 400, "75": 475, "90": 535},
    "800": {"60": 410, "75": 490, "90": 555},
    "900": {"60": 435, "75": 520, "90": 585},
    "1000": {"60": 455, "75": 545, "90": 615},
}

AMPACITY_TABLE_310_15_B_16_ALUMINUM: Dict[str, Dict[str, int]] = {
    "12": {"60": 15, "75": 20, "90": 25},
    "10": {"60": 25, "75": 30, "90": 35},
    "8": {"60": 35, "75": 40, "90": 45},
    "6": {"60": 40, "75": 50, "90": 55},
    "4": {"60": 55, "75": 65, "90": 75},
    "3": {"60": 65, "75": 75, "90": 85},
    "2": {"60": 75, "75": 90, "90": 100},
    "1": {"60": 85, "75": 100, "90": 115},
    "1/0": {"60": 100, "75": 120, "90": 135},
    "2/0": {"60": 115, "75": 135, "90": 150},
    "3/0": {"60": 130, "75": 155, "90": 175},
    "4/0": {"60": 150, "75": 180, "90": 205},
    "250": {"60": 170, "75": 205, "90": 230},
    "300": {"60": 190, "75": 230, "90": 260},
    "350": {"60": 210, "75": 250, "90": 280},
    "400": {"60": 225, "75": 270, "90": 305},
    "500": {"60": 260, "75": 310, "90": 350},
    "600": {"60": 285, "75": 340, "90": 385},
    "700": {"60": 315, "75": 375, "90": 425},
    "750": {"60": 320, "75": 385, "90": 435},
}

AMPACITY_TABLE_310_15_B_17_COPPER: Dict[str, Dict[str, int]] = {
    "14": {"60": 25, "75": 30, "90": 35},
    "12": {"60": 30, "75": 35, "90": 40},
    "10": {"60": 40, "75": 50, "90": 55},
    "8": {"60": 60, "75": 70, "90": 80},
    "6": {"60": 80, "75": 95, "90": 105},
    "4": {"60": 105, "75": 125, "90": 140},
    "3": {"60": 120, "75": 145, "90": 165},
    "2": {"60": 140, "75": 170, "90": 190},
    "1": {"60": 165, "75": 195, "90": 220},
    "1/0": {"60": 195, "75": 230, "90": 260},
    "2/0": {"60": 225, "75": 265, "90": 300},
    "3/0": {"60": 260, "75": 310, "90": 350},
    "4/0": {"60": 300, "75": 360, "90": 405},
}

CONDUCTOR_RESISTANCE_COPPER: Dict[str, float] = {
    "18": 7.77,
    "16": 4.89,
    "14": 3.14,
    "12": 1.98,
    "10": 1.24,
    "8": 0.778,
    "6": 0.491,
    "4": 0.308,
    "3": 0.245,
    "2": 0.194,
    "1": 0.154,
    "1/0": 0.122,
    "2/0": 0.0967,
    "3/0": 0.0766,
    "4/0": 0.0608,
    "250": 0.0515,
    "300": 0.0429,
    "350": 0.0367,
    "400": 0.0321,
    "500": 0.0258,
    "600": 0.0214,
    "700": 0.0184,
    "750": 0.0171,
    "800": 0.0161,
    "900": 0.0143,
    "1000": 0.0129,
}

CONDUCTOR_RESISTANCE_ALUMINUM: Dict[str, float] = {
    "12": 3.25,
    "10": 2.04,
    "8": 1.28,
    "6": 0.808,
    "4": 0.508,
    "3": 0.403,
    "2": 0.319,
    "1": 0.253,
    "1/0": 0.201,
    "2/0": 0.159,
    "3/0": 0.126,
    "4/0": 0.100,
    "250": 0.0847,
    "300": 0.0707,
    "350": 0.0605,
    "400": 0.0529,
    "500": 0.0424,
    "600": 0.0353,
    "700": 0.0303,
    "750": 0.0282,
}

CONDUCTOR_AREA_THHN: Dict[str, float] = {
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
}

CONDUCTOR_AREA_XHHW: Dict[str, float] = {
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
}

CONDUIT_AREA: Dict[str, Dict[str, float]] = {
    "1/2": {"EMT": 0.304, "RMC": 0.314, "PVC": 0.285},
    "3/4": {"EMT": 0.533, "RMC": 0.549, "PVC": 0.508},
    "1": {"EMT": 0.864, "RMC": 0.887, "PVC": 0.832},
    "1-1/4": {"EMT": 1.496, "RMC": 1.526, "PVC": 1.453},
    "1-1/2": {"EMT": 2.036, "RMC": 2.071, "PVC": 1.986},
    "2": {"EMT": 3.356, "RMC": 3.408, "PVC": 3.291},
    "2-1/2": {"EMT": 5.858, "RMC": 5.858, "PVC": 5.695},
    "3": {"EMT": 8.846, "RMC": 8.846, "PVC": 8.709},
    "3-1/2": {"EMT": 11.545, "RMC": 11.545, "PVC": 11.365},
    "4": {"EMT": 14.753, "RMC": 14.753, "PVC": 14.448},
}

CONDUIT_FILL_PERCENT: Dict[int, float] = {
    1: 0.53,  # 1 conductor: 53%
    2: 0.31,  # 2 conductors: 31%
    3: 0.40,  # 3+ conductors: 40%
}

LIGHTING_LOAD_TABLE_220_12: Dict[str, float] = {
    "armory": 1.0,
    "auditorium": 1.0,
    "bank": 3.5,
    "barber_shop": 3.0,
    "beauty_parlor": 3.0,
    "church": 1.0,
    "club": 2.0,
    "courthouse": 2.0,
    "dwelling": 3.0,
    "residential": 3.0,
    "garage_commercial": 0.5,
    "hospital": 2.0,
    "hotel": 2.0,
    "motel": 2.0,
    "industrial": 2.0,
    "lodge": 1.5,
    "office": 3.5,
    "restaurant": 2.0,
    "retail": 3.0,
    "school": 3.0,
    "storage": 0.25,
    "warehouse": 0.25,
}

LIGHTING_DEMAND_FACTORS_220_42: Dict[str, List[Tuple[float, float]]] = {
    "dwelling": [
        (3000, 1.00),  # First 3000 VA at 100%
        (120000, 0.35),  # 3001 to 120000 VA at 35%
        (float("inf"), 0.25),  # Over 120000 VA at 25%
    ],
    "hospital": [
        (50000, 0.40),  # First 50000 VA at 40%
        (float("inf"), 0.20),  # Over 50000 VA at 20%
    ],
    "hotel": [
        (20000, 0.50),  # First 20000 VA at 50%
        (100000, 0.40),  # 20001 to 100000 VA at 40%
        (float("inf"), 0.30),  # Over 100000 VA at 30%
    ],
    "warehouse": [
        (12500, 1.00),  # First 12500 VA at 100%
        (float("inf"), 0.50),  # Over 12500 VA at 50%
    ],
    "default": [
        (float("inf"), 1.00),
    ],
}

RECEPTACLE_DEMAND_FACTORS_220_44: List[Tuple[float, float]] = [
    (10000, 1.00),  # First 10 kVA at 100%
    (float("inf"), 0.50),  # Remainder at 50%
]

TEMP_CORRECTION_FACTORS: Dict[str, Dict[str, float]] = {
    "21-25": {"60": 1.08, "75": 1.05, "90": 1.04},
    "26-30": {"60": 1.00, "75": 1.00, "90": 1.00},
    "31-35": {"60": 0.91, "75": 0.94, "90": 0.96},
    "36-40": {"60": 0.82, "75": 0.88, "90": 0.91},
    "41-45": {"60": 0.71, "75": 0.82, "90": 0.87},
    "46-50": {"60": 0.58, "75": 0.75, "90": 0.82},
    "51-55": {"60": 0.41, "75": 0.67, "90": 0.76},
    "56-60": {"60": 0.00, "75": 0.58, "90": 0.71},
}

CONDUCTOR_ADJUSTMENT_FACTORS: Dict[str, float] = {
    "4-6": 0.80,
    "7-9": 0.70,
    "10-20": 0.50,
    "21-30": 0.45,
    "31-40": 0.40,
    "41+": 0.35,
}

INSULATION_TEMP_RATING: Dict[str, str] = {
    "TW": "60",
    "UF": "60",
    "THW": "75",
    "THWN": "75",
    "XHHW": "75",  # When wet
    "THHN": "90",
    "THWN-2": "90",
    "XHHW-2": "90",
    "USE-2": "90",
}

CONDUCTOR_SIZES: List[str] = [
    "14",
    "12",
    "10",
    "8",
    "6",
    "4",
    "3",
    "2",
    "1",
    "1/0",
    "2/0",
    "3/0",
    "4/0",
    "250",
    "300",
    "350",
    "400",
    "500",
    "600",
    "700",
    "750",
    "800",
    "900",
    "1000",
]

def get_ampacity(
    conductor_size: str,
    material: str = "copper",
    temp_rating: str = "75",
    in_raceway: bool = True,
) -> Optional[int]:
    """
    Get ampacity for a conductor from NEC Table 310.15(B)(16) or (B)(17).

    Args:
        conductor_size: AWG or kcmil size (e.g., "10", "1/0", "250")
        material: "copper" or "aluminum"
        temp_rating: "60", "75", or "90"
        in_raceway: True for Table 310.15(B)(16), False for (B)(17)

    Returns:
        Ampacity in amps, or None if not found
    """
    if material.lower() == "copper":
        if in_raceway:
            table = AMPACITY_TABLE_310_15_B_16_COPPER
        else:
            table = AMPACITY_TABLE_310_15_B_17_COPPER
    else:
        table = AMPACITY_TABLE_310_15_B_16_ALUMINUM

    if conductor_size in table:
        return table[conductor_size].get(str(temp_rating))
    return None

def get_resistance(conductor_size: str, material: str = "copper") -> Optional[float]:
    """
    Get DC resistance per 1000 feet from NEC Chapter 9 Table 8.

    Args:
        conductor_size: AWG or kcmil size
        material: "copper" or "aluminum"

    Returns:
        Resistance in ohms per 1000 feet, or None if not found
    """
    if material.lower() == "copper":
        return CONDUCTOR_RESISTANCE_COPPER.get(conductor_size)
    else:
        return CONDUCTOR_RESISTANCE_ALUMINUM.get(conductor_size)

def get_temp_correction_factor(
    ambient_temp: float, insulation_rating: str = "75"
) -> float:
    """
    Get temperature correction factor from Table 310.15(B)(1).

    Args:
        ambient_temp: Ambient temperature in Celsius
        insulation_rating: "60", "75", or "90"

    Returns:
        Correction factor (multiply by ampacity)
    """
    if ambient_temp <= 25:
        range_key = "21-25"
    elif ambient_temp <= 30:
        range_key = "26-30"
    elif ambient_temp <= 35:
        range_key = "31-35"
    elif ambient_temp <= 40:
        range_key = "36-40"
    elif ambient_temp <= 45:
        range_key = "41-45"
    elif ambient_temp <= 50:
        range_key = "46-50"
    elif ambient_temp <= 55:
        range_key = "51-55"
    else:
        range_key = "56-60"

    return TEMP_CORRECTION_FACTORS.get(range_key, {}).get(str(insulation_rating), 1.0)

def get_conductor_adjustment_factor(num_conductors: int) -> float:
    """
    Get adjustment factor for more than 3 current-carrying conductors.
    Per NEC Table 310.15(C)(1).

    Args:
        num_conductors: Number of current-carrying conductors

    Returns:
        Adjustment factor (multiply by ampacity)
    """
    if num_conductors <= 3:
        return 1.0
    elif num_conductors <= 6:
        return 0.80
    elif num_conductors <= 9:
        return 0.70
    elif num_conductors <= 20:
        return 0.50
    elif num_conductors <= 30:
        return 0.45
    elif num_conductors <= 40:
        return 0.40
    else:
        return 0.35

def get_insulation_temp_rating(insulation_type: str) -> str:
    """
    Get temperature rating for insulation type.

    Args:
        insulation_type: e.g., "THHN", "THWN", "XHHW"

    Returns:
        Temperature rating as string: "60", "75", or "90"
    """
    return INSULATION_TEMP_RATING.get(insulation_type.upper(), "75")

def get_lighting_load(occupancy: str) -> float:
    """
    Get lighting load VA per square foot from Table 220.12.

    Args:
        occupancy: Occupancy type (e.g., "office", "warehouse")

    Returns:
        VA per square foot
    """
    return LIGHTING_LOAD_TABLE_220_12.get(occupancy.lower(), 3.0)

def select_conductor_size(
    required_ampacity: float, material: str = "copper", temp_rating: str = "75"
) -> Optional[str]:
    """
    Select the minimum conductor size for a given ampacity requirement.

    Args:
        required_ampacity: Required ampacity in amps
        material: "copper" or "aluminum"
        temp_rating: "60", "75", or "90"

    Returns:
        Conductor size string, or None if no suitable size found
    """
    for size in CONDUCTOR_SIZES:
        ampacity = get_ampacity(size, material, temp_rating)
        if ampacity and ampacity >= required_ampacity:
            return size
    return None

GEC_TABLE_250_66_COPPER: Dict[str, str] = {
    "18": "8",
    "16": "8",
    "14": "8",
    "12": "8",
    "10": "8",
    "8": "8",
    "6": "8",
    "4": "8",
    "3": "8",
    "2": "8",
    "1": "6",
    "1/0": "6",
    "2/0": "4",
    "3/0": "4",
    "4/0": "2",
    "250": "2",
    "300": "2",
    "350": "2",
    "400": "1/0",
    "500": "1/0",
    "600": "1/0",
    "700": "2/0",
    "750": "2/0",
    "800": "2/0",
    "900": "2/0",
    "1000": "2/0",
    "1100": "3/0",
    "1250": "3/0",
    "1500": "3/0",
    "1750": "3/0",
    "2000": "3/0",
}

GEC_TABLE_250_66_ALUMINUM: Dict[str, str] = {
    "12": "6",
    "10": "6",
    "8": "6",
    "6": "6",
    "4": "6",
    "3": "6",
    "2": "6",
    "1": "6",
    "1/0": "4",
    "2/0": "4",
    "3/0": "2",
    "4/0": "2",
    "250": "1/0",
    "300": "1/0",
    "350": "1/0",
    "400": "1/0",
    "500": "1/0",
    "600": "2/0",
    "700": "2/0",
    "750": "3/0",
    "800": "3/0",
    "900": "3/0",
    "1000": "3/0",
    "1100": "4/0",
    "1250": "4/0",
    "1500": "4/0",
    "1750": "250",
    "2000": "250",
}

EGC_TABLE_250_122_COPPER: Dict[int, str] = {
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

EGC_TABLE_250_122_ALUMINUM: Dict[int, str] = {
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
    4000: "800",
    5000: "1000",
    6000: "1250",
}

EGC_OCPD_RATINGS: List[int] = [
    15,
    20,
    30,
    40,
    60,
    100,
    200,
    300,
    400,
    500,
    600,
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

RANGE_DEMAND_TABLE_220_55: Dict[int, float] = {
    1: 8.0,
    2: 11.0,
    3: 14.0,
    4: 17.0,
    5: 20.0,
    6: 21.0,
    7: 22.0,
    8: 23.0,
    9: 24.0,
    10: 25.0,
    11: 26.0,
    12: 27.0,
}

RANGE_DEMAND_EXTENDED: List[Tuple[int, int, float, float]] = [
    (13, 25, 26.0, 1.0),
    (26, 40, 26.0, 0.75),
    (41, 50, 26.0, 0.65),
    (51, 60, 26.0, 0.55),
    (61, 999, 26.0, 0.50),
]

def get_gec_size(
    service_conductor_size: str, material: str = "copper"
) -> Optional[str]:
    """
    Get Grounding Electrode Conductor (GEC) size from NEC Table 250.66.

    Per NEC 250.66, the grounding electrode conductor shall not be required
    to be larger than 3/0 AWG copper or 250 kcmil aluminum.

    Args:
        service_conductor_size: Size of largest ungrounded service-entrance
                                conductor (e.g., "2", "1/0", "350")
        material: "copper" or "aluminum" for both service conductor and GEC

    Returns:
        GEC size string (e.g., "8", "6", "4"), or None if not found

    Reference:
        NEC 2023 Table 250.66 - Grounding Electrode Conductor for
        Alternating-Current Systems
    """
    if material.lower() == "copper":
        return GEC_TABLE_250_66_COPPER.get(service_conductor_size)
    else:
        return GEC_TABLE_250_66_ALUMINUM.get(service_conductor_size)

def get_egc_size(ocpd_rating: int, material: str = "copper") -> Optional[str]:
    """
    Get Equipment Grounding Conductor (EGC) size from NEC Table 250.122.

    Selects the minimum EGC size based on the rating or setting of the
    automatic overcurrent device (OCPD) in the circuit ahead of the equipment.

    Args:
        ocpd_rating: Rating of overcurrent protective device in amps
                     (e.g., 15, 20, 100, 200)
        material: "copper" or "aluminum"

    Returns:
        EGC size string (e.g., "14", "12", "8"), or None if rating exceeds table

    Reference:
        NEC 2023 Table 250.122 - Minimum Size Equipment Grounding Conductors
        for Grounding Raceway and Equipment
    """
    if material.lower() == "copper":
        table = EGC_TABLE_250_122_COPPER
    else:
        table = EGC_TABLE_250_122_ALUMINUM

    if ocpd_rating in table:
        return table[ocpd_rating]

    for rating in EGC_OCPD_RATINGS:
        if rating >= ocpd_rating:
            return table.get(rating)

    return None

def get_range_demand(num_appliances: int, max_rating_kw: float = 12.0) -> float:
    """
    Get demand load for household electric ranges from NEC Table 220.55.

    For ranges rated more than 12 kW but not more than 27 kW, the maximum
    demand in Column C shall be increased 5% for each additional kW of
    rating or major fraction thereof by which the rating exceeds 12 kW.

    Args:
        num_appliances: Number of appliances (1 or more)
        max_rating_kw: Maximum rating of any single appliance in kW
                       (default 12.0 kW, the Column C baseline)

    Returns:
        Demand load in kW

    Reference:
        NEC 2023 Table 220.55 - Demand Factors and Loads for Household
        Electric Ranges, Wall-Mounted Ovens, Counter-Mounted Cooking Units,
        and Other Household Cooking Appliances over 1-3/4 kW Rating

    Notes:
        - Column C values are used (for ranges not over 12 kW each)
        - For ranges over 12 kW: add 5% per kW (or major fraction) over 12 kW
        - For 13+ appliances, extended calculation per table notes applies
    """
    if num_appliances < 1:
        return 0.0

    if num_appliances <= 12:
        base_demand = RANGE_DEMAND_TABLE_220_55[num_appliances]
    else:
        for min_count, max_count, base_kw, kw_per_appliance in RANGE_DEMAND_EXTENDED:
            if min_count <= num_appliances <= max_count:
                base_demand = base_kw + (num_appliances * kw_per_appliance)
                break
        else:
            base_demand = 26.0 + (num_appliances * 0.50)

    if max_rating_kw > 12.0:
        kw_over_12 = int(max_rating_kw - 12.0)
        if (max_rating_kw - 12.0) > kw_over_12:
            kw_over_12 += 1  # Round up for major fraction
        multiplier = 1.0 + (0.05 * kw_over_12)
        base_demand = base_demand * multiplier

    return round(base_demand, 2)
