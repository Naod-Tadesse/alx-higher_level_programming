def validate(value, unit):
    """validator"""
    arr = ["x", "y"]
    if not isinstance(value, int):
        raise TypeError(f"{unit} must be an integer")
    if unit in arr:
        if value < 0:
            raise ValueError(f"{unit} must be >= 0")
    else:
        if value <= 0:
            raise ValueError(f"{unit} must be > 0")
