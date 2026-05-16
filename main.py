import sys
sys.path.append(".")

from textilecalc import *


# ================================
# FULL FORM DICTIONARY
# ================================
TEXTILE_DICT = {
    "Ne": "English Cotton Count (840 yards per pound)",
    "Tex": "Linear density (g/1000m)",
    "Denier": "Linear density (g/9000m)",
    "CV%": "Coefficient of Variation (uneven yarn quality)",
    "CSP": "Count Strength Product",
    "GSM": "Gram per Square Meter",
    "EPI": "Ends Per Inch",
    "PPI": "Picks Per Inch",
    "TPI": "Twist Per Inch",
    "TPM": "Twist Per Meter"
}


def show_term(term):
    if term in TEXTILE_DICT:
        print(f"\n📘 {term} → {TEXTILE_DICT[term]}")


# ================================
# SAFE INPUT
# ================================
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid input. Enter number.")


# ================================
# HEADER
# ================================
def header(title):
    print("\n" + "=" * 75)
    print(f"        TEXTILE CALC TOOLKIT | {title}")
    print("=" * 75)


# ================================
# YARN MENU
# ================================
def yarn_menu():
    while True:
        header("YARN CALCULATIONS")

        print("""
1. Ne → Tex
2. Tex → Ne
3. Tex → Denier
4. CV%
5. CSP
6. Back
""")

        c = input("Choice: ")

        if c == "1":
            ne = get_float("Enter Count (Ne): ")
            print(f"Result = {ne_to_tex(ne)} Tex")

        elif c == "2":
            tex = get_float("Enter Count (Tex): ")
            print(f"Result = {tex_to_ne(tex)} Ne")

        elif c == "3":
            tex = get_float("Enter Count (Tex): ")
            print(f"Result = {tex_to_denier(tex)} Denier")

        elif c == "4":
            sd = get_float("Enter Standard Deviation (SD): ")
            mean = get_float("Enter Mean Value: ")
            print(f"Result = {cv_percentage(sd, mean)} %")

        elif c == "5":
            cval = get_float("Enter Yarn Count (Ne): ")
            strength = get_float("Enter Lea Strength (lbs): ")
            print(f"Result = {csp(cval, strength)} CSP")

        elif c == "6":
            break


# ================================
# FABRIC MENU
# ================================
def fabric_menu():
    while True:
        header("FABRIC CALCULATIONS")

        print("""
1. GSM
2. Fabric Weight
3. Cover Factor
4. Back
""")

        c = input("Choice: ")

        if c == "1":
            w = get_float("Enter Sample Weight (g): ")
            l = get_float("Enter Sample Length (cm): ")
            b = get_float("Enter Sample Width (cm): ")
            print(f"Result = {gsm(w, l, b)} GSM (g/m²)")

        elif c == "2":
            g = get_float("Enter Fabric GSM (g/m²): ")
            w = get_float("Enter Fabric Width (meters): ")
            l = get_float("Enter Fabric Length (meters): ")
            print(f"Result = {fabric_weight(g, w, l)} grams")

        elif c == "3":
            epi = get_float("Enter EPI: ")
            ppi = get_float("Enter PPI: ")
            cval = get_float("Enter Yarn Count (Ne): ")
            print(f"Result = {cover_factor(epi, ppi, cval)} (Total Cover Factor)")

        elif c == "4":
            break


# ================================
# DYEING MENU
# ================================
def dyeing_menu():
    while True:
        header("DYEING CALCULATIONS")

        print("""
1. Dye Required
2. Liquor Required
3. Chemical Required
4. Back
""")

        c = input("Choice: ")

        if c == "1":
            w = get_float("Enter Fabric/Yarn Weight (g): ")
            s = get_float("Enter Shade (%): ")
            print(f"Result = {dye_required(w, s)} grams")

        elif c == "2":
            w = get_float("Enter Fabric/Yarn Weight (kg): ")
            r = get_float("Enter Material liquor Ratio (1:X, enter X): ")
            print(f"Result = {liquor_required(w, r)} Liters")

        elif c == "3":
            w = get_float("Enter Fabric/Yarn Weight (g): ")
            p = get_float("Enter Chemical Percentage (%): ")
            print(f"Result = {chemical_required(w, p)} grams")

        elif c == "4":
            break


