from utils.validator import validate_positive

def ne_to_tex(ne):
    validate_positive(ne, "Ne")
    return 590.5 / ne

def tex_to_ne(tex):
    validate_positive(tex, "Tex")
    return 590.5 / tex

def tex_to_denier(tex):
    validate_positive(tex, "Tex")
    return tex * 9

def cv_percentage(sd, mean):
    validate_positive(mean, "Mean")
    return (sd / mean) * 100

def csp(count, strength):
    return count * strength