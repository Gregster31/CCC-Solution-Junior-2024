def main():
    num_participants: int = int(input())

    scores = []
    for _ in range(num_participants):
        score: int = int(input())
        scores.append(score)
    scores.sort()

    third_place: int = scores[-3]
    print(f"{third_place} {scores.count(third_place)}")


if __name__ == "__main__":
    main()
