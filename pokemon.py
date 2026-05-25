class pokemon:
    def __init__(self,name, hp, defense, moves, attack):
        self.name = name
        self.vida = hp
        self.max_hp = hp  # guarda o HP máximo para poder curar
        self.defense = defense
        self.moves = moves
        self.attack = attack
    
    def take_damage(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
 
    def heal(self):
        self.vida = self.max_hp
 
    def is_fainted(self, hp):
        if hp <= 0:
            return True
        else:
            return False