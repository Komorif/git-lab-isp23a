from main import add, subtract, multiply, divide, parse_number

def run():
    assert add(2, 3) == 5
    assert subtract(8, 3) == 5
    assert multiply(4, 3) == 12
    assert divide(8, 2) == 4
    assert parse_number("2.5") == 2.5
    try: divide(1, 0); assert False
    except ZeroDivisionError: pass
    try: parse_number("bad"); assert False
    except ValueError: pass
    print("6 tests passed")
if __name__ == "__main__": run()
