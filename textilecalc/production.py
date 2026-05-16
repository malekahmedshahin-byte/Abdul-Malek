from utils.validator import validate_positive

def efficiency(actual, target):
    validate_positive(target, "Target")
    return (actual / target) * 100

def production_rate(output, hours):
    validate_positive(hours, "Hours")
    return output / hours

def machine_utilization(run_time, available_time):
    return (run_time / available_time) * 100