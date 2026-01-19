import json
import os
import sys

# Add lib to path for modular access
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.electrical_calculations import calculate_voltage_drop, size_grounding_conductor

def size_circuit(load_amps, voltage, length, phases=3, max_vd=3.0):
    # Load wire data
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'standard_wire_data.json')
    with open(data_path, 'r') as f:
        wire_data = json.load(f)["wire_sizes"]

    # 1. Min Ampacity (125% for continuous)
    min_ampacity = load_amps * 1.25
    
    # 2. Select wire based on ampacity
    selected_wire = None
    for wire, info in wire_data.items():
        if info["ampacity_75c"] >= min_ampacity:
            selected_wire = wire
            break
            
    if not selected_wire:
        return {"error": "Load exceeds standard table limits"}

    # 3. Check Voltage Drop
    vd_result = calculate_voltage_drop(
        voltage, load_amps, length, 
        wire_data[selected_wire]["circular_mils"], 
        phases=phases
    )
    
    # 4. Upsize if VD > max_vd
    current_wire = selected_wire
    while vd_result["percent_drop"] > max_vd:
        # Find next wire size
        wires = list(wire_data.keys())
        idx = wires.index(current_wire)
        if idx + 1 >= len(wires):
            break
        current_wire = wires[idx + 1]
        vd_result = calculate_voltage_drop(
            voltage, load_amps, length, 
            wire_data[current_wire]["circular_mils"], 
            phases=phases
        )

    # 5. Size Ground
    ground_size = size_grounding_conductor(min_ampacity)

    return {
        "load_amps": load_amps,
        "min_ampacity": round(min_ampacity, 2),
        "base_wire": selected_wire,
        "final_wire": current_wire,
        "voltage_drop_pct": vd_result["percent_drop"],
        "egc_size": ground_size,
        "upsized_for_vd": selected_wire != current_wire
    }

if __name__ == "__main__":
    # Example execution
    print(json.dumps(size_circuit(65, 480, 400), indent=2))
