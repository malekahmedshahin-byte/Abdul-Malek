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
            ne = get_float("Ne: ")
            print(ne_to_tex(ne))

        elif c == "2":
            tex = get_float("Tex: ")
            print(tex_to_ne(tex))

        elif c == "3":
            tex = get_float("Tex: ")
            print(tex_to_denier(tex))

        elif c == "4":
            sd = get_float("SD: ")
            mean = get_float("Mean: ")
            print(cv_percentage(sd, mean))

        elif c == "5":
            cval = get_float("Count: ")
            strength = get_float("Strength: ")
            print(csp(cval, strength))

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
            w = get_float("Weight: ")
            l = get_float("Length: ")
            b = get_float("Width: ")
            print(gsm(w, l, b))

        elif c == "2":
            g = get_float("GSM: ")
            w = get_float("Width: ")
            l = get_float("Length: ")
            print(fabric_weight(g, w, l))

        elif c == "3":
            epi = get_float("EPI: ")
            ppi = get_float("PPI: ")
            cval = get_float("Count: ")
            print(cover_factor(epi, ppi, cval))

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
            w = get_float("Weight: ")
            s = get_float("Shade %: ")
            print(dye_required(w, s))

        elif c == "2":
            w = get_float("Weight: ")
            r = get_float("Ratio: ")
            print(liquor_required(w, r))

        elif c == "3":
            w = get_float("Weight: ")
            p = get_float("Percent: ")
            print(chemical_required(w, p))

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
            w = get_float("Weight: ")
            r = get_float("Rate: ")
            print(yarn_cost(w, r))

        elif c == "2":
            m = get_float("Material: ")
            l = get_float("Labor: ")
            o = get_float("Overhead: ")
            print(process_cost(m, l, o))

        elif c == "3":
            cst = get_float("Cost: ")
            p = get_float("Profit %: ")
            print(profit_price(cst, p))

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
            a = get_float("Actual: ")
            t = get_float("Target: ")
            print(efficiency(a, t))

        elif c == "2":
            o = get_float("Output: ")
            h = get_float("Hours: ")
            print(production_rate(o, h))

        elif c == "3":
            r = get_float("Run time: ")
            a = get_float("Available: ")
            print(machine_utilization(r, a))

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
            i = get_float("Input: ")
            o = get_float("Output: ")
            print(wastage_percentage(i, o))

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
            print(kg_to_lbs(get_float("Kg: ")))

        elif c == "2":
            print(lbs_to_kg(get_float("Lb: ")))

        elif c == "3":
            print(inch_to_meter(get_float("Inch: ")))

        elif c == "4":
            print(meter_to_inch(get_float("Meter: ")))

        elif c == "5":
            print(gsm_to_oz_yd2(get_float("GSM: ")))

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
            o = get_float("Original: ")
            d = get_float("Dry: ")
            print(moisture_regain(o, d))

        elif c == "2":
            o = get_float("Original: ")
            f = get_float("Final: ")
            print(shrinkage_percent(o, f))

        elif c == "3":
            w = get_float("Water: ")
            d = get_float("Dry: ")
            print(absorbency_rate(w, d))

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
            twist = get_float("Twist: ")
            length = get_float("Length: ")
            print(f"TPI = {yarn_twist_tpi(twist, length):.2f}")

        elif choice == "2":
            tpi = get_float("TPI: ")
            print(f"TPM = {yarn_tpm(tpi):.2f}")

        elif choice == "3":
            u = get_float("U%: ")
            thin = get_float("Thin places: ")
            thick = get_float("Thick places: ")
            neps = get_float("Neps: ")
            print(f"Imperfection Index = {yarn_imperfection(u, thin, thick, neps):.2f}")

        elif choice == "4":
            actual = get_float("Actual Output: ")
            theoretical = get_float("Theoretical Output: ")
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
            actual = get_float("Actual Output: ")
            ideal = get_float("Ideal Output: ")
            print(f"Efficiency = {loom_efficiency(actual, ideal):.2f}%")

        elif c == "2":
            breaks = get_float("Warp breaks: ")
            ends = get_float("Total ends: ")
            print(f"Warp Break Rate = {warp_break_rate(breaks, ends):.2f}%")

        elif c == "3":
            breaks = get_float("Weft breaks: ")
            picks = get_float("Picks: ")
            print(f"Weft Break Rate = {weft_break_rate(breaks, picks):.2f}%")

        elif c == "4":
            defects = get_float("Defects: ")
            length = get_float("Length: ")
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
            initial = get_float("Initial dye: ")
            remaining = get_float("Remaining dye: ")
            print(f"Exhaustion = {dye_exhaustion(initial, remaining):.2f}%")

        elif c == "2":
            fixed = get_float("Fixed dye: ")
            applied = get_float("Applied dye: ")
            print(f"Fixation = {dye_fixation(fixed, applied):.2f}%")

        elif c == "3":
            m = get_float("Material: ")
            l = get_float("Liquor: ")
            print(f"Liquor Ratio = {liquor_ratio(m, l):.2f}")

        elif c == "4":
            a = get_float("Actual: ")
            t = get_float("Theoretical: ")
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
            f = get_float("Force: ")
            a = get_float("Area: ")
            print(f"Tensile Strength = {tensile_strength(f, a):.2f}")

        elif c == "2":
            f = get_float("Final length: ")
            o = get_float("Original length: ")
            print(f"Elongation = {elongation_percent(f, o):.2f}%")

        elif c == "3":
            f = get_float("Force: ")
            a = get_float("Area: ")
            print(f"Bursting Strength = {bursting_strength(f, a):.2f}")

        elif c == "4":
            loss = get_float("Loss weight: ")
            init = get_float("Initial weight: ")
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
            cost = get_float("Total cost: ")
            length = get_float("Length: ")
            print(f"Cost per Meter = {cost_per_meter(cost, length):.2f}")

        elif c == "2":
            power = get_float("Power (kW): ")
            hours = get_float("Hours: ")
            rate = get_float("Rate: ")
            print(f"Energy Cost = {energy_cost(power, hours, rate):.2f}")

        elif c == "3":
            mc = get_float("Machine cost: ")
            life = get_float("Life (years): ")
            print(f"Depreciation = {depreciation(mc, life):.2f}")

        elif c == "4":
            sp = get_float("Selling price: ")
            cp = get_float("Cost price: ")
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