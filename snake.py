import pygame
import time
import random

 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height)) 
pygame.display.set_caption('Snake Game adaptado')

 
clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 

 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 25)




 
 
def Your_score(score):
    value = score_font.render("Pontos: " + str(score), True, yellow)
    dis.blit(value, [10, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, (230, 150))
    
def desenha_ret (tam_ret_x, tam_ret_y, pos_x, pos_y):
    rect = pygame.draw.rect(dis, yellow, (pos_x, pos_y, tam_ret_x, tam_ret_y))    
    
    
    
def calcula_pos_retangulo(pos_x, pos_y):
    print("lalal")
    
def pisca_tela():
        cont = 5000
        while cont!=0:
            pygame.draw.rect(dis, black, (0,400,600,400))
            cont-=1    
        
 

     
 
def gameLoop():
    game_over = False
    game_close = False
    
    tam_ret_x = 570
    tam_ret_y = 380
    
    pos_x = 15
    pos_y = 10
    
    pos_ret_x_1 = 570
    pos_ret_x_2 = 25
    
    pos_ret_y_1 = 380
    pos_ret_y_2 = 15
    
    contador = 5
    
    
    
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, tam_ret_x - snake_block - 5) / 10.0) * 10.0
    foody = round(random.randrange(0, tam_ret_y - snake_block - 5) / 10.0) * 10.0
    
    temporizador = 60
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("Voce perdeu!", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                        
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            if event.type == CLOCKTICK:
                temporizador-=1    
                contador -=1
                if contador == 0:
                    tam_ret_x-=15
                    tam_ret_y-=10
                    pos_ret_x_1-=8
                    pos_ret_x_2-=8
                    pos_ret_y_1-=5
                    pos_ret_y_2-=5
                    pos_x+=8
                    pos_y+=5
                    contador = 4
                    pisca_tela()
                
                print(str(temporizador))     
            
        x_cord = int(x1)
        y_cord = int(y1)            
        if x_cord >= pos_ret_x_1 or x_cord <= pos_ret_x_2 or y_cord <= pos_ret_y_2 or y_cord >= pos_ret_y_1 :
            print("BATEEEEU   " +str(x_cord))
            print(str(pos_ret_x_1))
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        desenha_ret(tam_ret_x, tam_ret_y, pos_x, pos_y)  
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                
                
             
        our_snake(snake_block, snake_List)
        
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            
            foodx = round(random.randrange(0, tam_ret_x) / 10.0) * 10.0
            foody = round(random.randrange(0, tam_ret_y) / 10.0) * 10.0
            Length_of_snake += 1
            contador+=2
            
            
            
            print (str(pos_x))
            print (str(pos_y))
            
        
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()