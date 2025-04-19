def predict_logic(value: int) -> str:
    if value < 5:
        return "Low"
    elif 5 <= value <= 15:
        return "Medium"
    else:
        return "High"

def make_prediction(value: int) -> str:
    return predict_logic(value)
