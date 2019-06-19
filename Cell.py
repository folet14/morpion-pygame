import pygame


class Cell:
    def __init__(self, n_case, x_pos, y_pos, empty=True, team=0):
        self.n_case = n_case
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.empty = empty
        self.team = team

    def draw_cell(self, display, textures):
        if self.empty:
            display.blit(textures["empty"], self.x_pos, self.y_pos)
        else:
            if self.team == 1:
                display.blit(textures["cross"], self.x_pos, self.y_pos)
            elif self.team == 2:
                display.blit(textures["circle"], self.x_pos, self.y_pos)

    def update_cell(self, empty, team=0):
        self.empty = empty
        self.team = team
