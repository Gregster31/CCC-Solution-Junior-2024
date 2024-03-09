# Problem J4:
from typing import Optional


def main():
    # Get inputs
    keys_pressed = input().strip()
    letters_displayed = input().strip()

    silly_key = None
    quiet_key = None
    wrong_letter = None
    for key, letter in zip(keys_pressed, letters_displayed):
        if key != letter:
            silly_key = key
            wrong_letter = letter
            break

    # If there's no quiet key, return '-'
    if silly_key is None:
        print(f"{silly_key} {wrong_letter}\n-")

    # Find the quiet key
    for i in range(len(keys_pressed) - 1):
        if keys_pressed[i] == silly_key and keys_pressed[i + 1] != quiet_key:
            quiet_key = keys_pressed[i + 1]
            break

    if quiet_key is None:
        quiet_key = '-'

    print(f"{silly_key} {wrong_letter}\n{quiet_key}")


if __name__ == "__main__":
    main()