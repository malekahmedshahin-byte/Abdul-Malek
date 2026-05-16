import sys
sys.path.append(".")

from textilecalc import *
from colorama import Fore, Style, init

init(autoreset=True)


# ================================
# FULL FORMS
# ================================
TEXTILE_FULL_FORM = {
    "Ne": "English Cotton Count",
    "Tex": "Tex (g per 1000m)",
    "Denier": "Denier (g per 9000m)",
    "CV%": "Coefficient of Variation",
    "CSP": "Count Strength Product",
    "GSM": "Gram per Square Meter",
    "EPI": "Ends Per Inch",
    "PPI": "Picks Per Inch"
}


# ================================
# INPUT HANDLER
# ================================
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "❌ Invalid input!")


# ================================
# HEADER
# ================================
def header(title):
    print(Fore.CYAN + "\n" + "=" * 70)
    print(Fore.YELLOW + Style.BRIGHT + f"🧵 TEXTILE CALC TOOLKIT | {title}")
    print(Fore.CYAN + "=" * 70)


# ================================
# FULL FORM DISPLAY
# ================================
def show(term):
    if term in TEXTILE_FULL_FORM:
        print(Fore.MAGENTA + f"📘 {term} → {TEXTILE_FULL_FORM[term]}")


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

        c = input("👉 ")

        if c == "1":
            show("Ne"); show("Tex")
            ne = get_float("Ne: ")
            print(Fore.GREEN + f"✔ {ne} Ne → {ne_to_tex(ne):.2f} Tex")

        elif c == "2":
            show("Tex"); show("Ne")
            tex = get_float("Tex: ")
            print(Fore.GREEN + f"✔ {tex} Tex → {tex_to_ne(tex):.2f} Ne")

        elif c == "3":
            show("Tex"); show("Denier")
            tex = get_float("Tex: ")
            print(Fore.GREEN + f"✔ {tex} Tex → {tex_to_denier(tex):.2f} Denier")

        elif c == "4":
            show("CV%")
            sd = get_float("SD: ")
            mean = get_float("Mean: ")
            if mean > 0:
                print(Fore.GREEN + f"✔ CV% = {cv_percentage(sd, mean):.2f}%")

        elif c == "5":
            show("CSP")
            c1 = get_float("Count: ")
            s = get_float("Strength: ")
            print(Fore.GREEN + f"✔ CSP = {csp(c1, s):.2f}")

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

        c = input("👉 ")

        if c == "1":
            show("GSM")
            w = get_float("Weight: ")
            l = get_float("Length: ")
            b = get_float("Width: ")
            print(Fore.GREEN + f"✔ GSM = {gsm(w,l,b):.2f}")

        elif c == "2":
            g = get_float("GSM: ")
            w = get_float("Width: ")
            l = get_float("Length: ")
            print(Fore.GREEN + f"✔ Weight = {fabric_weight(g,w,l):.2f} g")

        elif c == "3":
            show("EPI"); show("PPI")
            epi = get_float("EPI: ")
            ppi = get_float("PPI: ")
            c1 = get_float("Count: ")
            print(Fore.GREEN + f"✔ Cover Factor = {cover_factor(epi,ppi,c1):.2f}")

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

        c = input("👉 ")

        if c == "1":
            w = get_float("Weight kg: ")
            s = get_float("Shade %: ")
            print(Fore.GREEN + f"✔ Dye = {dye_required(w,s):.2f} kg")

        elif c == "2":
            w = get_float("Weight kg: ")
            r = get_float("Ratio: ")
            print(Fore.GREEN + f"✔ Liquor = {liquor_required(w,r):.2f} L")

        elif c == "3":
            w = get_float("Weight kg: ")
            p = get_float("Chemical %: ")
            print(Fore.GREEN + f"✔ Chemical = {chemical_required(w,p):.2f} kg")

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

        c = input("👉 ")

        if c == "1":
            w = get_float("Weight: ")
            r = get_float("Rate: ")
            print(Fore.GREEN + f"✔ Cost = {yarn_cost(w,r):.2f}")

        elif c == "2":
            m = get_float("Material: ")
            l = get_float("Labor: ")
            o = get_float("Overhead: ")
            print(Fore.GREEN + f"✔ Total = {process_cost(m,l,o):.2f}")

        elif c == "3":
            c1 = get_float("Cost: ")
            p = get_float("Profit %: ")
            print(Fore.GREEN + f"✔ Price = {profit_price(c1,p):.2f}")

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
2. Production Rate
3. Machine Utilization
4. Back
""")

        c = input("👉 ")

        if c == "1":
            a = get_float("Actual: ")
            t = get_float("Target: ")
            print(Fore.GREEN + f"✔ Efficiency = {efficiency(a,t):.2f}%")

        elif c == "2":
            o = get_float("Output: ")
            h = get_float("Hours: ")
            print(Fore.GREEN + f"✔ Rate = {production_rate(o,h):.2f}/hr")

        elif c == "3":
            r = get_float("Run Time: ")
            a = get_float("Available: ")
            print(Fore.GREEN + f"✔ Utilization = {machine_utilization(r,a):.2f}%")


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

        c = input("👉 ")

        if c == "1":
            i = get_float("Input: ")
            o = get_float("Output: ")
            print(Fore.GREEN + f"✔ Wastage = {wastage_percentage(i,o):.2f}%")

        elif c == "2":
            break


# ================================
# UNIT CONVERSION MENU
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

        c = input("👉 ")

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

        c = input("👉 ")

        if c == "1":
            o = get_float("Original: ")
            d = get_float("Dry: ")
            print(Fore.GREEN + f"✔ Moisture = {moisture_regain(o,d):.2f}%")

        elif c == "2":
            o = get_float("Original: ")
            f = get_float("Final: ")
            print(Fore.GREEN + f"✔ Shrinkage = {shrinkage_percent(o,f):.2f}%")

        elif c == "3":
            w = get_float("Water: ")
            d = get_float("Dry: ")
            print(Fore.GREEN + f"✔ Absorbency = {absorbency_rate(w,d):.2f}%")

        elif c == "4":
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
7. Unit Conversion
8. Quality Control
9. Exit
""")

        c = input("👉 ")

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
            print(Fore.YELLOW + "👋 Exiting Toolkit...")
            break


if __name__ == "__main__":
    main()