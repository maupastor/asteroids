import pygame
from constants import SCORE_CENTER_Y, SCORE_FONT_SIZE

class Score():

    def __init__(self):
        self.__score = 0

    def draw(self, screen):
        if pygame.font:
            font = pygame.font.Font(None, SCORE_FONT_SIZE)
            text = font.render(f"SCORE: {self.get_score()}", True, "white")
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=SCORE_CENTER_Y)
            screen.blit(text,textpos)

    def update_score(self, points):
        self.__score += points

    def get_score(self):
        return int(self.__score)

    