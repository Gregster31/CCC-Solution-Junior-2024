def main():
    initial_size: int = int(input())
    total_size: int = initial_size

    current_yobi: int = int(input())
    while current_yobi:
        if current_yobi >= total_size:
            print(total_size)
            return
        else:
            total_size += current_yobi
            current_yobi: int = int(input())


if __name__ == "__main__":
    main()
