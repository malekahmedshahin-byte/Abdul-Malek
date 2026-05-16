def validate_positive(value, name="Value"):
    if value <= 0:
        raise ValueError(f"{name} must be positive.")
    return value