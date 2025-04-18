def predict_category(value: int) -> str:
    if value < 5:
        return "Low"
    elif 5 <= value < 15:
        return "Medium"
    else:
        return "High"