# Complete Load Calculation Worksheet - NEC Article 220

## Overview

This document provides comprehensive load calculation templates following NEC Article 220 for various occupancy types. Each template includes input fields, NEC article references, formulas, demand factor applications, and service size determination.

**Templates Included:**
1. Dwelling Unit - Standard Method (NEC 220.40)
2. Dwelling Unit - Optional Method (NEC 220.82)
3. Multifamily Dwelling Calculation
4. Commercial Building Calculation
5. School Building Calculation

**Integration with Reference Documents:**
These templates implement the detailed procedures from `Article_220_Load_Calculations_Detailed.md` and can be used for manual calculations or implemented in Excel/Python.

**How to Use:**
- Fill in all input fields with actual project data
- Apply demand factors per NEC tables
- Sum loads and determine service size
- Have Professional Engineer review and seal calculation

---

## Template 1: Dwelling Unit - Standard Method (NEC 220.40)

**Project Information:**
- Project Name: _____________________________________________________
- Address: __________________________________________________________
- Owner: ____________________________________________________________
- Calculated By: ________________________ Date: ___________________
- Reviewed By (PE): _____________________ License #: ______________

**Building Data:**
- Square Footage: ____________ sq ft (outside dimensions)
- Number of Bedrooms: ____________
- Voltage/Phase: [ ] 120/240V, 1Ø  [ ] Other: __________________

---

### Step 1: General Lighting and Receptacles
**NEC Reference:** 220.12, Table 220.12

| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Square footage | __________ sq ft | |
| Unit load (3 VA/sq ft for dwelling) | × 3 VA/sq ft | |
| **General Lighting Load** | | **__________ VA** |

---

### Step 2: Small Appliance Branch Circuits
**NEC Reference:** 220.52(A)

| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Number of small appliance circuits | __________ circuits | |
| (Minimum 2 required per NEC 210.11(C)(1)) | | |
| Load per circuit | × 1500 VA | |
| **Small Appliance Load** | | **__________ VA** |

---

### Step 3: Laundry Branch Circuit
**NEC Reference:** 220.52(B)

| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Number of laundry circuits | __________ circuit | |
| (Minimum 1 required per NEC 210.11(C)(2)) | | |
| Load per circuit | × 1500 VA | |
| **Laundry Circuit Load** | | **__________ VA** |

---

### Step 4: Demand Factor Application (220.42)
**NEC Reference:** Table 220.42

| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| General lighting (from Step 1) | __________ VA | |
| Small appliance (from Step 2) | + __________ VA | |
| Laundry (from Step 3) | + __________ VA | |
| **Subtotal** | | **__________ VA** |
| | | |
| **Apply Demand Factors per Table 220.42:** | | |
| First 3,000 VA | × 100% = | __________ VA |
| Next 117,000 VA (3,001 to 120,000) | × 35% = | __________ VA |
| Remainder over 120,000 VA | × 25% = | __________ VA |
| **Demand Load (Lighting/Appliances)** | | **__________ VA** |

---

### Step 5: Electric Range (or Cooktop and Oven)
**NEC Reference:** 220.55, Table 220.55

**For Standard Electric Range:**
| Item | Nameplate Rating | Demand Load (VA) |
|------|------------------|------------------|
| Electric range rating | __________ kW | |
| Demand per Table 220.55 (Column C) | | __________ VA |
| (8 kW for one range, if <12 kW nameplate) | | |
| **Electric Range Demand Load** | | **__________ VA** |

**For Separate Cooktop and Oven(s):**
| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Cooktop nameplate rating | __________ kW | __________ VA |
| Wall oven(s) nameplate rating | + __________ kW | + __________ VA |
| Total rating | | __________ VA |
| Apply Table 220.55, Column C | | __________ VA |
| **Cooktop/Oven Demand Load** | | **__________ VA** |

---

### Step 6: Electric Dryer
**NEC Reference:** 220.54

| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Dryer nameplate rating | __________ kW | __________ VA |
| Minimum if nameplate < 5000 VA | 5000 VA | |
| Use larger of nameplate or 5000 VA | | |
| **Electric Dryer Load** | | **__________ VA** |

---

### Step 7: Electric Water Heater
**NEC Reference:** 220.14(C)

| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Water heater nameplate rating | __________ kW | __________ VA |
| **Electric Water Heater Load** | | **__________ VA** |

---

### Step 8: Fixed Appliances (Dishwasher, Disposal, etc.)
**NEC Reference:** 220.53

