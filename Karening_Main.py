
from Settings_Karen import *

#Initialize Variables

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Karening")

clock = pygame.time.Clock()
pygame.mixer.music.play(loops = -1)
print("Initial Variables")
#Sprite Group



player = Player()
platinum = Platform()
exp = Exp(0)
health = Health()
mob = Enemy(400, 50, player.getPosX(), player.getPosY())
lvl = Level(0)
mobless = NoMob()




pew = Bullet(player.rect.centerx, player.rect.top, "UP")


all_sprites.add(player)
print("Spawn Slayer")
all_sprites.add(exp)
print("Spawn Exp Board")
all_sprites.add(platinum)
print("Spawn Car")
all_sprites.add(health)
print("Spawn Health Board")

print("Spawn Mob")
all_sprites.add(lvl)
print("Spawn Level Board")


print("All Sprites Added")

bullets.add(pew)
print("Bullets added to list")
all_sprites.add(mob) #TEST CODE!
mobs.add(mob)
print("Enemy added to list")
protag.add(player)
print("Player added to list")

background = pygame.image.load(os.path.join(img_folder, "scree.png")).convert()
backg = pygame.transform.scale(background,(width, height))
background_rect = background.get_rect()

ded = pygame.image.load(os.path.join(img_folder, "itsOver1.png")).convert()
ded = pygame.transform.scale(ded, (width, height))
ded_rect = ded.get_rect()
ded.set_colorkey(red)




#Draw Text
font_name = pygame.font.match_font('Comic Sans MS')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, l_blue)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

mouse_pos = pygame.mouse.get_pos()

#draw_text(screen, mouse_pos, 16, 730, 780)



print("draw text")
def show_start_screen():
    screen.blit(background, background_rect)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                print("Key pressed to start game!")
                waiting = False

def show_end_screen():
    screen.blit(ded, ded_rect)
    
    pygame.display.flip()

    dying = True
    while dying:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                print("Ending Game")
                dying = False

def game_over():
    screen.blit(background, background_reckt)
    pygame.display.flip()

    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                print("Ha, You lost")
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()

def stageBanner0(e):
    banner0 = [pygame.image.load(os.path.join(img_folder, "stageBanner0.png")).convert(),
               ]
    banner_count = e
    
    
    screen.blit(banner0[banner_count], (width, height))
    pygame.display.flip()

    waitings = True
    while waitings:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                print("Game Ready")
                waitings = False


'''
def invasion1(i):
    newMob()
'''

def newMob(tomato, tomahto):

    coordx = random.randrange(50, 750)
    coordy = random.randrange(50, 750)

    mob = Enemy(tomato, tomahto, player.getPosX(), player.getPosY())
    all_sprites.add(mob)
    mobs.add(mob)

#Runs Once, YAY
dead = False
if dead == True:
    mobs.add(mob)
    dead = False
    
            
lot = [pygame.image.load(os.path.join(img_folder, "stage_0.png")).convert(),
       pygame.image.load(os.path.join(img_folder, "stage2.png")).convert(),
       pygame.image.load(os.path.join(img_folder, "stage3.png")).convert()]
lot_count = 0
background_image = lot[lot_count]


bg = pygame.transform.scale(background_image, (width, height))
bg_rect = bg.get_rect()
print("start_screen")



print("Sprite Group")

#Game Loops:
#Process Events
#Update
#Draw
start = True
running = True
bbanner = True
dying = True
while running:

    #Start Screen x 1
    if start:
        print("making start screen")
        show_start_screen()
        start = False
        print("ending start screen")

    '''
    if bbanner:
        print("Banner")
        stageBanner0(0)
        bbanner = False
    '''
    
    clock.tick(fps)


    
    #Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    bcoll = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in bcoll:
        print("hit")
        
        bullet_sound.stop()
        exp.useExp(5)
        if exp.useExp(5) == False:
            Level.setLever(1)
            exp.self.exp = 0
            
            
            
        
        randY = random.randint(50, 750)
        randX = random.randrange(50, 750)
        newMob(randY, randX)

    pcoll = pygame.sprite.groupcollide(protag, mobs, False, True)
    for hit in pcoll:
        print("Damaged")

        randY = random.randrange(50, 750)
        randX = random.randrange(50, 750)

    
        newMob(randY, randX)
        if health.setHealth(-1) == False:

            dying = True
            show_end_screen()
            pygame.quit()

        emote = random.randint(3,4) 
        speech = Emote(emote, player.rect.centerx, player.rect.bottom)
        all_sprites.add(speech)






    #Updates
    all_sprites.update()
    
    #Draw
    
    screen.blit(bg, bg_rect)
    
    all_sprites.draw(screen)

    pygame.display.flip()
    
pygame.quit()

