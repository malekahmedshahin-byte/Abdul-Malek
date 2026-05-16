# spinning.py

def yarn_twist_tpi(twist, length):
    return twist / length

def yarn_tpm(tpi):
    return tpi * 39.37

def yarn_imperfection(u_percent, thin, thick, neps):
    return u_percent + (thin + thick + neps) / 3

def spinning_efficiency(actual_output, theoretical_output):
    return (actual_output / theoretical_output) * 100