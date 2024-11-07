def calculate(a: float, b: float, f):
    x = a
    while x < b:
        yield f(x)
        x += 0.01


def main():
    a = -20
    b = 100
    f = lambda x: -1.5 * x + 2
    result = calculate(a, b, f)
    print([next(result) for _ in range(20)])


if __name__ == "__main__":
    main()
    