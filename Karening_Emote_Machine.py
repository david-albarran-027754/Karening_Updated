from Settings_Karen import *

class Emote(pygame.sprite.Sprite):
    def __init__(self, emote, x, y):
        print("BMing")
        pygame.sprite.Sprite.__init__(self)

        self.catchphrase = [pygame.image.load(os.path.join(img_folder, "script0.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "script1.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "script2.png")).convert(),
                        pygame.image.load(os.path.join(img_folder, "script3.png")).convert(),
                        pygame.image.load(os.path.join(img_folder, "script3.png")).convert()]
        
        self.count = emote

        self.image = self.catchphrase[self.count]
        self.image.set_colorkey(red_d)
        


        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.image = pygame.transform.scale(self.image, (120 ,50))

        #Delay
        self.emote_delay = 2000
        self.last_emote = pygame.time.get_ticks()

    def update(self):



        self.image = self.catchphrase[self.count]
        self.image.set_colorkey(red_d)
        self.image = pygame.transform.scale(self.image, (120 ,50))
'''
        
            wait = 0
            self.kill()'''

