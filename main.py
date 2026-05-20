# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from player import Player
from battle_ui import *
from battle import *
from pokemon import *
from map import *
from npc import NPC
from inicio import *

game_mode = 'inicio'
pygame.mixer.init()
pygame.init()
fonte = pygame.font.Font(None, 14)
# ----- Gera tela principal
width_base = 160
height_base = 144
frame_width = 256
frame_height = 224
game_x = 48
game_y = 40
escala = 4
WIDTH = frame_width * escala
HEIGHT = frame_height * escala
screen = pygame.display.set_mode((WIDTH, HEIGHT))
tela_base = pygame.Surface((width_base, height_base))
frame_base = pygame.Surface((frame_width, frame_height))
frame = pygame.image.load("assets/frame_blue_english.png").convert()
pygame.display.set_caption('Matias, Lucas, Gabriel')


#----- Musicas
musica_atual = None

def toca_musica(path, volume=0.5):
    global musica_atual


    if musica_atual != path:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        musica_atual = path

toca_musica("assets/sounds/inicio.mp3", 0.5)
    
# ----- Inicia estruturas de dados
tick = pygame.time.Clock()
mapa = load_map()
mask = load_mask()
mapa_width = mapa.get_width()
mapa_height = mapa.get_height()
game = True
player = Player(175,500)
npc_cura = NPC(175, 470)



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
    if game_mode == 'andando':

        loc_x_antiga = player.x
        loc_y_antiga = player.y

        player.move(keys, mask, is_collision, is_ledge)
        player.x = max(0, min(player.x, mapa_width - player.width))
        player.y = max(0, min(player.y, mapa_height - player.height))
        camera_x = player.x - width_base // 2
        camera_y = player.y - height_base // 2
        


        camera_x = max(0, min(camera_x, mapa_width - width_base))
        camera_y = max(0, min(camera_y, mapa_height - height_base))

        draw_map(tela_base, mapa, camera_x, camera_y)

        player.draw(tela_base, camera_x, camera_y)
        npc_cura.draw(tela_base, camera_x, camera_y)

        if keys[pygame.K_b]:
            game_mode = 'batalha'

    elif game_mode == 'batalha':
        desenha_tela(tela_base, fonte)
        game_mode = draw_battle(tela_base, fonte)
        
    elif game_mode == 'inicio':
        inicio = tela_inicio()
        draw_inicio(tela_base, inicio)

        if keys[pygame.K_RETURN]:
            game_mode = 'andando'
            toca_musica("assets/sounds/Route1.mp3", 0.5)

    # ----- Atualiza estado do jogo
    frame_base.blit(frame, (0, 0))  
    frame_base.blit(tela_base, (game_x, game_y))
    tela_escalada = pygame.transform.scale(frame_base, (WIDTH, HEIGHT))
    screen.blit(tela_escalada, (0, 0))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
