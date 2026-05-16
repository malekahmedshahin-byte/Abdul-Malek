import sys
sys.path.append(".")

from textilecalc import *


# =========================
# YARN MENU
# =========================
def yarn_menu():
    while True:
        print("\n--- YARN CALCULATIONS ---")
        print("1. Ne to Tex")
        print("2. Tex to Ne")
        print("3. Tex to Denier")
        print("4. CV%")
        print("5. CSP")
        print("6. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                ne = float(input("Enter Ne: "))
                print("Tex =", ne_to_tex(ne))

            elif choice == "2":
                tex = float(input("Enter Tex: "))
                print("Ne =", tex_to_ne(tex))

            elif choice == "3":
                tex = float(input("Enter Tex: "))
                print("Denier =", tex_to_denier(tex))

            elif choice == "4":
                sd = float(input("Enter Standard Deviation: "))
                mean = float(input("Enter Mean: "))
                print("CV% =", cv_percentage(sd, mean))

            elif choice == "5":
                count = float(input("Enter Count: "))
                strength = float(input("Enter Strength: "))
                print("CSP =", csp(count, strength))

            elif choice == "6":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# FABRIC MENU
# =========================
def fabric_menu():
    while True:
        print("\n--- FABRIC CALCULATIONS ---")
        print("1. GSM")
        print("2. Fabric Weight")
        print("3. Cover Factor")
        print("4. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                weight = float(input("Weight (g): "))
                length = float(input("Length (m): "))
                width = float(input("Width (m): "))
                print("GSM =", gsm(weight, length, width))

            elif choice == "2":
                gsm_val = float(input("Enter GSM: "))
                width = float(input("Width (m): "))
                length = float(input("Length (m): "))
                print("Fabric Weight =", fabric_weight(gsm_val, width, length))

            elif choice == "3":
                ends = float(input("Ends: "))
                picks = float(input("Picks: "))
                count = float(input("Count: "))
                print("Cover Factor =", cover_factor(ends, picks, count))

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# DYEING MENU
# =========================
def dyeing_menu():
    while True:
        print("\n--- DYEING CALCULATIONS ---")
        print("1. Dye Required")
        print("2. Liquor Required")
        print("3. Chemical Required")
        print("4. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                fw = float(input("Fabric Weight (kg): "))
                shade = float(input("Shade %: "))
                print("Dye Required =", dye_required(fw, shade), "kg")

            elif choice == "2":
                mw = float(input("Material Weight (kg): "))
                mlr = float(input("MLR: "))
                print("Liquor Required =", liquor_required(mw, mlr))

            elif choice == "3":
                mw = float(input("Material Weight (kg): "))
                percent = float(input("Chemical %: "))
                print("Chemical Required =", chemical_required(mw, percent))

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# COSTING MENU
# =========================
def costing_menu():
    while True:
        print("\n--- COSTING CALCULATIONS ---")
        print("1. Yarn Cost")
        print("2. Process Cost")
        print("3. Profit Price")
        print("4. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                weight = float(input("Weight: "))
                rate = float(input("Rate: "))
                print("Yarn Cost =", yarn_cost(weight, rate))

            elif choice == "2":
                material = float(input("Material Cost: "))
                labor = float(input("Labor Cost: "))
                overhead = float(input("Overhead: "))
                print("Process Cost =", process_cost(material, labor, overhead))

            elif choice == "3":
                total = float(input("Total Cost: "))
                profit = float(input("Profit %: "))
                print("Profit Price =", profit_price(total, profit))

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# PRODUCTION MENU
# =========================
def production_menu():
    while True:
        print("\n--- PRODUCTION CALCULATIONS ---")
        print("1. Efficiency")
        print("2. Production Rate")
        print("3. Machine Utilization")
        print("4. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                actual = float(input("Actual Production: "))
                target = float(input("Target Production: "))
                print("Efficiency =", efficiency(actual, target), "%")

            elif choice == "2":
                output = float(input("Output: "))
                hours = float(input("Hours: "))
                print("Production Rate =", production_rate(output, hours))

            elif choice == "3":
                run = float(input("Run Time: "))
                available = float(input("Available Time: "))
                print("Machine Utilization =", machine_utilization(run, available), "%")

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# WASTAGE MENU
# =========================
def wastage_menu():
    while True:
        print("\n--- WASTAGE CALCULATIONS ---")
        print("1. Wastage Percentage")
        print("2. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                inp = float(input("Input Weight: "))
                out = float(input("Output Weight: "))
                print("Wastage =", wastage_percentage(inp, out), "%")

            elif choice == "2":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# UNIT CONVERSION MENU
# =========================
def unit_menu():
    while True:
        print("\n--- UNIT CONVERSIONS ---")
        print("1. KG to LBS")
        print("2. LBS to KG")
        print("3. Inch to Meter")
        print("4. Meter to Inch")
        print("5. GSM to Oz/yd²")
        print("6. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                kg = float(input("Enter KG: "))
                print("LBS =", kg_to_lbs(kg))

            elif choice == "2":
                lbs = float(input("Enter LBS: "))
                print("KG =", lbs_to_kg(lbs))

            elif choice == "3":
                inch = float(input("Enter Inch: "))
                print("Meter =", inch_to_meter(inch))

            elif choice == "4":
                meter = float(input("Enter Meter: "))
                print("Inch =", meter_to_inch(meter))

            elif choice == "5":
                gsm_val = float(input("Enter GSM: "))
                print("Oz/yd² =", gsm_to_oz_yd2(gsm_val))

            elif choice == "6":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# QC MENU
# =========================
def qc_menu():
    while True:
        print("\n--- QC CALCULATIONS ---")
        print("1. Moisture Regain")
        print("2. Shrinkage %")
        print("3. Absorbency Rate")
        print("4. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                orig = float(input("Original Weight: "))
                dry = float(input("Dry Weight: "))
                print("Moisture Regain =", moisture_regain(orig, dry), "%")

            elif choice == "2":
                orig = float(input("Original Dimension: "))
                final = float(input("Final Dimension: "))
                print("Shrinkage % =", shrinkage_percent(orig, final), "%")

            elif choice == "3":
                water = float(input("Water Absorbed: "))
                dry = float(input("Dry Weight: "))
                print("Absorbency Rate =", absorbency_rate(water, dry), "%")

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


# =========================
# MAIN MENU
# =========================
def main():
    while True:
        print("\n===== TEXTILECALC TOOLKIT =====")
        print("1. Yarn Calculations")
        print("2. Fabric Calculations")
        print("3. Dyeing Calculations")
        print("4. Costing Calculations")
        print("5. Production Calculations")
        print("6. Wastage Calculations")
        print("7. Unit Conversions")
        print("8. QC Calculations")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            yarn_menu()

        elif choice == "2":
            fabric_menu()

        elif choice == "3":
            dyeing_menu()

        elif choice == "4":
            costing_menu()

        elif choice == "5":
            production_menu()

        elif choice == "6":
            wastage_menu()

        elif choice == "7":
            unit_menu()

        elif choice == "8":
            qc_menu()

        elif choice == "9":
            print("Exiting TextileCalc Toolkit...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()