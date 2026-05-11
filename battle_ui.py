import pygame
pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 320
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Matias, Lucas, Gabriel')
nome_pokemon = pygame.Rect((0,0), (100, 100))
# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    
    # ----- Gera saídas
    window.fill((0, 0, 50))  # Preenche com a cor branca
    pygame.draw.rect(window, (0,0,0), nome_pokemon)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
