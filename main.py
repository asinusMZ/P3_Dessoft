# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from player import Player
from battle_ui import *
from battle import *
from pokemon import *
from map import *

pygame.init()
fonte = pygame.font.Font(None, 16)
# ----- Gera tela principal
width_base = 160
height_base = 160
escala = 4
WIDTH = width_base*escala
HEIGHT = height_base*escala
screen = pygame.display.set_mode((WIDTH, HEIGHT))
tela_base = pygame.Surface((width_base, height_base))
pygame.display.set_caption('Matias, Lucas, Gabriel')


# ----- Inicia estruturas de dados
tick = pygame.time.Clock()
map = load_map()
game = True
game_mode = 'andando'
player = Player(100,100)



# ===== Loop principal =====
while game:
    tick.tick(60)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    
    # ----- Gera saídas
    tela_base.fill((0, 0, 0)) # Preenche com a cor branca
    if keys[pygame.K_b]:
        game_mode = 'batalha'
    if game_mode == 'andando':
        player.move(keys)
        draw_map(screen, map)
        player.draw(tela_base) 
    elif game_mode == 'batalha':
        mostra_caixa_acoes = False
        desenha_tela(tela_base, fonte)
        if keys[pygame.K_RETURN]:
            mostra_caixa_acoes = True
        if mostra_caixa_acoes == True:
            desenha_caixas('acoes', tela_base)
        

    # ----- Atualiza estado do jogo
    tela_escalada = pygame.transform.scale(tela_base, (WIDTH, HEIGHT))
    screen.blit(tela_escalada, (0, 0))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
