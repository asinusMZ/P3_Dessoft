import random
import pygame
from pokemon import *
from models import Move
from battle_ui import *


mostra_caixa_acoes = False
mostra_caixa_ataques = False
selected = 'fight'
selected_attack = 0



class battle:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player = player_pokemon
        self.enemy = enemy_pokemon
        self.state = "ESCOLHA_ACAO"
        self.message = ""

    
    def player_attack(self, move):
        damage = self.calculate_damage(move, self.player, self.enemy)
        print(damage)
        self.enemy.take_damage(damage)
        self.message = f"{self.player.name} usou {move.name}!"
        self.state = "TURNO_INIMIGO"
        print(self.enemy.vida)
    def enemy_attack(self):
        move = random.choice(self.enemy.moves)
        damage = self.calculate_damage(move, self.enemy, self.player)
        self.player.take_damage(damage)
        self.message = f"{self.enemy.name} usou {move.name}"
    
    def calculate_damage(self, move, attacker, defender):
        return int((move.power + attacker.attack) / defender.defense)
    
    def check_winner(self):
        if self.enemy.is_fainted():
            return "JOGADOR"
        if self.player.is_fainted():
            return "INIMIGO"
        return None
    
batalha = battle(player, enemy)
def handle_input(event): #IA
    global mostra_caixa_acoes, mostra_caixa_ataques, selected, selected_attack

    if event.type != pygame.KEYDOWN:
        return

    if mostra_caixa_ataques:
        if event.key == pygame.K_ESCAPE:
            mostra_caixa_ataques = False
            selected_attack = 0
            return

        elif event.key == pygame.K_UP:
            selected_attack = 0
            return

        elif event.key == pygame.K_DOWN:
            selected_attack = 1
            return

        elif event.key == pygame.K_RETURN:
            battle.player_attack(batalha, ataques_player[selected_attack])
            mostra_caixa_ataques = False
            mostra_caixa_acoes = False
            return
        
    elif mostra_caixa_acoes:
        if event.key == pygame.K_ESCAPE:
            mostra_caixa_acoes = False
            return

        elif event.key == pygame.K_UP:
            selected = 'fight'
            return

        elif event.key == pygame.K_DOWN:
            selected = 'run'
            return

        elif event.key == pygame.K_RETURN:
            if selected == 'fight':
                mostra_caixa_ataques = True
                selected_attack = 0
            elif selected == 'run':
                # aqui você coloca a lógica de fugir
                pass
            return
    else:
        if event.key == pygame.K_RETURN:
            mostra_caixa_acoes = True
            selected = 'fight'
            selected_attack = 0
            return

def draw_battle(tela, fonte):
    if batalha.state == 'ESCOLHA_ACAO':
        if mostra_caixa_acoes:
            desenha_caixas('acoes', tela, fonte)
            desenha_seta('acoes', tela, selected, fonte)
            if mostra_caixa_ataques:
                desenha_caixas('ataques', tela, fonte)
                desenha_seta('ataques', tela, selected_attack, fonte)