| Appliance | Nameplate Rating | Load (VA) |
|-----------|------------------|-----------|
| Dishwasher | __________ VA | __________ VA |
| Garbage disposal | __________ VA | __________ VA |
| Trash compactor | __________ VA | __________ VA |
| Bathroom exhaust fan | __________ VA | __________ VA |
| Other: ______________ | __________ VA | __________ VA |
| **Subtotal Fixed Appliances** | | **__________ VA** |
| | | |
| **Demand Factor per NEC 220.53:** | | |
| If 4 or more appliances: Apply 75% demand | | |
| Fixed appliances × 75% | | __________ VA |
| (If 3 or fewer, use 100%) | | |
| **Fixed Appliance Demand Load** | | **__________ VA** |

---

### Step 9: Heating or Air Conditioning (Larger Load)
**NEC Reference:** 220.60

**Electric Heating:**
| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Electric heating nameplate | __________ kW | __________ VA |
| **Electric Heating Load** | | **__________ VA** |

**Air Conditioning:**
| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| A/C compressor nameplate MCA | __________ A | |
| Voltage | × __________ V | |
| **Air Conditioning Load** | | **__________ VA** |

**Use Larger Load (Heating or A/C):**
| **Heating/Cooling Load** | | **__________ VA** |

---

### Step 10: Total Calculated Load Summary

| Item | Load (VA) | Amperes @ 240V |
|------|-----------|----------------|
| Demand load (lighting/appliances) - Step 4 | __________ VA | __________ A |
| Electric range - Step 5 | + __________ VA | + __________ A |
| Electric dryer - Step 6 | + __________ VA | + __________ A |
| Water heater - Step 7 | + __________ VA | + __________ A |
| Fixed appliances (demand) - Step 8 | + __________ VA | + __________ A |
| Heating or A/C (larger) - Step 9 | + __________ VA | + __________ A |
| **Total Calculated Load** | **__________ VA** | **__________ A** |

**Formula:** Amperes = VA ÷ 240V

---

### Step 11: Service Size Determination
**NEC Reference:** 230.42(B), 310.15(B)(7)

| Standard Service Sizes (NEC 240.6) | Selected |
|------------------------------------|----------|
| 100 amperes | [ ] |
| 125 amperes | [ ] |
| 150 amperes | [ ] |
| 200 amperes | [ ] |
| 400 amperes | [ ] |

**Recommended Service Size:** __________ amperes

**Notes:**
- Minimum service for dwelling ≥ 100 amperes per NEC 230.79(C)
- Service conductors sized per NEC Table 310.15(B)(7) (for dwelling services only)
- If calculated load < 100A, still provide 100A minimum service

---

### Step 12: Service Conductor Sizing
**NEC Reference:** Table 310.15(B)(7) - Dwelling Services 120/240V, Single Phase

| Copper Conductors (AWG or kcmil) | Aluminum Conductors (AWG or kcmil) | Service Rating |
|-----------------------------------|-------------------------------------|----------------|
| 4 AWG | 2 AWG | 100A |
| 3 AWG | 1 AWG | 110A |
| 2 AWG | 1/0 AWG | 125A |
| 1 AWG | 2/0 AWG | 150A |
| 1/0 AWG | 3/0 AWG | 175A |
| 2/0 AWG | 4/0 AWG | 200A |
| 3/0 AWG | 250 kcmil | 225A |
| 4/0 AWG | 300 kcmil | 250A |

**Selected Conductor:** __________ AWG/kcmil [ ] Copper [ ] Aluminum

**Neutral Conductor Sizing (NEC 220.61):**
- Neutral may be sized per NEC 220.61 for unbalanced load
- Minimum neutral: __________ AWG/kcmil

---

### Calculation Certification

I certify that this load calculation has been prepared in accordance with NEC Article 220 and represents the anticipated electrical load for this dwelling unit.

**Calculated By:**
Signature: _________________________ Date: _________________
Printed Name: ______________________

**Professional Engineer Review:**
Signature: _________________________ Date: _________________
Printed Name: ______________________
PE License Number: _________________ State: ______________

---

## Template 2: Dwelling Unit - Optional Method (NEC 220.82)

**Project Information:**
- Project Name: _____________________________________________________
- Address: __________________________________________________________
- Owner: ____________________________________________________________
- Calculated By: ________________________ Date: ___________________
- Reviewed By (PE): _____________________ License #: ______________

**Building Data:**
- Square Footage: ____________ sq ft (outside dimensions)
- Voltage/Phase: 120/240V, 1Ø
- Number of Bedrooms: ____________

**Note:** Optional method may be used for dwelling unit served by single 120/240V or 208Y/120V, 3-wire, single-phase service with total connected load ≥ 10 kVA (100A @ 240V or more).

---

### Step 1: General Loads (Air Conditioning and Heating Excluded)
**NEC Reference:** 220.82(B)(1) through (B)(4)

