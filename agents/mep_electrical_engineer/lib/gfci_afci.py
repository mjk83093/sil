"""
NEC 210.8/210.12 GFCI and AFCI Protection Validation
=====================================================
Deterministic validation of GFCI and AFCI protection requirements.
All validation logic is pure Python - NO LLM involvement.

Reference: NEC 2023 Articles 210.8 and 210.12
"""

from typing import List, Dict, Any
from .validation_result import ValidationResult

GFCI_LOCATIONS: Dict[str, Dict[str, Any]] = {
    "bathroom": {
        "code_ref": "210.8(A)(1)",
        "description": "All 125V through 250V receptacles in bathrooms",
        "distance_ft": None,  # All receptacles in space
    },
    "garage": {
        "code_ref": "210.8(A)(2)",
        "description": "Garages and accessory buildings with floor at or below grade",
        "distance_ft": None,
    },
    "outdoor": {
        "code_ref": "210.8(A)(3)",
        "description": "Outdoors (all outdoor receptacles)",
        "distance_ft": None,
    },
    "crawl_space": {
        "code_ref": "210.8(A)(4)",
        "description": "Crawl spaces at or below grade level",
        "distance_ft": None,
    },
    "unfinished_basement": {
        "code_ref": "210.8(A)(5)",
        "description": "Unfinished portions of basements",
        "distance_ft": None,
    },
    "kitchen_countertop": {
        "code_ref": "210.8(A)(6)",
        "description": "Kitchen countertop surfaces",
        "distance_ft": None,
    },
    "sink": {
        "code_ref": "210.8(A)(7)",
        "description": "Areas with sinks (within 6 feet of outside edge)",
        "distance_ft": 6.0,
    },
    "boathouse": {
        "code_ref": "210.8(A)(8)",
        "description": "Boathouses",
        "distance_ft": None,
    },
    "bathtub_shower": {
        "code_ref": "210.8(A)(9)",
        "description": "Bathtubs or shower stalls (within 6 feet)",
        "distance_ft": 6.0,
    },
    "laundry": {
        "code_ref": "210.8(A)(10)",
        "description": "Laundry areas",
        "distance_ft": None,
    },
    "indoor_damp": {
        "code_ref": "210.8(A)(11)",
        "description": "Indoor damp and wet locations",
        "distance_ft": None,
    },
}

GFCI_LOCATIONS_COMMERCIAL: Dict[str, Dict[str, Any]] = {
    "bathroom": {
        "code_ref": "210.8(B)(1)",
        "description": "Bathrooms",
        "distance_ft": None,
    },
    "kitchen": {
        "code_ref": "210.8(B)(2)",
        "description": "Kitchens",
        "distance_ft": None,
    },
    "rooftop": {
        "code_ref": "210.8(B)(3)",
        "description": "Rooftops",
        "distance_ft": None,
    },
    "outdoor": {
        "code_ref": "210.8(B)(4)",
        "description": "Outdoors (public spaces, below 6.5 ft)",
        "distance_ft": None,
    },
    "sink": {
        "code_ref": "210.8(B)(5)",
        "description": "Sinks (within 6 feet)",
        "distance_ft": 6.0,
    },
    "indoor_wet": {
        "code_ref": "210.8(B)(6)",
        "description": "Indoor wet locations",
        "distance_ft": None,
    },
    "locker_room": {
        "code_ref": "210.8(B)(7)",
        "description": "Locker rooms with shower facilities",
        "distance_ft": None,
    },
    "garage": {
        "code_ref": "210.8(B)(8)",
        "description": "Garages, service bays, similar areas",
        "distance_ft": None,
    },
    "crawl_space": {
        "code_ref": "210.8(B)(9)",
        "description": "Crawl spaces at or below grade",
        "distance_ft": None,
    },
    "unfinished_basement": {
        "code_ref": "210.8(B)(10)",
        "description": "Unfinished portions of basements",
        "distance_ft": None,
    },
    "boat_hoist": {
        "code_ref": "210.8(B)(11)",
        "description": "Boat hoists",
        "distance_ft": None,
    },
}

