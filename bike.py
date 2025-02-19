def calculate_inspection_cost(base_price):
    # Typical 20% negotiation leverage from identified flaws
    return base_price * 0.2 if base_price > 80000 else 0


c = calculate_inspection_cost(90000)
print(c)
