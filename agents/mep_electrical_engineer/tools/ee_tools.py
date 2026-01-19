import json
import os
import sys
import argparse
from typing import Dict, Any

# Add agent root to path for relative imports in libs to work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import (
    voltage_drop,
    short_circuit,
    load_calc,
    conduit_fill,
    feeder_sizing,
    grounding,
    conductor_protection,
    equipment_selection,
    gfci_afci,
    working_space,
)

def to_dict(obj):
    """Recursively convert objects (like ValidationResult) to dictionaries."""
    if hasattr(obj, "__dict__"):
        return {k: to_dict(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [to_dict(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: to_dict(v) for k, v in obj.items()}
    return obj

def handle_voltage_drop(args):
    if args.subcommand == "calculate":
        return voltage_drop.calculate(
            conductor_size=args.size,
            length_feet=args.length,
            current_amps=args.current,
            voltage=args.voltage,
            phases=args.phases,
            power_factor=args.pf,
            conductor_material=args.material
        )
    elif args.subcommand == "recommend":
        return voltage_drop.calculate_required_size(
            length_feet=args.length,
            current_amps=args.current,
            voltage=args.voltage,
            max_voltage_drop_percent=args.limit,
            phases=args.phases,
            power_factor=args.pf,
            conductor_material=args.material
        )

def handle_short_circuit(args):
    if args.subcommand == "transformer":
        return short_circuit.calculate(
            transformer_kva=args.kva,
            transformer_impedance_percent=args.z,
            primary_voltage=args.v_pri,
            secondary_voltage=args.v_sec,
            conductor_size=args.size,
            conductor_length_feet=args.length,
            conductor_material=args.material,
            phases=args.phases,
            utility_sca=args.utility_sca
        )
    elif args.subcommand == "motor":
        return short_circuit.calculate_motor_contribution(
            motor_hp=args.hp,
            motor_voltage=args.voltage,
            motor_efficiency=args.eff,
            motor_power_factor=args.pf,
            phases=args.phases
        )

def handle_load_calc(args):
    if args.subcommand == "area":
        add_loads = None
        if args.additional:
            try:
                add_loads = json.loads(args.additional)
            except:
                return {"error": "Invalid JSON in --additional loads"}
        
        return load_calc.calculate(
            area_sqft=args.area,
            occupancy=args.occupancy,
            voltage=args.voltage,
            additional_loads=add_loads,
            apply_demand_factors=not args.no_demand
        )
    elif args.subcommand == "dwelling":
        return load_calc.calculate_dwelling_unit(
            area_sqft=args.area,
            num_small_appliance_circuits=args.sac,
            num_laundry_circuits=args.laundry,
            electric_range_kw=args.range,
            electric_dryer_kw=args.dryer,
            hvac_load_va=args.hvac,
            water_heater_kw=args.water_heater,
            voltage=args.voltage
        )

def handle_conduit_fill(args):
    try:
        conds = json.loads(args.conductors)
    except:
        return {"error": "Invalid JSON in --conductors"}
    
    if args.subcommand == "calculate":
        return conduit_fill.calculate(
            conductors=conds,
            conduit_type=args.type,
            include_ground=not args.no_ground,
            ground_size=args.ground_size,
            conduit_size=args.size
        )
    elif args.subcommand == "nipple":
        return conduit_fill.calculate_nipple_fill(
            conductors=conds,
            conduit_type=args.type
        )

def handle_feeder_sizing(args):
    if args.subcommand == "calculate":
        return feeder_sizing.calculate(
            load_amps=args.current,
            voltage=args.voltage,
            phases=args.phases,
            distance_feet=args.length,
            conductor_type=args.type,
            conduit_type=args.conduit,
            temperature=args.temp,
            conductor_material=args.material,
            max_voltage_drop_percent=args.limit,
            power_factor=args.pf,
            continuous_load=not args.non_continuous,
            num_current_carrying=args.count
        )
    elif args.subcommand == "parallel":
        return feeder_sizing.calculate_parallel_conductors(
            load_amps=args.current,
            voltage=args.voltage,
            phases=args.phases,
            distance_feet=args.length,
            conductor_type=args.type,
            conductor_material=args.material,
            max_voltage_drop_percent=args.limit,
            power_factor=args.pf
        )

def handle_grounding(args):
    if args.subcommand == "gec":
        return to_dict(grounding.validate_gec_size(
            service_conductor_size=args.service_size,
            gec_size=args.gec_size,
            material=args.material
        ))
    elif args.subcommand == "egc":
        return to_dict(grounding.validate_egc_size(
            ocpd_rating=args.ocpd,
            egc_size=args.egc_size,
            material=args.material
        ))

def handle_protection(args):
    if args.subcommand == "validate":
        return to_dict(conductor_protection.validate_conductor_protection(
            conductor_ampacity=args.ampacity,
            ocpd_rating=args.ocpd,
            conductor_size=args.size,
            allow_next_size_up=not args.no_next_size
        ))
    elif args.subcommand == "standard_size":
        return {"next_standard_size": conductor_protection.get_next_standard_ocpd_size(args.ampacity)}

def handle_equipment(args):
    if args.subcommand == "panel":
        return equipment_selection.select_panelboard(
            total_load_va=args.va,
            voltage=args.voltage,
            phases=args.phases,
            num_circuits=args.circuits,
            main_breaker=not args.mlo,
            aic_rating=args.aic
        )
    elif args.subcommand == "transformer":
        return equipment_selection.select_transformer(
            load_kva=args.kva,
            primary_voltage=args.v_pri,
            secondary_voltage=args.v_sec,
            phases=args.phases,
            application=args.app
        )
    elif args.subcommand == "disconnect":
        return equipment_selection.select_disconnect(
            load_amps=args.current,
            voltage=args.voltage,
            phases=args.phases,
            motor_load=args.motor,
            fused=not args.non_fused,
            nema_rating=args.nema
        )

def handle_gfci_afci(args):
    if args.subcommand == "check_gfci":
        try:
            receps = json.loads(args.receptacles)
            return to_dict(gfci_afci.check_gfci_protection(receps))
        except:
            return {"error": "Invalid JSON in --receptacles"}
    elif args.subcommand == "check_afci":
        try:
            circuits = json.loads(args.circuits)
            return to_dict(gfci_afci.check_afci_protection(circuits))
        except:
            return {"error": "Invalid JSON in --circuits"}

def handle_working_space(args):
    if args.subcommand == "depth":
        return to_dict(working_space.validate_working_space_depth(
            voltage=args.voltage,
            condition=args.condition,
            actual_depth_ft=args.depth
        ))
    elif args.subcommand == "width":
        return to_dict(working_space.validate_working_space_width(
            equipment_width_in=args.equip_width,
            actual_width_in=args.width
        ))
    elif args.subcommand == "dedicated":
        try:
            obs = json.loads(args.obstructions)
            return to_dict(working_space.validate_dedicated_space(obs))
        except:
            return {"error": "Invalid JSON in --obstructions"}

def main():
    parser = argparse.ArgumentParser(description="MEP Electrical Engineering Master Tools")
    subparsers = parser.add_subparsers(dest="tool", help="Engineering tool to use")

    # TOOL: voltage_drop
    vd_parser = subparsers.add_parser("voltage_drop")
    vd_subs = vd_parser.add_subparsers(dest="subcommand")
    v_calc = vd_subs.add_parser("calculate")
    v_calc.add_argument("--size", required=True)
    v_calc.add_argument("--length", type=float, required=True)
    v_calc.add_argument("--current", type=float, required=True)
    v_calc.add_argument("--voltage", type=int, required=True)
    v_calc.add_argument("--phases", type=int, default=3)
    v_calc.add_argument("--material", default="copper")
    v_calc.add_argument("--pf", type=float, default=0.85)
    v_rec = vd_subs.add_parser("recommend")
    v_rec.add_argument("--length", type=float, required=True)
    v_rec.add_argument("--current", type=float, required=True)
    v_rec.add_argument("--voltage", type=int, required=True)
    v_rec.add_argument("--limit", type=float, default=3.0)
    v_rec.add_argument("--phases", type=int, default=3)
    v_rec.add_argument("--material", default="copper")
    v_rec.add_argument("--pf", type=float, default=0.85)

    # TOOL: short_circuit
    sc_parser = subparsers.add_parser("short_circuit")
    sc_subs = sc_parser.add_subparsers(dest="subcommand")
    sc_trans = sc_subs.add_parser("transformer")
    sc_trans.add_argument("--kva", type=float, required=True)
    sc_trans.add_argument("--z", type=float)
    sc_trans.add_argument("--v_pri", type=int, default=480)
    sc_trans.add_argument("--v_sec", type=int, default=208)
    sc_trans.add_argument("--size", default="500")
    sc_trans.add_argument("--length", type=float, default=10)
    sc_trans.add_argument("--material", default="copper")
    sc_trans.add_argument("--utility_sca", type=float)
    sc_trans.add_argument("--phases", type=int, default=3)
    sc_motor = sc_subs.add_parser("motor")
    sc_motor.add_argument("--hp", type=float, required=True)
    sc_motor.add_argument("--voltage", type=int, default=480)
    sc_motor.add_argument("--eff", type=float, default=0.90)
    sc_motor.add_argument("--pf", type=float, default=0.85)
    sc_motor.add_argument("--phases", type=int, default=3)

    # TOOL: load_calc
    lc_parser = subparsers.add_parser("load_calc")
    lc_subs = lc_parser.add_subparsers(dest="subcommand")
    lc_area = lc_subs.add_parser("area")
    lc_area.add_argument("--area", type=float, required=True)
    lc_area.add_argument("--occupancy", required=True)
    lc_area.add_argument("--voltage", type=int, default=120)
    lc_area.add_argument("--additional")
    lc_area.add_argument("--no_demand", action="store_true")
    lc_dwell = lc_subs.add_parser("dwelling")
    lc_dwell.add_argument("--area", type=float, required=True)
    lc_dwell.add_argument("--sac", type=int, default=2)
    lc_dwell.add_argument("--laundry", type=int, default=1)
    lc_dwell.add_argument("--range", type=float, default=0)
    lc_dwell.add_argument("--dryer", type=float, default=0)
    lc_dwell.add_argument("--hvac", type=float, default=0)
    lc_dwell.add_argument("--water_heater", type=float, default=0)
    lc_dwell.add_argument("--voltage", type=int, default=240)

    # TOOL: conduit_fill
    cf_parser = subparsers.add_parser("conduit_fill")
    cf_subs = cf_parser.add_subparsers(dest="subcommand")
    cf_calc = cf_subs.add_parser("calculate")
    cf_calc.add_argument("--conductors", required=True)
    cf_calc.add_argument("--type", default="EMT")
    cf_calc.add_argument("--no_ground", action="store_true")
    cf_calc.add_argument("--ground_size")
    cf_calc.add_argument("--size")
    cf_nipple = cf_subs.add_parser("nipple")
    cf_nipple.add_argument("--conductors", required=True)
    cf_nipple.add_argument("--type", default="EMT")

    # TOOL: feeder_sizing
    fs_parser = subparsers.add_parser("feeder_sizing")
    fs_subs = fs_parser.add_subparsers(dest="subcommand")
    fs_calc = fs_subs.add_parser("calculate")
    fs_calc.add_argument("--current", type=float, required=True)
    fs_calc.add_argument("--voltage", type=int, required=True)
    fs_calc.add_argument("--phases", type=int, default=3)
    fs_calc.add_argument("--length", type=float, required=True)
    fs_calc.add_argument("--type", default="THHN")
    fs_calc.add_argument("--conduit", default="EMT")
    fs_calc.add_argument("--temp", type=float, default=30.0)
    fs_calc.add_argument("--material", default="copper")
    fs_calc.add_argument("--limit", type=float, default=3.0)
    fs_calc.add_argument("--pf", type=float, default=0.85)
    fs_calc.add_argument("--non_continuous", action="store_true")
    fs_calc.add_argument("--count", type=int, default=3)
    fs_par = fs_subs.add_parser("parallel")
    fs_par.add_argument("--current", type=float, required=True)
    fs_par.add_argument("--voltage", type=int, required=True)
    fs_par.add_argument("--phases", type=int, default=3)
    fs_par.add_argument("--length", type=float, required=True)
    fs_par.add_argument("--type", default="THHN")
    fs_par.add_argument("--material", default="copper")
    fs_par.add_argument("--limit", type=float, default=3.0)
    fs_par.add_argument("--pf", type=float, default=0.85)

    # TOOL: grounding
    gr_parser = subparsers.add_parser("grounding")
    gr_subs = gr_parser.add_subparsers(dest="subcommand")
    gr_gec = gr_subs.add_parser("gec")
    gr_gec.add_argument("--service_size", required=True)
    gr_gec.add_argument("--gec_size", required=True)
    gr_gec.add_argument("--material", default="copper")
    gr_egc = gr_subs.add_parser("egc")
    gr_egc.add_argument("--ocpd", type=int, required=True)
    gr_egc.add_argument("--egc_size", required=True)
    gr_egc.add_argument("--material", default="copper")

    # TOOL: protection
    pr_parser = subparsers.add_parser("protection")
    pr_subs = pr_parser.add_subparsers(dest="subcommand")
    pr_val = pr_subs.add_parser("validate")
    pr_val.add_argument("--ampacity", type=float, required=True)
    pr_val.add_argument("--ocpd", type=int, required=True)
    pr_val.add_argument("--size")
    pr_val.add_argument("--no_next_size", action="store_true")
    pr_std = pr_subs.add_parser("standard_size")
    pr_std.add_argument("--ampacity", type=float, required=True)

    # TOOL: equipment
    eq_parser = subparsers.add_parser("equipment")
    eq_subs = eq_parser.add_subparsers(dest="subcommand")
    eq_pan = eq_subs.add_parser("panel")
    eq_pan.add_argument("--va", type=float, required=True)
    eq_pan.add_argument("--voltage", type=int, required=True)
    eq_pan.add_argument("--phases", type=int, default=3)
    eq_pan.add_argument("--circuits", type=int, required=True)
    eq_pan.add_argument("--mlo", action="store_true")
    eq_pan.add_argument("--aic", type=int, default=10000)
    eq_trans = eq_subs.add_parser("transformer")
    eq_trans.add_argument("--kva", type=float, required=True)
    eq_trans.add_argument("--v_pri", type=int, required=True)
    eq_trans.add_argument("--v_sec", type=int, required=True)
    eq_trans.add_argument("--phases", type=int, default=3)
    eq_trans.add_argument("--app", default="general")
    eq_disc = eq_subs.add_parser("disconnect")
    eq_disc.add_argument("--current", type=float, required=True)
    eq_disc.add_argument("--voltage", type=int, required=True)
    eq_disc.add_argument("--phases", type=int, default=3)
    eq_disc.add_argument("--motor", action="store_true")
    eq_disc.add_argument("--non_fused", action="store_true")
    eq_disc.add_argument("--nema", default="1")

    # TOOL: safety (GFCI/AFCI)
    sf_parser = subparsers.add_parser("safety")
    sf_subs = sf_parser.add_subparsers(dest="subcommand")
    sf_gfci = sf_subs.add_parser("check_gfci")
    sf_gfci.add_argument("--receptacles", required=True, help="JSON array of objects")
    sf_afci = sf_subs.add_parser("check_afci")
    sf_afci.add_argument("--circuits", required=True, help="JSON array of objects")

    # TOOL: clearance (Working Space)
    cl_parser = subparsers.add_parser("clearance")
    cl_subs = cl_parser.add_subparsers(dest="subcommand")
    cl_dep = cl_subs.add_parser("depth")
    cl_dep.add_argument("--voltage", type=int, required=True)
    cl_dep.add_argument("--condition", type=int, choices=[1, 2, 3], required=True)
    cl_dep.add_argument("--depth", type=float, required=True)
    cl_wid = cl_subs.add_parser("width")
    cl_wid.add_argument("--equip_width", type=float, required=True)
    cl_wid.add_argument("--width", type=float, required=True)
    cl_ded = cl_subs.add_parser("dedicated")
    cl_ded.add_argument("--obstructions", required=True, help="JSON list of strings")

    args = parser.parse_args()

    try:
        if args.tool == "voltage_drop":
            result = handle_voltage_drop(args)
        elif args.tool == "short_circuit":
            result = handle_short_circuit(args)
        elif args.tool == "load_calc":
            result = handle_load_calc(args)
        elif args.tool == "conduit_fill":
            result = handle_conduit_fill(args)
        elif args.tool == "feeder_sizing":
            result = handle_feeder_sizing(args)
        elif args.tool == "grounding":
            result = handle_grounding(args)
        elif args.tool == "protection":
            result = handle_protection(args)
        elif args.tool == "equipment":
            result = handle_equipment(args)
        elif args.tool == "safety":
            result = handle_gfci_afci(args)
        elif args.tool == "clearance":
            result = handle_working_space(args)
        else:
            parser.print_help()
            sys.exit(1)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2))

if __name__ == "__main__":
    main()
