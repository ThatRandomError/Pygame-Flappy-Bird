import pygame
from sys import exit
from random import *

def bird_animation():
    global bird_surf, bird_index
    bird_index += 0.1
    if (bird_index >= len(bird_flap)): 
        bird_index = 0

    bird_surf = bird_flap[int(bird_index)]

pygame.init()
screen_x=576
screen_y=1024

pipe1_pass = 0
pipe2_pass = 0

pipe_scroll = 0

gravity = 0

change1_height = 0
change2_height = 0

change1_dis = 0
change2_dis = 0

if_die = 1
if1_die = 0

bird_index = 0

score = 0

screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

background = pygame.image.load("imgs/background.png")

text_font = pygame.font.Font("fonts/PixelFont.ttf", 25)
bottom1_t = text_font.render("Press Space, Mouse", False, "White")
bottom2_t = text_font.render("or Up Arrow", False, "White")

score_font = pygame.font.Font("fonts/PixelFont.ttf", 70)
score_t = score_font.render(f"{score}", False, "White")

bird1 = pygame.image.load("imgs/bird_down.png")
bird2 = pygame.image.load("imgs/bird_middle.png")
bird3 = pygame.image.load("imgs/bird_up.png")
Scaled_bird1 = pygame.transform.scale(bird1, (68,48))
Scaled_bird2 = pygame.transform.scale(bird2, (68,48))
Scaled_bird3 = pygame.transform.scale(bird3, (68,48))
bird_flap = [Scaled_bird3,Scaled_bird2,Scaled_bird1]
bird_index = 0
bird_surf = bird_flap[bird_index]
bird_rect = bird_surf.get_rect(topleft = (45, 100))

pipe1_u_y = randint(500, 800)
pipe1_d_y = randint(500, 800)
pipe2_d_y = randint(500, 800)
pipe2_u_y = randint(500, 800)


pipe1_distance = randint(200,300)+640
pipe2_distance = randint(200,300)+640

pipe1_u = pygame.image.load("imgs/pipe.png").convert()
Scaled_pipe1_u = pygame.transform.scale(pipe1_u, (104,640))
pipe1_u_rect = Scaled_pipe1_u.get_rect(topleft = (700,pipe1_u_y))

pipe2_u = pygame.image.load("imgs/pipe.png").convert()
Scaled_pipe2_u = pygame.transform.scale(pipe2_u, (104,640))
pipe2_u_rect = Scaled_pipe2_u.get_rect(topleft = (1250,pipe2_u_y))

pipe1_d = pygame.image.load("imgs/pipe.png").convert()
Scaled_pipe1_d = pygame.transform.scale(pipe1_d, (104,640))
Rotated_pipe1_d = pygame.transform.rotate(Scaled_pipe1_d, 180)
pipe1_d_rect = Rotated_pipe1_d.get_rect(topleft = (700,pipe1_d_y-pipe1_distance))

pipe2_d = pygame.image.load("imgs/pipe.png").convert()
Scaled_pipe2_d = pygame.transform.scale(pipe2_d, (104,640))
Rotated_pipe2_d = pygame.transform.rotate(Scaled_pipe2_d, 180)
pipe2_d_rect = Rotated_pipe2_d.get_rect(topleft = (1250,pipe2_d_y-pipe2_distance))

