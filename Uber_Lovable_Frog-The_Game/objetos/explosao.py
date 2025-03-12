from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep,lsize,psize,qsize,ystepqsize

x1 = 0
y1 = 0

rsize = 100

xstep = 1.0
ystep = 1.0


def Desenha():
    global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep,lsize,psize,qsize,xstep,ystep
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT)

#Parte Traseira Vermelha

    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-30),y1+(rsize-30))
    glVertex2f(x1+(rsize+0),y1+(rsize-10))
    glVertex2f(x1+(rsize-10),y1+(rsize+0))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-30),y1+(rsize+30))
    glVertex2f(x1+(rsize+0),y1+(rsize+10))
    glVertex2f(x1+(rsize-10),y1+(rsize+0))
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+30),y1+(rsize+30))
    glVertex2f(x1+(rsize+0),y1+(rsize+10))
    glVertex2f(x1+(rsize+10),y1+(rsize+0))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+30),y1+(rsize-30))
    glVertex2f(x1+(rsize+0),y1+(rsize-10))
    glVertex2f(x1+(rsize+10),y1+(rsize+0))
    glEnd()

    

#Parte Vermelha
    
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+0),y1+(rsize-50))
    glVertex2f(x1+(rsize-10),y1+(rsize-10))
    glVertex2f(x1+(rsize+10),y1+(rsize-10))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-10),y1+(rsize-10))
    glVertex2f(x1+(rsize-50),y1+(rsize+0))
    glVertex2f(x1+(rsize-10),y1+(rsize+10))
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+0),y1+(rsize+50))
    glVertex2f(x1+(rsize+10),y1+(rsize+10))
    glVertex2f(x1+(rsize-10),y1+(rsize+10))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+50),y1+(rsize+0))
    glVertex2f(x1+(rsize+10),y1+(rsize+10))
    glVertex2f(x1+(rsize+10),y1+(rsize-10))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-10),y1+(rsize-10))
    glVertex2f(x1+(rsize-10),y1+(rsize+10))
    glVertex2f(x1+(rsize+10),y1+(rsize+10))
    glVertex2f(x1+(rsize+10),y1+(rsize-10))
    glEnd()

#Parte Traseira Amarela

    glColor(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-25),y1+(rsize-25))
    glVertex2f(x1+(rsize+0),y1+(rsize-5))
    glVertex2f(x1+(rsize-5),y1+(rsize+0))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-25),y1+(rsize+25))
    glVertex2f(x1+(rsize+0),y1+(rsize+5))
    glVertex2f(x1+(rsize-5),y1+(rsize+0))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+25),y1+(rsize+25))
    glVertex2f(x1+(rsize+0),y1+(rsize+5))
    glVertex2f(x1+(rsize+5),y1+(rsize+0))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+25),y1+(rsize-25))
    glVertex2f(x1+(rsize+0),y1+(rsize-5))
    glVertex2f(x1+(rsize+5),y1+(rsize+0))
    glEnd()

#Parte Amarela
    
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+0),y1+(rsize-40))
    glVertex2f(x1+(rsize-5),y1+(rsize-5))
    glVertex2f(x1+(rsize+5),y1+(rsize-5))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-5),y1+(rsize-5))
    glVertex2f(x1+(rsize-40),y1+(rsize+0))
    glVertex2f(x1+(rsize-5),y1+(rsize+5))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+0),y1+(rsize+40))
    glVertex2f(x1+(rsize+5),y1+(rsize+5))
    glVertex2f(x1+(rsize-5),y1+(rsize+5))
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize+40),y1+(rsize+0))
    glVertex2f(x1+(rsize+5),y1+(rsize+5))
    glVertex2f(x1+(rsize+5),y1+(rsize-5))
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize-5),y1+(rsize-5))
    glVertex2f(x1+(rsize-5),y1+(rsize+5))
    glVertex2f(x1+(rsize+5),y1+(rsize+5))
    glVertex2f(x1+(rsize+5),y1+(rsize-5))
    glEnd()




    
    glutSwapBuffers()

def Inicializa():   
    glClearColor(0.0, 0.0, 0.0, 1.0)

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

