import random
import pygame
from battle_ui import *
from pokemon import *
from models import Move

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
    
def handle_input(event):
    global mostra_caixa_acoes, mostra_caixa_ataques, selected, selected_attack #IA

    if not mostra_caixa_acoes:
        if event.key == pygame.K_RETURN:
            mostra_caixa_acoes = True
    else:
        if event.key == pygame.K_ESCAPE:
            mostra_caixa_acoes = False
        if event.key == pygame.K_DOWN:
            selected = 'run'
        if event.key == pygame.K_UP:
            selected_attack = 0
        if event.key == pygame.K_DOWN:
            selected_attack = 1
        if event.key == pygame.K_UP:
            selected = 'fight'
        if selected == 'fight' and event.key == pygame.K_RETURN:
            mostra_caixa_ataques = True
        

def draw_battle(tela, fonte):
    if mostra_caixa_acoes:
        desenha_caixas('acoes', tela, fonte)
        desenha_seta('acoes', tela, selected, fonte)
        if mostra_caixa_ataques:
            desenha_caixas('ataques', tela, fonte)
            desenha_seta('ataques', tela, selected_attack, fonte)