# ================================
# COSTING MENU
# ================================
def costing_menu():
    while True:
        header("COSTING CALCULATIONS")

        print("""
1. Yarn Cost
2. Process Cost
3. Selling Price
4. Back
""")

        c = input("Choice: ")

        if c == "1":
            w = get_float("Enter Yarn Weight (kg/lb): ")
            r = get_float("Enter Rate per Unit Weight: ")
            print(f"Result = {yarn_cost(w, r)} (Total Yarn Cost)")

        elif c == "2":
            m = get_float("Enter Material Cost: ")
            l = get_float("Enter Labor Cost: ")
            o = get_float("Enter Overhead Cost: ")
            print(f"Result = {process_cost(m, l, o)} (Total Process Cost)")

        elif c == "3":
            cst = get_float("Enter Total Cost Price: ")
            p = get_float("Enter Desired Profit (%): ")
            print(f"Result = {profit_price(cst, p)} (Selling Price)")

        elif c == "4":
            break


# ================================
# PRODUCTION MENU
# ================================
def production_menu():
    while True:
        header("PRODUCTION")

        print("""
1. Efficiency
2. Rate
3. Utilization
4. Back
""")

        c = input("Choice: ")

        if c == "1":
            a = get_float("Enter Actual Production: ")
            t = get_float("Enter Target Production: ")
            print(f"Result = {efficiency(a, t)} %")

        elif c == "2":
            o = get_float("Enter Total Output (kg/meter): ")
            h = get_float("Enter Total Hours: ")
            print(f"Result = {production_rate(o, h)} per hour")

        elif c == "3":
            r = get_float("Enter Machine Run Time (hours): ")
            a = get_float("Enter Total Available Time (hours): ")
            print(f"Result = {machine_utilization(r, a)} %")

        elif c == "4":
            break


# ================================
# WASTAGE MENU
# ================================
def wastage_menu():
    while True:
        header("WASTAGE")

        print("""
1. Wastage %
2. Back
""")

        c = input("Choice: ")

        if c == "1":
            i = get_float("Enter Input Material Weight: ")
            o = get_float("Enter Output Material Weight: ")
            print(f"Result = {wastage_percentage(i, o)} %")

        elif c == "2":
            break


# ================================
# UNIT MENU
# ================================
def unit_menu():
    while True:
        header("UNIT CONVERSION")

        print("""
1. Kg → Lb
2. Lb → Kg
3. Inch → Meter
4. Meter → Inch
5. GSM → Oz/yd²
6. Back
""")

        c = input("Choice: ")

        if c == "1":
            print(f"Result = {kg_to_lbs(get_float('Enter Weight in Kg: '))} Lbs")

        elif c == "2":
            print(f"Result = {lbs_to_kg(get_float('Enter Weight in Lb: '))} Kg")

        elif c == "3":
            print(f"Result = {inch_to_meter(get_float('Enter Length in Inch: '))} Meters")

        elif c == "4":
            print(f"Result = {meter_to_inch(get_float('Enter Length in Meter: '))} Inches")

        elif c == "5":
            print(f"Result = {gsm_to_oz_yd2(get_float('Enter Fabric GSM: '))} Oz/yd²")

        elif c == "6":
            break


# ================================
# QC MENU
# ================================
def qc_menu():
    while True:
        header("QUALITY CONTROL")

        print("""
1. Moisture Regain
2. Shrinkage
3. Absorbency
4. Back
""")

        c = input("Choice: ")

        if c == "1":
            o = get_float("Enter Original Weight (g): ")
            d = get_float("Enter Oven-Dry Weight (g): ")
            print(f"Result = {moisture_regain(o, d)} %")

        elif c == "2":
            o = get_float("Enter Original Length/Width (cm): ")
            f = get_float("Enter Final Length/Width after Wash (cm): ")
            print(f"Result = {shrinkage_percent(o, f)} %")

        elif c == "3":
            w = get_float("Enter Absorbed Water Weight (g): ")
            d = get_float("Enter Dry Fabric Weight (g): ")
            print(f"Result = {absorbency_rate(w, d)} %")

        elif c == "4":
            break


