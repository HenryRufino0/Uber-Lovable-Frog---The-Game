from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Player():
  def __init__(self, x, y, s, name):
    if name =="protagonista":      
      self.width = 1*s
      self.height = 2*s
      self.x = x + self.width/2
    if name =="inimigo":
      self.width = 1.5*s
      self.height = 3*s
      self.x = x - self.width/2
    self.y = y
    self.score = 0
    self.type = name

  def _draw_player_(self):
    if self.type=="protagonista":
      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*2, self.y - self.height/2 + self.height/6*2)
      glVertex2f(self.x -11/18*self.width + self.width/18*2, self.y - self.height/2 + self.height/6*3.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*20, self.y - self.height/2 + self.height/6*3.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*20, self.y - self.height/2 + self.height/6*2)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*3,self.y - self.height/2 + self.height/6*1.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*3,self.y - self.height/2 + self.height/6*4)
      glVertex2f(self.x -11/18*self.width + self.width/18*19,self.y - self.height/2 + self.height/6*4)
      glVertex2f(self.x -11/18*self.width + self.width/18*19,self.y - self.height/2 + self.height/6*1.5)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*6,self.y - self.height/2 + self.height/6*1)
      glVertex2f(self.x -11/18*self.width + self.width/18*6,self.y - self.height/2 + self.height/6*1.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*16,self.y - self.height/2 + self.height/6*1.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*16,self.y - self.height/2 + self.height/6*1)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*6,self.y - self.height/2 + self.height/6*4)
      glVertex2f(self.x -11/18*self.width + self.width/18*6,self.y - self.height/2 + self.height/6*6)
      glVertex2f(self.x -11/18*self.width + self.width/18*10,self.y - self.height/2 + self.height/6*6)
      glVertex2f(self.x -11/18*self.width + self.width/18*10,self.y - self.height/2 + self.height/6*4)
      glEnd()

      glColor3f(0,1,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*16,self.y - self.height/2 + self.height/6*4)
      glVertex2f(self.x -11/18*self.width + self.width/18*16,self.y - self.height/2 + self.height/6*6)
      glVertex2f(self.x -11/18*self.width + self.width/18*12,self.y - self.height/2 + self.height/6*6)
      glVertex2f(self.x -11/18*self.width + self.width/18*12,self.y - self.height/2 + self.height/6*4)
      glEnd()
    
      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*7,self.y - self.height/2 + self.height/6*4.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*7,self.y - self.height/2 + self.height/6*5.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*9,self.y - self.height/2 + self.height/6*5.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*9,self.y - self.height/2 + self.height/6*4.5)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*7.6,self.y - self.height/2 + self.height/6*4.8)
      glVertex2f(self.x -11/18*self.width + self.width/18*7.6,self.y - self.height/2 + self.height/6*5.2)
      glVertex2f(self.x -11/18*self.width + self.width/18*8.4,self.y - self.height/2 + self.height/6*5.2)
      glVertex2f(self.x -11/18*self.width + self.width/18*8.4,self.y - self.height/2 + self.height/6*4.8)
      glEnd()

      glColor(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*13,self.y - self.height/2 + self.height/6*4.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*13,self.y - self.height/2 + self.height/6*5.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*15,self.y - self.height/2 + self.height/6*5.5)
      glVertex2f(self.x -11/18*self.width + self.width/18*15,self.y - self.height/2 + self.height/6*4.5)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f(self.x -11/18*self.width + self.width/18*13.6,self.y - self.height/2 + self.height/6*4.8)
      glVertex2f(self.x -11/18*self.width + self.width/18*13.6,self.y - self.height/2 + self.height/6*5.2)
      glVertex2f(self.x -11/18*self.width + self.width/18*14.4,self.y - self.height/2 + self.height/6*5.2)
      glVertex2f(self.x -11/18*self.width + self.width/18*14.4,self.y - self.height/2 + self.height/6*4.8)
      glEnd()

      glColor3f(1,0,0)
      glBegin(GL_LINES)
      glVertex2f(self.x -11/18*self.width + self.width/18*7,self.y - self.height/2 + self.height/6*2)
      glVertex2f(self.x -11/18*self.width + self.width/18*15,self.y - self.height/2 + self.height/6*2)
      
      glVertex2f(self.x -11/18*self.width + self.width/18*7,self.y - self.height/2 + self.height/6*2.3)
      glVertex2f(self.x -11/18*self.width + self.width/18*7,self.y - self.height/2 + self.height/6*2)

      glVertex2f(self.x -11/18*self.width + self.width/18*15,self.y - self.height/2 + self.height/6*2.3)
      glVertex2f(self.x -11/18*self.width + self.width/18*15,self.y - self.height/2 + self.height/6*2)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_TRIANGLES)
      glVertex2f(self.x -11/18*self.width + self.width/18*11,self.y - self.height/2 + self.height/6*1)
      glVertex2f(self.x -11/18*self.width + self.width/18*16,self.y - self.height/2 + self.height/6*2)
      glVertex2f(self.x -11/18*self.width + self.width/18*16,self.y - self.height/2 + self.height/6*0)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_TRIANGLES)
      glVertex2f(self.x -11/18*self.width + self.width/18*11,self.y - self.height/2 + self.height/6*1)
      glVertex2f(self.x -11/18*self.width + self.width/18*6,self.y - self.height/2 + self.height/6*2)
      glVertex2f(self.x -11/18*self.width + self.width/18*6,self.y - self.height/2 + self.height/6*0)
      glEnd()

    if self.type=='inimigo':
      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glEnd()

      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.52),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.52),self.y -5*self.height/6 + 5*self.height/3*0.75)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.78),self.y -5*self.height/6 + 5*self.height/3*0.75)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.78),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glEnd()

      glColor3f(1,1,1)
      glBegin(GL_QUADS)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.55),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.55),self.y -5*self.height/6 + 5*self.height/3*0.80)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.75),self.y -5*self.height/6 + 5*self.height/3*0.80)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.75),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_QUADS)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.57),self.y -5*self.height/6 + 5*self.height/3*0.60)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.57),self.y -5*self.height/6 + 5*self.height/3*0.65)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.62),self.y -5*self.height/6 + 5*self.height/3*0.65)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.62),self.y -5*self.height/6 + 5*self.height/3*0.60)
      glEnd()

      glColor3f(0,0,0)
      glBegin(GL_LINES)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.57),self.y -5*self.height/6 + 5*self.height/3*0.65)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.63),self.y -5*self.height/6 + 5*self.height/3*0.68)
      glEnd()

      glColor3f(1,1,0)
      glBegin(GL_TRIANGLES)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.55)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.2),self.y -5*self.height/6 + 5*self.height/3*0.5)
  
      glEnd()
      glColor3f(0,0,0)
      glBegin(GL_LINES)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.2),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.60)
      glEnd()

      glColor3f(0.8,0.4,0)
      glBegin(GL_POLYGON)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.55),self.y -5*self.height/6 + 5*self.height/3*0.55)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.59),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.63),self.y -5*self.height/6 + 5*self.height/3*0.55)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.67),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.71),self.y -5*self.height/6 + 5*self.height/3*0.55)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.75),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.79),self.y -5*self.height/6 + 5*self.height/3*0.55)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glEnd()

      glColor(0,0,0)
      glBegin(GL_LINES)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.55)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.55)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.2),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.2),self.y -5*self.height/6 + 5*self.height/3*0.5)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.52),self.y -5*self.height/6 + 5*self.height/3*0.70)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.52),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.52),self.y -5*self.height/6 + 5*self.height/3*0.75)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.52),self.y -5*self.height/6 + 5*self.height/3*0.75)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.55),self.y -5*self.height/6 + 5*self.height/3*0.75)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.55),self.y -5*self.height/6 + 5*self.height/3*0.75)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.55),self.y -5*self.height/6 + 5*self.height/3*0.80)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.55),self.y -5*self.height/6 + 5*self.height/3*0.80)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.75),self.y -5*self.height/6 + 5*self.height/3*0.80)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.75),self.y -5*self.height/6 + 5*self.height/3*0.80)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.75),self.y -5*self.height/6 + 5*self.height/3*0.75)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.75),self.y -5*self.height/6 + 5*self.height/3*0.75)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.78),self.y -5*self.height/6 + 5*self.height/3*0.75)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.78),self.y -5*self.height/6 + 5*self.height/3*0.75)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.78),self.y -5*self.height/6 + 5*self.height/3*0.70)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.78),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.70)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.70)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.2)

      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.80),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glVertex2f((self.x + -5*self.width/6 + 5*self.width/3*0.5),self.y -5*self.height/6 + 5*self.height/3*0.2)
      glEnd()
