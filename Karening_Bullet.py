from Settings_Karen import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,d):
        pygame.sprite.Sprite.__init__(self)

        Flearth = [
                    pygame.image.load(os.path.join(img_folder, "Disk0.png")).convert(),
                    pygame.image.load(os.path.join(img_folder, "Disk1.png")).convert(),
                    pygame.image.load(os.path.join(img_folder, "Disk2.png")).convert(),
                    pygame.image.load(os.path.join(img_folder, "Disk3.png")).convert()]
        
        TP =        [pygame.image.load(os.path.join(img_folder, "tp0.png")).convert(),
                  pygame.image.load(os.path.join(img_folder, "tp1.png")).convert(),
                  pygame.image.load(os.path.join(img_folder, "tp2.png")).convert(),
                  pygame.image.load(os.path.join(img_folder, "tp3.png")).convert(),]
        
        Potion =     [pygame.image.load(os.path.join(img_folder, "dumb_juice0.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "dumb_juice1.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "dumb_juice2.png")).convert(),
                     pygame.image.load(os.path.join(img_folder, "dumb_juice3.png")).convert(),]

        Quack = [pygame.image.load(os.path.join(img_folder, "quack0.png")).convert(),
                 pygame.image.load(os.path.join(img_folder, "quack1.png")).convert(),
                 pygame.image.load(os.path.join(img_folder, "quack2.png")).convert(),
                 pygame.image.load(os.path.join(img_folder, "quack3.png")).convert(),]

        self.pews = [Flearth, TP, Potion, Quack]



        self.pow = random.randint(0,3)
        self.pew_count = 0

        self.image = self.pews[self.pow][self.pew_count]
        self.image.set_colorkey(red_d)
        
        self.direction = d
        
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speed = 50


    def update(self):
        if self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed


        if self.rect.left > width:
            self.kill()
            self.pow = random.randint(0,3)

        elif self.rect.right < 0:
            self.kill()
            self.pow = random.randint(0,3)

        elif self.rect.top > height:
            self.kill()
            self.pow = random.randint(0,3)

        elif self.rect.bottom < 0:
            self.kill()
            self.pow = random.randint(0,3)


        
        self.pew_count += 1
        if self.pew_count > 3:
            self.pew_count = 0

        


        self.image = self.pews[self.pow][self.pew_count]
        self.image.set_colorkey(red_d)


        
