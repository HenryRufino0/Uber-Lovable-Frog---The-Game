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
         
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize/2),y1+(rsize/5))
    glVertex2f(x1+(rsize/2),y1+(rsize*0.70))
    glVertex2f(x1+(rsize*0.80),y1+(rsize*0.70))
    glVertex2f(x1+(rsize*0.80),y1+(rsize/5))
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize*0.52),y1+(rsize/5))
    glVertex2f(x1+(rsize*0.52),y1+(rsize*0.75))
    glVertex2f(x1+(rsize*0.78),y1+(rsize*0.75))
    glVertex2f(x1+(rsize*0.78),y1+(rsize/5))
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize*0.55),y1+(rsize/5))
    glVertex2f(x1+(rsize*0.55),y1+(rsize*0.80))
    glVertex2f(x1+(rsize*0.75),y1+(rsize*0.80))
    glVertex2f(x1+(rsize*0.75),y1+(rsize/5))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_QUADS)
    glVertex2f(x1+(rsize*0.57),y1+(rsize*0.60))
    glVertex2f(x1+(rsize*0.57),y1+(rsize*0.65))
    glVertex2f(x1+(rsize*0.62),y1+(rsize*0.65))
    glVertex2f(x1+(rsize*0.62),y1+(rsize*0.60))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(x1+(rsize*0.57),y1+(rsize*0.65))
    glVertex2f(x1+(rsize*0.63),y1+(rsize*0.68))
    glEnd()

    glColor3f(1,1,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1+(rsize/2),y1+(rsize*0.55))
    glVertex2f(x1+(rsize/2),y1+(rsize*0.70))
    glVertex2f(x1+(rsize/5),y1+(rsize/2))
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(x1+(rsize/5),y1+(rsize/2))
    glVertex2f(x1+(rsize/2),y1+(rsize*0.60))
    glEnd()

    glColor3f(0.8,0.4,0)
    glBegin(GL_POLYGON)
    glVertex2f(x1+(rsize/2),y1+(rsize/5))
    glVertex2f(x1+(rsize/2),y1+(rsize/2))
    glVertex2f(x1+(rsize*0.55),y1+(rsize*0.55))
    glVertex2f(x1+(rsize*0.59),y1+(rsize/2))
    glVertex2f(x1+(rsize*0.63),y1+(rsize*0.55))
    glVertex2f(x1+(rsize*0.67),y1+(rsize/2))
    glVertex2f(x1+(rsize*0.71),y1+(rsize*0.55))
    glVertex2f(x1+(rsize*0.75),y1+(rsize/2))
    glVertex2f(x1+(rsize*0.79),y1+(rsize*0.55))
    glVertex2f(x1+(rsize*0.80),y1+(rsize/2))
    glVertex2f(x1+(rsize*0.80),y1+(rsize/5))
    glEnd()

    glColor(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(x1+(rsize/2),y1+(rsize/5))
    glVertex2f(x1+(rsize/2),y1+(rsize*0.55))

    glVertex2f(x1+(rsize/2),y1+(rsize*0.55))
    glVertex2f(x1+(rsize/5),y1+(rsize/2))

    glVertex2f(x1+(rsize/5),y1+(rsize/2))
    glVertex2f(x1+(rsize/2),y1+(rsize*0.70))

    glVertex2f(x1+(rsize/2),y1+(rsize*0.70))
    glVertex2f(x1+(rsize*0.52),y1+(rsize*0.70))

    glVertex2f(x1+(rsize*0.52),y1+(rsize*0.70))
    glVertex2f(x1+(rsize*0.52),y1+(rsize*0.75))

    glVertex2f(x1+(rsize*0.52),y1+(rsize*0.75))
    glVertex2f(x1+(rsize*0.55),y1+(rsize*0.75))

    glVertex2f(x1+(rsize*0.55),y1+(rsize*0.75))
    glVertex2f(x1+(rsize*0.55),y1+(rsize*0.80))

    glVertex2f(x1+(rsize*0.55),y1+(rsize*0.80))
    glVertex2f(x1+(rsize*0.75),y1+(rsize*0.80))

    glVertex2f(x1+(rsize*0.75),y1+(rsize*0.80))
    glVertex2f(x1+(rsize*0.75),y1+(rsize*0.75))

    glVertex2f(x1+(rsize*0.75),y1+(rsize*0.75))
    glVertex2f(x1+(rsize*0.78),y1+(rsize*0.75))

    glVertex2f(x1+(rsize*0.78),y1+(rsize*0.75))
    glVertex2f(x1+(rsize*0.78),y1+(rsize*0.70))

    glVertex2f(x1+(rsize*0.78),y1+(rsize*0.70))
    glVertex2f(x1+(rsize*0.80),y1+(rsize*0.70))

    glVertex2f(x1+(rsize*0.80),y1+(rsize*0.70))
    glVertex2f(x1+(rsize*0.80),y1+(rsize/5))

    glVertex2f(x1+(rsize*0.80),y1+(rsize/5))
    glVertex2f(x1+(rsize/2),y1+(rsize/5))
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

