from utils import Utils

class Prism:
    """A rectangular prisme with height, width, and length"""

    def __init__(self, chaine: str):
        chaine = self.parse(chaine)
        self.l: int = int(chaine[0])
        self.w: int = int(chaine[1])
        self.h: int = int(chaine[2])


    def __repr__(self):
        return f"l={self.l} w={self.w} h={self.h}"

    def parse(self, chaine: str) -> list:
        """ Convert from "1x2x1" to [1,2,1]."""
        return chaine.rsplit("x")

    def aire_cote(self) -> list:
        return [self.l*self.w, self.w*self.h, self.h*self.l]

    def aire_total(self) -> int:
        return sum(2*air for air in self.aire_cote()) + min(self.aire_cote())

    def perimetre_cote(self):
        return [ (self.l+self.w)*2, (self.w+self.h)*2, (self.h+self.l)*2 ]

    def perimetre_petit_cote(self):
        return min(self.perimetre_cote())

    def ruban_distance_plus_courte(self):
        return 2*(self.l+self.w)

    def ruban_volume_noeud(self):
        return self.l*self.w*self.h 

    def ruban_total(self):
        return min(self.ruban_distance_plus_courte(), self.perimetre_petit_cote()) + self.ruban_volume_noeud()

def parse_puzzle_before(chaine: str):
    """Convert from '4x23x21\n2x3x13\n10x4x20' to '["4x23x21","2x3x13","10x4x20"]' """
    return puzzle.split("\n")

if __name__ == "__main__":
    puzzle=Utils("https://adventofcode.com/2015/day/2/input").get_puzzle()
    prisms = parse_puzzle_before(puzzle)

    air=0
    for prism in prisms:
        if prism != '':
            p=Prism(prism)
            air+=p.aire_total()
    print("Part 1 : The total air is", air, ".")


    ribbon=0
    for prism in prisms:
        if prism != '':
            p=Prism(prism)
            ribbon+=p.ruban_total()
    print("Part 2 : The total ribbon requirement is", ribbon, ".")
