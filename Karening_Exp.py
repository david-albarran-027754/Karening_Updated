from Settings_Karen import *

class Exp(pygame.sprite.Sprite):
    def __init__(self, e):

        pygame.sprite.Sprite.__init__(self)

        self.expo = [pygame.image.load(os.path.join(img_folder, "SHINY_EXP0.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP1.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP2.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP3.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP4.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "SHINY_EXP5.png")).convert(),
                     ]


        self.expoMarker = 0

        self.image = self.expo[self.expoMarker]


        
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 0
        self.exp = 0

        # DELAY
        self.xp_delay = 10000
        self.last_xp = pygame.time.get_ticks()

    def getExp(self):
        return self.expoMarker

    def useExp(self, e):
        self.exp += e
        print(self.exp)


        if self.exp == 0:
            self.expoMarker = 0
        elif self.exp == 25:
            self.expoMarker = 1
        elif self.exp == 50:
            self.expoMarker = 2
        elif self.exp == 75:
            self.expoMarker = 3
        elif self.exp == 100:
            self.expoMarker = 4
        elif self.exp == 125:
            self.expoMarker = 5
        elif self.exp == 150:
            return False
 
    def update(self):

        self.image = self.expo[self.expoMarker]
        self.image = pygame.transform.scale(self.image, (200, 140))
        self.image.set_colorkey(white)

        xp = pygame.time.get_ticks()
        if xp - self.last_xp > self.xp_delay:
            self.last_xp = xp
            print(xp)
            #if xp >= 10000:

            xp = 0
            self.useExp(2)
            if self.useExp(2) == False:
                
                self.exp = 0
            print("Passive Exp")




        