AFCI_LOCATIONS: Dict[str, str] = {
    "bedroom": "210.12(A)",
    "family_room": "210.12(A)",
    "dining_room": "210.12(A)",
    "living_room": "210.12(A)",
    "parlor": "210.12(A)",
    "library": "210.12(A)",
    "den": "210.12(A)",
    "sunroom": "210.12(A)",
    "recreation_room": "210.12(A)",
    "closet": "210.12(A)",
    "hallway": "210.12(A)",
    "laundry": "210.12(A)",
    "similar_room": "210.12(A)",
}

def validate_gfci_required(location_type: str, occupancy: str) -> bool:
    """
    Determine if GFCI protection is required for a location.

    Args:
        location_type: Type of location (e.g., "bathroom", "kitchen_countertop")
        occupancy: Occupancy type ("dwelling" or "commercial")

    Returns:
        True if GFCI protection is required, False otherwise

    Example:
        >>> validate_gfci_required("bathroom", "dwelling")
        True
        >>> validate_gfci_required("bedroom", "dwelling")
        False
    """
    location_normalized = location_type.lower().strip().replace(" ", "_")
    occupancy_normalized = occupancy.lower().strip()

    if occupancy_normalized == "dwelling":
        return location_normalized in GFCI_LOCATIONS
    else:
        return location_normalized in GFCI_LOCATIONS_COMMERCIAL

def validate_afci_required(space_type: str, occupancy: str) -> bool:
    """
    Determine if AFCI protection is required for a space.

    AFCI protection is required for dwelling unit branch circuits supplying
    outlets and devices in specific areas per NEC 210.12(A).

    Args:
        space_type: Type of space (e.g., "bedroom", "living_room")
        occupancy: Occupancy type ("dwelling" or "commercial")

    Returns:
        True if AFCI protection is required, False otherwise

    Example:
        >>> validate_afci_required("bedroom", "dwelling")
        True
        >>> validate_afci_required("bathroom", "dwelling")
        False
    """
    space_normalized = space_type.lower().strip().replace(" ", "_")
    occupancy_normalized = occupancy.lower().strip()

    if occupancy_normalized != "dwelling":
        return False

    return space_normalized in AFCI_LOCATIONS

def check_gfci_protection(receptacles: List[Dict[str, Any]]) -> List[ValidationResult]:
    """
    Check GFCI protection for a list of receptacles.

    Each receptacle dict should contain:
        - tag: Receptacle identifier (e.g., "R-101")
        - location_type: Type of location (e.g., "bathroom", "kitchen_countertop")
        - gfci_protected: Boolean indicating if GFCI protected
        - occupancy: "dwelling" or "commercial" (optional, defaults to "dwelling")
        - distance_to_water_ft: Distance to sink/tub in feet (optional)

    Args:
        receptacles: List of receptacle dictionaries

    Returns:
        List of ValidationResult objects, one per receptacle

    Example:
        >>> receptacles = [
        ...     {"tag": "R-101", "location_type": "bathroom", "gfci_protected": True},
        ...     {"tag": "R-102", "location_type": "bathroom", "gfci_protected": False},
        ... ]
        >>> results = check_gfci_protection(receptacles)
        >>> results[0].status
        'PASS'
        >>> results[1].status
        'FAIL'
    """
    results = []

    for recep in receptacles:
        tag = recep.get("tag", "Unknown")
        location_type = recep.get("location_type", "").lower().strip().replace(" ", "_")
        gfci_protected = recep.get("gfci_protected", False)
        occupancy = recep.get("occupancy", "dwelling").lower().strip()
        distance_to_water = recep.get("distance_to_water_ft")

        if occupancy == "dwelling":
            location_table = GFCI_LOCATIONS
        else:
            location_table = GFCI_LOCATIONS_COMMERCIAL

        gfci_required = location_type in location_table

        if gfci_required and location_type in ("sink", "bathtub_shower"):
            location_info = location_table[location_type]
            max_distance = location_info.get("distance_ft")

            if max_distance and distance_to_water is not None:
                if distance_to_water > max_distance:
                    gfci_required = False

        details = {
            "tag": tag,
            "location_type": location_type,
            "occupancy": occupancy,
            "gfci_protected": gfci_protected,
            "gfci_required": gfci_required,
        }

        if distance_to_water is not None:
            details["distance_to_water_ft"] = distance_to_water

        if gfci_required:
            code_ref = location_table[location_type]["code_ref"]

            if gfci_protected:
                results.append(
                    ValidationResult(
                        status="PASS",
                        message=f"Receptacle {tag} in {location_type} is GFCI protected as required",
                        nec_reference=f"NEC {code_ref}",
                        details=details,
                    )
                )
            else:
                results.append(
                    ValidationResult(
                        status="FAIL",
                        message=f"Receptacle {tag} in {location_type} requires GFCI protection",
                        nec_reference=f"NEC {code_ref}",
                        details=details,
                    )
                )
        else:
            if gfci_protected:
                results.append(
                    ValidationResult(
                        status="PASS",
                        message=f"Receptacle {tag} has GFCI protection (not required but acceptable)",
                        nec_reference="NEC 210.8",
                        details=details,
                    )
                )
            else:
                results.append(
                    ValidationResult(
                        status="PASS",
                        message=f"Receptacle {tag} in {location_type} - GFCI not required",
                        nec_reference="NEC 210.8",
                        details=details,
                    )
                )

    return results

