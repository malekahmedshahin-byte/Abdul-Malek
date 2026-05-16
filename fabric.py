from utils.validator import validate_positive

def gsm(weight_g, length_m, width_m):
    validate_positive(weight_g, "Weight")
    validate_positive(length_m, "Length")
    validate_positive(width_m, "Width")
    return weight_g / (length_m * width_m)

def fabric_weight(gsm_val, width_m, length_m):
    validate_positive(gsm_val, "GSM")
    return gsm_val * width_m * length_m

def cover_factor(ends, picks, count):
    validate_positive(count, "Count")
    return (ends + picks) / count