game_over = pygame.image.load("imgs/gameover.png")
Scaled_gameover = pygame.transform.scale(game_over, (384, 84))
gameover_rect = Scaled_gameover.get_rect(topleft = (96, 450))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if (event.type == pygame.KEYDOWN):
            if (event.key==pygame.K_SPACE and if_die == 0 or event.key==pygame.K_w and if_die == 0 or event.key==pygame.K_UP and if_die == 0):
                gravity = -12
            if (event.key==pygame.K_SPACE and if_die == 1 or event.key==pygame.K_w and if_die == 1 or event.key==pygame.K_UP and if_die == 1):
                bird_index = 0
                if_die = 0
                if1_die = 0
                gravity += -15
                score = 0
                pipe_scroll = 0

                gravity = 0

                bird_index = 0

                change1_height = 0
                change2_height = 0

                change1_dis = 0
                change2_dis = 0

                bird_rect.y = 300

                pipe1_u_rect = Scaled_pipe1_u.get_rect(topleft = (700,pipe1_u_y))
                
                pipe2_u_rect = Scaled_pipe2_u.get_rect(topleft = (1250,pipe2_u_y))
                
                pipe1_d_rect = Rotated_pipe1_d.get_rect(topleft = (700,pipe1_d_y-pipe1_distance))

                pipe2_d_rect = Rotated_pipe2_d.get_rect(topleft = (1250,pipe2_d_y-pipe2_distance))

        if (event.type == pygame.MOUSEBUTTONDOWN and if_die == 0):
            gravity = -12
        if (event.type == pygame.MOUSEBUTTONDOWN and if_die == 1):
            if_die = 0
            if1_die = 0
            gravity += -15
            score = 0
            pipe_scroll = 0

            gravity = 0

            bird_index = 0

            change1_height = 0
            change2_height = 0

            change1_dis = 0
            change2_dis = 0

            bird_rect.y = 300

            pipe1_u_rect = Scaled_pipe1_u.get_rect(topleft = (700,pipe1_u_y))

            pipe2_u_rect = Scaled_pipe2_u.get_rect(topleft = (1250,pipe2_u_y))

            pipe1_d_rect = Rotated_pipe1_d.get_rect(topleft = (700,pipe1_d_y-pipe1_distance))

            pipe2_d_rect = Rotated_pipe2_d.get_rect(topleft = (1250,pipe2_d_y-pipe2_distance))
    

    

    if (if_die == 0): 
        if (bird_rect.colliderect(pipe1_u_rect) or bird_rect.colliderect(pipe2_u_rect) or bird_rect.colliderect(pipe2_d_rect) or bird_rect.colliderect(pipe1_d_rect) or bird_rect.y <= 0 or bird_rect.y >= 1024):
            if_die = 1
            if1_die = 1
            gravity += -15
            score = 0
            score_t = score_font.render(f"{score}", False, "White")
            pipe_scroll = 0

            gravity = 0

            change1_height = 0
            change2_height = 0

            change1_dis = 0
            change2_dis = 0
        
    if (change1_height == 0):
        pipe1_u_y = randint(400, 700)
        change1_height = 1
    if (change2_height == 0):
        pipe2_u_y = randint(400, 700)
        change2_height = 1


    if (change1_dis == 0):
        pipe1_distance = randint(165, 250)+640  
        change1_dis = 1
    if (change2_dis == 0):  
        pipe2_distance = randint(165, 250)+640
        change2_dis = 1
        

    pipe1_u_rect = Scaled_pipe1_u.get_rect(topleft = (pipe1_u_rect.x,pipe1_u_y))

    pipe2_u_rect = Scaled_pipe2_u.get_rect(topleft = (pipe2_u_rect.x,pipe2_u_y))

    pipe1_d_rect = Rotated_pipe1_d.get_rect(topleft = (pipe1_d_rect.x,pipe1_u_y-pipe1_distance))

    pipe2_d_rect = Rotated_pipe2_d.get_rect(topleft = (pipe2_d_rect.x,pipe2_u_y-pipe2_distance))


    screen.blit(background, (0,0))
    if (if_die == 0):
        pipe_scroll += -0.0007
        pipe1_u_rect.x +=  -4 + pipe_scroll
        pipe2_u_rect.x +=  -4 + pipe_scroll
        pipe1_d_rect.x +=  -4 + pipe_scroll
        pipe2_d_rect.x +=  -4 + pipe_scroll

        gravity += 1
        bird_rect.y += gravity
    screen.blit(Scaled_pipe1_u, pipe1_u_rect)
    screen.blit(Scaled_pipe2_u, pipe2_u_rect)
    screen.blit(Rotated_pipe1_d, pipe1_d_rect)
    screen.blit(Rotated_pipe2_d, pipe2_d_rect)

    if (if1_die==1):
        screen.blit(Scaled_gameover, gameover_rect)
    
    if (pipe1_u_rect.x <= -300):
         change1_height = 0
         change1_dis = 0
         pipe1_u_rect.x = 700
         pipe1_d_rect.x = 700
         pipe1_pass = 0
    if (pipe2_u_rect.x <= -300):
         change2_height = 0
         change2_dis = 0
         pipe2_u_rect.x = 700
         pipe2_d_rect.x = 700
         pipe2_pass = 0

    if (if_die==0):
        if (pipe1_pass == 0):
            if (bird_rect.x >= pipe1_u_rect.x):
                score += 1
                score_t = score_font.render(f"{score}", False, "White")
                pipe1_pass = 1
        if (pipe2_pass == 0):
            if (bird_rect.x >= pipe2_u_rect.x):
                score += 1
                score_t = score_font.render(f"{score}", False, "White")
                pipe2_pass = 1
        
    screen.blit(score_t, (250,100))
    
    screen.blit(bird_surf, bird_rect)
    bird_animation()
    if (if_die == 1):
        screen.blit(bottom1_t, (70,900))
        screen.blit(bottom2_t, (145,950))

    pygame.display.update()
    clock.tick(60)