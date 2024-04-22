import pygame, random, pygame.time

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# rgb values used in the game
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_BLUE = (0,0,255)

def main():
    #game setup
    #initializing pygame library
    pygame.init()

    #creating a window for the game
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    #setting the window title
    pygame.display.set_caption("Pong")

    #create clock object to keep track of time
    clock = pygame.time.Clock()

    #this will check whether or not to move the ball, will move after 3 seconds
    ball_in_center = True

    #points
    point1 = 0
    point2 = 0

    game_state = "start"

    #players game paddles, pygame.Rect needs x y width and height
    paddle_1_rect = pygame.Rect(30,0,7,100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50,0,7,100)

    #gameline
    game_line = pygame.Rect(SCREEN_WIDTH / 2, 0, 7, 720)

    #tracking by how much players paddle will move per frame
    paddle_1_move = 0
    paddle_2_move = 0

    #rectangle that represents the ball
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

    #determine the x and y speed of the ball (0.1 is just to scale the speed down)
    ball_accel_x = random.randint(3,4) * 0.1
    ball_accel_y = random.randint(3,4) * 0.1

    #randomize the direction of the ball
    if random.randint(1,2) == 1:
        ball_accel_x *= -1
    if random.randint(1,2) == 1:
        ball_accel_y *= -1

    
    

    #game loop
    while True:
        #setting background color to black everytime the game updates
        screen.fill(COLOR_BLACK)
            
        #making the ball move after three seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == "start":
                        game_state = "playing"
                    delta_time = clock.tick(60)   
             
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if game_state == "end":
                    if restart_button.collidepoint(pos):
                        game_state = "start" 
                        point1 = 0
                        point2 = 0
                    

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if game_state == "end":
                    if quit_button.collidepoint(pos):
                        return


        if game_state == "start":
          start_screen(screen)
           
            
        elif game_state == "playing":
            screen.fill(COLOR_BLUE)
            #scores
            font = pygame.font.SysFont('Arcade Classic', 50)
            score1 = font.render(str(point1), True, COLOR_WHITE)
            score1_rect = score1.get_rect()
            score1_rect = (150,10)
            screen.blit(score1, score1_rect)

            font = pygame.font.SysFont('Arcade Classic', 50)
            score2 = font.render(str(point2), True, COLOR_WHITE)
            score2_rect = score2.get_rect()
            score2_rect = (800,10)
            screen.blit(score2, score2_rect)

           
                 
            #getting time elapse between now and the last frame, 
            delta_time = clock.tick(60)
            ball_rect.left += ball_accel_x * delta_time
            ball_rect.top += ball_accel_y * delta_time

            #checking for events
            for event in pygame.event.get():

                #if user exits window
                if event.type == pygame.QUIT:

                    #exit the function
                    return
            
                #if user is pressing a key
                if event.type == pygame.KEYDOWN:

                    #player 1
                    #if the key is w, set the movement of paddle1 to go up
                    if event.key == pygame.K_w:
                        paddle_1_move = -0.5
            
                    #if the key is S set the move of paddle 1 to go down
                    if event.key == pygame.K_s:
                        paddle_1_move = 0.5

                    #player 2
                    #if the key is the up arrow, set the movement of paddle 2 to go up
                    if event.key == pygame.K_UP:
                        paddle_2_move = -0.5
            
                    #if the key is the down arrow, set the movement of paddle 2 to go down
                    if event.key == pygame.K_DOWN:
                        paddle_2_move = 0.5

                #if the player releases key
                if event.type == pygame.KEYUP:
                    #if the key released is w or s stop the movement of paddle1
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        paddle_1_move = 0.0
            
                    #if the key released is up or down stop the movement of paddle2
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        paddle_2_move = 0.0

            #moving paddle1 and paddle 2 according to their move variables, 
            #also multiplying the move variable by the delta time to keep the movement consistent
            paddle_1_rect.top += paddle_1_move * delta_time
            paddle_2_rect.top += paddle_2_move * delta_time

            #making sure players go off limits with paddles
            if paddle_1_rect.top < 0:
                paddle_1_rect.top = 0
            if paddle_1_rect.bottom > SCREEN_HEIGHT:
                paddle_1_rect.bottom = SCREEN_HEIGHT

            if paddle_2_rect.top < 0:
                paddle_2_rect.top = 0
            if paddle_2_rect.bottom > SCREEN_HEIGHT:
                paddle_2_rect.bottom = SCREEN_HEIGHT
        
        
            #if the ball is getting close to the top
            if ball_rect.top < 0:
                #invert its vertical velocity
                ball_accel_y *= -1
                #adding a bit of y for it to not trigger the above code again
                ball_rect.top = 0
        
            #same concept for the bottm
            #if the ball is getting close to the bottom
            if ball_rect.top > SCREEN_HEIGHT - ball_rect.height:
                #invert its vertical velocity
                ball_accel_y *= -1 
                #adding a bit of y to the bottom so it doesnt trigger the above code again
                ball_rect.top = SCREEN_HEIGHT - ball_rect.height
            

            #if the ball goes out of bounds on the right or left side, end the game
            if ball_rect.left < 0: 
               
                ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
                ball_in_center = True
                 
                if ball_in_center:
                    
                    ball_accel_x = random.randint(3,4) * 0.1
                    ball_accel_y = random.randint(3,4) * 0.1
                    if random.randint(1,2) == 1:
                        ball_accel_x *= -1
                    if random.randint(1,2) == 1:
                        ball_accel_y *= -1
                    ball_in_center = False
                 
                point1 += 1
                if point1 == 10:
                    game_state = "end"
                            
            elif ball_rect.left >= SCREEN_WIDTH:
                ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
                ball_in_center = True
                 
                if ball_in_center:
                    
                    ball_accel_x = random.randint(3,4) * 0.1
                    ball_accel_y = random.randint(3,4) * 0.1
                    if random.randint(1,2) == 1:
                        ball_accel_x *= -1
                    if random.randint(1,2) == 1:
                        ball_accel_y *= -1
                    ball_in_center = False

                point2 += 1
                if point2 == 10:
                    game_state = "end"
                

             #if padding 1 collides with the balla nd the ball is in front of it, change the speed of the ball and
            #make it move a little in the opposite direction, when it collides
            if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
                ball_accel_x *= -1
                ball_rect.left += 5
        
            # do the same with paddle 2
            if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
                ball_accel_x *= -1
                ball_rect.left -= 5

      
            #drawing player 1 and 2 paddles rect with white
            pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
            pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

            #drawing the ball with white color
            pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

            #drawing gameline
            pygame.draw.rect(screen, COLOR_WHITE, game_line)

        elif game_state == "end":
            
            quit_screen(screen)
            restart_button = pygame.Rect(300, 300, 150, 40) 
            restart(screen)

            #quit button
            quit_button = pygame.Rect(500, 300, 150, 40) 
            quit(screen)
            
                               
        
        #updating display (necessary)
        pygame.display.update()

