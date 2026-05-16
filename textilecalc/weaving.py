# weaving.py

def loom_efficiency(actual, ideal):
    return (actual / ideal) * 100

def warp_break_rate(breaks, total_ends):
    return (breaks / total_ends) * 100

def weft_break_rate(breaks, picks):
    return (breaks / picks) * 100

def fabric_defect_rate(defects, total_length):
    return (defects / total_length) * 100