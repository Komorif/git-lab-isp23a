def add(a, b):
    return a + b

if __name__ == "__main__":
    print(calculate(2, 3))

def subtract(a, b):
    return a - b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('division by zero')
    return a / b
def parse_number(value):
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError('invalid numeric value') from exc
