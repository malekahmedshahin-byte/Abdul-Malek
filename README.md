# 🧵 Textile Calc Toolkit

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

A comprehensive Python-based Command Line Interface (CLI) tool and library for textile engineering calculations. Whether you are working in spinning, weaving, dyeing, quality control, or costing, this toolkit provides fast and accurate conversions and formulas.

## ✨ Features

The interactive toolkit includes multiple industry-specific modules:
* **🧶 Yarn Calculations:** Ne ↔ Tex ↔ Denier conversions, CV%, CSP, TPI/TPM.
* **👕 Fabric Calculations:** GSM, Fabric Weight, Cover Factor.
* **🧪 Dyeing & Advanced Dyeing:** Dye/Chemical requirements, Liquor Ratio, Exhaustion, Fixation.
* **🏭 Production & Costing:** Machine Efficiency, Utilization, Cost per Meter, Profit Margins, Depreciation.
* **🔬 Quality Control & Testing:** Moisture Regain, Shrinkage, Tensile Strength, Bursting Strength.
* **⚙️ Spinning & Weaving:** Imperfection Index (IPI), Break Rates, Defect Rates.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/malekahmedshahin-byte/Abdul-Malek.git]
   cd Abdul-Malek

For colab user or Jupyter notebook 
use :
```bash
   !git clone
[https://github.com/malekahmedshahin-byte/Abdul-Malek.git]
   %cd Abdul-Malek
   !python main.py

```bash
   python main.py
   from textilecalc import gsm

   from textilecalc import gsm, ne_to_tex

# Calculate GSM
fabric_gsm = gsm(weight=5.2, length=10, width=10)
print(f"Fabric GSM: {fabric_gsm}")

# Convert Ne to Tex
tex_count = ne_to_tex(30)
print(f"30 Ne is equivalent to {tex_count} Tex")


