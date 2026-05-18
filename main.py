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
mapa = load_map()
mask = load_mask()
mapa_width = mapa.get_width()
mapa_height = mapa.get_height()
game = True
game_mode = 'andando'
player = Player(182,522)
print(mapa.get_size())
print(mask.get_size())


# ===== Loop principal =====
while game:
    tick.tick(60)
    # ----- Trata eventos
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if game_mode == 'batalha':
                handle_input(event)
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    
    # ----- Gera saídas
    tela_base.fill((0, 0, 0)) # Preenche com a cor branca
    if keys[pygame.K_b]:
        game_mode = 'batalha'
    if game_mode == 'andando':
        loc_x_antiga = player.x
        loc_y_antiga = player.y

        player.move(keys, mask, is_collision)
        player.x = max(0, min(player.x, mapa_width - player.width))
        player.y = max(0, min(player.y, mapa_height - player.height))
        camera_x = player.x - width_base // 2
        camera_y = player.y - height_base // 2
        


        camera_x = max(0, min(camera_x, mapa_width - width_base))
        camera_y = max(0, min(camera_y, mapa_height - height_base))

        draw_map(tela_base, mapa, camera_x, camera_y)

        player.draw(tela_base, camera_x, camera_y)
    elif game_mode == 'batalha':
        desenha_tela(tela_base, fonte)
        draw_battle(tela_base, fonte)
        

    # ----- Atualiza estado do jogo
    tela_escalada = pygame.transform.scale(tela_base, (WIDTH, HEIGHT))
    screen.blit(tela_escalada, (0, 0))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
