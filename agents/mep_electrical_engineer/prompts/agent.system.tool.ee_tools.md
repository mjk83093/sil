### ee_tools:
Unified engineering calculator for MEP Electrical Engineering.
Performs deterministic calculations per **NEC 2017** and **EE_CalculationR1-25.pdf**.

Usage:
~~~json
{
    "thoughts": [
        "Analyzing feeder sizing per NEC 2017 Article 215...",
    ],
    "headline": "Sizing Feeder",
    "tool_name": "run_shell_command",
    "tool_args": {
        "command": "python3 tools/ee_tools.py feeder_sizing calculate --current 100 --voltage 480 --length 150"
    }
}
~~~

Available Tools:

#### 1. `voltage_drop`
- `calculate`: Get VD for a specific conductor.
- `recommend`: Get required conductor size for a VD limit.
- Args: `--size`, `--length`, `--current`, `--voltage`, `--phases`, `--limit`.

#### 2. `short_circuit`
- `transformer`: SCA at transformer secondary and a downstream point.
- `motor`: Motor short circuit contribution.
- Args: `--kva`, `--z`, `--v_sec`, `--size`, `--length`, `--hp`.

#### 3. `load_calc`
- `area`: General lighting and receptacle loads per NEC 220.
- `dwelling`: Full dwelling unit service calculation.
- Args: `--area`, `--occupancy`, `--sac`, `--range`, `--dryer`.

#### 4. `conduit_fill`
- `calculate`: Conduit sizing based on conductor list.
- `nipple`: Fill for nipples 24" or less (60% fill).
- Args: `--conductors` (JSON string), `--type` (EMT/PVC/RMC).

#### 5. `feeder_sizing`
- `calculate`: Full ampacity + voltage drop sizing.
- `parallel`: Parallel conductor sizing per NEC 310.10(G).
- Args: `--current`, `--voltage`, `--length`, `--type`.

#### 6. `grounding`
- `gec`: Validate Grounding Electrode Conductor per Table 250.66.
- `egc`: Validate Equipment Grounding Conductor per Table 250.122.
- Args: `--service_size`, `--ocpd`, `--gec_size`, `--egc_size`.

#### 7. `protection`
- `validate`: Validate conductor protection per NEC 240.4.
- `standard_size`: Get next standard OCPD size for an ampacity.
- Args: `--ampacity`, `--ocpd`, `--size`.

#### 8. `equipment`
- `panel`: Select panelboard size and AIC rating.
- `transformer`: Select transformer kVA and OCPD.
- `disconnect`: Select disconnect size and NEMA rating.
- Args: `--va`, `--voltage`, `--circuits`, `--kva`, `--current`, `--motor`.

#### 9. `safety`
- `check_gfci`: Check GFCI requirements for a list of locations.
- `check_afci`: Check AFCI requirements for dwelling unit circuits.
- Args: `--receptacles` (JSON array), `--circuits` (JSON array).

#### 10. `clearance`
- `depth`: Validate working space depth per Table 110.26(A)(1).
- `width`: Validate working space width per 110.26(A)(2).
- `dedicated`: Validate dedicated space clear of obstructions (110.26(E)).
- Args: `--voltage`, `--condition`, `--depth`, `--equip_width`, `--obstructions`.