from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import *

global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep,lsize,psize,qsize,ystepqsize

x1 = 0
y1 = 0

points = 50
radius = 40



def Desenha():
    global windowWidth,windowHeight,x1,y1,points,radius
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    import math
    

    glBegin(GL_POLYGON)
    glColor3f(0,0,1)
    for i in range(points):
        cos = radius * math.cos(i * 2 * math.pi / points) + x1+2*radius
        sin = radius * math.sin(i * 2 * math.pi / points) + y1+2*radius
        glVertex2f(cos, sin)
    glEnd()

    glColor(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x1+1.8*radius,y1+3*radius)
    glVertex2f(x1+2.2*radius,y1+3*radius)
    glVertex2f(x1+2.2*radius,y1+radius)
    glVertex2f(x1+1.8*radius,y1+radius)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+radius,y1+1.8*radius)
    glVertex2f(x1+radius,y1+2.2*radius)
    glVertex2f(x1+3*radius,y1+2.2*radius)
    glVertex2f(x1+3*radius,y1+1.8*radius)
    glEnd()
   
    
    glutSwapBuffers()

    

def Inicializa():   
    glClearColor(1.0, 1.0, 1.0, 1.0)

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
        windowHeight = 250*h/w
        windowWidth = 250.0
    else:
        windowWidth = 250.0*w/h
        windowHeight = 250.0

    #windowWidth = w
    #windowHeight = h
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(600,600);
    glutInitWindowPosition(10,10);
    glutCreateWindow(b"Anima");
    glutDisplayFunc(Desenha);
    glutReshapeFunc(AlteraTamanhoJanela);
    
    Inicializa();
    glutMainLoop();

main()

