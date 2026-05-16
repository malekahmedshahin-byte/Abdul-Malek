import sys
sys.path.append(".")

from textilecalc import *


# =========================================
# YARN CALCULATIONS MENU
# =========================================
def yarn_menu():
    while True:
        print("\n========== YARN CALCULATIONS ==========")
        print("1. Convert English Cotton Count (Ne) to Tex")
        print("2. Convert Tex to English Cotton Count (Ne)")
        print("3. Convert Tex to Denier")
        print("4. Calculate Coefficient of Variation (CV%)")
        print("5. Calculate Count Strength Product (CSP)")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                english_count_ne = float(input("Enter English Cotton Count (Ne): "))
                print("Yarn Linear Density =", ne_to_tex(english_count_ne), "Tex")

            elif choice == "2":
                yarn_tex = float(input("Enter Yarn Linear Density (Tex): "))
                print("English Cotton Count =", tex_to_ne(yarn_tex), "Ne")

            elif choice == "3":
                yarn_tex = float(input("Enter Yarn Linear Density (Tex): "))
                print("Yarn Count =", tex_to_denier(yarn_tex), "Denier")

            elif choice == "4":
                standard_deviation = float(input("Enter Standard Deviation: "))
                mean_value = float(input("Enter Mean Value: "))
                print("Coefficient of Variation =", cv_percentage(standard_deviation, mean_value), "%")

            elif choice == "5":
                yarn_count = float(input("Enter Yarn Count: "))
                yarn_strength = float(input("Enter Yarn Strength (lb): "))
                print("Count Strength Product =", csp(yarn_count, yarn_strength))

            elif choice == "6":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# FABRIC CALCULATIONS MENU
# =========================================
def fabric_menu():
    while True:
        print("\n========== FABRIC CALCULATIONS ==========")
        print("1. Calculate Fabric GSM (Gram per Square Meter)")
        print("2. Calculate Total Fabric Weight")
        print("3. Calculate Fabric Cover Factor")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                fabric_weight_grams = float(input("Enter Fabric Weight (grams): "))
                fabric_length_meters = float(input("Enter Fabric Length (meters): "))
                fabric_width_meters = float(input("Enter Fabric Width (meters): "))
                print("Fabric GSM =", gsm(fabric_weight_grams, fabric_length_meters, fabric_width_meters), "g/m²")

            elif choice == "2":
                fabric_gsm = float(input("Enter Fabric GSM (g/m²): "))
                fabric_width_meters = float(input("Enter Fabric Width (meters): "))
                fabric_length_meters = float(input("Enter Fabric Length (meters): "))
                print("Total Fabric Weight =", fabric_weight(fabric_gsm, fabric_width_meters, fabric_length_meters), "grams")

            elif choice == "3":
                ends_per_inch = float(input("Enter Ends per Inch (EPI): "))
                picks_per_inch = float(input("Enter Picks per Inch (PPI): "))
                yarn_count = float(input("Enter Yarn Count: "))
                print("Fabric Cover Factor =", cover_factor(ends_per_inch, picks_per_inch, yarn_count))

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# DYEING CALCULATIONS MENU
# =========================================
def dyeing_menu():
    while True:
        print("\n========== DYEING CALCULATIONS ==========")
        print("1. Calculate Required Dye Amount")
        print("2. Calculate Required Liquor Amount")
        print("3. Calculate Required Chemical Amount")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                fabric_weight_kg = float(input("Enter Fabric Weight (kg): "))
                shade_percentage = float(input("Enter Shade Percentage (%): "))
                print("Required Dye =", dye_required(fabric_weight_kg, shade_percentage), "kg")

            elif choice == "2":
                material_weight_kg = float(input("Enter Material Weight (kg): "))
                material_liquor_ratio = float(input("Enter Material to Liquor Ratio (example: 10 for 1:10): "))
                print("Required Liquor =", liquor_required(material_weight_kg, material_liquor_ratio), "liters")

            elif choice == "3":
                material_weight_kg = float(input("Enter Material Weight (kg): "))
                chemical_percentage = float(input("Enter Chemical Percentage (%): "))
                print("Required Chemical =", chemical_required(material_weight_kg, chemical_percentage), "kg")

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# COSTING CALCULATIONS MENU
# =========================================
def costing_menu():
    while True:
        print("\n========== COSTING CALCULATIONS ==========")
        print("1. Calculate Yarn Cost")
        print("2. Calculate Total Process Cost")
        print("3. Calculate Selling Price with Profit")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                yarn_weight_kg = float(input("Enter Yarn Weight (kg): "))
                yarn_rate_per_kg = float(input("Enter Yarn Rate per kg: "))
                print("Total Yarn Cost =", yarn_cost(yarn_weight_kg, yarn_rate_per_kg))

            elif choice == "2":
                material_cost = float(input("Enter Material Cost: "))
                labor_cost = float(input("Enter Labor Cost: "))
                overhead_cost = float(input("Enter Overhead Cost: "))
                print("Total Process Cost =", process_cost(material_cost, labor_cost, overhead_cost))

            elif choice == "3":
                total_cost = float(input("Enter Total Cost: "))
                profit_percentage = float(input("Enter Profit Percentage (%): "))
                print("Final Selling Price =", profit_price(total_cost, profit_percentage))

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# PRODUCTION CALCULATIONS MENU
# =========================================
def production_menu():
    while True:
        print("\n========== PRODUCTION CALCULATIONS ==========")
        print("1. Calculate Production Efficiency")
        print("2. Calculate Production Rate")
        print("3. Calculate Machine Utilization")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                actual_production = float(input("Enter Actual Production Quantity: "))
                target_production = float(input("Enter Target Production Quantity: "))
                print("Production Efficiency =", efficiency(actual_production, target_production), "%")

            elif choice == "2":
                total_output = float(input("Enter Total Output Quantity: "))
                production_hours = float(input("Enter Total Production Hours: "))
                print("Production Rate =", production_rate(total_output, production_hours), "units/hour")

            elif choice == "3":
                machine_run_time = float(input("Enter Machine Run Time (hours): "))
                available_time = float(input("Enter Total Available Time (hours): "))
                print("Machine Utilization =", machine_utilization(machine_run_time, available_time), "%")

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# WASTAGE CALCULATIONS MENU
# =========================================
def wastage_menu():
    while True:
        print("\n========== WASTAGE CALCULATIONS ==========")
        print("1. Calculate Wastage Percentage")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                input_weight_kg = float(input("Enter Input Material Weight (kg): "))
                output_weight_kg = float(input("Enter Output Material Weight (kg): "))
                print("Wastage Percentage =", wastage_percentage(input_weight_kg, output_weight_kg), "%")

            elif choice == "2":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# UNIT CONVERSION MENU
