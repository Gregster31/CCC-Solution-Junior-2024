# Problem J4:
from typing import Optional


def main():
    silence: str = ""
    absurde: str = ""
    replace: str = ""
    overcooked: int = 0

    frapper = "forloops"
    afficher = "frlpz"

    # No silence touch
    if len(frapper) == len(afficher):
        silence = "-"
        for i in range(len(frapper)):
            if frapper[i] != afficher[i]:
                absurde = frapper[i]
                replace = afficher[i]
                break
    else:
        silent = find_silent(frapper, silence)

        # Delete all silent in frapper
        for j in range(len(frapper)):
            if frapper[j] == silent:
                frapper[j] = ""

        # check which are not the same letters
        for a in range(len(frapper)):
            if frapper[a] != afficher[a]:
                absurde = frapper[a]
                replace = afficher[a]
    print(f"{absurde} {replace}\n{silence}")


def find_silent(frapper, afficher) -> str:
    for i in range(len(frapper) - 1):
        if frapper[i] == afficher[i]:
            continue
        else:
            if frapper[i + 1] == afficher[i]:
                return frapper[i]


if __name__ == "__main__":
    main()