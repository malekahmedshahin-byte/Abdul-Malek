import sys
sys.path.append(".")

from textilecalc import *


# ================================
# SAFE INPUT HANDLER
# ================================
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.\n")


# ================================
# HEADER DESIGN
# ================================
def header(title):
    print("\n" + "=" * 60)
    print(f"        🧵 TEXTILE CALC TOOLKIT | {title}")
    print("=" * 60)


# ================================
# YARN MENU
# ================================
def yarn_menu():
    while True:
        header("YARN CALCULATIONS")

        print("""
1. Convert Ne → Tex (English Cotton Count to Linear Density)
2. Convert Tex → Ne
3. Convert Tex → Denier
4. Calculate Coefficient of Variation (CV%)
5. Calculate Count Strength Product (CSP)
6. Back to Main Menu
""")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            ne = get_float("Enter English Cotton Count (Ne): ")
            tex = ne_to_tex(ne)
            print(f"\n📌 Result: {ne} Ne = {tex:.2f} Tex (g/1000m)")

        elif choice == "2":
            tex = get_float("Enter Yarn Linear Density (Tex): ")
            ne = tex_to_ne(tex)
            print(f"\n📌 Result: {tex} Tex = {ne:.2f} Ne")

        elif choice == "3":
            tex = get_float("Enter Yarn Linear Density (Tex): ")
            denier = tex_to_denier(tex)
            print(f"\n📌 Result: {tex} Tex = {denier:.2f} Denier (g/9000m)")

        elif choice == "4":
            sd = get_float("Enter Standard Deviation: ")
            mean = get_float("Enter Mean Value: ")
            if mean <= 0:
                print("❌ Mean value must be greater than 0")
            else:
                cv = cv_percentage(sd, mean)
                print(f"\n📌 Coefficient of Variation (CV%) = {cv:.2f}%")

        elif choice == "5":
            count = get_float("Enter Yarn Count: ")
            strength = get_float("Enter Yarn Strength (lb): ")
            csp_value = csp(count, strength)
            print(f"\n📌 Count Strength Product (CSP) = {csp_value:.2f}")

        elif choice == "6":
            break

        else:
            print("❌ Invalid choice. Try again.")


# ================================
# FABRIC MENU
# ================================
def fabric_menu():
    while True:
        header("FABRIC CALCULATIONS")

        print("""
1. Fabric GSM (Gram per Square Meter)
2. Total Fabric Weight
3. Fabric Cover Factor
4. Back
""")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            w = get_float("Fabric Weight (grams): ")
            l = get_float("Length (meters): ")
            b = get_float("Width (meters): ")

            gsm_value = gsm(w, l, b)
            print(f"\n📌 Fabric GSM = {gsm_value:.2f} g/m²")

        elif choice == "2":
            gsm_value = get_float("Fabric GSM (g/m²): ")
            w = get_float("Width (m): ")
            l = get_float("Length (m): ")

            weight = fabric_weight(gsm_value, w, l)
            print(f"\n📌 Total Fabric Weight = {weight:.2f} grams")

        elif choice == "3":
            epi = get_float("Ends per Inch (EPI): ")
            ppi = get_float("Picks per Inch (PPI): ")
            count = get_float("Yarn Count: ")

            cf = cover_factor(epi, ppi, count)
            print(f"\n📌 Fabric Cover Factor = {cf:.2f}")

        elif choice == "4":
            break

        else:
            print("❌ Invalid choice")


# ================================
# DYEING MENU
# ================================
def dyeing_menu():
    while True:
        header("DYEING CALCULATIONS")

        print("""
1. Required Dye Amount
2. Required Liquor Amount
3. Required Chemical Amount
4. Back
""")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            weight = get_float("Fabric Weight (kg): ")
            shade = get_float("Shade (%): ")

            dye = dye_required(weight, shade)
            print(f"\n📌 Required Dye = {dye:.2f} kg")

        elif choice == "2":
            weight = get_float("Material Weight (kg): ")
            ratio = get_float("Liquor Ratio (e.g. 10 for 1:10): ")

            liquor = liquor_required(weight, ratio)
            print(f"\n📌 Required Liquor = {liquor:.2f} L")

        elif choice == "3":
            weight = get_float("Material Weight (kg): ")
            percent = get_float("Chemical (%): ")

            chem = chemical_required(weight, percent)
            print(f"\n📌 Required Chemical = {chem:.2f} kg")

        elif choice == "4":
            break

        else:
            print("❌ Invalid choice")


# ================================
# COSTING MENU
# ================================
def costing_menu():
    while True:
        header("COSTING CALCULATIONS")

        print("""
1. Yarn Cost
2. Total Process Cost
3. Selling Price with Profit
4. Back
""")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            w = get_float("Yarn Weight (kg): ")
            rate = get_float("Rate per kg: ")

            cost = yarn_cost(w, rate)
            print(f"\n📌 Yarn Cost = {cost:.2f}")

        elif choice == "2":
            mat = get_float("Material Cost: ")
            labor = get_float("Labor Cost: ")
            overhead = get_float("Overhead Cost: ")

            total = process_cost(mat, labor, overhead)
            print(f"\n📌 Total Process Cost = {total:.2f}")

        elif choice == "3":
            cost = get_float("Total Cost: ")
            profit = get_float("Profit %: ")

            price = profit_price(cost, profit)
            print(f"\n📌 Selling Price = {price:.2f}")

        elif choice == "4":
            break

        else:
            print("❌ Invalid choice")


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
5. Exit
""")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            yarn_menu()
        elif choice == "2":
            fabric_menu()
        elif choice == "3":
            dyeing_menu()
        elif choice == "4":
            costing_menu()
        elif choice == "5":
            print("\n👋 Exiting TextileCalc Toolkit... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()