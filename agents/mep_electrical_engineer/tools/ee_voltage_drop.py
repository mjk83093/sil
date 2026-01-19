import json
import os
import sys
import argparse

# Add agent root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.voltage_drop import calculate, calculate_required_size

def main():
    parser = argparse.ArgumentParser(description="NEC Voltage Drop Calculator")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Command: calculate
    calc_parser = subparsers.add_parser("calculate", help="Calculate VD for a specific conductor")
    calc_parser.add_argument("--size", required=True, help="Conductor size (e.g., '10', '1/0')")
    calc_parser.add_argument("--length", type=float, required=True, help="Length in feet")
    calc_parser.add_argument("--current", type=float, required=True, help="Current in amps")
    calc_parser.add_argument("--voltage", type=int, required=True, help="System voltage")
    calc_parser.add_argument("--phases", type=int, default=3, choices=[1, 3], help="Phases")
    calc_parser.add_argument("--material", default="copper", choices=["copper", "aluminum"], help="Material")
    calc_parser.add_argument("--pf", type=float, default=0.85, help="Power factor")

    # Command: recommend
    rec_parser = subparsers.add_parser("recommend", help="Recommend conductor size based on VD limit")
    rec_parser.add_argument("--length", type=float, required=True, help="Length in feet")
    rec_parser.add_argument("--current", type=float, required=True, help="Current in amps")
    rec_parser.add_argument("--voltage", type=int, required=True, help="System voltage")
    rec_parser.add_argument("--limit", type=float, default=3.0, help="Max VD percentage")
    rec_parser.add_argument("--phases", type=int, default=3, choices=[1, 3], help="Phases")
    rec_parser.add_argument("--material", default="copper", choices=["copper", "aluminum"], help="Material")
    rec_parser.add_argument("--pf", type=float, default=0.85, help="Power factor")

    args = parser.parse_args()

    if args.command == "calculate":
        result = calculate(
            conductor_size=args.size,
            length_feet=args.length,
            current_amps=args.current,
            voltage=args.voltage,
            phases=args.phases,
            power_factor=args.pf,
            conductor_material=args.material
        )
    elif args.command == "recommend":
        result = calculate_required_size(
            length_feet=args.length,
            current_amps=args.current,
            voltage=args.voltage,
            max_voltage_drop_percent=args.limit,
            phases=args.phases,
            power_factor=args.pf,
            conductor_material=args.material
        )
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
