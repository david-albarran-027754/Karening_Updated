from Settings_Karen import *




#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "playeridle.png")).convert()
        self.image = pygame.transform.scale(self.image, (150, 50))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.y_speed = 8
        self.radius = 20
        print("Player Init")


        self.rect.centerx = width / 2
        self.rect.bottom = height - 200
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

        # DIRECTION CODE
        print("Drawing dirction indicator")
        self.direction_indicator = Direction()
        all_sprites.add(self.direction_indicator)
        self.direction_indicator.setDirection("UP")
        self.direction = "UP"

    def getPosX(self):
        return (self.rect.centerx)

    def getPosY(self):
        return(self.rect.centery)

    def shoot(self, mouse_x, mouse_y):
        #pew_sound = pygame.mixer.Sound("Bullet_Disk_Noise.wav")
        
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            

            emote = random.randint(0, 2)
            bullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
            speech = Emote(emote, self.rect.centerx, self.rect.bottom)
            all_sprites.remove(speech)
            all_sprites.add(bullet)
            all_sprites.add(speech)
            bullets.add(bullet)
            
            bullet_sound.play()


    def update(self):

        self.speedx = 0
        #Returns a list, keystate, of all pressed keys
        keystate = pygame.key.get_pressed()

        #Checks to see which keys were in the list(a.k.a pressed)
        running = True
        if running == True:
            if keystate[pygame.K_d]:
                self.rect.x += 5
                self.image = pygame.image.load(os.path.join(img_folder, "playerright.png")).convert()
                self.image = pygame.transform.scale(self.image, (50, 100))
                self.image.set_colorkey(white)

                self.direction_indicator.setDirection("RIGHT")

                if keystate[pygame.K_SPACE]:
                    self.rect.x += 15
                self.direction = "RIGHT"
            elif keystate[pygame.K_a]:
                self.rect.x += -5
                self.image = pygame.image.load(os.path.join(img_folder, "playerleft.png")).convert()
                self.image = pygame.transform.scale(self.image, (50, 100))
                self.image.set_colorkey(white)
                self.direction_indicator.setDirection("LEFT")

                if keystate[pygame.K_SPACE]:
                    self.rect.x -= 15
                self.direction = "LEFT"
            elif keystate[pygame.K_w]:
                self.rect.y += -5
                self.image = pygame.image.load(os.path.join(img_folder, "playerup.png")).convert()
                self.image = pygame.transform.scale(self.image, (100, 50))
                self.image.set_colorkey(white)
                self.direction_indicator.setDirection("UP")

                if keystate[pygame.K_SPACE]:
                    self.rect.y -= 15
                self.direction = "UP"
            elif keystate[pygame.K_s]:
                self.rect.y += 5
                self.image = pygame.image.load(os.path.join(img_folder, "playerdown.png")).convert()
                self.image = pygame.transform.scale(self.image, (100, 50))
                self.image.set_colorkey(white)
                self.direction_indicator.setDirection("DOWN")

                if keystate[pygame.K_SPACE]:
                    self.rect.y += 15
                self.direction = "DOWN"
            else:
                self.image = pygame.image.load(os.path.join(img_folder, "playeridle.png")).convert()
                self.image = pygame.transform.scale(self.image, (100, 50))
                self.image.set_colorkey(white)
            
        self.rect.x += self.speedx

        if self.rect.bottom > 800:
            self.rect.bottom = 800
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > 900:
            self.rect.right = 900

        mouseState = pygame.mouse.get_pressed()

        
        if mouseState[0] == 1:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]

            self.shoot(mouse_x, mouse_y)
            item = random.randrange(0,3)
            return item

            
class Foot(pygame.sprite.Sprite):
    def __init__(self, d):
        pygame.sprite.Sprite.__init__(self)

                
        leftstep = [pygame.image.load(os.path.join(img_folder, "footsteps_4.png")),
                    pygame.image.load(os.path.join(img_folder, "footsteps_5.png"))]
        lstep = 0

        upstep = [pygame.image.load(os.path.join(img_folder, "footsteps_0.png")),
                  pygame.image.load(os.path.join(img_folder, "footsteps_1.png"))]

        ustep = 0

        rightstep = [pygame.image.load(os.path.join(img_folder, "footsteps_3.png")),
                     pygame.image.load(os.path.join(img_folder, "footsteps_4.png"))]

        rstep = 0

        downstep = [pygame.image.load(os.path.join(img_folder, "footsteps_6.png")),
                    pygame.image.load(os.path.join(img_folder, "footsteps_7.png"))]

        
        self.image = set_colorkey(black)

        self.direction = d

        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery

        self.image = pygame.transform.scale(self.image, (150,150))


    def update(self):

        if self.direction == "RIGHT":
            self.image = rightstep[rstep]
            rstep += 1
            if rstep > 1:
                rstep = 0
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed

        self.image = self.pews[self.pew_count]
        self.image.set_colorkey(black)

        self.pew_count += 1
        if self.pew_count > 3:
            self.pew_count = 0
        print(self.pew_count)
                












        