# ================================
# NEW INDUSTRY MODULES
# ================================

# ===== Spinning =====
def spinning_menu():
    while True:
        header("SPINNING CALCULATIONS")

        print("""
1. Yarn Twist (TPI)
2. Yarn Twist (TPM)
3. Imperfection Index
4. Spinning Efficiency
5. Back
""")

        choice = input("Enter choice: ")

        if choice == "1":
            twist = get_float("Enter Total Number of Twists: ")
            length = get_float("Enter Sample Length (inches): ")
            print(f"TPI = {yarn_twist_tpi(twist, length):.2f} Twist Per Inch")

        elif choice == "2":
            tpi = get_float("Enter TPI (Twist Per Inch): ")
            print(f"TPM = {yarn_tpm(tpi):.2f} Twist Per Meter")

        elif choice == "3":
            u = get_float("Enter U% (Evenness): ")
            thin = get_float("Enter Thin places per km: ")
            thick = get_float("Enter Thick places per km: ")
            neps = get_float("Enter Neps per km: ")
            print(f"Imperfection Index = {yarn_imperfection(u, thin, thick, neps):.2f} (IPI)")

        elif choice == "4":
            actual = get_float("Enter Actual Production Output: ")
            theoretical = get_float("Enter Theoretical Production Output: ")
            print(f"Efficiency = {spinning_efficiency(actual, theoretical):.2f}%")

        elif choice == "5":
            break


# ===== Weaving =====
def weaving_menu():
    while True:
        header("WEAVING CALCULATIONS")

        print("""
1. Loom Efficiency
2. Warp Break Rate
3. Weft Break Rate
4. Fabric Defect Rate
5. Back
""")

        c = input("Enter choice: ")

        if c == "1":
            actual = get_float("Enter Actual Pick/Output: ")
            ideal = get_float("Enter Ideal Pick/Output: ")
            print(f"Efficiency = {loom_efficiency(actual, ideal):.2f}%")

        elif c == "2":
            breaks = get_float("Enter Total Warp Breaks: ")
            ends = get_float("Enter Total Warp Ends: ")
            print(f"Warp Break Rate = {warp_break_rate(breaks, ends):.2f}%")

        elif c == "3":
            breaks = get_float("Enter Total Weft Breaks: ")
            picks = get_float("Enter Total Picks: ")
            print(f"Weft Break Rate = {weft_break_rate(breaks, picks):.2f}%")

        elif c == "4":
            defects = get_float("Enter Total Defects Found: ")
            length = get_float("Enter Total Inspected Length (meters/yards): ")
            print(f"Defect Rate = {fabric_defect_rate(defects, length):.2f}%")

        elif c == "5":
            break


# ===== Advance Dyeing =====

def dyeing_advanced_menu():
    while True:
        header("ADVANCED DYEING")

        print("""
1. Dye Exhaustion
2. Dye Fixation
3. Liquor Ratio
4. Chemical Utilization
5. Back
""")

        c = input("Enter choice: ")

        if c == "1":
            initial = get_float("Enter Initial Dye Concentration: ")
            remaining = get_float("Enter Remaining Dye in Dyebath: ")
            print(f"Exhaustion = {dye_exhaustion(initial, remaining):.2f}%")

        elif c == "2":
            fixed = get_float("Enter Amount of Fixed Dye on Fabric: ")
            applied = get_float("Enter Total Applied Dye: ")
            print(f"Fixation = {dye_fixation(fixed, applied):.2f}%")

        elif c == "3":
            m = get_float("Enter Material Weight (g/kg): ")
            l = get_float("Enter Total Liquor Volume (ml/L): ")
            print(f"Liquor Ratio = 1 : {liquor_ratio(m, l):.2f}")

        elif c == "4":
            a = get_float("Enter Actual Chemical Used: ")
            t = get_float("Enter Theoretical Chemical Required: ")
            print(f"Utilization = {chemical_utilization(a, t):.2f}%")

        elif c == "5":
            break


