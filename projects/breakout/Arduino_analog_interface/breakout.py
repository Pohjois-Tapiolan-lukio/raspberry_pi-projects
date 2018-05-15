import pygame
import time
from dial import dial

screen_size = (400,640)
lv = min(screen_size)
pygame.display.init()
screen = pygame.display.set_mode (screen_size)

class ball(object):
    def __init__(self):
        self.pos = (screen_size[0]/2, screen_size[1]/2)
        self.ball = pygame.draw.circle(screen, (200,200,255), (self.pos),5)
        self.vx = int(screen_size[0]/lv)
        self.vy = int(screen_size[1]/lv)
        
    def move(self):
        pygame.draw.circle(screen, (0,0,0), self.ball.center, 5)
        self.ball.move_ip(self.vx, self.vy)
        pygame.draw.circle(screen, (200,200,255), self.ball.center, 5)
    
    def collision(self, obstacle):
        hit=self.ball.collidelist(obstacle)
        if hit != -1:
            self.bounce(obstacle[hit])
        
        return hit
    
    def bounce(self, obstacle):
        distx = abs(self.ball.centerx - obstacle.centerx)
        if distx == (((self.ball.width+obstacle.width)/2)-1):
            self.vx = -self.vx
        else:
            self.vy = -self.vy

class level(object):
    def __init__(self):
        self.court = [
            "WWWWWWWWWWWWWWWWWWWW",
            "W                  W",
            "W                  W",
            "WBBBBBBBBBBBBBBBBBBW",
            "WBBBBBBBBBBBBBBBBBBW",
            "WBBBBBBBBBBBBBBBBBBW",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            "W                  W",
            ]
        
        self.brick_size=(screen_size[0]/len(self.court[0]), screen_size[1]/len(self.court))
        self.limits=(self.brick_size[0], (screen_size[0] - self.brick_size[0]))
        
        self.wall=[]
        self.bricks=[]
        
        self.setup()
        self.draw()
        
    def setup(self):
        y=0
        for i in self.court:
            x=0
            for j in i:
                pos_size=(x,y,self.brick_size[0],self.brick_size[1])
                if j=="W":
                    self.wall.append(pygame.Rect(pos_size))
                elif j=="B":
                    self.bricks.append(pygame.Rect(pos_size))
                
                x += self.brick_size[0]
            y += self.brick_size[1]
                    
    def draw(self):
        screen.fill((0, 0, 0))
        for i in self.wall:
            pygame.draw.rect(screen, (255, 255, 255), i)
        
        for i in self.bricks:
            pygame.draw.rect(screen, (255, 255, 0), i)
    
    def rm_brick(self, hit):
        del self.bricks[hit]
        
        self.draw()

class paddle(object):
    def __init__(self, limits, brick_size):
        self.paddle = []
        self.paddle.append (pygame.Rect (((screen_size[0]/2) - brick_size[0], screen_size[1] - brick_size[1]), (brick_size[0]*2, (brick_size[1]/2))))
        
        self.limits = limits

        self.step = brick_size[0]/2

        self.dial = dial()
        self.dial_pos = 0
        self.calibration()
        
        self.draw((255,0,0))
        
    def calibration(self):
        while self.dial_pos < 0.45 or self.dial_pos > 0.55:
            self.dial_pos=self.dial.get()

    def place(self):
        new_dial_pos = round(self.dial.get(),2)
        
        if new_dial_pos != self.dial_pos:
            self.draw((0,0,0))
            self.paddle[0].x=(self.limits[1]-self.limits[0])-((((self.limits[1]-self.paddle[0].width)-self.limits[0])*new_dial_pos)+self.limits[0])
            self.dial_pos=new_dial_pos
            self.draw((255,0,0))
    
    def draw(self, color):
        pygame.draw.rect(screen, color, self.paddle[0])

if __name__ == '__main__':
    
    level=level()
    level.draw()
    ball=ball()
    pygame.display.flip()
    
    paddle=paddle(level.limits, level.brick_size)

    while True:
        if pygame.event.get(pygame.QUIT): break

        paddle.place()

        ball.move()
        if ball.ball.y > paddle.paddle[0].y: break
 
        if ball.collision(level.wall) != -1:
            level.draw()
            paddle.draw((255,0,0))
            
        hit=ball.collision(level.bricks)
        if hit != -1:
            level.rm_brick(hit)
            paddle.draw((255,0,0))
            
        ball.collision(paddle.paddle)
            
        pygame.display.flip()

	time.sleep(0.01)
