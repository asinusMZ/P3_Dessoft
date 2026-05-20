import pygame

pygame.init()

sheet = pygame.image.load("assets/sgb_frames.png")

x = 272
y = 272
width = 256
height = 224

frame = sheet.subsurface((x, y, width, height)).copy()

pygame.image.save(frame, "assets/frame_blue_english.png")

pygame.quit()

print("sucesso")