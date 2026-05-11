class pokemon:
    def __init__(name, hp, defense, moves):
        self.name = name
        self.vida = hp
        self.defense = defense
        self.moves = moves
    
    def take_damage(self, dano):
        self.vida -= dano
    

    def is_fainted(self, hp):
        if hp <= 0:
            return True
        else:
            return False