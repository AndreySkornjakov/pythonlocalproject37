from random import randint


def main():
    a = [randint(1, 9) for _ in range(5)]
    b = [randint(1, 9) for _ in range(5)]

    c = func(a, b)
    print(f"Список {a}")
    print(f"Список {b}")
    print(f"Результат: {c}")


def check_unique(lst: list) -> bool:
    ...


def func(a: list, b: list) -> list:
    """"""
    c = []
    for elem in a:
        if elem not in b:
            c.append(elem)
    return c


if __name__ == "__main__":
    main()
