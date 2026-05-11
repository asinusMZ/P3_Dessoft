# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from player import Player

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    screen.fill((0, 0, 50))  # Preenche com a cor branca

    player.draw(screen)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
