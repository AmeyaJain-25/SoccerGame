import pygame
import random
from pygame import mixer



pygame.init()

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Dimension of the screen
width = 1350
height = 700

# Creating a Screen
screen = pygame.display.set_mode((width, height))
# Title
pygame.display.set_caption("Football")



#Score
leftPlayerScore = 0
rightPlayerScore = 0

game_font = pygame.font.Font("freesansbold.ttf", 32)


#Ball
ballImg = pygame.image.load("soccer.png")
ball_X = width/2 - 12
ball_Y = height/2 - 12
ball_XChange = 1.5 * random.choice((1, -1))
ball_YChange = 1.5
ballPixel = 32


def ball(x, y):
    screen.blit(ballImg, (x, y))



#LefttFootPlayer
leftFoot = pygame.image.load("rightfoot.png")
playerLeft_Xpos = 110
playerLeft_Ypos = 200
playerLeftSpeed = 0



#RightFootPlayer
rightFoot = pygame.image.load("shoe1.png")
playerRight_Xpos = width - 128 - 110
playerRight_Ypos = 200
playerRightSpeed = 0




#Score
playerAScore = 0
playerBScore = 0

#Font
game_font = pygame.font.Font("freesansbold.ttf", 80)



#Start Game:
startImg = pygame.image.load("play.png")
startImg_X = width/2 - 64
startImg_Y = height/2 - 64

