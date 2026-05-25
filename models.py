# arquivo so pra nao ficar dando erro de importacao circular
import json
from pokemon import *
import random

player = ''

class Move: #IA # cria classe move (ataque do pokemon) com seus status
    def __init__(self, name, move_type, power, accuracy, pp):
        self.name = name          # "Lança-Chamas"
        self.move_type = move_type  # "Fogo"
        self.power = power        # 90  (quão forte é)
        self.accuracy = accuracy  # 100 (% de chance de acertar)
        self.pp = pp              # 15  (quantas vezes pode usar)
        self.current_pp = pp      # PP atual (vai diminuindo)

    def use(self): #usa o ataque
        if self.current_pp > 0:
            self.current_pp -= 1
            return True
        return False  # sem PP, não pode usar
    
def pega_ataques(poke_data): #transforma os ataques do dicionario em um lista de moves
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


with open('pokemons_ataque.json') as f: #abre o arquivo
    dicionario_ataques = json.load(f)

with open('sprites.json') as sprites:
    sprites_coordenadas = json.load(sprites)


for poke in dicionario_ataques: #cria o player pokemon (no caso é o charmander)
    if poke["name"] == "Charmander":
        player = pokemon(poke["name"],
                         poke['hp'],
                         poke['defense'],
                         poke['moves'],
                         poke['attack']
                         )
        break



player.moves = pega_ataques(player)


def get_enemy_sprite(enemy): #pega as coordenadas do sprite do enemy (pokemons.png)
    for poke in  sprites_coordenadas:
        if poke['name'] == enemy.name:
            return poke['x'], poke['y'], poke['width'], poke['height']
    return None

def define_enemy(): #define um inimigo aleatorio
    escolhido = random.choice(dicionario_ataques)
    enemy = pokemon(escolhido['name'], escolhido['hp'], escolhido['defense'], escolhido['moves'], escolhido['attack'])
    enemy.moves = pega_ataques(enemy)
    return enemy
enemy = define_enemy()
