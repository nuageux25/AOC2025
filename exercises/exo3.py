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

    santa_map = [Point(0,0)]
    santa_position = Point(0,0)

    for direction in puzzle:

        santa_position.move(direction)

        if not point_exist(santa_map, santa_position):
            santa_map.append(Point(santa_position.x,santa_position.y))

    print(f"Part 1: The Santa Claus will distribute {len(santa_map)} gifts.")


    i=0

    santa_map=[Point(0,0)]
    santa_position=Point(0,0)

    robot_map=[Point(0,0)]
    robot_position=Point(0,0)

    for direction in puzzle:

        #santa
        if i%2==0:
            santa_position.move(direction)
            if not point_exist(santa_map,santa_position) and not point_exist(robot_map,santa_position):
                santa_map.append(Point(santa_position.x,santa_position.y))
        #robot
        else:
            robot_position.move(direction)
            if not point_exist(robot_map,robot_position) and not point_exist(santa_map,robot_position):
                robot_map.append(Point(robot_position.x,robot_position.y))
        i += 1

    print(len(santa_map)+len(robot_map)-1,"houses will get at least one gift.")
