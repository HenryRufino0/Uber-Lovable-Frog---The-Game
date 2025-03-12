from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import *

global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep,lsize,psize,qsize,ystepqsize

x1 = 0
y1 = 0

rsize = 0
points = 50
radius = 25
radius2 = 23
radius3 = 2


xstep = 1.0
ystep = 1.0


def Desenha():
    global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep,lsize,psize,qsize,xstep,ystep
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT)
         
    glColor3f(1,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize+0),y1+(rsize+0))
    glVertex2f(x1+(rsize+0),y1+(rsize+600))
    glVertex2f(x1+(rsize+3),y1+(rsize+600))
    glVertex2f(x1+(rsize+3),y1+(rsize+0))
    glEnd()

    
    glColor3f(1,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize+497),y1+(rsize+0))
    glVertex2f(x1+(rsize+497),y1+(rsize+600))
    glVertex2f(x1+(rsize+500),y1+(rsize+600))
    glVertex2f(x1+(rsize+500),y1+(rsize+0))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize+0),y1+(rsize+0))
    glVertex2f(x1+(rsize+500),y1+(rsize+0))
    glVertex2f(x1+(rsize+500),y1+(rsize+5))
    glVertex2f(x1+(rsize+0),y1+(rsize+5))
    glEnd()

    glColor(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize+0),y1+(rsize+245))
    glVertex2f(x1+(rsize+500),y1+(rsize+245))
    glVertex2f(x1+(rsize+500),y1+(rsize+600))
    glVertex2f(x1+(rsize+0),y1+(rsize+600))
    glEnd()

    glColor(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize+248),y1+(rsize+5))
    glVertex2f(x1+(rsize+251),y1+(rsize+5))
    glVertex2f(x1+(rsize+251),y1+(rsize+245))
    glVertex2f(x1+(rsize+248),y1+(rsize+245))
    glEnd()

    

    import math
    

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for i in range(points):
        cos = radius * math.cos(i * 2 * math.pi / points) + x1+(rsize+250)
        sin = radius * math.sin(i * 2 * math.pi / points) + y1+(rsize+125)
        glVertex2f(cos, sin)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.3,0.8,1)
    for i in range(points):
        cos = radius2 * math.cos(i * 2 * math.pi / points) + x1+(rsize+250)
        sin = radius2 * math.sin(i * 2 * math.pi / points) + y1+(rsize+125)
        glVertex2f(cos, sin)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    for i in range(points):
        cos = radius3 * math.cos(i * 2 * math.pi / points) + x1+(rsize+250)
        sin = radius3 * math.sin(i * 2 * math.pi / points) + y1+(rsize+125)
        glVertex2f(cos, sin)
    glEnd()
    
    
    

    

    glutSwapBuffers()

def Inicializa():   
    glClearColor(0.3, 0.8, 1, 1)

def AlteraTamanhoJanela(w, h):
    global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep
    # Evita a divisao por zero
    if(h == 0):
        h = 1
                           
    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Estabelece a janela de seleção (left, right, bottom, top)     
    if (w <= h):
        windowHeight = 250.0*h/w
        windowWidth = 250.0
    else:
        windowWidth = 250.0*w/h
        windowHeight = 250.0

    #windowWidth = w
    #windowHeight = h
    gluOrtho2D(0.0, windowWidth,0,windowHeight)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(1200,600);
    glutInitWindowPosition(10,10);
    glutCreateWindow(b"Anima");
    glutDisplayFunc(Desenha);
    glutReshapeFunc(AlteraTamanhoJanela);
    
    Inicializa();
    glutMainLoop();

main()

