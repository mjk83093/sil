# NEC Terminology

## Overview
This file provides a glossary of core National Electrical Code (NEC) terms essential for Electrical Engineering AI (EEAI) systems to ensure regulatory compliance and technical accuracy.

## Definition
The terminology defined here follows the NFPA 70 (NEC) Article 100 definitions, adapted for automated system processing.

## Key Terms

- **Ampacity**: The maximum current, in amperes, that a conductor can carry continuously under the conditions of use without exceeding its temperature rating.
- **Bonding (Bonded)**: Connected to establish electrical continuity and conductivity.
- **Branch Circuit**: The circuit conductors between the final overcurrent device protecting the circuit and the outlet(s).
- **Continuous Load**: A load where the maximum current is expected to continue for 3 hours or more.
- **Feeder**: All circuit conductors between the service equipment, the source of a separately derived system, or other power supply source and the final branch-circuit overcurrent device.
- **Grounding Conductor, Equipment (EGC)**: The conductive path(s) that provides a ground-fault current path and connects normally non-current-carrying metal parts of equipment together and to the system grounded conductor or to the grounding electrode conductor, or both.
- **Grounded Conductor**: A system or circuit conductor that is intentionally grounded (usually the Neutral).
- **Overcurrent Protective Device (OCPD)**: A device capable of providing protection for service, feeder, and branch circuits and equipment over the full range of overcurrents between its rated current and its interrupting rating.
- **Service**: The conductors and equipment for delivering electric energy from the serving utility to the wiring system of the premises served.
- **Qualified Person**: One who has skills and knowledge related to the construction and operation of the electrical equipment and installations and has received safety training to recognize and avoid the hazards involved.
- **Raceway**: An enclosed channel of metal or nonmetallic materials designed expressly for holding wires, cables, or busbars, with additional functions as permitted in this Code.
- **Voltage to Ground**: For grounded circuits, the voltage between the given conductor and that point or conductor of the circuit that is grounded; for ungrounded circuits, the greatest voltage between the given conductor and any other conductor of the circuit.
- **In Sight From (Within Sight From)**: Where this Code specifies that one equipment shall be "in sight from" another equipment, the specified equipment is to be visible and not more than 15 m (50 ft) distant from the other.

## Business Rules
1. **Strict Adherence**: All system outputs must use Article 100 definitions when referencing regulatory requirements.
2. **Contextual Usage**: Distinguish between "Grounded" (Neutral) and "Grounding" (Safety Earth) in all calculations and diagrams.

## Relationships
- **Depends on**: None
- **Used by**: `electrical-entities.md`, `calculation-workflows.md`, `nec-2023-core-rules.md`

## Examples
```yaml
term_application:
  term: "Continuous Load"
  application: "Office lighting operating during business hours (8am-5pm)"
  calculation_impact: "Must be sized at 125% of actual load per NEC 210.19(A)(1)"
```

## Common Patterns
- **Accessible vs. Readily Accessible**: Used to determine mounting heights and enclosure types.
- **Bonding vs. Grounding**: Used in service entrance vs. sub-panel wiring logic.