# ===== Testing =====
def testing_menu():
    while True:
        header("TEXTILE TESTING LAB")

        print("""
1. Tensile Strength
2. Elongation %
3. Bursting Strength
4. Abrasion Index
5. Back
""")

        c = input("Enter choice: ")

        if c == "1":
            f = get_float("Enter Breaking Force (N/kg/lbs): ")
            a = get_float("Enter Cross-sectional Area (mm²/cm²): ")
            print(f"Tensile Strength = {tensile_strength(f, a):.2f} (Force per Unit Area)")

        elif c == "2":
            f = get_float("Enter Extended/Final Length (mm/cm): ")
            o = get_float("Enter Original Gauge Length (mm/cm): ")
            print(f"Elongation = {elongation_percent(f, o):.2f}%")

        elif c == "3":
            f = get_float("Enter Pressure/Force (kPa/psi): ")
            a = get_float("Enter Test Area: ")
            print(f"Bursting Strength = {bursting_strength(f, a):.2f}")

        elif c == "4":
            loss = get_float("Enter Weight Loss after Test (g): ")
            init = get_float("Enter Initial Weight before Test (g): ")
            print(f"Abrasion Index = {abrasion_index(loss, init):.2f}%")

        elif c == "5":
            break


# ===== Costing =====
def costing_advanced_menu():
    while True:
        header("ADVANCED COSTING")

        print("""
1. Cost per Meter
2. Energy Cost
3. Machine Depreciation
4. Profit Margin
5. Back
""")

        c = input("Enter choice: ")

        if c == "1":
            cost = get_float("Enter Total Production Cost: ")
            length = get_float("Enter Total Produced Length (meters): ")
            print(f"Cost per Meter = {cost_per_meter(cost, length):.2f} per meter")

        elif c == "2":
            power = get_float("Enter Power Consumption (kW): ")
            hours = get_float("Enter Total Running Hours: ")
            rate = get_float("Enter Electricity Rate per kWh: ")
            print(f"Energy Cost = {energy_cost(power, hours, rate):.2f} (Total Energy Cost)")

        elif c == "3":
            mc = get_float("Enter Total Machine Purchase Cost: ")
            life = get_float("Enter Estimated Machine Life (years): ")
            print(f"Depreciation = {depreciation(mc, life):.2f} per year")

        elif c == "4":
            sp = get_float("Enter Total Selling Price: ")
            cp = get_float("Enter Total Cost Price: ")
            print(f"Profit Margin = {profit_margin(sp, cp):.2f}%")

        elif c == "5":
            break

# ================================
# MAIN MENU
# ================================
def main():
    while True:
        header("MAIN MENU")

        print("""
1. Yarn
2. Fabric
3. Dyeing
4. Costing
5. Production
6. Wastage
7. Unit
8. Quality Control
9. Spinning
10. Weaving
11. Advanced Dyeing
12. Testing Lab
13. Advanced Costing
14. Exit
""")

        c = input("Choice: ")

        if c == "1":
            yarn_menu()
        elif c == "2":
            fabric_menu()
        elif c == "3":
            dyeing_menu()
        elif c == "4":
            costing_menu()
        elif c == "5":
            production_menu()
        elif c == "6":
            wastage_menu()
        elif c == "7":
            unit_menu()
        elif c == "8":
            qc_menu()
        elif c == "9":
            spinning_menu()
        elif c == "10":
            weaving_menu()
        elif c == "11":
            dyeing_advanced_menu()
        elif c == "12":
            testing_menu()
        elif c == "13":
            costing_advanced_menu()
        elif c == "14":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
