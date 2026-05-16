# costing_advanced.py

def cost_per_meter(total_cost, length):
    return total_cost / length

def energy_cost(power_kw, hours, rate):
    return power_kw * hours * rate

def depreciation(machine_cost, life_years):
    return machine_cost / life_years

def profit_margin(selling_price, cost_price):
    return ((selling_price - cost_price) / cost_price) * 100