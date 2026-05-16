def moisture_regain(original_weight, dry_weight):
    return ((original_weight - dry_weight) / dry_weight) * 100

def shrinkage_percent(original, final):
    return ((original - final) / original) * 100

def absorbency_rate(water_absorbed, dry_weight):
    return (water_absorbed / dry_weight) * 100