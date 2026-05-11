import random

class Move: #IA
    def __init__(self, name, move_type, power, accuracy, pp):
        self.name = name          # "Lança-Chamas"
        self.move_type = move_type  # "Fogo"
        self.power = power        # 90  (quão forte é)
        self.accuracy = accuracy  # 100 (% de chance de acertar)
        self.pp = pp              # 15  (quantas vezes pode usar)
        self.current_pp = pp      # PP atual (vai diminuindo)

    def use(self):
        if self.current_pp > 0:
            self.current_pp -= 1
            return True
        return False  # sem PP, não pode usar

class battle:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player = player_pokemon
        self.enemy = enemy_pokemon
        self.state = "ESCOLHA_ACAO"
        self.message = ""

    
    def player_attack(self, move):
        damage = self.calculate_damage(move, self.player, self.enemy)
        self.enemy.take_damage(damage)
        self.message = f"{self.player.name} usou {move.name}!"
        self.state = "TURNO_INIMIGO"

    def enemy_attack(self):
        move = random.choice(self.enemy.moves)
        damage = self.calculate_damage(move, self.enemy, self.player)
        self.player.take_damage(damage)
        self.message = f"{self.enemy.name} usou {move.name}"
    
    def calculate_damage(self, move, attacker, defender): #IA
        return int((move.power * attacker.attack) / defender.defense * 0.5)
    
    def check_winner(self):
        if self.enemy.is_fainted():
            return "JOGADOR"
        if self.player.is_fainted():
            return "INIMIGO"
        return None