| Load Item | Calculation | Load (VA) |
|-----------|-------------|-----------|
| **General Lighting and Receptacles:** | | |
| Square footage | __________ sq ft | |
| × 3 VA/sq ft | × 3 VA/sq ft | __________ VA |
| | | |
| **Small Appliance and Laundry Circuits:** | | |
| Number of circuits (min 3: 2 small appliance + 1 laundry) | __________ circuits | |
| × 1500 VA per circuit | × 1500 VA | __________ VA |
| | | |
| **All Other Loads:** | | |
| Electric range (nameplate) | __________ kW | __________ VA |
| Electric dryer (nameplate or 5000 VA min) | __________ kW | __________ VA |
| Water heater (nameplate) | __________ kW | __________ VA |
| Dishwasher | __________ VA | __________ VA |
| Garbage disposal | __________ VA | __________ VA |
| Other appliances: _____________ | __________ VA | __________ VA |
| Other appliances: _____________ | __________ VA | __________ VA |
| | | |
| **Subtotal (Excluding HVAC)** | | **__________ VA** |

---

### Step 2: Apply Demand Factors to General Loads
**NEC Reference:** Table 220.82

| Load Range | Demand Factor | Demand Load (VA) |
|------------|---------------|------------------|
| **First 10 kVA (10,000 VA)** | 100% | __________ VA |
| (Use lesser of subtotal or 10,000 VA) | | |
| | | |
| **Remainder over 10 kVA** | 40% | __________ VA |
| (Subtotal minus 10,000 VA) × 40% | | |
| | | |
| **Total Demand Load (General)** | | **__________ VA** |

---

### Step 3: Heating and Air Conditioning
**NEC Reference:** 220.82(C)

**Air Conditioning:**
| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| A/C compressor nameplate MCA | __________ A | |
| × Voltage (typically 240V) | × __________ V | |
| Air conditioning load (100%) | | __________ VA |

**Electric Heating:**
| Item | Calculation | Load (VA) |
|------|-------------|-----------|
| Electric heating nameplate | __________ kW | __________ VA |
| (Include heat pump auxiliary strips) | | |

**Select the Larger of A/C or Heating:**
| **Heating/Cooling Load (100%)** | | **__________ VA** |

**If both A/C and heating exist, apply 220.82(C):**
- Use 100% of air conditioning load
- If central electric heat, include at 100% (largest of A/C or heat)
- If A/C and separate heating units, use larger at 100%

---

### Step 4: Total Optional Calculated Load

| Item | Load (VA) | Amperes @ 240V |
|------|-----------|----------------|
| General loads (demand) - Step 2 | __________ VA | __________ A |
| Heating or A/C (100%) - Step 3 | + __________ VA | + __________ A |
| **Total Optional Calculated Load** | **__________ VA** | **__________ A** |

**Formula:** Amperes = VA ÷ 240V

---

### Step 5: Service Size Determination
**NEC Reference:** 230.42(B), 310.15(B)(7)

| Standard Service Sizes (NEC 240.6) | Selected |
|------------------------------------|----------|
| 100 amperes | [ ] |
| 125 amperes | [ ] |
| 150 amperes | [ ] |
| 200 amperes | [ ] |

**Recommended Service Size:** __________ amperes

**Notes:**
- Minimum service for dwelling ≥ 100 amperes per NEC 230.79(C)
- Optional method typically results in smaller service than standard method
- Verify total connected load ≥ 10 kVA for optional method to be valid

---

### Step 6: Service Conductor Sizing
**NEC Reference:** Table 310.15(B)(7) - Dwelling Services 120/240V, Single Phase

**Selected Conductor:** __________ AWG/kcmil [ ] Copper [ ] Aluminum

**Neutral Conductor Sizing (NEC 220.61):**
- Neutral sized for maximum unbalanced load
- Minimum neutral: __________ AWG/kcmil

---

### Calculation Certification

I certify that this optional load calculation has been prepared in accordance with NEC 220.82 and represents the anticipated electrical load for this dwelling unit.

**Calculated By:**
Signature: _________________________ Date: _________________
Printed Name: ______________________

**Professional Engineer Review:**
Signature: _________________________ Date: _________________
Printed Name: ______________________
PE License Number: _________________ State: ______________

---

## Template 3: Multifamily Dwelling Calculation

**Project Information:**
- Project Name: _____________________________________________________
- Address: __________________________________________________________
- Owner: ____________________________________________________________
- Calculated By: ________________________ Date: ___________________
- Reviewed By (PE): _____________________ License #: ______________

**Building Data:**
- Total Number of Dwelling Units: ____________
- Service Voltage/Phase: [ ] 120/208V, 3Ø  [ ] 277/480V, 3Ø  [ ] Other: __________

