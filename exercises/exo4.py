from utils import Utils
import hashlib

def start_with_5_zero(chaine: str):
    return chaine[:5] == "00000"

def start_with_6_zero(chaine: str):
    print(chaine[:6])
    return chaine[:6] == "000000"
     
def hash_text(text: str):
    hs = hashlib.md5()
    hs.update(text.encode())
    return hs.hexdigest()

def parse(text):
    """from 'abcdef\n' to 'abcdef'"""
    return text.rstrip()

if __name__ == "__main__":
    puzzle = Utils("https://adventofcode.com/2015/day/4/input").get_puzzle()
    puzzle = parse(puzzle)

    number = 0
    hashed_puzzle = hash_text(puzzle)

    while (not start_with_5_zero(hashed_puzzle)):
        number += 1
        text_number = puzzle + str(number)
        hashed_puzzle = hash_text(text_number)
    print(f"Part 1 : The string {text_number} get this hash {hashed_puzzle} on number {number}.")   

    while (not start_with_6_zero(hashed_puzzle)):
        number += 1
        text_number = puzzle + str(number)
        hashed_puzzle = hash_text(text_number)
    print(f"Part 2 : The string {text_number} get this hash {hashed_puzzle} on number {number}.")     
