def get_sort(d: dict):
    sorted_keys = sorted(d, reverse=True)
    sorted_values = []
    for i in sorted_keys:
        sorted_values.append(d[i])
    return sorted_values


def main():
    d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
    sorted_values = get_sort(d)
    print(sorted_values)


if __name__ == "__main__":
    main()
