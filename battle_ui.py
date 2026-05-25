import pygame
from pokemon import *
from models import *
import models

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
hp_player = sprite_sheet.get_sprite(104,235, 1, 236-235)
barra_de_vida = sprite_sheet.get_sprite(22, 178, 91-22, 184-178)
caixa_de_texto = sprite_sheet.get_sprite(8, 104, 167-8, 151-104)
caixa_de_acoes = sprite_sheet.get_sprite(72,256,167-72,303-256)
setinha = sprite_sheet.get_sprite(344,72,351-344,79-71)
caixa_de_ataques = sprite_sheet.get_sprite(8, 376, 167-8, 455-376)




def get_enemy_surface():
    coords = get_enemy_sprite(models.enemy)
    if coords:
        ex, ey, ew, eh = coords
        return sprites_pokemons.get_sprite(ex, ey, ew, eh)
    return None

charmander = sprites_pokemons.get_sprite(424, 140, 455-424, 171-140)


lista_sprites = [sublinhado, barra_de_vida, caixa_de_texto, caixa_de_acoes, setinha, caixa_de_ataques, hp_player]
lista_pokemons = [charmander]


for poke in dicionario_ataques:
    if poke["name"] == player.name:
        hp_max_player = poke["hp"]

for poke in dicionario_ataques:
    if poke["name"] == enemy.name:
        hp_max_enemy = poke["hp"]
        



ataques = player.moves
def desenha_tela(tela):
    enemy_sprite = get_enemy_surface() 
    hp_max_enemy = next(p['hp'] for p in dicionario_ataques if p['name'] == models.enemy.name) # loop ate achar o hp do enemy
    
    tela.fill((245, 245, 245))
    #calcula barra de vida
    largura_hp_player = player.vida / hp_max_player * (87-39) 
    largura_hp_enemy = models.enemy.vida / hp_max_enemy * (87-39)

    hp_player_barra = pygame.transform.scale(
        hp_player,
        (int(largura_hp_player), 2)
    )

    hp_enemy_barra = pygame.transform.scale(
        hp_player,
        (int(largura_hp_enemy), 2)
)
    #coloca tudo na tela
    tela.blit(charmander, (7, 85))
    tela.blit(enemy_sprite, (100, 20))
    tela.blit(sublinhado, (8,10))
    tela.blit(pygame.transform.flip(sublinhado, True, False), (81,98))
    tela.blit(barra_de_vida, (11,13))
    tela.blit(barra_de_vida, (86,94))
    tela.blit(hp_enemy_barra, (29,14))
    tela.blit(caixa_de_texto, (0, 112))
    tela.blit(hp_player_barra, (104,95))
    

def desenha_mensagem(tela, fonte, texto): # desenha a mensagem da batalha
    texto = fonte.render(texto, False, (0,0,0))
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


        texto = fonte.render(ataques[0].name, False, (0,0,0))
        tela.blit(texto, (53, 117))
        texto = fonte.render(ataques[1].name, False, (0,0,0))
        tela.blit(texto, (53, 127))
def desenha_seta(caixa, tela, selected, fonte):
    if caixa == 'acoes':
        if selected == 'fight':
            tela.blit(setinha, (67, 110))
        elif selected == 'run':
            tela.blit(setinha, (67, 125))
    elif caixa == 'ataques':
        if selected == 0:
            tela.blit(setinha, (45, 117))
            texto = fonte.render(f"Type: {ataques[selected].move_type}", False, (0,0,0))
            tela.blit(texto, (8,90))
            texto = fonte.render(f" {ataques[selected].current_pp} / {ataques[selected].pp}", False, (0,0,0))
            tela.blit(texto, (8,100))
        elif selected == 1:
            tela.blit(setinha, (45, 127))
            texto = fonte.render(f"Type: {ataques[selected].move_type}", False, (0,0,0))
            tela.blit(texto, (8,90))
            texto = fonte.render(f" {ataques[selected].current_pp} / {ataques[selected].pp}", False, (0,0,0))
            tela.blit(texto, (8,100))

