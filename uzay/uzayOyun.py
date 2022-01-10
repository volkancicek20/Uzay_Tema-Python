import time
from tkinter import messagebox
import pygame
import sys
import random
from tkinter import *

pygame.init()

clock = pygame.time.Clock()

ekran = pygame.display.set_mode((800, 600))
bg = pygame.image.load("resimler/astroitoyun.jpg")
ekran.blit(bg, (0, 0))
asteroitt = pygame.image.load("resimler/asteroit.jpg")
gemiYukari = pygame.image.load("resimler/gemiYukari.png")
gemiAsagi = pygame.image.load("resimler/gemiAsagi.png")
gemiSag = pygame.image.load("resimler/gemiSag.png")
gemiSol = pygame.image.load("resimler/gemiSol.png")
gemiSolYukari = pygame.image.load("resimler/gemiSolYukari.png")
sari = (255, 255, 0)
mavi = (0, 0, 255)
kirmizi = (255, 0, 0)
beyaz = (255, 255, 255)
siyah = (0, 0, 0)

class Asteroit:
    def __init__(self):
        self.x = random.randint(250, 750)
        self.y = random.randint(50, 580)
        self.topla = False
    def draw(self):
        pygame.draw.circle(ekran, beyaz, (self.x, self.y), 5)

class Gemi:
    def __init__(self):
        self.x = 745
        self.y = 550
        self.ivme = 0.2
        self.puan = 0

    def draw(self):
        ekran.blit(gemiSolYukari, (self.x, self.y))


class Carpma:
    def __init__(self, x, en):
        self.x = x
        self.en = en
        self.text = ""

    def guncelle(self, skor):
        pass

g = Gemi()
para = []
puan = Carpma(10, 25)
for i in range(125):
    p = Asteroit()
    para.append(p)
def yenile():
    g.draw()
    for p in para:
        if p.topla == False:
            p.draw()
    puan.guncelle(g.puan)
    pygame.display.update()

calis = True
while calis:
    yenile()
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_UP] and g.y > 0 and g.x < 746:
        if g.y < 250 and g.x < 250:
            messagebox.showinfo("!!!!", "Görev Tamamlandı")
            pygame.quit()
        g.y -= g.ivme
    if tuslar[pygame.K_DOWN] and g.y < 580:
        if g.y < 250 and g.x < 250:
            messagebox.showinfo("!!!!", "Görev Tamamlandı")
            pygame.quit()
        g.y += g.ivme
    if tuslar[pygame.K_RIGHT] and g.x < 780:
        if g.y < 250 and g.x < 250:
            messagebox.showinfo("!!!!", "Görev Tamamlandı")
            pygame.quit()
        g.x += g.ivme
    if tuslar[pygame.K_LEFT] and g.x > 0 and g.y < 580:
        if g.y < 250 and g.x < 250:
            messagebox.showinfo("!!!!", "Görev Tamamlandı")
            pygame.quit()
        g.x -= g.ivme
    for p in para:
        if p.x >= g.x and p.x <= (g.x + 25) and p.y >= g.y and p.y <= (g.y + 25):
            messagebox.showinfo("!!!!", "Görev Başarısız")
            pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calis = False
            pygame.quit()
            break
