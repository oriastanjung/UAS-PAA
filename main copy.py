from asyncio.windows_events import NULL
import time
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


# VARIABLE CONSTANT POSISI COURIER DARI SUDUT PANDANG 2D
UTARA = 1
SELATAN = -1
TIMUR = 2
BARAT = -2

# VARIABLE CEK SISI COURIER 
DEPAN_COURIER = 1
KIRI_COURIER = 2
KANAN_COURIER = 3
BELAKANG_COURIER = 4

class Courier : 
    def __init__(self, x, y):
        self.posisiX = x
        self.posisiY = y
        self.Arah_Kepala_Courier = UTARA # KARENA GAMBAR ARAH AWAL PANAH KE ATAS JADI ARAH UTARA
        self.Kurir_PICTURE = pygame.image.load('courier.png')

    def check_arah_kepala(self) :
        return self.Arah_Kepala_Courier
    def check_posisi_baris(self) :
        return self.posisiY
    def check_posisi_kolom(self) :
        return self.posisiX

    def majukan_courier(self):
        if (self.Arah_Kepala_Courier == UTARA):
            self.posisiY -= 1
        elif(self.Arah_Kepala_Courier == SELATAN):
            self.posisiY += 1
        elif(self.Arah_Kepala_Courier == BARAT):
            self.posisiX -= 1
        elif(self.Arah_Kepala_Courier == TIMUR):
            self.posisiX += 1

    def putar_kanan(self):
        if (self.Arah_Kepala_Courier == UTARA):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Kepala_Courier = TIMUR
        elif(self.Arah_Kepala_Courier == TIMUR):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Kepala_Courier = SELATAN
        elif(self.Arah_Kepala_Courier == SELATAN):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Kepala_Courier = BARAT
        elif(self.Arah_Kepala_Courier == BARAT):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Kepala_Courier = UTARA
            
    def putar_kiri(self):
        if (self.Arah_Kepala_Courier == UTARA):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Kepala_Courier = TIMUR
        elif(self.Arah_Kepala_Courier == TIMUR):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Kepala_Courier = SELATAN
        elif(self.Arah_Kepala_Courier == SELATAN):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Kepala_Courier = BARAT
        elif(self.Arah_Kepala_Courier == BARAT):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Kepala_Courier = UTARA

    def cek_tempat_kosong(self,arah_cek,x,y):
        
        if (self.Arah_Kepala_Courier == UTARA):
            if (arah_cek == DEPAN_COURIER):
                if (grid[x][y-1].wall != True ):
                    return True
            if (arah_cek == KANAN_COURIER):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == BELAKANG_COURIER):
                if (grid[x][y+1].wall != True ):
                    return True
            if (arah_cek == KIRI_COURIER):
                if (grid[x-1][y].wall != True ):
                    return True
        
        if (self.Arah_Kepala_Courier == TIMUR):
            if (arah_cek == DEPAN_COURIER):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == KANAN_COURIER):
                if (grid[x][y+1].wall != True ):
                    return True
            if (arah_cek == BELAKANG_COURIER):
                if (grid[x-1][y].wall != True ):
                    return True
            if (arah_cek == KIRI_COURIER):
                if (grid[x][y-1].wall != True ):
                    return True
        
        if (self.Arah_Kepala_Courier == SELATAN):
            if (arah_cek == DEPAN_COURIER):
                if (grid[x][y+1].wall != True ):
                    return True
            if (arah_cek == KANAN_COURIER):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == BELAKANG_COURIER):
                if (grid[x][y-1].wall != True ):
                    return True
            if (arah_cek == KIRI_COURIER):
                if (grid[x-1][y].wall != True ):
                    return True
        
        if (self.Arah_Kepala_Courier == BARAT):
            if (arah_cek == DEPAN_COURIER):
                if (grid[x-1][y].wall != True ):
                    return True
            if (arah_cek == KANAN_COURIER):
                if (grid[x][y-1].wall != True ):
                    return True
            if (arah_cek == BELAKANG_COURIER):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == KIRI_COURIER):
                if (grid[x][y+1].wall != True ):
                    return True

        
    # def gambar_courier(self, xInput,yInput):
    #     self.posisiX = xInput
    #     self.posisiY = yInput
    #     window.blit(self.Kurir_PICTURE, (xInput * window_width // columns, yInput * window_height // rows))
    def gambar_courier(self):
        window.blit(self.Kurir_PICTURE, (self.posisiX * window_width // columns, self.posisiY * window_height // rows))


def main():
    begin_search = False
    posisiStartX = 0
    posisiStartY = 0

    posisi_finis_kolom= 0
    posisi_finis_baris = 0

#Membuat random wall
    for i in range(25) :
        wall_box_x = random.randint(0, columns - 1)
        wall_box_y = random.randint(0, rows - 1)
        wall_box = grid[wall_box_y][wall_box_x]
        wall_box.wall = True
      
# membuat wall di sisi2
    for i in range(columns-1):
        wall_sisi_y = 0
        wall_sisi_x = i
        wall_sisi = grid[wall_sisi_x][wall_sisi_y]
        wall_sisi.wall = True
    for i in range(columns-1):
        wall_sisi_y = rows-1
        wall_sisi_x = i
        wall_sisi = grid[wall_sisi_x][wall_sisi_y]
        wall_sisi.wall = True
    for i in range (rows-1):
        wall_sisi_y = i
        if (i == 0):
            wall_sisi_x = 0
        wall_sisi = grid[wall_sisi_x][wall_sisi_y]
        wall_sisi.wall = True

    for i in range (rows):
        wall_sisi_y = i
        wall_sisi_x = columns-1
        wall_sisi = grid[wall_sisi_x][wall_sisi_y]
        wall_sisi.wall = True



 #Membuat posisi Start Courier
    for i in range(columns * rows):
        kurir_box_x = random.randint(0, columns - 1)
        kurir_box_y = random.randint(0, rows - 1)
        kurir_box = grid[kurir_box_y][kurir_box_x]
        if (grid[kurir_box_x][kurir_box_y].wall == False): 
            kurir_box.start = True
            kurirUtama = Courier(kurir_box_x, kurir_box_y)
            break
    
    
#Membuat Target Finish
    target_box_x = random.randint(0, columns - 1)
    target_box_y = random.randint(0, rows - 1)
    target_box = grid[target_box_x][target_box_y]
    target_box.target = True
    target_box_set = True
    target = pygame.image.load('flag.png')
    posisi_finis_kolom = target_box_x
    posisi_finis_baris = target_box_y
    pencarian = 0
    # MAIN PROGRAM ADA DI BAWAH INI
    start = 0
    while True:
        posisiBarisCourier = kurirUtama.check_posisi_baris()
        posisiKolomCourier = kurirUtama.check_posisi_kolom()

        for event in pygame.event.get():
            #Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
                # if box.start:
                #     # window.blit(kurir, (i * window_width // columns, j * window_height // rows))
                if box.target:
                    box.draw(window, (90, 90, 90))
                    window.blit(target, (i * window_width // columns, j * window_height // rows))
        
        ###### CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######
        if(start == 0):
            if (grid[kurir_box_y][kurir_box_x].start == True):
                    window.blit(kurirUtama.Kurir_PICTURE, (posisiKolomCourier * window_width // columns, posisiBarisCourier * window_height // rows))
        else :
            if (grid[kurir_box_y][kurir_box_x].start == True):
                grid[posisiStartY][posisiStartX].draw(window, (20,20,20))
        ###### END CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######

        















        if (begin_search) :
            # all main searching function start here
            # kurirUtama.gambar_courier(posisiKolomCourier, posisiBarisCourier)
            
            kurirUtama.gambar_courier()

            test = 1


                        ###### START CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######
            if(start == 0):
                start = 1
            
            if (start == 1):
                posisiStartX = posisiKolomCourier
                posisiStartY = posisiBarisCourier
                start = 2

                        ###### END CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######
        
            # if (test == 1):
            #     print("arah kepala = ")
            #     print(kurirUtama.check_arah_kepala())
            #     print("posisi baris (Y) = ")
            #     print(posisiBarisCourier)
            #     print("posisi kolom (X) = ")
            #     print(posisiKolomCourier)
            #     test = 2
            # if (test == 2):
            #     # CARA BUAT ANIMATION
            #     # posisiBarisCourier += 1
            #     posisiKolomCourier += 1
            #     print("AFTER arah kepala = ")
            #     print(kurirUtama.check_arah_kepala())
            #     print("AFTER posisi baris (Y) = ")
            #     print(posisiBarisCourier)
            #     print("AFTER posisi kolom (X) = ")
            #     print(posisiKolomCourier)
            #     time.sleep(1)

            #kurirUtama.majukan_courier()
            #kurirUtama.putar_kanan()
            #kurirUtama.putar_kiri()
          
            # if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER,posisiKolomCourier,posisiBarisCourier)):
            #     print("depan_kosong")
            # if (kurirUtama.cek_tempat_kosong(KANAN_COURIER,posisiKolomCourier,posisiBarisCourier)):
            #     print("kanan_kosong")
            # if (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER,posisiKolomCourier,posisiBarisCourier)):
            #     print("belakang_kosong")
            # if (kurirUtama.cek_tempat_kosong(KIRI_COURIER,posisiKolomCourier,posisiBarisCourier)):
            #     print("kiri_kosong")
            # print("\n")
            #kurirUtama.putar_kanan()
            
            print("running")
            # posisi sampai di bendera
            if (posisiBarisCourier == posisi_finis_baris and posisiKolomCourier == posisi_finis_kolom):
                target_box_x = random.randint(0, columns - 1)
                target_box_y = random.randint(0, rows - 1)
                target_box = grid[target_box_x][target_box_y]
                target_box.target = True
                target_box_set = True
                target = pygame.image.load('flag.png')
                posisi_finis_kolom = target_box_x
                posisi_finis_baris = target_box_y
                
                pencarian = pencarian + 1
            # posisi kurir di bawah dan kanan bendera
            if (posisiBarisCourier > posisi_finis_baris and posisiKolomCourier > posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == BARAT):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    else:
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                        kurirUtama.putar_kiri()
                    
                
            
            
            elif (posisiBarisCourier > posisi_finis_baris and posisiKolomCourier < posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    else:
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == BARAT): 
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
            
            if (posisiBarisCourier < posisi_finis_baris and posisiKolomCourier  > posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == BARAT):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER ,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
            
            elif (posisiBarisCourier < posisi_finis_baris and posisiKolomCourier < posisi_finis_kolom): 
                if (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == BARAT):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
            
            if (posisiBarisCourier < posisi_finis_baris and posisiKolomCourier == posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == BARAT):
                    if (kurirUtama.cek_tempat_kosong(KIRI_COURIER,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    else:
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
            
            elif (posisiBarisCourier > posisi_finis_baris and posisiKolomCourier == posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == BARAT):
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER,posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
            
            if (posisiBarisCourier == posisi_finis_baris and posisiKolomCourier > posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == BARAT):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    else:
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
            
            elif (posisiBarisCourier == posisi_finis_baris and posisiKolomCourier < posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == UTARA):
                    if (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == SELATAN):
                    if (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == BARAT):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == TIMUR):
                    if (kurirUtama.cek_tempat_kosong(DEPAN_COURIER , posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif (kurirUtama.cek_tempat_kosong(KANAN_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(BELAKANG_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                        kurirUtama.putar_kanan()
                    
                    elif (kurirUtama.cek_tempat_kosong(KIRI_COURIER, posisiKolomCourier,posisiBarisCourier)):
                        kurirUtama.putar_kiri()

            if(pencarian == 2):
                
                window.blit(target, (target_box_x * window_width // columns, target_box_y * window_height // rows))
                print("selesai")
                return False
            
            time.sleep(1)

    
                
        pygame.display.flip()


main()