# =========================================
def unit_menu():
    while True:
        print("\n========== UNIT CONVERSIONS ==========")
        print("1. Kilogram to Pound")
        print("2. Pound to Kilogram")
        print("3. Inch to Meter")
        print("4. Meter to Inch")
        print("5. GSM to Ounce per Square Yard")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                kilogram_value = float(input("Enter Weight (kg): "))
                print("Weight =", kg_to_lbs(kilogram_value), "lb")

            elif choice == "2":
                pound_value = float(input("Enter Weight (lb): "))
                print("Weight =", lbs_to_kg(pound_value), "kg")

            elif choice == "3":
                inch_value = float(input("Enter Length (inch): "))
                print("Length =", inch_to_meter(inch_value), "meter")

            elif choice == "4":
                meter_value = float(input("Enter Length (meter): "))
                print("Length =", meter_to_inch(meter_value), "inch")

            elif choice == "5":
                gsm_value = float(input("Enter Fabric GSM (g/m²): "))
                print("Fabric Weight =", gsm_to_oz_yd2(gsm_value), "oz/yd²")

            elif choice == "6":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# QUALITY CONTROL MENU
# =========================================
def qc_menu():
    while True:
        print("\n========== QUALITY CONTROL CALCULATIONS ==========")
        print("1. Calculate Moisture Regain")
        print("2. Calculate Shrinkage Percentage")
        print("3. Calculate Absorbency Rate")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                original_weight = float(input("Enter Original Weight (grams or kg): "))
                dry_weight = float(input("Enter Dry Weight (same unit): "))
                print("Moisture Regain =", moisture_regain(original_weight, dry_weight), "%")

            elif choice == "2":
                original_dimension = float(input("Enter Original Dimension (cm/meter): "))
                final_dimension = float(input("Enter Final Dimension (same unit): "))
                print("Shrinkage Percentage =", shrinkage_percent(original_dimension, final_dimension), "%")

            elif choice == "3":
                absorbed_water_weight = float(input("Enter Absorbed Water Weight: "))
                dry_weight = float(input("Enter Dry Weight: "))
                print("Absorbency Rate =", absorbency_rate(absorbed_water_weight, dry_weight), "%")

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)


# =========================================
# MAIN MENU
# =========================================
def main():
    while True:
        print("\n================ TEXTILECALC TOOLKIT ================")
        print("1. Yarn Calculations")
        print("2. Fabric Calculations")
        print("3. Dyeing Calculations")
        print("4. Costing Calculations")
        print("5. Production Calculations")
        print("6. Wastage Calculations")
        print("7. Unit Conversions")
        print("8. Quality Control Calculations")
        print("9. Exit")

        choice = input("Enter your choice: ")

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
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()