---

### Step 1: Individual Dwelling Unit Load
**NEC Reference:** 220.84 (Optional Method for Multifamily)

**Calculate load for one typical unit using NEC 220.82 Optional Method:**

| Load Item | Calculation | Load (VA) |
|-----------|-------------|-----------|
| General lighting (3 VA/sq ft) | __________ sq ft × 3 VA | __________ VA |
| Small appliance circuits (2 min) | __________ circuits × 1500 VA | __________ VA |
| Laundry circuit (1) | 1 × 1500 VA | 1500 VA |
| Electric range (nameplate) | __________ kW | __________ VA |
| Electric dryer (nameplate or 5 kW min) | __________ kW | __________ VA |
| Water heater | __________ kW | __________ VA |
| A/C or heating (larger) | __________ kW | __________ VA |
| Other appliances | __________ VA | __________ VA |
| **Total Connected Load per Unit** | | **__________ VA** |

**Apply Demand per Table 220.82:**
| First 10 kVA @ 100% | | __________ VA |
| Remainder @ 40% | | + __________ VA |
| **Demand Load per Unit** | | **__________ VA** |

---

### Step 2: Total House Load (All Units)
**NEC Reference:** Table 220.84 (Demand Factor for Multiple Units)

| Number of Units | Total Connected Load | Demand Factor | Demand Load |
|-----------------|----------------------|---------------|-------------|
| __________ units | __________ VA/unit | | |
| Total connected | × __________ units | | __________ VA |
| | | | |
| **Apply Demand Factor per Table 220.84:** | | | |
| Demand factor for _____ units | × _____ % | | |
| (See Table 220.84 for factor) | | | |
| **Total House Load (All Units)** | | | **__________ VA** |

**NEC Table 220.84 Demand Factors:**
| Number of Units | Demand Factor |
|-----------------|---------------|
| 3-5 | 45% |
| 6-7 | 44% |
| 8-10 | 43% |
| 11-15 | 42% |
| 16-20 | 41% |
| 21-25 | 40% |
| 26-30 | 39% |
| 31-40 | 38% |
| 41-50 | 37% |
| 51-62 | 36% |
| 63+ | 35% |

---

### Step 3: House Loads (Common Areas)
**NEC Reference:** 220.14, 220.42

| Load Item | Calculation | Load (VA) |
|-----------|-------------|-----------|
| **Common Area Lighting:** | | |
| Corridors, stairways, lobby | __________ sq ft × 0.5 VA/sq ft | __________ VA |
| Laundry room | __________ sq ft × 3 VA/sq ft | __________ VA |
| Office | __________ sq ft × 3.5 VA/sq ft | __________ VA |
| | | |
| **Exterior Lighting:** | __________ VA | __________ VA |
| **Elevator(s):** | __________ VA | __________ VA |
| **Fire pump:** | __________ VA | __________ VA |
| **HVAC common areas:** | __________ VA | __________ VA |
| **Parking lot lighting:** | __________ VA | __________ VA |
| **Other house loads:** _____________ | __________ VA | __________ VA |
| | | |
| **Total House Loads** | | **__________ VA** |

---

### Step 4: Total Building Load Summary

| Load Item | Load (VA) | Amperes @ 208V, 3Ø |
|-----------|-----------|---------------------|
| Dwelling unit demand (Step 2) | __________ VA | __________ A |
| House loads (Step 3) | + __________ VA | + __________ A |
| **Total Building Load** | **__________ VA** | **__________ A** |

**Formula for 3-phase:** Amperes = VA ÷ (208V × √3) = VA ÷ 360

---

### Step 5: Service Size Determination

| Standard Service Sizes (NEC 240.6) | Selected |
|------------------------------------|----------|
| 400 amperes | [ ] |
| 600 amperes | [ ] |
| 800 amperes | [ ] |
| 1000 amperes | [ ] |
| 1200 amperes | [ ] |
| 1600 amperes | [ ] |
| 2000 amperes | [ ] |

**Recommended Service Size:** __________ amperes

**Service Configuration:**
- [ ] Single service
- [ ] Multiple services (per NEC 230.2 exception)
- Number of services if multiple: __________

---

### Step 6: Service Conductor Sizing
**NEC Reference:** Table 310.15(B)(16), 75°C column

**Selected Conductor:** __________ AWG/kcmil per phase [ ] Copper [ ] Aluminum
**Neutral Conductor:** __________ AWG/kcmil (sized per NEC 220.61)
**Grounding Electrode Conductor:** __________ AWG (per NEC Table 250.66)

---

### Calculation Certification

I certify that this multifamily dwelling load calculation has been prepared in accordance with NEC 220.84 and represents the anticipated electrical load for this building.

