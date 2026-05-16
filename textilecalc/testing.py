# testing.py

def tensile_strength(force, area):
    return force / area

def elongation_percent(final_length, original_length):
    return ((final_length - original_length) / original_length) * 100

def bursting_strength(force, fabric_area):
    return force / fabric_area

def abrasion_index(loss_weight, initial_weight):
    return (loss_weight / initial_weight) * 100