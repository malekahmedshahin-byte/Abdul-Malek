from utils.validator import validate_positive

def dye_required(fabric_weight, shade_percent):
    validate_positive(fabric_weight, "Fabric Weight")
    validate_positive(shade_percent, "Shade %")
    return (fabric_weight * shade_percent) / 100

def liquor_required(material_weight, mlr):
    validate_positive(material_weight, "Material Weight")
    validate_positive(mlr, "MLR")
    return material_weight * mlr

def chemical_required(material_weight, percent):
    return (material_weight * percent) / 100