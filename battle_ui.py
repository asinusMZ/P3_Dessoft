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

sprite_sheet = SpriteSheet('assetspokemon.png')
sprites_pokemons = SpriteSheet('pokemons.png')
vermelho_transparente = sprite_sheet.get_color(215,28)
cinza_transparente = sprites_pokemons.get_color(411,123)

## sprites
sublinhado = sprite_sheet.get_sprite(187, 24, 264-187, 36-24)
barra_de_vida = sprite_sheet.get_sprite(22, 178, 91-22, 184-178)
caixa_de_texto = sprite_sheet.get_sprite(8, 104, 167-8, 151-104)
caixa_de_acoes = sprite_sheet.get_sprite(72,256,167-72,303-256)

charmander = sprites_pokemons.get_sprite(424, 140, 455-424, 171-140)
pikachu = sprites_pokemons.get_sprite(522,378,561-522, 417-378)

lista_sprites = [sublinhado, barra_de_vida, caixa_de_texto, caixa_de_acoes]
lista_pokemons = [charmander, pikachu]
for sprite in lista_sprites:
    sprite.set_colorkey(vermelho_transparente)
for sprite in lista_pokemons:
    sprite.set_colorkey(cinza_transparente)


def desenha_tela(tela, fonte):
    tela.fill((255, 255, 255))  # Preenche com a cor branca


    texto = fonte.render("pica wants to fight", False, (0, 0, 0))
    tela.blit(charmander, (2, 70))
    tela.blit(pikachu, (100, 20))
    tela.blit(texto, (5, 120))
    tela.blit(sublinhado, (8,10))
    tela.blit(pygame.transform.flip(sublinhado, True, False), (81,98))
    tela.blit(barra_de_vida, (11,13))
    tela.blit(barra_de_vida, (86,94))
    tela.blit(caixa_de_texto, (0, 112))

def desenha_caixas(caixa, tela):
    if caixa == 'acoes':
        tela.blit(caixa_de_acoes, (60, 100))
