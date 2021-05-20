from Settings_Karen import *

class Direction(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.catalog = [pygame.image.load(os.path.join(img_folder, "pew_dir0.png")).convert(),
                   pygame.image.load(os.path.join(img_folder, "pew_dir1.png")).convert(),
                   pygame.image.load(os.path.join(img_folder, "pew_dir2.png")).convert(),
                   pygame.image.load(os.path.join(img_folder, "pew_dir3.png")).convert(),
                   pygame.image.load(os.path.join(img_folder, "pew_dir4.png")).convert()]

        self.cat_count = 0

        self.image = self.catalog[self.cat_count]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey(red_d)

        self.rect = self.image.get_rect()
        self.direction = "DOWN"

        self.rect.x = 0
        self.rect.y = 700

    def update(self):
        
        if self.direction == "UP":
            self.cat_count = 4

        
        elif self.direction == "DOWN":
            self.cat_count = 1
   
        elif self.direction == "LEFT":
            self.cat_count = 2

        elif self.direction == "RIGHT":
            self.cat_count = 3

        else:
            self.cat_count = 0


        
        self.image = self.catalog[self.cat_count]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey(red_d)
        
                
    def setDirection(self, d):
        self.direction = d