def start():
    startRun = True
    while startRun:
        screen.fill((0, 255, 50))
        screen.blit(startImg, (startImg_X, startImg_Y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if startImg_X < mouse[0] and (startImg_X + 128) > mouse[0]:
            if startImg_Y < mouse[1] and (startImg_Y + 128) > mouse[1]:
                if click[0] == 1:
                    gameLoop()
        pygame.display.update()


def playing():
    global playerLeft_Ypos, playerRight_Ypos, ball_X,ball_Y, leftPlayerScore, rightPlayerScore, ball_YChange, ball_XChange
    #RightPlayerMovement
    playerRight_Ypos += playerRightSpeed
    if playerRight_Ypos <= 5:
        playerRight_Ypos = 5
    if playerRight_Ypos + 128 >= height - 5:
        playerRight_Ypos = height - 5 - 128

    #LedtPlayerMovement
    playerLeft_Ypos += playerLeftSpeed
    if playerLeft_Ypos <= 5:
        playerLeft_Ypos = 5
    if playerLeft_Ypos + 128 >= height - 5:
        playerLeft_Ypos = height - 5 - 128






    # Bouncing the ball
    if ball_X + ballPixel >= width - 5:
        # ball_XChange *= -1
        ball_X = width / 2 - 12
        ball_Y = height / 2 - 12

        ball_YChange = 1.5 * random.choice((1, -1))
        ball_XChange = 1.5 * random.choice((1, -1))
        leftPlayerScore += 1


    if ball_X <= 5:
        # ball_XChange *= -1
        ball_X = width / 2 - 12
        ball_Y = height / 2 - 12

        ball_YChange = 1.5 * random.choice((1, -1))
        ball_XChange = 1.5 * random.choice((1, -1))
        rightPlayerScore += 1



    if ball_Y + ballPixel >= height - 5 or ball_Y <= 5:
        ball_YChange *= -1

    # Moving the ball
    ball_X += ball_XChange
    ball_Y += ball_YChange

    # Drawing the ball
    ball(ball_X, ball_Y)

    playerAText = game_font.render(str(leftPlayerScore), True, blue)
    screen.blit(playerAText, (width / 2 - 75 - 40, 600))

    playerBText = game_font.render(str(rightPlayerScore), True, blue)
    screen.blit(playerBText, (width / 2 + 75, 600))










def crash():
    global ball_XChange
    if (ball_Y > playerLeft_Ypos and ball_Y < playerLeft_Ypos + 128) or (
            ball_Y + ballPixel > playerLeft_Ypos and ball_Y + ballPixel < playerLeft_Ypos+ 128):
        if (ball_X <= playerLeft_Xpos + 128 and ball_X >= playerLeft_Xpos + 90) or (
                ball_X + ballPixel <= playerLeft_Xpos + 128 and ball_X + ballPixel >= playerLeft_Xpos + 90):
            ball_XChange *= -1


    if (ball_Y > playerRight_Ypos and ball_Y < playerRight_Ypos + 128) or (
            ball_Y + ballPixel > playerRight_Ypos and ball_Y + ballPixel < playerRight_Ypos + 128):
        if (ball_X + ballPixel >= playerRight_Xpos and ball_X + ballPixel <= playerRight_Xpos + 50) or (
                ball_X >= playerRight_Xpos and ball_X <= playerRight_Xpos + 50):
            ball_XChange *= -1


    # if (ball_Y > playerRight_Ypos and ball_Y < playerRight_Ypos + 128) or (
    #         ball_Y + ballPixel > playerRight_Ypos and ball_Y + ballPixel < playerRight_Ypos + 128):
    #     if (ball_X + ballPixel >= playerRight_Xpos) or (
    #             ball_X >= playerRight_Xpos):
    #         ball_XChange *= -1


mixer.music.load("football_chant.wav")
mixer.music.play(-1)







# Gaming Loop:
def gameLoop():
    global playerLeftSpeed, playerRightSpeed, startRun
    startRun = False
    running = True
    while running:
        screen.fill(black)
        screen.fill((0, 255, 50))
        pygame.draw.line(screen, white, (width/2, 3), (width/2, height - 3), 5)   #MidLine
        pygame.draw.line(screen, white, (3, 3), (width - 3, 3), 5)                #UpLine
        pygame.draw.line(screen, white, (3, height - 5), (width - 3, height - 5), 5)        #DownLine
        pygame.draw.line(screen, white, (5, 1), (5, height - 3), 5)               #LeftLine
        pygame.draw.line(screen, white, (width - 5, 1), (width - 5, height - 3), 5)   #RightLine
        pygame.draw.circle(screen, white, (675, 350), 10)            #CentrePoint
        pygame.draw.circle(screen, white, (675, 350), 100, 5)        #Centre Circle
        leftRect = pygame.Rect(5, 150, 200, 400 )
        pygame.draw.rect(screen, white, leftRect, 5)   #LeftRect
        leftSmallRect = pygame.Rect(5, 230, 100, 240)
        pygame.draw.rect(screen, white, leftSmallRect, 5)  # LeftSmallRect
        RightSmallRect = pygame.Rect(width - 5 - 100, 230, 100, 240)
        pygame.draw.rect(screen, white, RightSmallRect, 5)  # RightSmallRect
        RightRect = pygame.Rect(width - 5 - 200, 150, 200, 400)
        pygame.draw.rect(screen, white, RightRect, 5)  # RightRect
        # pygame.draw.arc(screen, white, (4, 3, 20, 20), 45, 90, 2)

        pygame.draw.line(screen, red, (10, 270), (10, 420), 15)  #LeftGoal
        pygame.draw.line(screen, red, (width - 10, 270), (width - 10, 420), 15)   #RightGoal

        #LeftFootPlayer
        screen.blit(leftFoot, (playerLeft_Xpos, playerLeft_Ypos))
        #RightFootPlayer
        screen.blit(rightFoot, (playerRight_Xpos, playerRight_Ypos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    playerLeftSpeed += 2
                if event.key == pygame.K_w:
                    playerLeftSpeed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    playerLeftSpeed -= 2
                if event.key == pygame.K_w:
                    playerLeftSpeed += 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    playerRightSpeed += 2
                if event.key == pygame.K_UP:
                    playerRightSpeed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    playerRightSpeed -= 2
                if event.key == pygame.K_UP:
                    playerRightSpeed += 2







        playing()

        crash()
        pygame.display.update()




start()