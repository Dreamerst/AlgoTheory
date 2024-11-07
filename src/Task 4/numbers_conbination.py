def random_numbers_generator():
    d = "0123456789"
    numbers = (x+y+z for x in d if x != '0' for y in d if y != x for z in d if z != x and z != y)
    return numbers


def main():
    numbers = random_numbers_generator()
    print([int(next(numbers)) for _ in range(50)])


if __name__ == "__main__":
    main()
