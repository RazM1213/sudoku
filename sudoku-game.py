import pygame
import requests

#Setting up pygame:
WIDTH = 550
background_color = (251,247,245)

#Sudoku generator api:
response = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption('Sudoku')
    win.fill(background_color)
    for i in range(0,10):
        if (i % 3 == 0):
            #Every third line is bold
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i,500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == '__main__':
    main()