import pygame
pygame.init()

# ----- Gera tela principal

width_base = 160
height_base = 160
escala = 3
WIDTH = width_base * escala
HEIGHT = height_base * escala
window = pygame.display.set_mode((WIDTH, HEIGHT))
tela_base = pygame.Surface((width_base, height_base))
pygame.display.set_caption('Matias, Lucas, Gabriel')

class SpriteSheet: #IA
    def __init__(self, path):
        self.sheet = pygame.image.load(path)
    
    def get_color(self, x, y):
        return self.sheet.get_at((x, y))

    def get_sprite(self, x, y, width, height):
        rect = pygame.Rect(x, y, width, height)
        return self.sheet.subsurface(rect)

    def get_sprite_by_index(self, col, row, width, height):
        x = col * width
        y = row * height
        return self.get_sprite(x, y, width, height)

sprite_sheet = SpriteSheet('assetspokemon.png')
vermelho_transparente = sprite_sheet.get_color(215,28)

## sprites
sublinhado = sprite_sheet.get_sprite(187, 24, 264-187, 36-24)
barra_de_vida = sprite_sheet.get_sprite(22, 178, 91-22, 184-178)
caixa_de_texto = sprite_sheet.get_sprite(8, 104, 167-8, 151-104)

lista_sprites = [sublinhado, barra_de_vida, caixa_de_texto]
for sprite in lista_sprites:
    sprite.set_colorkey(vermelho_transparente)
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
    tela_base.fill((255, 255, 255))  # Preenche com a cor branca
    tela_base.blit(sublinhado, (4,3))
    tela_base.blit(barra_de_vida, (8,6))
    tela_base.blit(caixa_de_texto, (0, 112))

    # ----- Atualiza estado do jogo
    tela_escalada = pygame.transform.scale(tela_base, (WIDTH, HEIGHT))
    window.blit(tela_escalada, (0, 0))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
