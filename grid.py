from tkinter import messagebox, Tk
from turtle import window_width
import pygame
import sys
import random

window_width = 500
window_height = 500

window = pygame.display.set_mode((window_width,window_height))

columns = 10
rows = 10

box_width = window_width // columns
box_height = window_height // rows

grid = []

class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 2, box_height - 2))

# Create Grid
for i in range(columns):
    arr =[]
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)



def main():
    begin_search = False
    target_box_set = False

#Membuat random wall
    for i in range(25) :
        wall_box_x = random.randint(0, columns - 1)
        wall_box_y = random.randint(0, rows - 1)
        wall_box = grid[wall_box_y][wall_box_x]
        wall_box.wall = True
 
 #Membuat posisi Start Courier
    for i in range(columns * rows):
        kurir_box_x = random.randint(0, columns - 1)
        kurir_box_y = random.randint(0, rows - 1)
        if (kurir_box_x != wall_box_x and kurir_box_y != wall_box_y): 
            kurir_box = grid[kurir_box_y][kurir_box_x]
            kurir_box.start = True
            kurir = pygame.image.load('courier.png')
            break
    

#Membuat Target Finish
    target_box_x = random.randint(0, columns - 1)
    target_box_y = random.randint(0, rows - 1)
    target_box = grid[target_box_y][target_box_x]
    target_box.target = True
    target = pygame.image.load('flag.png')
    
    # MAIN PROGRAM ADA DI BAWAH INI

    while True:
        for event in pygame.event.get():
            #Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse Controls
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                

                #Set Target
                if event.buttons[2] and not target_box_set:
                    i = x // box_width
                    j = y // box_height
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True

            #Start Algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True


        window.fill ((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (20,20,20))
                if box.wall:
                    box.draw(window, (90, 90, 90))
                if box.start:
                    window.blit(kurir, (i * window_width // columns, j * window_height // rows))
                if box.target:
                    box.draw(window, (90, 90, 90))
                    window.blit(target, (i * window_width // columns, j * window_height // rows))
        pygame.display.flip()


main()