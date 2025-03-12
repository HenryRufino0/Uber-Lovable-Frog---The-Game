import random
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Ball():
  def __init__(self, x, y, r, s, red = 0):
    self.red = red
    self.x = x
    self.y = y
    self.radius = r    
    self.points = 50
    self.ball_speed = s
    _y_direction = random.choice([np.pi/(i/10) for i in range(25,150)])
    self.xstep = self.ball_speed*np.cos(np.pi/4) if random.randint(0,1) == 1 else -self.ball_speed*np.cos(np.pi/4)
    self.ystep = self.ball_speed*(np.sin(_y_direction)) if random.randint(0,1) == 1 else -self.ball_speed*(np.sin(_y_direction))

  def _draw_ball_(self):
    if self.red:
      glBegin(GL_POLYGON)
      glColor3f(0,0,1)
      for i in range(self.points):
          cos = self.radius * np.cos(i * 2 * np.pi / self.points) + self.x
          sin = 1.5*self.radius * np.sin(i * 2 * np.pi / self.points) + self.y
          glVertex2f(cos, sin)
      glEnd()

      glColor(1,0,0)
      glBegin(GL_POLYGON)
      glVertex2f(1.8*self.radius - 2*self.radius + self.x,3.5*self.radius- 2*self.radius+self.y)
      glVertex2f(2.2*self.radius- 2*self.radius+ self.x,3.5*self.radius- 2*self.radius+self.y)
      glVertex2f(2.2*self.radius- 2*self.radius+ self.x,.5*self.radius- 2*self.radius+self.y)
      glVertex2f(1.8*self.radius- 2*self.radius+ self.x,.5*self.radius- 2*self.radius+self.y)
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(self.radius- 2*self.radius+ self.x,1.8*self.radius- 2*self.radius+self.y)
      glVertex2f(self.radius- 2*self.radius+ self.x,2.2*self.radius- 2*self.radius+self.y)
      glVertex2f(3*self.radius- 2*self.radius+ self.x,2.2*self.radius- 2*self.radius+self.y)
      glVertex2f(3*self.radius- 2*self.radius+ self.x,1.8*self.radius- 2*self.radius+self.y)
      glEnd()
    
    else:
      glBegin(GL_POLYGON)
      glColor3f(1,1,1)
      for i in range(self.points):
          cos = self.radius * np.cos(i * 2 * np.pi / self.points) + self.x
          sin = 1.5*self.radius * np.sin(i * 2 * np.pi / self.points) + self.y
          glVertex2f(cos, sin)
      glEnd()

  def _draw_explosion_(self,x, y):
    if self.red:
      glColor3f(1,0,0)
      glBegin(GL_POLYGON)
      glVertex2f(x+(-30),y+(-30))
      glVertex2f(x+(+0),y+(-10))
      glVertex2f(x+(-10),y+(+0))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(-30),y+(+30))
      glVertex2f(x+(+0),y+(+10))
      glVertex2f(x+(-10),y+(+0))
      glEnd()
      
      glBegin(GL_POLYGON)
      glVertex2f(x+(+30),y+(+30))
      glVertex2f(x+(+0),y+(+10))
      glVertex2f(x+(+10),y+(+0))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(+30),y+(-30))
      glVertex2f(x+(+0),y+(-10))
      glVertex2f(x+(+10),y+(+0))
      glEnd()

      

  #Parte Vermelha
      
      glColor3f(1,0,0)
      glBegin(GL_POLYGON)
      glVertex2f(x+(+0),y+(-50))
      glVertex2f(x+(-10),y+(-10))
      glVertex2f(x+(+10),y+(-10))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(-10),y+(-10))
      glVertex2f(x+(-50),y+(+0))
      glVertex2f(x+(-10),y+(+10))
      glEnd()
      
      glBegin(GL_POLYGON)
      glVertex2f(x+(+0),y+(+50))
      glVertex2f(x+(+10),y+(+10))
      glVertex2f(x+(-10),y+(+10))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(+50),y+(+0))
      glVertex2f(x+(+10),y+(+10))
      glVertex2f(x+(+10),y+(-10))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(-10),y+(-10))
      glVertex2f(x+(-10),y+(+10))
      glVertex2f(x+(+10),y+(+10))
      glVertex2f(x+(+10),y+(-10))
      glEnd()

  #Parte Traseira Amarela

      glColor(1,1,0)
      glBegin(GL_POLYGON)
      glVertex2f(x+(-25),y+(-25))
      glVertex2f(x+(+0),y+(-5))
      glVertex2f(x+(-5),y+(+0))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(-25),y+(+25))
      glVertex2f(x+(+0),y+(+5))
      glVertex2f(x+(-5),y+(+0))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(+25),y+(+25))
      glVertex2f(x+(+0),y+(+5))
      glVertex2f(x+(+5),y+(+0))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(+25),y+(-25))
      glVertex2f(x+(+0),y+(-5))
      glVertex2f(x+(+5),y+(+0))
      glEnd()

  #Parte Amarela
      
      glColor3f(1,1,0)
      glBegin(GL_POLYGON)
      glVertex2f(x+(+0),y+(-40))
      glVertex2f(x+(-5),y+(-5))
      glVertex2f(x+(+5),y+(-5))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(-5),y+(-5))
      glVertex2f(x+(-40),y+(+0))
      glVertex2f(x+(-5),y+(+5))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(+0),y+(+40))
      glVertex2f(x+(+5),y+(+5))
      glVertex2f(x+(-5),y+(+5))
      glEnd()

      glBegin(GL_POLYGON)
      glVertex2f(x+(+40),y+(+0))
      glVertex2f(x+(+5),y+(+5))
      glVertex2f(x+(+5),y+(-5))
      glEnd()
      
      glBegin(GL_POLYGON)
      glVertex2f(x+(-5),y+(-5))
      glVertex2f(x+(-5),y+(+5))
      glVertex2f(x+(+5),y+(+5))
      glVertex2f(x+(+5),y+(-5))
      glEnd()
