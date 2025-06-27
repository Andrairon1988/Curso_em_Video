import pygame
pygame.init() # Inicia o módulo.
pygame.mixer.music.load('ex0021.mp3') # Carrega o audio para o projeto.
pygame.mixer.music.play() # Toca o audio.
pygame.event.wait() # Espera até o final do evento.