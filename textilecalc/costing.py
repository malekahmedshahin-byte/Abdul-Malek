def yarn_cost(weight, rate):
    return weight * rate

def process_cost(material_cost, labor_cost, overhead):
    return material_cost + labor_cost + overhead

def profit_price(total_cost, profit_percent):
    return total_cost + (total_cost * profit_percent / 100)