**Calculated By:**
Signature: _________________________ Date: _________________
Printed Name: ______________________

**Professional Engineer Review:**
Signature: _________________________ Date: _________________
Printed Name: ______________________
PE License Number: _________________ State: ______________

---

## Template 4: Commercial Building Calculation

**Project Information:**
- Project Name: _____________________________________________________
- Address: __________________________________________________________
- Owner: ____________________________________________________________
- Calculated By: ________________________ Date: ___________________
- Reviewed By (PE): _____________________ License #: ______________

**Building Data:**
- Total Square Footage: ____________ sq ft
- Occupancy Type(s): _________________________________________________
- Service Voltage/Phase: [ ] 120/208V, 3Ø  [ ] 277/480V, 3Ø  [ ] Other: __________

---

### Step 1: General Lighting Load
**NEC Reference:** 220.12, Table 220.12

| Occupancy Type | Area (sq ft) | Unit Load (VA/sq ft) | Load (VA) |
|----------------|--------------|----------------------|-----------|
| Office | __________ | 3.5 VA/sq ft | __________ VA |
| Retail/Sales | __________ | 3.0 VA/sq ft | __________ VA |
| Warehouse | __________ | 0.25 VA/sq ft | __________ VA |
| School/Classroom | __________ | 3.0 VA/sq ft | __________ VA |
| Restaurant | __________ | 2.0 VA/sq ft | __________ VA |
| Hospital | __________ | 2.0 VA/sq ft | __________ VA |
| Other: __________ | __________ | _____ VA/sq ft | __________ VA |
| | | | |
| **Total General Lighting Load** | | | **__________ VA** |

---

### Step 2: Receptacle Load
**NEC Reference:** 220.14(I), 220.44

**Non-Dwelling Receptacles:**
| Load Item | Calculation | Load (VA) |
|-----------|-------------|-----------|
| Number of receptacles | __________ receptacles | |
| × 180 VA per receptacle | × 180 VA | __________ VA |
| (or actual load if known to be more) | | |
| | | |
| **Receptacle Load Subtotal** | | **__________ VA** |

**Demand Factor per NEC 220.44:**
| First 10 kVA @ 100% | | __________ VA |
| Remainder @ 50% | × 50% | + __________ VA |
| **Receptacle Demand Load** | | **__________ VA** |

---

### Step 3: HVAC Load
**NEC Reference:** 220.50, 220.60

| Equipment | Nameplate or MCA | Load (VA) |
|-----------|------------------|-----------|
| Rooftop unit #1 | __________ A @ _____ V, ___ Ø | __________ VA |
| Rooftop unit #2 | __________ A @ _____ V, ___ Ø | __________ VA |
| Split system #1 (outdoor) | __________ A @ _____ V, ___ Ø | __________ VA |
| Split system #1 (indoor AHU) | __________ A @ _____ V, ___ Ø | __________ VA |
| Exhaust fans | __________ A @ _____ V, ___ Ø | __________ VA |
| Other HVAC: ____________ | __________ A @ _____ V, ___ Ø | __________ VA |
| | | |
| **Total HVAC Load (100%)** | | **__________ VA** |

**Formula for 3-phase:** VA = Amps × Volts × √3 × PF (use PF = 1.0 if unknown)

---

### Step 4: Motors and Motor-Driven Equipment
**NEC Reference:** 220.50, 430.24

| Motor Equipment | Nameplate HP | FLA from NEC Table 430.250 | Load (VA) |
|-----------------|--------------|----------------------------|-----------|
| Motor #1: __________ | _____ HP | _____ A @ _____ V | __________ VA |
| Motor #2: __________ | _____ HP | _____ A @ _____ V | __________ VA |
| Motor #3: __________ | _____ HP | _____ A @ _____ V | __________ VA |
| | | | |
| **Total Motor Load** | | | **__________ VA** |

**Note:** Use 125% of largest motor FLA plus 100% of other motors per NEC 430.24

---

### Step 5: Kitchen Equipment
**NEC Reference:** 220.56

| Equipment | Nameplate Rating | Demand Factor | Demand Load (VA) |
|-----------|------------------|---------------|------------------|
| Electric range | __________ kW | See Table 220.56 | __________ VA |
| Fryer | __________ kW | 100% | __________ VA |
| Griddle | __________ kW | 100% | __________ VA |
| Ovens | __________ kW | 100% | __________ VA |
| Dishwasher (booster heater) | __________ kW | 100% | __________ VA |
| Other: ____________ | __________ kW | 100% | __________ VA |
| | | | |
| **Total Kitchen Equipment Demand** | | | **__________ VA** |

**Note:** Apply Table 220.56 demand factors if applicable (typically for larger commercial kitchens with 6+ units)

