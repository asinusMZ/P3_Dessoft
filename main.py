# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from player import Player

pygame.init()

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
game = True
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
    player.movimento(keys)


    # ----- Gera saídas
    tela_base.fill((255, 255, 255)) # Preenche com a cor branca

    player.draw(screen)

    # ----- Atualiza estado do jogo
    tela_escalada = pygame.transform.scale(tela_base, (WIDTH, HEIGHT))
    screen.blit(tela_escalada, (0, 0))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
