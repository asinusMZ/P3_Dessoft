class pokemon:
    def __init__(self,name, hp, defense, moves, attack):
        self.name = name
        self.vida = hp
        self.defense = defense
        self.moves = moves
        self.attack = attack
    
    def take_damage(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def is_fainted(self, hp):
        if hp <= 0:
            return True
        else:
            return False