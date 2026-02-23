from utils import Utils

class Point:
    """A point consists of an abscissa and an ordinate"""
    def __init__(self, x: int, y: int):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def move(self, direction: str):
        match direction:
            case "<":
                self.x -= 1
            case ">":
                self.x += 1
            case "^":
                self.y += 1
            case "v":
                self.y -= 1

def point_exist(points: list, point: bool) -> bool:
    for p in points:
        if p.x == point.x and p.y == point.y:
            return True
    return False


if __name__ == "__main__":

    puzzle = Utils("https://adventofcode.com/2015/day/3/input").get_puzzle()

    points = [Point(0,0)]
    tmp_point = Point(0,0)

    for direction in puzzle:
        tmp_point.move(direction)
        
        if point_exist(points,tmp_point):
            continue
        else:
            points.append(Point(tmp_point.x,tmp_point.y))
    print(f"Part 1: The Santa Claus will distribute {len(points)} gifts.")


