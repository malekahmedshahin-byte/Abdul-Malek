from textilecalc import *

def main():
    while True:
        print("\n===== TEXTILE LIBRARY TOOLKIT =====")
        print("1. Yarn Count Conversion")
        print("2. Fabric GSM")
        print("3. Dyeing Calculation")
        print("4. Production Efficiency")
        print("5. Wastage Calculation")
        print("6. Unit Conversion")
        print("7. QC")
        print("8. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                ne = float(input("Enter Ne: "))
                print("Tex =", ne_to_tex(ne))

            elif choice == "2":
                weight = float(input("Weight (g): "))
                length = float(input("Length (m): "))
                width = float(input("Width (m): "))
                print("GSM =", gsm(weight, length, width))

            elif choice == "3":
                fw = float(input("Fabric Weight (kg): "))
                shade = float(input("Shade %: "))
                print("Dye Required =", dye_required(fw, shade), "kg")

            elif choice == "4":
                actual = float(input("Actual Production: "))
                target = float(input("Target Production: "))
                print("Efficiency =", efficiency(actual, target), "%")

            elif choice == "5":
                inp = float(input("Input Weight: "))
                out = float(input("Output Weight: "))
                print("Wastage =", wastage_percentage(inp, out), "%")

            elif choice == "6":
                kg = float(input("Enter KG: "))
                print("LBS =", kg_to_lbs(kg))

            elif choice == "7":
                orig = float(input("Original Weight: "))
                dry = float(input("Dry Weight: "))
                print("Moisture Regain =", moisture_regain(orig, dry), "%")

            elif choice == "8":
                print("Exiting Textile Toolkit...")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()