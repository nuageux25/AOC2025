from utils import Utils

def get_santa_floor(puzzle: str) -> int :
    floor=0
    for parenthesis in puzzle:
        match parenthesis:
            case "(":
                floor += 1
            case _:
                floor -= 1
    return floor

def get_elve_position(puzzle: str) -> int|None :
    floor=0
    for i in range(0,len(puzzle)):   
        match puzzle[i]:
            case "(":
                floor +=1
            case _:
                floor -= 1
                if floor == -1 :
                    return i + 1
    return None

if __name__ == "__main__":
    puzzle=Utils("https://adventofcode.com/2015/day/1/input").get_puzzle()
    print("Part 1 : The christmas santa will get on floor",get_santa_floor(puzzle),".")
    print("Part 2 : The elve will be at position",get_elve_position(puzzle),".")
