from utils.validator import validate_positive

def wastage_percentage(input_weight, output_weight):
    validate_positive(input_weight, "Input Weight")
    return ((input_weight - output_weight) / input_weight) * 100