---

### Step 6: Water Heaters and Large Appliances
**NEC Reference:** 220.51, 220.82

| Equipment | Nameplate Rating | Load (VA) |
|-----------|------------------|-----------|
| Water heater(s) | __________ kW | __________ VA |
| Boiler | __________ kW | __________ VA |
| Other large appliances: ________ | __________ kW | __________ VA |
| | | |
| **Total Water Heater/Appliance Load** | | **__________ VA** |

---

### Step 7: Special Loads

| Load Type | Calculation | Load (VA) |
|-----------|-------------|-----------|
| Elevator(s) | __________ A @ _____ V | __________ VA |
| Fire pump | __________ A @ _____ V | __________ VA |
| Emergency generator (house loads) | __________ A @ _____ V | __________ VA |
| Data center/server room | __________ VA | __________ VA |
| Electric vehicle charging (EVSE) | __________ VA | __________ VA |
| Other: _________________ | __________ VA | __________ VA |
| | | |
| **Total Special Loads** | | **__________ VA** |

---

### Step 8: Exterior and Parking Lot Lighting
**NEC Reference:** 220.14(F)

| Load Item | Calculation | Load (VA) |
|-----------|-------------|-----------|
| Parking lot lighting | __________ fixtures × _____ W | __________ VA |
| Building perimeter lighting | __________ fixtures × _____ W | __________ VA |
| Signage | __________ VA | __________ VA |
| | | |
| **Total Exterior Lighting** | | **__________ VA** |

---

### Step 9: Total Commercial Building Load Summary

| Load Item | Load (VA) | Amperes @ 208V, 3Ø |
|-----------|-----------|---------------------|
| General lighting (Step 1) | __________ VA | __________ A |
| Receptacles (demand) (Step 2) | __________ VA | __________ A |
| HVAC (Step 3) | __________ VA | __________ A |
| Motors (Step 4) | __________ VA | __________ A |
| Kitchen equipment (Step 5) | __________ VA | __________ A |
| Water heaters/appliances (Step 6) | __________ VA | __________ A |
| Special loads (Step 7) | __________ VA | __________ A |
| Exterior lighting (Step 8) | __________ VA | __________ A |
| **Total Calculated Load** | **__________ VA** | **__________ A** |

**Formula for 3-phase:** Amperes = VA ÷ (208V × √3 × PF) = VA ÷ 360 (assuming PF = 1.0)

---

### Step 10: Service Size Determination

| Standard Service Sizes (NEC 240.6) | Selected |
|------------------------------------|----------|
| 400 amperes | [ ] |
| 600 amperes | [ ] |
| 800 amperes | [ ] |
| 1000 amperes | [ ] |
| 1200 amperes | [ ] |
| 1600 amperes | [ ] |
| 2000 amperes | [ ] |

**Recommended Service Size:** __________ amperes

**Future Growth Allowance:** __________ % (typically 20-25%)
**Service with Future Growth:** __________ amperes

---

### Step 11: Service Conductor Sizing
**NEC Reference:** Table 310.15(B)(16), 75°C column

**Selected Conductor:** __________ AWG/kcmil per phase [ ] Copper [ ] Aluminum
**Number of conductors per phase:** __________ (if parallel)
**Neutral Conductor:** __________ AWG/kcmil (sized per NEC 220.61)
**Grounding Electrode Conductor:** __________ AWG (per NEC Table 250.66)

---

### Calculation Certification

I certify that this commercial building load calculation has been prepared in accordance with NEC Article 220 and represents the anticipated electrical load for this facility.

**Calculated By:**
Signature: _________________________ Date: _________________
Printed Name: ______________________

**Professional Engineer Review:**
Signature: _________________________ Date: _________________
Printed Name: ______________________
PE License Number: _________________ State: ______________

---

## Template 5: School Building Calculation

**Project Information:**
- Project Name: _____________________________________________________
- Address: __________________________________________________________
- School District: ___________________________________________________
- Calculated By: ________________________ Date: ___________________
- Reviewed By (PE): _____________________ License #: ______________

**Building Data:**
- Total Square Footage: ____________ sq ft
- Grade Levels: [ ] Elementary  [ ] Middle  [ ] High  [ ] Other: __________
- Student Capacity: ____________ students
- Service Voltage/Phase: [ ] 120/208V, 3Ø  [ ] 277/480V, 3Ø

---

### Step 1: General Lighting Load by Space Type
**NEC Reference:** 220.12, Table 220.12

