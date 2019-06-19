from Cell import *


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nb_case = height*width
        self.list_nb_case = [i for i in range(self.nb_case)]
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.create_list_case()

    def create_list_case(self):
        print(self.width, self.height)
        i = 0
        for w in range(self.width):
            for h in range(self.height):
                n_case = self.list_nb_case[i]
                self.grid[w][h] = Cell(n_case, w*100, h*100)
                i += 1

    def update_list_case(self, n_case, empty, team=0):
        for line in range(len(self.grid)):
            for case in range(len(self.grid[line])):
                if self.grid[line][case].n_case == n_case:
                    self.grid[line][case].update_cell(empty, team)
                    return

    def test_ho(self):
        if len(self.grid) > 3:
            win = 4
        else:
            win = 3
        adj = 0
        sign = 0
        for line in self.grid:
            for case in line:
                if case.team != sign:
                    adj = 1
                    sign = case.team
                else:
                    adj += 1
                if adj == win and sign != 0:
                    return sign
        return 0

    def test_ver(self):
        if len(self.grid) > 3:
            win = 4
        else:
            win = 3
        adj = 0
        sign = 0
        for column in range(len(self.grid[0])):
            for case in range(len(self.grid)):
                if self.grid[case][column] != sign:
                    adj = 1
                    sign = self.grid[case][column].team
                else:
                    adj += 1
                if adj == win and sign != 0:
                    return sign
        return 0

    def test_d1(self):
        if len(self.grid) > 3:
            win = 4
        else:
            win = 3
        adj = 0
        for n in range(-len(self.grid), len(self.grid)):
            sign = 0
            for i in range(len(self.grid)):
                for j in range(len(self.grid)):
                    if i-j == n:
                        if self.grid[j][i] != sign:
                            adj = 1
                            sign = self.grid[j][i]
                        else:
                            adj += 1
                        if adj == win and sign != 0:
                            return sign
        return 0

    def test_d2(self):
        if len(self.grid) > 3:
            win = 4
        else:
            win = 3
        adj = 0
        for n in range(2*len(self.grid)):
            sign = 0
            for i in range(len(self.grid)):
                for j in range(len(self.grid)):
                    if i+j == n:
                        if self.grid[j][i] != sign:
                            adj = 1
                            sign = self.grid[j][i]
                        else:
                            adj += 1
                        if adj == win and sign != 0:
                            return sign
        return 0

    def win(self):
        sign_ho = self.test_ho()
        sign_ver = self.test_ver()
        sign_d1 = self.test_d1()
        sign_d2 = self.test_d2()
        return sign_ho, sign_ver, sign_d1, sign_d2

    def is_a_win(self):
        a, b, c, d = self.win()
        if a != 0 or b != 0 or c != 0 or d != 0:
            return True


    def pos_to_index(self, x_pos, y_pos):
        pass

    def draw_grid(self, display, textures):
        for i in self.grid:
            for j in i:
                j.draw_cell(display, textures)
