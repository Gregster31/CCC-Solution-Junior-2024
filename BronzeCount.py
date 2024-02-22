def main():
    # key being the numbers and values being the number of times in inputs
    list_nums: dict[int, int] = {}

    current_num: int = int(input())
    # Add the num to the dict
    list_nums += {current_num, 1}

    while current_num:
        if list_nums.__contains__(current_num):




if __name__ == "__main__":
    main()