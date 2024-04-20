import pygame, random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# rgb values used in the game
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)

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
    started = False

    #points
    point = 0
    point2 = 0

    #players game paddles, pygame.Rect needs x y width and height
    paddle_1_rect = pygame.Rect(30,0,7,100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50,0,7,100)

    #tracking by how much players paddle will move per frame
    paddle_1_move = 0
    paddle_2_move = 0

    #rectangle that represents the ball
    ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

    #determine the x and y speed of the ball (0.1 is just to scale the speed down)
    ball_accel_x = random.randint(2,4) * 0.1
    ball_accel_y = random.randint(2,4) * 0.1

    #randomize the direction of the ball
    if random.randint(1,2) == 1:
        ball_accel_x *= -1
    if random.randint(1,2) == 1:
        ball_accel_y *= -1

   

    #game loop
    while True:
        #setting background color to black everytime the game updates
        screen.fill(COLOR_BLACK)
        if not started:
            screen.fill(COLOR_BLACK)
            start_screen(screen)
            
        #making the ball move after three seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
         
                        delta_time = clock.tick(60)
        else:
                  
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
            if ball_rect.left <= -1: 
                pygame.time.wait(3000)
                ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
                
                

               

            elif ball_rect.left >= SCREEN_WIDTH + 1:
                pygame.time.wait(100)
                ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)
                
                

             #if padding 1 collides with the balla nd the ball is in front of it, change the speed of the ball and
            #make it move a little in the opposite direction, when it collides
            if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
                ball_accel_x *= -1
                ball_rect.left += 5
        
            # do the same with paddle 2
            if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
                ball_accel_x *= -1
                ball_rect.left -= 5

            #if the ball can move, game is started, it moves the ball

      
            #drawing player 1 and 2 paddles rect with white
            pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
            pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

            #drawing the ball with white color
            pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

         
        #moves the ball
        
            
       
        #updating display (necessary)
        pygame.display.update()

       

def start_screen(screen):
    screen.fill(COLOR_BLACK)
    font = pygame.font.SysFont('Consolas', 30)

    #drawing text to the center of the screen
    text = font.render("Press Space to Start", True, COLOR_WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(text, text_rect)

    pygame.display.flip()


#running the game
if __name__ == "__main__":
    main()
   

    