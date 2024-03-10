def calculate_tax(amount, age, tax_rate=17.0):
    """Calculate income tax based on the amount and the age of the person."""
 
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be an integer or a float")
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
 
    if age < 0:
        raise ValueError("Age cannot be negative")
    if amount < 0:
        raise ValueError("Amount cannot be negative")
 
    if age <= 18:
        return int(min(amount * tax_rate / 100, 6000))
    elif age <= 65:
        return int(amount * tax_rate / 100)
    else:
        return int(min(amount * tax_rate / 100, 9000))


def income_tax(income, first_thresh=17.0, second_thresh=32.0):
    first_rate = first_thresh / 100.0
    second_rate = second_thresh / 100.0
    threshold = 85528
    if income < threshold:
        return income * first_rate
    else:
        return threshold * first_rate + (income - threshold) * second_rate
