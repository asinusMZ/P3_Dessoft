# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from player import Player
from battle_ui import *
from battle import *
from pokemon import *
from map import *
from npc import NPC
from inicio import *
import models
 
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
 
#------ encontros com pokemons na grama
 
def tentar_encontro(player_esta_na_grama, player_se_moveu):
    if player_esta_na_grama and player_se_moveu:
        chance = random.randint(1, 180)
 
        if chance == 1:
            return True
 
    return False
    
# ----- Inicia estruturas de dados
tick = pygame.time.Clock()
mapa = load_map()
mask = load_mask()
jogavel_width = 320
jogavel_height = 576
mapa_width = mapa.get_width()
mapa_height = mapa.get_height()
game = True
player = Player(175,500)
npc_cura = NPC(175, 470)
 
mensagem_cura = ""
mensagem_cura_timer = 0
 
 
 
# ===== Loop principal =====
while game:
    tick.tick(60)
    # ----- Trata eventos
    for event in pygame.event.get():
 
        if event.type == pygame.KEYDOWN:
            if game_mode == 'batalha':
                handle_input(event)
            elif game_mode == 'andando':
                if event.key == pygame.K_c:
                    if npc_cura.is_near_player(player):
                        models.player.heal()
                        mensagem_cura = f"{models.player.name} foi curado!"
                        mensagem_cura_timer = 180  # 3 segundos a 60fps
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
        player_esta_na_grama = is_grass(mask, player.get_rect())
        player_se_moveu = player.x != loc_x_antiga or player.y != loc_y_antiga
        player.x = max(0, min(player.x, jogavel_width - player.width))
        player.y = max(0, min(player.y, jogavel_height - player.height))
        camera_x = player.x - width_base // 2
        camera_y = player.y - height_base // 2
        
 
        camera_x = max(0, min(camera_x, jogavel_width - width_base))
        camera_y = max(0, min(camera_y, jogavel_height - height_base))
 
        draw_map(tela_base, mapa, camera_x, camera_y)
 
        player.draw(tela_base, camera_x, camera_y)
 
        if is_grass(mask, player.get_rect()):
            draw_cover(tela_base, mapa, player, camera_x, camera_y)
 
        
        if player_esta_na_grama:
            draw_cover(tela_base, mapa, player, camera_x, camera_y)
 
        if tentar_encontro(player_esta_na_grama, player_se_moveu):
            game_mode = 'batalha'
            reset_batalha()
            toca_musica("assets/sounds/battle.mp3", 0.5)
        
        npc_cura.draw(tela_base, camera_x, camera_y)
 
        # Mostra indicador de interação quando perto do NPC
        if npc_cura.is_near_player(player):
            hint_surf = fonte.render("[C] Curar", True, (255, 255, 255))
            npc_screen_x = npc_cura.x - camera_x
            npc_screen_y = npc_cura.y - camera_y - 10
            tela_base.blit(hint_surf, (npc_screen_x - 10, npc_screen_y))
 
        # Mostra mensagem de cura
        if mensagem_cura_timer > 0:
            mensagem_cura_timer -= 1
            msg_surf = fonte.render(mensagem_cura, True, (100, 255, 100))
            tela_base.blit(msg_surf, (5, 5))
        else:
            mensagem_cura = ""
 
 
    elif game_mode == 'batalha':
            desenha_tela(tela_base)
            toca_musica("assets/sounds/battle.mp3", 0.5)
            novo_modo = draw_battle(tela_base, fonte)
            if novo_modo == 'andando':
                game_mode = 'andando'
                toca_musica("assets/sounds/Route1.mp3", 0.5)
            else:
                game_mode = novo_modo
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
 