def start_screen(screen):
    font = pygame.font.SysFont('Arcade Classic', 30)
   
    #drawing text to the center of the screen
    welcome_text = font.render("Welcome  to  Pong !  Reach  10  points  to  win  the  game !", True, COLOR_WHITE)
    text = font.render("Press  Space  to  Start", True, COLOR_WHITE)
    text_rect = text.get_rect()
    welcome_text_rect = welcome_text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    welcome_text_rect.center = (SCREEN_WIDTH //2 , 300)
    screen.blit(text, text_rect)
    screen.blit(welcome_text,welcome_text_rect)
    pygame.display.flip()

def quit_screen(screen):
    
    font = pygame.font.SysFont('Arcade Classic', 30)
    text = font.render("Thank  you  for  playing !", True, COLOR_WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, 250)
    screen.blit(text, text_rect)

def restart(screen):
    restart_button = pygame.Rect(300, 300, 150, 40) 
    pygame.draw.rect(screen, COLOR_WHITE, restart_button)
    font = pygame.font.SysFont('Arcade Classic', 35)
    text = font.render("Restart", True, COLOR_BLACK)
    text_rect = text.get_rect(center=restart_button.center)
    screen.blit(text, text_rect)

def quit(screen):
    quit_button = pygame.Rect(500, 300, 150, 40) 
    pygame.draw.rect(screen, COLOR_WHITE, quit_button)
    font = pygame.font.SysFont('Arcade Classic', 35)
    text = font.render("Quit", True, COLOR_BLACK)
    text_rect = text.get_rect(center=quit_button.center)
    screen.blit(text, text_rect)
       
#running the game
if __name__ == "__main__":
    main()
   

    