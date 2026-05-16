import sys
sys.path.append(".")

from textilecalc import *


# ================================
# FULL FORM DICTIONARY
# ================================
TEXTILE_DICT = {
    "Ne": "English Cotton Count (Number of 840 yards per pound)",
    "Tex": "Linear density in grams per 1000 meters",
    "Denier": "Linear density in grams per 9000 meters",
    "CV%": "Coefficient of Variation (unevenness of yarn)",
    "CSP": "Count Strength Product (yarn strength indicator)",
    "GSM": "Gram per Square Meter (fabric weight)",
    "EPI": "Ends Per Inch (warp density)",
    "PPI": "Picks Per Inch (weft density)"
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
        except ValueError:
            print("❌ Invalid input. Please enter numeric value.\n")


# ================================
# HEADER
# ================================
def header(title):
    print("\n" + "=" * 70)
    print(f"        TEXTILE CALC TOOLKIT | {title}")
    print("=" * 70)


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

        c = input("Enter choice: ")

        if c == "1":
            show_term("Ne")
            show_term("Tex")
            ne = get_float("Enter Ne: ")
            print(f"Result: {ne} Ne = {ne_to_tex(ne):.2f} Tex")

        elif c == "2":
            show_term("Tex")
            show_term("Ne")
            tex = get_float("Enter Tex: ")
            print(f"Result: {tex} Tex = {tex_to_ne(tex):.2f} Ne")

        elif c == "3":
            show_term("Tex")
            show_term("Denier")
            tex = get_float("Enter Tex: ")
            print(f"Result: {tex} Tex = {tex_to_denier(tex):.2f} Denier")

        elif c == "4":
            show_term("CV%")
            sd = get_float("Standard Deviation: ")
            mean = get_float("Mean Value: ")
            if mean > 0:
                print(f"CV% = {cv_percentage(sd, mean):.2f}%")

        elif c == "5":
            show_term("CSP")
            count = get_float("Yarn Count: ")
            strength = get_float("Strength (lb): ")
            print(f"CSP = {csp(count, strength):.2f}")

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

        c = input("Enter choice: ")

        if c == "1":
            show_term("GSM")
            w = get_float("Weight (grams): ")
            l = get_float("Length (meters): ")
            b = get_float("Width (meters): ")
            print(f"GSM = {gsm(w, l, b):.2f}")

        elif c == "2":
            gsm_value = get_float("GSM: ")
            w = get_float("Width: ")
            l = get_float("Length: ")
            print(f"Fabric Weight = {fabric_weight(gsm_value, w, l):.2f} grams")

        elif c == "3":
            show_term("EPI")
            show_term("PPI")
            epi = get_float("EPI: ")
            ppi = get_float("PPI: ")
            count = get_float("Yarn Count: ")
            print(f"Cover Factor = {cover_factor(epi, ppi, count):.2f}")

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

        c = input("Enter choice: ")

        if c == "1":
            w = get_float("Fabric Weight (kg): ")
            s = get_float("Shade %: ")
            print(f"Dye Required = {dye_required(w, s):.2f} kg")

        elif c == "2":
            w = get_float("Material Weight (kg): ")
            r = get_float("Liquor Ratio: ")
            print(f"Liquor Required = {liquor_required(w, r):.2f} L")

        elif c == "3":
            w = get_float("Material Weight (kg): ")
            p = get_float("Chemical %: ")
            print(f"Chemical Required = {chemical_required(w, p):.2f} kg")

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

        c = input("Enter choice: ")

        if c == "1":
            w = get_float("Yarn Weight: ")
            r = get_float("Rate per kg: ")
            print(f"Yarn Cost = {yarn_cost(w, r):.2f}")

        elif c == "2":
            m = get_float("Material Cost: ")
            l = get_float("Labor Cost: ")
            o = get_float("Overhead Cost: ")
            print(f"Process Cost = {process_cost(m, l, o):.2f}")

        elif c == "3":
            cst = get_float("Total Cost: ")
            p = get_float("Profit %: ")
            print(f"Selling Price = {profit_price(cst, p):.2f}")

        elif c == "4":
            break


# ================================
# PRODUCTION MENU
# ================================
def production_menu():
    while True:
        header("PRODUCTION CALCULATIONS")

        print("""
1. Efficiency
2. Production Rate
3. Machine Utilization
4. Back
""")

        c = input("Enter choice: ")

        if c == "1":
            a = get_float("Actual Production: ")
            t = get_float("Target Production: ")
            print(f"Efficiency = {efficiency(a, t):.2f}%")

        elif c == "2":
            o = get_float("Output: ")
            h = get_float("Hours: ")
            print(f"Production Rate = {production_rate(o, h):.2f}/hr")

        elif c == "3":
            r = get_float("Run Time: ")
            a = get_float("Available Time: ")
            print(f"Utilization = {machine_utilization(r, a):.2f}%")

        elif c == "4":
            break


# ================================
# WASTAGE MENU
# ================================
def wastage_menu():
    while True:
        header("WASTAGE CALCULATIONS")

        print("""
1. Wastage %
2. Back
""")

        c = input("Enter choice: ")

        if c == "1":
            i = get_float("Input Weight: ")
            o = get_float("Output Weight: ")
            print(f"Wastage = {wastage_percentage(i, o):.2f}%")

        elif c == "2":
            break


# ================================
# UNIT CONVERSION MENU
# ================================
def unit_menu():
    while True:
        header("UNIT CONVERSIONS")

        print("""
1. Kg → Lb
2. Lb → Kg
3. Inch → Meter
4. Meter → Inch
5. GSM → Oz/yd²
6. Back
""")

        c = input("Enter choice: ")

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
# QUALITY CONTROL MENU
# ================================
def qc_menu():
    while True:
        header("QUALITY CONTROL")

        print("""
1. Moisture Regain
2. Shrinkage %
3. Absorbency Rate
4. Back
""")

        c = input("Enter choice: ")

        if c == "1":
            o = get_float("Original Weight: ")
            d = get_float("Dry Weight: ")
            print(f"Moisture Regain = {moisture_regain(o, d):.2f}%")

        elif c == "2":
            o = get_float("Original Dimension: ")
            f = get_float("Final Dimension: ")
            print(f"Shrinkage = {shrinkage_percent(o, f):.2f}%")

        elif c == "3":
            w = get_float("Water Absorbed: ")
            d = get_float("Dry Weight: ")
            print(f"Absorbency Rate = {absorbency_rate(w, d):.2f}%")

        elif c == "4":
            break


# ================================
# MAIN MENU
# ================================
def main():
    while True:
        header("MAIN MENU")

        print("""
1. Yarn Calculations
2. Fabric Calculations
3. Dyeing Calculations
4. Costing Calculations
5. Production Calculations
6. Wastage Calculations
7. Unit Conversions
8. Quality Control
9. Exit
""")

        c = input("Enter choice: ")

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
            print("\nExiting Toolkit...")
            break


if __name__ == "__main__":
    main()