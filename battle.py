import random
import pygame
from pokemon import *
from models import *
from battle_ui import *


mostra_caixa_acoes = False
mostra_caixa_ataques = False
selected = 'fight'
selected_attack = 0
tempo_inicio = 0

class battle:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player = player_pokemon
        self.enemy = enemy_pokemon
        self.state = "ESCOLHA_ACAO"
        self.message = f"{self.enemy.name} wants to fight"

    
    def player_attack(self, move):
        damage = self.calculate_damage(move, self.player, self.enemy)
        self.enemy.take_damage(damage)
        self.message = f"{self.player.name} usou {move.name}!"
        move.use()
        self.state = "TURNO_INIMIGO"
    def enemy_attack(self):
        move = random.choice(self.enemy.moves)
        damage = self.calculate_damage(move, self.enemy, self.player)
        self.player.take_damage(damage)
        self.message = f"{self.enemy.name} usou {move.name}"
        move.use()
        self.state = "ESCOLHA_ACAO"
    
    def calculate_damage(self, move, attacker, defender):
        return int((move.power + attacker.attack) / (defender.defense/2))
    
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
            battle.player_attack(batalha, player.moves[selected_attack])
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
    global tempo_inicio
    desenha_mensagem(tela, fonte, batalha.message)
    if batalha.state == 'ESCOLHA_ACAO':
        if mostra_caixa_acoes:
            desenha_caixas('acoes', tela, fonte)
            desenha_seta('acoes', tela, selected, fonte)
            if mostra_caixa_ataques:
                desenha_caixas('ataques', tela, fonte)
                desenha_seta('ataques', tela, selected_attack, fonte)
    elif batalha.state == "TURNO_INIMIGO":
        if tempo_inicio == 0:
            tempo_inicio = pygame.time.get_ticks()s
        if pygame.time.get_ticks() - tempo_inicio >= 2000:
            tempo_inicio = 0
            battle.enemy_attack(batalha)



