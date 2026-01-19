import json
import os
import sys
import argparse

# Add agent root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.short_circuit import calculate, calculate_motor_contribution

def main():
    parser = argparse.ArgumentParser(description="NEC Short Circuit Calculator")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Command: transformer
    trans_parser = subparsers.add_parser("transformer", help="Calculate SCA at transformer and a point")
    trans_parser.add_argument("--kva", type=float, required=True, help="Transformer kVA")
    trans_parser.add_argument("--z", type=float, help="Transformer %Z (impedance)")
    trans_parser.add_argument("--v_pri", type=int, default=480, help="Primary Voltage")
    trans_parser.add_argument("--v_sec", type=int, default=208, help="Secondary Voltage")
    trans_parser.add_argument("--size", default="500", help="Conductor size")
    trans_parser.add_argument("--length", type=float, default=10, help="Conductor length (feet)")
    trans_parser.add_argument("--material", default="copper", choices=["copper", "aluminum"], help="Material")
    trans_parser.add_argument("--utility_sca", type=float, help="Utility available SCA")

    # Command: motor
    motor_parser = subparsers.add_parser("motor", help="Calculate motor short circuit contribution")
    motor_parser.add_argument("--hp", type=float, required=True, help="Motor Horsepower")
    motor_parser.add_argument("--voltage", type=int, default=480, help="Motor Voltage")
    motor_parser.add_argument("--eff", type=float, default=0.90, help="Efficiency")
    motor_parser.add_argument("--pf", type=float, default=0.85, help="Power factor")

    args = parser.parse_args()

    if args.command == "transformer":
        result = calculate(
            transformer_kva=args.kva,
            transformer_impedance_percent=args.z,
            primary_voltage=args.v_pri,
            secondary_voltage=args.v_sec,
            conductor_size=args.size,
            conductor_length_feet=args.length,
            conductor_material=args.material,
            utility_sca=args.utility_sca
        )
    elif args.command == "motor":
        result = calculate_motor_contribution(
            motor_hp=args.hp,
            motor_voltage=args.voltage,
            motor_efficiency=args.eff,
            motor_power_factor=args.pf
        )
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
