"""
Main Purpose:
   Learn pygame
   Game will work without data/highscore.txt due to try except
Idea stolen from:
   https://pythongeeks.org/python-pygame-snake-game/

Level: Advanced
What I learned:
   pygame has worst doc_string than tkinter
   FileNotFoundError
   UnboundLocalError

Created by HackerDu
"""

import sys, random
try:
    import pygame
except ImportError:
    print("pip3 install pygame")

WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)

class SnakeGame():
    def score_on_screen(self,text,color,x,y):
        """
        Displays score on screen
        """

        screen_text = font.render(text, True , color)
        game_window.blit(screen_text,[x,y])

    def plot_snake(self, gameWindow, color ,snake_list,snake_size):
        """
        Plotting the snake on canvas
        """

        for x,y in snake_list:
            pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

    def welcome_screen(self):
        """
        Menu Screen to press enter to start game
        """

        game_over = False
        
        while not game_over:
            game_window.fill((255,182,193))
            self.score_on_screen("Welcome to Snake",BLACK,90,250)
            self.score_on_screen("Press spacebar to play",BLACK,232,290)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.start_new_game()
            pygame.display.update()
            clock.tick(60)

    def start_new_game(self):
        game_exit, game_over = False, False
        snake_x, snake_y = 45, 55
        velocity_x, velocity_y, init_velocity = 0, 0, 5
        score= 0
        apple_x, apple_y = random.randint(20,screen_width/2), random.randint(20,screen_height/2)
        snake_size=30
        snake_list = []
        snake_length = 1
        fps=40

        try:
           with open("data/highscore.txt","r") as file:
              high_score = file.read()
        except FileNotFoundError:
            with open("data/highscore.txt", "w") as file:
               file.write("0")
               high_score = 0           # Note: if assign high_score here will not get UnboundLocalError

        while not game_exit:
            if game_over:
                with open ("data/highscore.txt","w") as file:
                    file.write(str(high_score))       # Note: write() as a str
                game_window.fill(WHITE)
                self.score_on_screen("Game Over! Press Enter to continue",RED,100,250)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_exit = True
                    if event.type== pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.welcome_screen()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_exit = True
                    if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x, velocity_y =  init_velocity, 0
                        elif event.key == pygame.K_LEFT:
                            velocity_x, velocity_y = -init_velocity, 0
                        elif event.key == pygame.K_UP:
                            velocity_y, velocity_x = -init_velocity, 0
                        elif event.key == pygame.K_DOWN:
                            velocity_y, velocity_x=  init_velocity, 0
                            velocity_x = 0

                if abs(snake_x - apple_x) < 20 and abs(snake_y - apple_y) < 20:
                    score += 10
                    apple_x = random.randint(20,screen_width/2)
                    apple_y = random.randint(20,screen_height/2)
                    snake_length+=5

                    if score > int(high_score):
                        high_score = score
                game_window.fill(WHITE)

                try:
                  self.score_on_screen("Score: "+str(score) + " highscore: "+str(high_score),RED,5,5)
                except UnboundLocalError:
                  self.score_on_screen("Score: "+str(score) + " highscore: "+str(high_score),RED,5,5)
                pygame.draw.rect(game_window,RED,[apple_x,apple_y,snake_size,snake_size])
                head=[]
                head.append(snake_x)
                head.append(snake_y)
                snake_list.append(head)
                if len(snake_list)>snake_length:
                    del snake_list[0]
                if head in snake_list[:-1]:
                    game_over=True
                if snake_x < 0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                    game_over = True
                self.plot_snake(game_window,BLACK,snake_list,snake_size)
                pygame.draw.rect(game_window,BLACK,[snake_x,snake_y,snake_size,snake_size])
            pygame.display.update() 
            clock.tick(fps)
        pygame.quit()
        quit()

def main():
   global font, game_window, clock, screen_width, screen_height
   screen_width, screen_height = 900, 600

   snake = SnakeGame()
   
   pygame.init()
   game_window = pygame.display.set_mode((screen_width, screen_height))
   pygame.display.set_caption("Snake Game")
   clock = pygame.time.Clock()
   font = pygame.font.SysFont(None,55)
   snake.welcome_screen()
   pygame.display.update()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()