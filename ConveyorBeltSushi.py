def main():
    total_cost: int = 0
    red: int = int(input())
    green: int = int(input())
    blue: int = int(input())

    total_cost = red * 3 + green * 4 + blue * 5
    print(total_cost)


if __name__ == "__main__":
    main()