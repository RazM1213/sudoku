import pygame
import requests

#Setting up pygame:
pygame.init()

WIDTH = 550
background_color = (251,247,245)
grid_original_element_color = (52,21,51)
buffer = 10

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Sudoku')
win.fill(background_color)
myfont = pygame.font.SysFont('comicsans', 35)
label = myfont.render('S U D O K U', True, (255, 0, 0))
win.blit(label, (208, 20))

#Sudoku generator api:
response = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

'''
[0,0,0,0,8,1,5,2,4],
[1,0,4,3,5,6,0,0,0],
[0,7,8,2,0,0,1,0,0],
[2,0,0,0,0,0,8,0,0],
[0,0,7,0,0,2,3,6,1],
[0,0,0,0,3,0,0,0,5],
[0,4,0,0,0,8,9,0,0],
[0,6,5,9,0,0,0,1,0],
[8,0,2,5,0,4,0,7,3]
'''

def insert(win,position):
    i,j = position[1], position[0]
    myfont = pygame.font.SysFont('comicsans', 35)

    while True:#The returns here serve as break in a loop - they take us out of the function!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == 48: #48 is ascii code for the number 0
                    grid[i-1][j-1] = 0
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - buffer, 50- buffer))
                    pygame.display.update()
                    return

                if (0 < event.key - 48 < 10):
                    pygame.draw.rect(win, background_color, (
                    position[0] * 50 + buffer , position[1] * 50 + buffer , 50 - buffer , 50 - buffer ))
                    value = myfont.render(str(event.key - 48), True, (255, 0, 0))
                    win.blit(value, (position[0] * 50 + 15, position[1] * 50 + 15))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return
def draw_grid():
    for i in range(0, 10):
        if (i % 3 == 0):
            # Every third line is bold
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

def fill_grid():
    # Filling the grid with values:
    # grid[0] is the value for board key in grid json
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, grid_original_element_color)
                win.blit(value, (50 * (j + 1) + 15, 50 * (i + 1) + 15))

    pygame.display.update()

def main():
    draw_grid()
    fill_grid()
    x = True
    while x:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                x = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))


if __name__ == '__main__':
    main()