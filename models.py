# arquivo so pra nao ficar dando erro de importacao circular
import json
from pokemon import *
import random

player = ''
enemy = ''
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
    
def pega_ataques(poke_data):
    pokemon_data = poke_data

    if pokemon_data == None:
        return []

    lista_ataques = pokemon_data.moves
    ataques_convertidos = []

    for ataque in lista_ataques:
        ataques_convertidos.append(
            Move(
                ataque["name"],
                ataque["type"],
                ataque["power"],
                ataque["accuracy"],
                ataque["pp"],
            )
        )

    return ataques_convertidos


with open('pokemons_ataque.json') as f:
    dicionario_ataques = json.load(f)

with open('sprites.json') as sprites:
    sprites_coordenadas = json.load(sprites)


for poke in dicionario_ataques:
    if poke["name"] == "Charmander":
        player = pokemon(poke["name"],
                         poke['hp'],
                         poke['defense'],
                         poke['moves'],
                         poke['attack']
                         )
        break
escolhido = random.choice(dicionario_ataques)
enemy = pokemon(
    escolhido['name'],
    escolhido['hp'],
    escolhido['defense'],
    escolhido['moves'],
    escolhido['attack']
)

for poke in sprites_coordenadas:
    if poke['name'] == enemy.name:
        enemy_x = poke['x']
        enemy_y = poke['y']
        enemy_height = poke['height']
        enemy_width = poke['width']
player.moves = pega_ataques(player)
enemy.moves = pega_ataques(enemy)
