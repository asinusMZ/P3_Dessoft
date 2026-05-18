import pygame



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

sprite_sheet = SpriteSheet('assets/assetspokemon.png')
sprites_pokemons = SpriteSheet('assets/pokemons.png')
vermelho_transparente = sprite_sheet.get_color(215,28)
cinza_transparente = sprites_pokemons.get_color(411,123)

## sprites
sublinhado = sprite_sheet.get_sprite(187, 24, 264-187, 36-24)
barra_de_vida = sprite_sheet.get_sprite(22, 178, 91-22, 184-178)
caixa_de_texto = sprite_sheet.get_sprite(8, 104, 167-8, 151-104)
caixa_de_acoes = sprite_sheet.get_sprite(72,256,167-72,303-256)
setinha = sprite_sheet.get_sprite(47,415,55-47,424-415)
caixa_de_ataques = sprite_sheet.get_sprite(8, 376, 167-8, 455-376)

charmander = sprites_pokemons.get_sprite(424, 140, 455-424, 171-140)
pikachu = sprites_pokemons.get_sprite(522,378,561-522, 417-378)

lista_sprites = [sublinhado, barra_de_vida, caixa_de_texto, caixa_de_acoes, setinha, caixa_de_ataques]
lista_pokemons = [charmander, pikachu]




def desenha_tela(tela, fonte):
    tela.fill((245, 245, 245))  # Preenche com a cor branca

    texto = fonte.render("pika wants to fight", False, (0, 0, 0))
    tela.blit(charmander, (2, 70))
    tela.blit(pikachu, (100, 20))
    tela.blit(sublinhado, (8,10))
    tela.blit(pygame.transform.flip(sublinhado, True, False), (81,98))
    tela.blit(barra_de_vida, (11,13))
    tela.blit(barra_de_vida, (86,94))
    tela.blit(caixa_de_texto, (0, 112))
    tela.blit(texto, (5, 120))

def desenha_caixas(caixa, tela, fonte):
    texto = ''
    if caixa == 'acoes':
        tela.blit(caixa_de_acoes, (60, 100))
        texto = fonte.render("Fight", False, (0,0,0))
        tela.blit(texto, (74, 110))
        texto = fonte.render("Run", False, (0,0,0))
        tela.blit(texto, (74, 125))
    elif caixa == 'ataques':
        tela.blit(caixa_de_ataques, (0, 80))
        texto = fonte.render("Bola de fogo", False, (0,0,0))
        tela.blit(texto, (53, 117))
        texto = fonte.render("pau quentinho", False, (0,0,0))
        tela.blit(texto, (53, 127))
def desenha_seta(caixa, tela, selected):
    if caixa == 'acoes':
        if selected == 'fight':
            tela.blit(setinha, (67, 110))
        elif selected == 'run':
            tela.blit(setinha, (67, 125))