| Space Type | Area (sq ft) | Unit Load (VA/sq ft) | Load (VA) |
|------------|--------------|----------------------|-----------|
| Classrooms | __________ | 3.0 VA/sq ft | __________ VA |
| Gymnasium | __________ | 3.0 VA/sq ft | __________ VA |
| Auditorium | __________ | 1.0 VA/sq ft | __________ VA |
| Cafeteria | __________ | 2.0 VA/sq ft | __________ VA |
| Library | __________ | 3.0 VA/sq ft | __________ VA |
| Shop/Lab | __________ | 3.0 VA/sq ft | __________ VA |
| Offices | __________ | 3.5 VA/sq ft | __________ VA |
| Corridors | __________ | 0.5 VA/sq ft | __________ VA |
| Storage | __________ | 0.25 VA/sq ft | __________ VA |
| Other: _________ | __________ | _____ VA/sq ft | __________ VA |
| | | | |
| **Total General Lighting Load** | | | **__________ VA** |

---

### Step 2: Receptacle Load
**NEC Reference:** 220.14(I), 220.44

| Space Type | Number of Receptacles | Calculation | Load (VA) |
|------------|----------------------|-------------|-----------|
| Classrooms | __________ | × 180 VA | __________ VA |
| Offices | __________ | × 180 VA | __________ VA |
| Library | __________ | × 180 VA | __________ VA |
| Other spaces | __________ | × 180 VA | __________ VA |
| | | | |
| **Receptacle Load Subtotal** | | | **__________ VA** |

**Demand Factor per NEC 220.44:**
| First 10 kVA @ 100% | | __________ VA |
| Remainder @ 50% | × 50% | + __________ VA |
| **Receptacle Demand Load** | | **__________ VA** |

---

### Step 3: HVAC Load
**NEC Reference:** 220.50, 220.60

| Equipment | Location | MCA | Load (VA) |
|-----------|----------|-----|-----------|
| Rooftop unit - Classroom wing | Wing A | ___ A @ ___ V, 3Ø | __________ VA |
| Rooftop unit - Classroom wing | Wing B | ___ A @ ___ V, 3Ø | __________ VA |
| AHU - Gymnasium | Gym | ___ A @ ___ V, 3Ø | __________ VA |
| AHU - Cafeteria | Cafeteria | ___ A @ ___ V, 3Ø | __________ VA |
| Exhaust fans | Various | ___ A @ ___ V | __________ VA |
| Boiler | Mech room | ___ A @ ___ V, 3Ø | __________ VA |
| Chiller (if applicable) | Mech room | ___ A @ ___ V, 3Ø | __________ VA |
| Cooling tower (if applicable) | Roof | ___ A @ ___ V, 3Ø | __________ VA |
| | | | |
| **Total HVAC Load (100%)** | | | **__________ VA** |

---

### Step 4: Kitchen Equipment
**NEC Reference:** 220.56

| Equipment | Nameplate Rating | Demand Load (VA) |
|-----------|------------------|------------------|
| Range(s) | __________ kW | __________ VA |
| Convection oven(s) | __________ kW | __________ VA |
| Steamer | __________ kW | __________ VA |
| Fryer | __________ kW | __________ VA |
| Dishwasher (booster heater) | __________ kW | __________ VA |
| Walk-in cooler/freezer | __________ kW | __________ VA |
| Other kitchen: _____________ | __________ kW | __________ VA |
| | | |
| **Total Kitchen Load** | | **__________ VA** |

**Note:** Apply Table 220.56 demand factors if 6 or more pieces of commercial cooking equipment

---

### Step 5: Shop and Lab Equipment
**NEC Reference:** 220.14

| Equipment | Location | Load (VA) |
|-----------|----------|-----------|
| Woodworking tools (table saw, etc.) | Shop | __________ VA |
| Welders | Shop | __________ VA |
| Science lab equipment | Lab | __________ VA |
| Computer lab equipment | Computer lab | __________ VA |
| Other shop/lab: ______________ | __________ | __________ VA |
| | | |
| **Total Shop/Lab Equipment** | | **__________ VA** |

---

### Step 6: Gymnasium and Auditorium Loads

| Load Type | Calculation | Load (VA) |
|-----------|-------------|-----------|
| Gymnasium lighting (high bay) | __________ fixtures × _____ W | __________ VA |
| Gym scoreboard | __________ VA | __________ VA |
| Auditorium stage lighting | __________ VA | __________ VA |
| Sound system | __________ VA | __________ VA |
| Projection equipment | __________ VA | __________ VA |
| | | |
| **Total Gym/Auditorium Load** | | **__________ VA** |

---

### Step 7: Special School Loads

