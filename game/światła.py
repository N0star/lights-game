# ŚWIATŁA # FDC # 0.2.1 ###

import random, time, os, sys, pygame
RX = 16
RY = 16

blank='█'
LIFE = 1
GAME = 1

LDB=[{(7,7)},{(6,7),(8,7)},{(6,7),(7,7),(8,7)},{(6,6),(6,7),(7,7),(8,7),(8,8)},
     #I,II,III,S #H,Q,A,T
     {(6,6),(6,7),(7,7),(8,7),(8,8),(9,7),(8,6),(5,7),(6,8),(10,7)},
     {(7,7),(7,8),(8,7),(8,8),(8,9),(9,8)},
     {(8,6),(9,6),(10,6),(8,8),(9,8),(10,8),(7,7),(7,8),(7,6),(9,7)},
     {(5,5),(6,5),(7,5),(8,5),(6,6),(7,6),(6,7),(7,7),(6,8),(7,8)},
     #
     {(8,6),(9,6),(10,6),(8,8),(9,8),(10,8),(8,7),(7,8),(6,5),(7,5),(8,5),
     (9,5),(10,5),(6,9),(7,9),(8,9),(9,9),(10,9),(10,6),(10,8),(10,7)},
     #
     {(5,5),(6,5),(7,5),(8,5),(5,6),(7,6),(8,6),(5,7),(6,7),(7,7),(8,7),
      (5,8),(6,8),(8,8),(9,8),(5,9),(6,9),(7,9),(5,10),(6,10),(5,11),(4,5)},
     #
     {(5,5),(6,5),(7,5),(8,5),(9,5),(5,6),(7,6),(9,6),(5,7),(6,7),(7,7),
      (8,7),(9,7),(5,8),(7,8),(9,8),(5,9),(6,9),(7,9),(8,9),(9,9)},
     #
     {(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(3,5),(4,5),(5,5),(6,5),
      (7,5),(8,5),(9,5),(10,5),(3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),
      (3,6),(10,6),(3,7),(10,7),(3,8),(10,8),(4,3)},
     #
     {(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(3,5),(4,5),(5,5),(6,5),
      (7,5),(8,5),(9,5),(10,5),(3,10),(4,10),(5,10),(6,10),(7,10),
      (8,10),(9,10),(10,10),(3,6),(10,6),(3,7),(10,7),(3,8),(10,8),
      (3,9),(10,9),(5,7),(6,7),(7,7),(8,7),(9,7),(11,7),(12,7),
      (12,8),(12,9),(12,10),(12,11),(12,12),(11,12),(10,12),(9,12),(8,12),
      (7,12),(6,12),(5,12),(5,11),(5,9),(5,8)},
     #
     {(2,2),(3,2),(4,2),(5,2),(8,2),(9,2),(10,2),(11,2),(13,2),(14,2),
      (1,3),(2,3),(3,3),(5,3),(6,3),(8,3),(9,3),(11,3),(13,3),(14,3),
      (2,4),(3,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(12,4),(13,4),
      (6,5),(5,5),(7,5),(8,5),(10,5),(11,5),(12,5),(13,5),(14,5),
      (6,6),(7,6),(8,6),(9,6),(12,6),(13,6),(14,6),
      (2,7),(3,7),(4,7),(5,7),(13,7),(14,7),(15,7),
      (3,8),(4,8),(5,6),(14,8),
      (3,9),(4,9),(14,9)},
     #
     {(2,2),(3,2),(4,2),(5,2),(8,2),(9,2),(10,2),(11,2),(13,2),(14,2),
      (2,3),(3,3),(5,3),(6,3),(8,3),(9,3),(11,3),(13,3),(14,3),
      (2,4),(3,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(12,4),(13,4),
      (6,5),(5,5),(7,5),(8,5),(10,5),(11,5),(12,5),(13,5),(14,5),
      (6,6),(7,6),(8,6),(9,6),(12,6),(13,6),(14,6),
      (3,7),(4,7),(5,7),(13,7),(14,7),(15,7),
      (3,8),(4,8),(5,6),(14,8),(4,4),
      (3,9),(4,9),(14,9),(5,9),(6,9),(7,9),(8,9),(9,9),(12,9),(13,9),
      (7,10),(8,10),(9,10),(12,10),(13,10),
      (6,11),(7,11),(8,11),(9,11),(10,11),(13,11),
      (4,12),(5,12),(6,12),(7,12),(9,12),(10,12),(12,12),(13,12),(14,12),
      (7,13),(13,13),(14,13),(12,14),(13,14),(5,1),(13,1),(15,9),(4,11)}
     ]

DLDB=[{(8,6),(9,6),(10,6),(8,8),(9,8),(10,8),(7,7),(7,8),(7,6),(9,7)}]

pygame.init()
ROZMIAR = 800,600
pygame.display.set_caption("Światła")
ekran = pygame.display.set_mode(ROZMIAR)
zegar = pygame.time.Clock()
biały = pygame.color.THECOLORS['white']
czerwony = pygame.color.THECOLORS['red']
czarny = pygame.color.THECOLORS['black']
złoty = pygame.color.THECOLORS['gold']
myfont = pygame.font.SysFont("monospace", 27)

#pygame.key.set_repeat(1,0)

tło = "tlo.jpg"
cel =  "cel.png"
wla = "zapal.png"
wyl = "zgas.png" #wyl = "zgasz.png"
brak = "brak.png"
blok = "blok.png"
siat = 32 #siatka
borx = 32 #ramka x (od lewej)
bory = 64 #ramka y (od góry)
vol = 0.8


class Gracz(pygame.sprite.Sprite): #player
    def __init__(self,xy=(borx+siat*7+siat/2,bory+siat*7+siat/2)):
        super().__init__()
        self.image = pygame.image.load(cel)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = xy

    def przesuń(self,kier=0): #navigation
      krok = pygame.mixer.Sound('step.wav')
      if   kier==0 or kier=='drzewo': pass
      elif (kier==1 or kier=='lewo'):
        self.rect.x -= siat; krok.play()
      elif (kier==2 or kier=='prawo'):
        self.rect.x += siat; krok.play()
      elif (kier==3 or kier=='góra'):
        self.rect.y -= siat; krok.play()
      elif (kier==4 or kier=='dół'):
        self.rect.y += siat; krok.play()
      else: pass


class Światło(pygame.sprite.Sprite): #light
  def __init__(self):
    super().__init__()
    self.image=pygame.image.load(brak)
    self.rect = self.image.get_rect()

class Blok(pygame.sprite.Sprite): #field
  def __init__(self):
    super().__init__()
    self.image=pygame.image.load(blok)
    self.rect = self.image.get_rect()


class Plansza(): #gameboard
  def __init__(self,x=RX,y=RY):
    self.x = x
    self.y = y
    self.tablica = []
    self.lampy = []
    self.lista_lamp = pygame.sprite.Group()

  def stworz(self): #tworzenie nowej planszy
    for _ in range(self.y):
        wiersz = []
        for _ in range(self.x):
            wiersz.append(blank)
        self.tablica.append(wiersz)

  def wypełnij(self,level):
    for i,elem in enumerate(LDB[level]):
      x=elem[1]
      y=elem[0]
      self.tablica[x][y]=0

    lw=0; lk=0;
    for wiersz in self.tablica:
        for indeks, element in enumerate(wiersz):
            i = lw*RX+indeks
            ś = Światło()
            self.lampy.append(ś)
            self.lista_lamp.add(ś)
            ś.rect.centerx = borx+indeks*siat
            ś.rect.centery = bory+lw*siat
        lw+=1

  def wypełnij2(self,level):
    for i,elem in enumerate(DLDB[level]):
      x=elem[1]
      y=elem[0]
      self.tablica[x][y]=0

    lw=0; lk=0;
    for wiersz in self.tablica:
        for indeks, element in enumerate(wiersz):
            i = lw*RX+indeks
            ś = Światło()
            self.lampy.append(ś)
            self.lista_lamp.add(ś)
            ś.rect.centerx = borx+indeks*siat
            ś.rect.centery = bory+lw*siat
        lw+=1

  def wypisz(self): #wyświetalnie plansz
    lw=0; lk=0
    for wiersz in self.tablica:
        if lk<len(wiersz):
         for i in range(len(wiersz)):
          print("|{}".format(lk%10), end='')
          lk+=1
         print("|~")
         for i in range(len(wiersz)):
          print("--", end='')
         print("---")
        for indeks, element in enumerate(wiersz):
            if indeks == 0:
                print('|{}|'.format(element), end = '')
            else:
                print('{}|'.format(element), end = '')
        print('~{}'.format(lw))
        lw+=1

  def maluj(self): #wyświetlanie plansz (graficzne)

    lw=0; lk=0;
    for wiersz in self.tablica:
        for indeks, element in enumerate(wiersz):
          i = lw*RX+indeks
          if element == 1:
            self.lampy[i].image=pygame.image.load(wla)
          elif element==0:
            self.lampy[i].image=pygame.image.load(wyl)
          else:
            self.lampy[i].image=pygame.image.load(brak)
        lw+=1

    self.lista_lamp.draw(ekran)

  def zaznacz(self,xy): #zanzaczanie obszarów do interakcji
    action = pygame.mixer.Sound('fire.wav')
    action.play()

    x=xy[0]
    y=xy[1]
    współrzędne = []

    współrzędne += [xy]
    współrzędne +=[(x+1,y)]
    współrzędne +=[(x-1,y)]
    współrzędne +=[(x,y+1)]
    współrzędne +=[(x,y-1)]
    #print(współrzędne)

    if self.tablica[xy[0]][xy[1]]!=blank:
     for i,elem in enumerate(współrzędne):
      x=elem[0]
      y=elem[1]
      if (0 <= x < RX) and (0 <= y < RY):
        self.odmień(elem)
    #self.wypisz()


  def odmień(self,xy): #zmiana wybranych obszarów
    x=xy[0]
    y=xy[1]

    if self.tablica[x][y]==1:
      self.tablica[x][y]=0
    elif self.tablica[x][y]==0:
      self.tablica[x][y]=1
    else: pass

  def sprawdź(self): #sprawdzanie warunków zwycięstwa
    warunek = 1
    for wiersz in self.tablica:
         for i,elem in enumerate(wiersz):
             if elem==0: warunek = 0
    return warunek-1

  def sprawdź2(self): #sprawdzanie warunków zwycięstwa dla II gracza
    warunek = 1
    for wiersz in self.tablica:
         for i,elem in enumerate(wiersz):
             if elem==1: warunek = 0
    return warunek-1

  def losowe_znaczenia(self,licznik):
    while licznik:
        x=random.choice(range(0,self.x))
        y=random.choice(range(0,self.y))
        if self.tablica[x][y]==0 or self.tablica[x][y]==0:
             self.zaznacz((x,y))
             licznik+=-1



class Cel():
  def __init__(self,x=RX,y=RY):
    self.x = int(x/2)
    self.y = int(y/2)
    self.grafika = Gracz()

  def __repr__(self):
    return 'Cel({},{})'.format(self.x,self.y)
  def __str__(self):
    return 'Cel na X:{} i Y:{}.'.format(self.x,self.y)

  def przesuń(self,kier): #przesuwanie celownika
    if   kier==0 or kier=='drzewo': pass
    elif (kier==1 or kier=='lewo') and self.x > 0:
      self.x-=1; self.grafika.przesuń(kier)
    elif (kier==2 or kier=='prawo') and self.x < RX-1:
      self.x+=1; self.grafika.przesuń(kier)
    elif (kier==3 or kier=='góra') and self.y > 0:
      self.y-=1; self.grafika.przesuń(kier)
    elif (kier==4 or kier=='dół') and self.y < RY-1:
      self.y+=1; self.grafika.przesuń(kier)
    else: pass


  def pobierz(self):
    namiary = [-1,-1]
    namiary[1]=self.x
    namiary[0]=self.y
    return namiary

  def maluj(self):
    GG = pygame.sprite.Group()
    GG.add(self.grafika)
    GG.draw(ekran)

class Komunikat():
    def __init__(self,xy=(borx+siat*7,bory+siat*7)):
        self.x = xy[0]
        self.y = xy[1]

    def tło(self):
        wyświetlanie = pygame.sprite.Group()
        grafika = Bgi()
        grafika.rect.centerx = 400
        grafika.rect.centery = 300
        wyświetlanie.add(grafika)
        wyświetlanie.draw(ekran)

    def domyślne(self):
        wyświetlanie = pygame.sprite.Group()
        grafika = Titel()
        grafika.rect.centerx = 400
        grafika.rect.centery = 25
        wyświetlanie.add(grafika)
        wyświetlanie.draw(ekran)
        grafika = Border()
        grafika.rect.centerx = 700
        grafika.rect.centery = 325
        wyświetlanie.add(grafika)
        grafika = Bottom()
        grafika.rect.centerx = 300
        grafika.rect.centery = 590
        wyświetlanie.add(grafika)
        wyświetlanie.draw(ekran)

    def menu(self):
        wyświetlanie = pygame.sprite.Group()
        grafika = Mtitel()
        grafika.rect.centerx = 295
        grafika.rect.centery = 75
        wyświetlanie.add(grafika)
        grafika = Blok()
        grafika.rect.centerx = 300
        grafika.rect.centery = 300
        wyświetlanie.add(grafika)
        grafika = Blok()
        grafika.rect.centerx = 300
        grafika.rect.centery = 375
        wyświetlanie.add(grafika)
        grafika = Blok()
        grafika.rect.centerx = 300
        grafika.rect.centery = 450
        wyświetlanie.add(grafika)
        wyświetlanie.draw(ekran)

    def pauza(self):
        s = pygame.Surface((ROZMIAR),pygame.SRCALPHA) 
        s.fill((128,128,55,155))                       
        ekran.blit(s, (0,0))
        
        wyświetlanie = pygame.sprite.Group()
        grafika = Pause()
        grafika.rect.centerx = self.x
        grafika.rect.centery = self.y
        wyświetlanie.add(grafika)
        wyświetlanie.draw(ekran)
    def porażka(self):
        wyświetlanie = pygame.sprite.Group()
        grafika = Defeat()
        grafika.rect.centerx = self.x
        grafika.rect.centery = self.y
        wyświetlanie.add(grafika)
        wyświetlanie.draw(ekran)
    def zwycięstwo(self):
        wyświetlanie = pygame.sprite.Group()
        grafika = Victory()
        grafika.rect.centerx = self.x
        grafika.rect.centery = self.y
        wyświetlanie.add(grafika)
        wyświetlanie.draw(ekran)

class Pause(pygame.sprite.Sprite): #imageClasses
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load("pauza.png")
  self.rect = self.image.get_rect()
class Victory(pygame.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load("zwyciestwo.png")
  self.rect = self.image.get_rect()
class Defeat(pygame.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load("porazka.png")
  self.rect = self.image.get_rect()
class Bgi(pygame.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load(tło)
  self.rect = self.image.get_rect()
class Border(pygame.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load("ramka.png")
  self.rect = self.image.get_rect()
class Bottom(pygame.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load("spod.png")
  self.rect = self.image.get_rect()
class Titel(pygame.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load("tytul.png")
  self.rect = self.image.get_rect()
class Mtitel(pygame.sprite.Sprite):
 def __init__(self):
  super().__init__()
  self.image=pygame.image.load("maintitel.png")
  self.rect = self.image.get_rect()

###   ~~MENU~~

k=Komunikat()
Du = 0
pygame.mixer.music.load('DRBR.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(vol)

while GAME:
    ekran.fill(biały)
    k.tło()
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            GAME = False


        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            mos_x, mos_y = pygame.mouse.get_pos()
            #KLIKNIĘCIE NA ROZPOCZNIJ
            if mos_x > 300-100 and mos_x <300+100:
                if mos_y > 300-25 and mos_y <300+25:
                    GAME=0
                    effect = pygame.mixer.Sound('clik.wav')
                    effect.play()
            #KLIKNIĘCIE NA DUEL
            if mos_x > 300-100 and mos_x <300+100:
                if mos_y > 375-25 and mos_y <375+25:
                    GAME=0; LIFE=0; Du=1
                    effect = pygame.mixer.Sound('clik.wav')
                    effect.play()
            #KLIKNIĘCIE NA WYJŚCIE
            if mos_x > 300-100 and mos_x <300+100:
                if mos_y > 450-25 and mos_y <450+25:
                    GAME=0; LIFE=0
                    effect = pygame.mixer.Sound('clik.wav')
                    effect.play()
                    time.sleep(1)

    k.domyślne()
    k.menu()
    label = myfont.render("Rozpocznij!", 5, biały)
    ekran.blit(label, (210, 288))
    label = myfont.render("Duel!", 5, biały)
    ekran.blit(label, (225, 363))
    label = myfont.render("Wyjście", 5, biały)
    ekran.blit(label, (210, 438))

    pygame.display.flip()
    zegar.tick(15)


###   ROZGRYWKA

ll=0; GAME=0
if LIFE == 1 and Du==0:
 ll = len(LDB)
 GAME = 1
 pygame.mixer.music.load('DRIK.mp3')
 pygame.mixer.music.play(-1)
poziom = 0
ruchy = 0
wynik = 0
czas = 0
kb=0; pause=0

while(ll):
 p=Plansza()
 p.stworz()
 p.wypełnij(poziom)
 #czas=(poziom+1)*60+(poziom-5)*7+poziom*3
 czas=(poziom*poziom)*5-poziom+30 #skalowanie czasu
 limit = len(LDB[poziom])*poziom+10 #skalowanie limitu

 c=Cel()
 k=Komunikat()

 while (LIFE and GAME):
   ekran.fill(biały)
   k.tło()
   for zdarzenie in pygame.event.get():
      if zdarzenie.type == pygame.QUIT:
           LIFE = False

   k.domyślne()
   p.maluj()
   c.maluj()

   GAME = -p.sprawdź()

   label = myfont.render("Poziom:"+str(poziom+1), 5, biały)
   ekran.blit(label, (620, 100))
   label = myfont.render("Wynik:"+str(int(wynik)), 5, biały)
   ekran.blit(label, (620, 150))
   if czas > 30:
    label = myfont.render("Czas:"+str(int(czas)), 5, biały)
    ekran.blit(label, (620, 200))
   else:
    label = myfont.render("Czas:"+str(int(czas)), 5, czerwony)
    ekran.blit(label, (620, 200))
   if ruchy < limit-int(limit/4): #7*(36+poziom*36+(poziom-4)*5)/10:
    label = myfont.render("Zamiany:"+str(int(ruchy)), 5, biały)
    ekran.blit(label, (620, 250))
   else:
    label = myfont.render("Zamiany:"+str(int(ruchy)), 5, czerwony)
    ekran.blit(label, (620, 250))
    label = myfont.render("x_x   :"+str(int(limit-ruchy)), 5, czerwony)
    ekran.blit(label, (635, 270))

   if(pause):
       key = pygame.key.get_pressed()
       if kb==0 and key[pygame.K_p]:
           pause=(pause+1)%2 #unpause
           if pygame.mixer.music.get_volume()!=0:
               pygame.mixer.music.set_volume(vol)
       k.pauza()
       
   else: #non-active segment during pause

       key = pygame.key.get_pressed()
       if kb==0: #key input check
           if key[pygame.K_SPACE]:p.zaznacz(c.pobierz());ruchy+=1
           if key[pygame.K_RIGHT]:c.przesuń(2)
           if key[pygame.K_LEFT]:c.przesuń(1)
           if key[pygame.K_UP]:c.przesuń(3)
           if key[pygame.K_DOWN]:c.przesuń(4)
           if key[pygame.K_q]: LIFE = 0
           if key[pygame.K_n]: GAME = 0
           if key[pygame.K_p]:
               pause=(pause+1)%2; pygame.mixer.music.set_volume(vol/5.33)
           if key[pygame.K_m]:
               if pygame.mixer.music.get_volume()==0:
                   pygame.mixer.music.set_volume(vol)
               else: pygame.mixer.music.set_volume(0.0)
       
   kb=0;    #key block
   for i in range(len(key)):
       if(key[i]!=0): kb=1; break;

   pygame.display.flip() 
   zegar.tick(15)
   if pause==0: czas-=0.1
   if czas < -1: LIFE = 0
   #if ruchy > 36+poziom*36+(poziom-4)*6+1000: LIFE =0
   if ruchy > limit and -p.sprawdź(): LIFE =0

 ll = ll-1
 poziom+=1
 if LIFE == 1:
     wynik-=ruchy*2
     wynik+=czas*5
     ruchy=0
 GAME = 1

if LIFE == 0 and GAME == 1: #defeat screen
  pygame.mixer.music.fadeout(3000)  
  ekran.fill(czerwony)
  k.porażka()
  label = myfont.render("Wynik:"+str(int(wynik)), 5, złoty)
  ekran.blit(label, (475, 250))
  pygame.display.flip()
  zegar.tick(15)
  time.sleep(4)

elif GAME == 1: #victory screen
  pygame.mixer.music.fadeout(3000)  
  ekran.fill(czarny)
  k.zwycięstwo()
  wynik+=1000
  label = myfont.render("Wynik:"+str(int(wynik)), 5, złoty)
  ekran.blit(label, (475, 250))
  pygame.display.flip()
  zegar.tick(15)
  time.sleep(4)

##  ROZGRYWKA (DUEL)
elif Du == 1:
 GRACZ1=1;GRACZ2=1;
 ll = len(DLDB)
 wyl="zgas.png"
 reve = pygame.mixer.Sound('re2.wav')

 pygame.mixer.music.load('DRDH.mp3')
 pygame.mixer.music.play(-1)

 poziom = 0
 ruchy = 1
 czas = 0
 tura = 0

 while(ll):
  p=Plansza()
  p.stworz()
  p.wypełnij2(poziom)
  czas=10+tura*9 #skalowanie czasu

  p.losowe_znaczenia(100)
  #p.wypisz()

  c=Cel()
  k=Komunikat()
  player=1

  while (GRACZ1 and GRACZ2):
   ekran.fill(biały)
   k.tło()
   for zdarzenie in pygame.event.get():
      if zdarzenie.type == pygame.QUIT:
           Du=0

   k.domyślne()
   p.maluj()
   c.maluj()

   GRACZ2 = -p.sprawdź()
   GRACZ1 = -p.sprawdź2()
   if Du==0:
       GRACZ1=0
       GRACZ2=GRACZ1

   if player == 1: gracz='P1'; tło="tlo.jpg"
   elif player == 2: gracz='P2'; tło="tlo2.jpg"
   else: gracz='błąd!'

   label = myfont.render("Poziom Duel", 5, biały)
   ekran.blit(label, (620, 100))
   label = myfont.render("Gracz:"+str(gracz), 5, biały)
   ekran.blit(label, (620, 150))
   if czas > 30:
    label = myfont.render("Czas:"+str(int(czas)), 5, biały)
    ekran.blit(label, (620, 200))
   else:
    label = myfont.render("Czas:"+str(int(czas)), 5, czerwony)
    ekran.blit(label, (620, 200))
   if ruchy < 7*(36+poziom*36+(poziom-4)*5)/10:
    label = myfont.render("Zamiany:"+str(int(ruchy)), 5, biały)
    ekran.blit(label, (620, 250))
   else:
    label = myfont.render("Zamiany:"+str(int(ruchy)), 5, czerwony)
    ekran.blit(label, (620, 250))

   if(pause):
       key = pygame.key.get_pressed()
       if kb==0 and key[pygame.K_p]:
           pause=(pause+1)%2 #unpause
           if pygame.mixer.music.get_volume()!=0:
               pygame.mixer.music.set_volume(vol)
       k.pauza()
       
   else: #non-active segment during pause
       key = pygame.key.get_pressed()
       if kb==0: #key input check
           if key[pygame.K_SPACE]:p.zaznacz(c.pobierz());ruchy-=1
           if key[pygame.K_RIGHT]:c.przesuń(2)
           if key[pygame.K_LEFT]:c.przesuń(1)
           if key[pygame.K_UP]:c.przesuń(3)
           if key[pygame.K_DOWN]:c.przesuń(4)
           if key[pygame.K_q]: GRACZ1=0; GRACZ2=GRACZ1;
           #if key[pygame.K_n]: GAME = 0
           if key[pygame.K_p]:
               pause=(pause+1)%2; pygame.mixer.music.set_volume(vol/5.33)
           if key[pygame.K_m]:
               if pygame.mixer.music.get_volume()==0:
                   pygame.mixer.music.set_volume(vol)
               else: pygame.mixer.music.set_volume(0.0)

   kb=0;    #key block
   for i in range(len(key)):
       if(key[i]!=0): kb=1; break;

   pygame.display.flip()
   zegar.tick(15)
   if pause==0: czas-=0.1
   if czas < -1:
       if player == 1: player=2
       elif player == 2: player=1
       else: pass
       tura+=1
       czas=0; ruchy=1
       czas=10+tura*9
       ruchy+=tura
       reve.play()
       time.sleep(1)

   if ruchy < 1:
       if player == 1: player=2
       elif player == 2: player=1
       else: pass
       tura+=1
       czas=0; ruchy=1
       czas=10+tura*9
       ruchy+=tura
       reve.play()
       time.sleep(1)

  ll=0

 if GRACZ1 == 1:
  pygame.mixer.music.fadeout(3000) 
  ekran.fill(czarny)
  k.zwycięstwo()
  label = myfont.render("Wygrał Gracz 1!", 5, złoty)
  ekran.blit(label, (475, 250))
  pygame.display.flip()
  zegar.tick(15)
  time.sleep(4)

 elif GRACZ2 == 1:
  pygame.mixer.music.fadeout(3000) 
  ekran.fill(czarny)
  k.zwycięstwo()
  label = myfont.render("Wygrał Gracz 2!", 5, złoty)
  ekran.blit(label, (475, 250))
  pygame.display.flip()
  zegar.tick(15)
  time.sleep(4)

 elif GRACZ1 == GRACZ2:
  pygame.mixer.music.fadeout(3000) 
  ekran.fill(czarny)
  k.porażka()
  label = myfont.render("Remis!!!", 5, złoty)
  ekran.blit(label, (475, 250))
  pygame.display.flip()
  zegar.tick(15)
  time.sleep(4)

else: pass

pygame.display.quit()
pygame.quit()
sys.exit()
