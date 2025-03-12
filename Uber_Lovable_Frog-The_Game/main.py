#https://www.youtube.com/watch?v=a4NVQC_2S2U&t=64s&ab_channel=NaseemShah
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
import numpy as np
from classes.player import Player
from classes.ball import Ball

import ctypes

class Main():
  def __init__(self, game_time_limit, player_size, initial_speed, radius):
    user32 = ctypes.windll.user32
    self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    self.screensize = list(self.screensize)
    self.screensize[1] -= 80

    self.window_coordinates = 100

    self.pause_game = True
    self.end_game = False
    self.game_time_limit = game_time_limit
    self.remaining_time = self.game_time_limit
    self.hold_time = 0
    self.reset_time = 0
    self.timer_red = 0
    self.delta_time_red = 0

    self.player_size = player_size

    self.player1 = Player(-self.window_coordinates,0,self.player_size, "protagonista")
    self.player2 = Player(self.window_coordinates,0,self.player_size, "inimigo")

    self.initial_speed = initial_speed 

    self.ball_radius = radius
    self.ball = Ball(0,0,self.ball_radius, self.initial_speed)
    self.red_ball = Ball(0,0,self.ball_radius, self.initial_speed, 1)

    self.ball_colision = 0
    self.red_ball_colision = 0

    self.radius = 25
    self.radius2 = 23
    self.radius3 = 2

    self.main()

  def Background(self):
      x1 = -self.window_coordinates
      y1 = 0
      glColor3f(1,0.5,0.5)
      glBegin(GL_QUADS)
      glVertex2f(x1+(0),y1+(0))
      glVertex2f(x1+(0),y1+(600))
      glVertex2f(x1+(self.window_coordinates + 1.5),y1+(600))
      glVertex2f(x1+(self.window_coordinates + 1.5),y1+(0))
      glEnd()
      
      glColor3f(1,0.5,0.5)
      glBegin(GL_QUADS)
      glVertex2f(x1+(496-self.window_coordinates),y1+(0))
      glVertex2f(x1+(496-self.window_coordinates),y1+(600))
      glVertex2f(x1+(500-self.window_coordinates),y1+(600))
      glVertex2f(x1+(500-self.window_coordinates),y1+(0))
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f(x1+(0),y1+(0))
      glVertex2f(x1+(500),y1+(0))
      glVertex2f(x1+(500),y1+(5))
      glVertex2f(x1+(0),y1+(5))
      glEnd()

      glColor(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f(x1+(0),y1+(245))
      glVertex2f(x1+(500),y1+(245))
      glVertex2f(x1+(500),y1+(600))
      glVertex2f(x1+(0),y1+(600))
      glEnd()

      glColor(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(x1+(248),y1+(5))
      glVertex2f(x1+(251),y1+(5))
      glVertex2f(x1+(251),y1+(245))
      glVertex2f(x1+(248),y1+(245))
      glEnd()    

      glBegin(GL_POLYGON)
      glColor3f(1,1,1)
      for i in range(50):
          cos = self.radius * np.cos(i * 2 * np.pi / 50) + x1+(250)
          sin = self.radius * np.sin(i * 2 * np.pi / 50) + y1+(125)
          glVertex2f(cos, sin)
      glEnd()

      glBegin(GL_POLYGON)
      glColor3f(0.3,0.8,1)
      for i in range(50):
          cos = self.radius2 * np.cos(i * 2 * np.pi / 50) + x1+(250)
          sin = self.radius2 * np.sin(i * 2 * np.pi / 50) + y1+(125)
          glVertex2f(cos, sin)
      glEnd()

      glBegin(GL_POLYGON)
      glColor3f(1,1,1)
      for i in range(50):
          cos = self.radius3 * np.cos(i * 2 * np.pi / 50) + x1+(250)
          sin = self.radius3 * np.sin(i * 2 * np.pi / 50) + y1+(125)
          glVertex2f(cos, sin)
      glEnd()

  def DesenhaObjeto(self,width, height, x, y,color):
    
    x_step = 0
    y_step = 0
    
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_QUADS)

    glVertex2f(-1*width + x*self.window_coordinates + x_step,-1*height + y*self.window_coordinates + y_step)
    glVertex2f(-1*width + x*self.window_coordinates + x_step,1*height + y*self.window_coordinates + y_step)
    glVertex2f(1*width + x*self.window_coordinates + x_step,1*height + y*self.window_coordinates + y_step)
    glVertex2f(1*width + x*self.window_coordinates + x_step,-1*height + y*self.window_coordinates + y_step)

    glEnd()

  def Desenha(self):    
    glClear(GL_COLOR_BUFFER_BIT)
    
    glViewport(0,0,self.screensize[0], self.screensize[1])
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0,300,0,250)
    
    self.Background()

    glViewport(0,0,self.screensize[0], self.screensize[1])
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-130,150,-130,150)

    if self.timer_red and self.delta_time_red < 500:
      self.red_ball._draw_explosion_(self.explosion_x, self.explosion_y)

    glViewport(0,0,self.screensize[0], self.screensize[1])
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-self.window_coordinates,self.window_coordinates,-self.window_coordinates,self.window_coordinates)
    
    self.DesenhaObjeto(self.window_coordinates, self.player_size, 0,1,(.7,.7,.7))
    self.DesenhaObjeto(self.window_coordinates, self.player_size, 0,-1,(.7,.7,.7))
    self.DesenhaObjeto(10,10,-.25,1,(0,0,0))
    self.DesenhaObjeto(10,10,0,1,(.8,0,0))
    self.DesenhaObjeto(10,10,.25,1,(0,0,0))
          
    self.player1._draw_player_()
    self.player2._draw_player_()

    self.DesenhaTexto(string = str(self.player1.score), pos = 0)
    self.DesenhaTexto(string = str(self.player2.score), pos= 1)
    
    self.ball._draw_ball_()
    self.red_ball._draw_ball_()

    self.DesenhaTexto(string = f"{self.remaining_time:.1f}", pos = 2)
    
    glutSwapBuffers()

  def Timer(self,value):
    self.t = glutGet(GLUT_ELAPSED_TIME) - self.reset_time
    self.delta_time_red = self.t - self.timer_red

    if  self.game_time_limit - (self.t/1000 - self.hold_time) <= 0:
      if self.player1.score > self.player2.score : 
        resultado = "Ganhador: Player 1"
      elif self.player1.score < self.player2.score : 
        resultado = "Ganhador: Player 2"
      else:
        resultado = "Empate"
      self.DesenhaTexto(string = f"Fim de jogo.", result = resultado)
      glutSwapBuffers()
      self.pause_game = True
      self.end_game = True
    self.remaining_time = self.game_time_limit - (self.t/1000 - self.hold_time)
    
    if not self.pause_game:
      if self.ball.x < 0:
        condicao_x = abs(self.ball.x) + abs(self.ball.xstep) >= self.window_coordinates-self.player1.width
        if self.ball.y > 0:
          is_y_above_bottom = (self.ball.y) + self.ball.radius >= (self.player1.y) - self.player1.height/2
          is_y_below_top = (self.ball.y)  - self.ball.radius <= (self.player1.y) + self.player1.height/2
        else:
          is_y_above_bottom = -self.ball.y - self.ball.radius <= -self.player1.y + self.player1.height/2
          is_y_below_top = -self.ball.y  + self.ball.radius >= -self.player1.y - self.player1.height/2
        condicao_y = is_y_above_bottom and is_y_below_top

        if condicao_x and condicao_y:
            self.ball.xstep = self.ball_colision/10*abs(self.initial_speed) + self.initial_speed
            self.ball_colision += 1          
            self.red_ball.xstep *= 1.15
            self.ball.x += 1

      if self.ball.x > 0:
        condicao_x = abs(self.ball.x) + abs(self.ball.xstep) >= self.window_coordinates-self.player2.width/2
        if self.ball.y > 0:
          is_y_above_bottom = (self.ball.y) + self.ball.radius >= (self.player2.y) - self.player2.height/2
          is_y_below_top = (self.ball.y)  - self.ball.radius <= (self.player2.y) + self.player2.height/2
        else:
          is_y_above_bottom = -self.ball.y - self.ball.radius <= -self.player2.y + self.player2.height/2
          is_y_below_top = -self.ball.y  + self.ball.radius >= -self.player2.y - self.player2.height/2

        condicao_y = is_y_above_bottom and is_y_below_top

        if condicao_x and condicao_y:            
            self.ball.xstep = -(self.ball_colision/10*abs(self.initial_speed) + self.initial_speed)
            self.ball_colision += 1        
            self.red_ball.xstep *= 1.15
            self.ball.x -= 1
      
      if abs(self.ball.y) > self.window_coordinates-20:
        self.ball.ystep *= -1

      if abs(self.ball.x) > self.window_coordinates:
        if self.ball.x > 0:
          self.player1.score += 1
        else:
          self.player2.score += 1

        self.ball = Ball(0 ,0 , self.ball_radius, self.initial_speed)

        self.red_ball = Ball(0,0,self.ball_radius,self.initial_speed, 1)
        self.red_ball_colision = 0
        self.ball_colision = 0
      self.ball.x += self.ball.xstep
      self.ball.y += self.ball.ystep
      
      glutPostRedisplay()
      glutTimerFunc(33, self.Timer, 1)

  def TimerRed(self,value):
    if not self.pause_game:
      if self.red_ball.x < 0:        
        condicao_x = abs(self.red_ball.x) + abs(self.red_ball.xstep) >= self.window_coordinates-self.player1.width
        if self.red_ball.y > 0:
          is_y_above_bottom = (self.red_ball.y) + self.red_ball.radius >= (self.player2.y) - self.player2.height/2
          is_y_below_top = (self.red_ball.y)  - self.red_ball.radius <= (self.player2.y) + self.player2.height/2
        else:
          is_y_above_bottom = -self.red_ball.y - self.red_ball.radius <= -self.player2.y + self.player2.height/2
          is_y_below_top = -self.red_ball.y  + self.red_ball.radius >= -self.player2.y - self.player2.height/2
        condicao_y = is_y_above_bottom and is_y_below_top

        if condicao_x and condicao_y:
            self.player1.score -= 1        
            self.explosion_x, self.explosion_y = self.player1.x, self.player1.y
            self.red_ball = Ball(0,0,self.ball_radius, self.initial_speed, 1)
            self.timer_red = self.t
      if self.red_ball.x > 0:        
        condicao_x = abs(self.red_ball.x) + abs(self.red_ball.xstep) >= self.window_coordinates-self.player2.width
        if self.red_ball.y > 0:
          is_y_above_bottom = (self.red_ball.y) + self.red_ball.radius >= (self.player2.y) - self.player2.height/2
          is_y_below_top = (self.red_ball.y)  - self.red_ball.radius <= (self.player2.y) + self.player2.height/2
        else:
          is_y_above_bottom = -self.red_ball.y - self.red_ball.radius <= -self.player2.y + self.player2.height/2
          is_y_below_top = -self.red_ball.y  + self.red_ball.radius >= -self.player2.y - self.player2.height/2
        condicao_y = is_y_above_bottom and is_y_below_top

        if condicao_x and condicao_y:
            self.player2.score -= 1
            self.explosion_x, self.explosion_y = self.player2.x, self.player2.y
            self.red_ball = Ball(0,0,self.ball_radius, self.initial_speed, 1)
            self.timer_red = self.t
      if abs(self.red_ball.y) > self.window_coordinates-20:
        self.red_ball.ystep *= -1
      if abs(self.red_ball.x) > self.window_coordinates:
        self.old_red_ball_speed =  self.red_ball_colision/10*abs(self.ball.xstep) + self.initial_speed
        self.red_ball = Ball(0,0,self.ball_radius, self.old_red_ball_speed, 1)
      self.red_ball.x += self.red_ball.xstep
      self.red_ball.y += self.red_ball.ystep
      
      glutPostRedisplay()
      glutTimerFunc(33, self.TimerRed, 1)

  def HandleMenu(self,op):
    match op:
      case 0:
        if not self.pause_game:
          self.hold_time += glutGet(GLUT_ELAPSED_TIME) / 1000
          self.pause_game = True
      case 1:
        if self.pause_game and not self.end_game:
          self.hold_time = glutGet(GLUT_ELAPSED_TIME) / 1000 - self.hold_time
          self.pause_game = False
          glutTimerFunc(33, self.Timer, 1)
          glutTimerFunc(33, self.TimerRed, 1)    
      case 2:
        self.player1.score = 0
        self.player2.score = 0

        self.reset_time = glutGet(GLUT_ELAPSED_TIME)
        self.remaining_time = self.game_time_limit
        self.hold_time = 0      
        self.timer_red = 0
        self.delta_time_red = 0
        
        self.ball.x, self.ball.y = 0,0
        self.ball.ball_speed = self.initial_speed
        self.ball.xstep = self.ball.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -self.ball.ball_speed*np.cos(np.pi/4)
        y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
        self.ball.ystep = self.ball.ball_speed*np.sin(y_direction) if random.randint(0,1) == 1 else -self.ball.ball_speed*(np.sin(y_direction))
      
        self.red_ball.x, self.red_ball.y = 0,0
        self.red_ball.ball_speed = self.initial_speed
        self.red_ball.xstep = self.red_ball.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -self.red_ball.ball_speed*np.cos(np.pi/4)
        y_direction = random.choice([np.pi/(i/10) for i in range(25,60)])
        self.red_ball.ystep = self.red_ball.ball_speed*np.sin(y_direction) if random.randint(0,1) == 1 else -self.red_ball.ball_speed*(np.sin(y_direction))
        
        if self.pause_game:
          self.end_game = False
          self.pause_game = False
          glutTimerFunc(33, self.Timer, 1)
          glutTimerFunc(33, self.TimerRed, 1)    
      case -1:
        glutLeaveMainLoop()

    return 0

  def CriaMenu(self,):
    glutCreateMenu(self.HandleMenu)
    glutAddMenuEntry("Pausar", 0)
    glutAddMenuEntry("Voltar", 1)
    glutAddMenuEntry("Reiniciar", 2)
    glutAddMenuEntry("Sair", -1)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

  def Teclado(self,key, x, y):
    if key == b'\x08':
      glutLeaveMainLoop()

    if not self.pause_game:
      match key:
        case b"w":
          if self.player1.y + 2*self.player_size <= self.window_coordinates - self.player_size:
            self.player1.y += 2*self.player_size
        case b"s":
          if self.player1.y - 2*self.player_size >= -self.window_coordinates + self.player_size:
            self.player1.y -= 2*self.player_size
        case 101:
          if self.player2.y + 2*self.player_size <= self.window_coordinates - self.player_size:
            self.player2.y += 2*self.player_size
        case 103:
          if self.player2.y - 2*self.player_size >= -self.window_coordinates + self.player_size:
              self.player2.y -= 2*self.player_size
    
      glutPostRedisplay()     

  def DesenhaTexto(self,string, result = None, pos = -1):
      glPushMatrix()
      glColor3f(1.0, 1.0, 1.0)
      if pos == 0:
        glRasterPos2f(-25,92.5)
      elif pos == 1:
        glRasterPos2f(25,92.5)
      elif pos == 2:
        glRasterPos2f(-3.25,92.5)
      else:
        glRasterPos2f(-7.5,0)

      if result:
          glColor3f(0.0, 0.0, 0.0)
          glRasterPos2f(-15,0)
          for char in result:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))
          
      else:
        for char in string:     
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(char))                                
      
      glPopMatrix()

  def main(self):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(self.screensize[0], self.screensize[1])
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"Uber Loveable Frog")
    #glutFullScreen()
    glutDisplayFunc(self.Desenha)
    glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
    glutKeyboardFunc(self.Teclado)
    glutSpecialFunc(self.Teclado)
    glutTimerFunc(33, self.Timer if not self.pause_game else lambda x:None, 1)
    glutTimerFunc(33, self.TimerRed if not self.pause_game else lambda x:None, 1)
    self.CriaMenu()
    glClearColor(0.3, 0.8, 1, 1)
    glutMainLoop()

if __name__ == "__main__":
  uber_loveable_frog = Main(
    game_time_limit=30, 
    player_size =10,
    initial_speed=3,
    radius=3.5
  )