def check_afci_protection(circuits: List[Dict[str, Any]]) -> List[ValidationResult]:
    """
    Check AFCI protection for a list of circuits.

    Each circuit dict should contain:
        - circuit_number: Circuit identifier (e.g., 1, 3, "EM-1")
        - space_type: Type of space served (e.g., "bedroom", "living_room")
        - afci_protected: Boolean indicating if AFCI protected
        - occupancy: "dwelling" or "commercial" (optional, defaults to "dwelling")

    Args:
        circuits: List of circuit dictionaries

    Returns:
        List of ValidationResult objects, one per circuit

    Example:
        >>> circuits = [
        ...     {"circuit_number": 5, "space_type": "bedroom", "afci_protected": True},
        ...     {"circuit_number": 7, "space_type": "living_room", "afci_protected": False},
        ... ]
        >>> results = check_afci_protection(circuits)
        >>> results[0].status
        'PASS'
        >>> results[1].status
        'FAIL'
    """
    results = []

    for circuit in circuits:
        circuit_num = circuit.get("circuit_number", "Unknown")
        space_type = circuit.get("space_type", "").lower().strip().replace(" ", "_")
        afci_protected = circuit.get("afci_protected", False)
        occupancy = circuit.get("occupancy", "dwelling").lower().strip()

        afci_required = (occupancy == "dwelling") and (space_type in AFCI_LOCATIONS)

        details = {
            "circuit_number": circuit_num,
            "space_type": space_type,
            "occupancy": occupancy,
            "afci_protected": afci_protected,
            "afci_required": afci_required,
        }

        if afci_required:
            code_ref = AFCI_LOCATIONS[space_type]

            if afci_protected:
                results.append(
                    ValidationResult(
                        status="PASS",
                        message=f"Circuit {circuit_num} serving {space_type} is AFCI protected as required",
                        nec_reference=f"NEC {code_ref}",
                        details=details,
                    )
                )
            else:
                results.append(
                    ValidationResult(
                        status="FAIL",
                        message=f"Circuit {circuit_num} serving {space_type} requires AFCI protection",
                        nec_reference=f"NEC {code_ref}",
                        details=details,
                    )
                )
        else:
            if afci_protected:
                results.append(
                    ValidationResult(
                        status="PASS",
                        message=f"Circuit {circuit_num} has AFCI protection (not required but acceptable)",
                        nec_reference="NEC 210.12",
                        details=details,
                    )
                )
            else:
                results.append(
                    ValidationResult(
                        status="PASS",
                        message=f"Circuit {circuit_num} serving {space_type} - AFCI not required",
                        nec_reference="NEC 210.12",
                        details=details,
                    )
                )

    return results