| Load Type | Calculation | Load (VA) |
|-----------|-------------|-----------|
| Elevator(s) | __________ A @ _____ V | __________ VA |
| Emergency generator house loads | __________ VA | __________ VA |
| Security system | __________ VA | __________ VA |
| Intercom/PA system | __________ VA | __________ VA |
| Clock system | __________ VA | __________ VA |
| Fire alarm system | __________ VA | __________ VA |
| Data network equipment | __________ VA | __________ VA |
| Exterior lighting/sports field | __________ VA | __________ VA |
| | | |
| **Total Special Loads** | | **__________ VA** |

---

### Step 8: Total School Building Load Summary

| Load Item | Load (VA) | Amperes @ 208V, 3Ø |
|-----------|-----------|---------------------|
| General lighting (Step 1) | __________ VA | __________ A |
| Receptacles (demand) (Step 2) | __________ VA | __________ A |
| HVAC (Step 3) | __________ VA | __________ A |
| Kitchen equipment (Step 4) | __________ VA | __________ A |
| Shop/lab equipment (Step 5) | __________ VA | __________ A |
| Gym/auditorium (Step 6) | __________ VA | __________ A |
| Special loads (Step 7) | __________ VA | __________ A |
| **Total Calculated Load** | **__________ VA** | **__________ A** |

**Formula for 3-phase:** Amperes = VA ÷ (208V × √3) = VA ÷ 360

---

### Step 9: Service Size Determination

| Standard Service Sizes (NEC 240.6) | Selected |
|------------------------------------|----------|
| 800 amperes | [ ] |
| 1000 amperes | [ ] |
| 1200 amperes | [ ] |
| 1600 amperes | [ ] |
| 2000 amperes | [ ] |

**Recommended Service Size:** __________ amperes

**Future Expansion Allowance:** __________ % (typically 25% for schools)
**Service with Future Expansion:** __________ amperes

---

### Step 10: Service Conductor Sizing
**NEC Reference:** Table 310.15(B)(16), 75°C column

**Selected Conductor:** __________ AWG/kcmil per phase [ ] Copper [ ] Aluminum
**Number of conductors per phase:** __________ (if parallel)
**Neutral Conductor:** __________ AWG/kcmil
**Grounding Electrode Conductor:** __________ AWG

---

### Calculation Certification

I certify that this school building load calculation has been prepared in accordance with NEC Article 220 and represents the anticipated electrical load for this facility.

**Calculated By:**
Signature: _________________________ Date: _________________
Printed Name: ______________________

**Professional Engineer Review:**
Signature: _________________________ Date: _________________
Printed Name: ______________________
PE License Number: _________________ State: ______________

---

## Excel Implementation Notes

These templates can be implemented in Excel with the following structure:

**Sheet 1: Input Data**
- All yellow-highlighted fields for user input
- Drop-down lists for voltage, phase, conductor material
- Data validation to prevent errors

**Sheet 2: Calculations**
- Formulas reference Input Data sheet
- Auto-calculation of demand factors per NEC tables
- Automatic ampere calculation from VA
- Color-coded cells (green = pass, red = exceed capacity)

**Sheet 3: NEC Tables**
- Embedded NEC tables (Table 220.12, 220.42, 220.55, 220.82, 220.84, etc.)
- VLOOKUP functions to pull demand factors automatically

**Sheet 4: Service Sizing**
- Standard service sizes with recommendations
- Conductor sizing tables with ampacity ratings
- Automatic conductor selection based on calculated load

**Sheet 5: Report Output**
- Professional formatted calculation report
- Ready for PE seal and signature
- Print-ready layout

---

## Python Implementation Notes

Python implementation using pandas for calculations:

```python
import pandas as pd
import numpy as np

class NECLoadCalculator:
    def __init__(self, occupancy_type):
        self.occupancy_type = occupancy_type
        self.loads = {}

    def calculate_general_lighting(self, sq_ft):
        unit_load = self.get_unit_load(self.occupancy_type)
        return sq_ft * unit_load

    def apply_demand_factor(self, load_va):
        # Implement Table 220.42 demand factors
        if load_va <= 3000:
            return load_va * 1.0
        elif load_va <= 120000:
            return 3000 + (load_va - 3000) * 0.35
        else:
            return 3000 + 117000 * 0.35 + (load_va - 120000) * 0.25

    def calculate_service_size(self):
        total_va = sum(self.loads.values())
        amperes = total_va / 240  # For single phase
        return self.next_standard_size(amperes)

    @staticmethod
    def next_standard_size(amperes):
        standard_sizes = [100, 125, 150, 200, 400, 600, 800, 1000, 1200, 1600, 2000]
        for size in standard_sizes:
            if amperes <= size:
                return size
        return standard_sizes[-1]
```

---

**Document Version:** 1.0
**Last Updated:** 2025-01-22
**Next Review:** 2026-01-22
**Owner:** Electrical Engineering Standards Committee
