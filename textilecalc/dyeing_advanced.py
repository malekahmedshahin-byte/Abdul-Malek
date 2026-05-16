# dyeing_advanced.py

def dye_exhaustion(initial_dye, remaining_dye):
    return ((initial_dye - remaining_dye) / initial_dye) * 100

def dye_fixation(fixed_dye, applied_dye):
    return (fixed_dye / applied_dye) * 100

def liquor_ratio(material, liquor):
    return liquor / material

def chemical_utilization(actual, theoretical):
    return (actual / theoretical) * 100