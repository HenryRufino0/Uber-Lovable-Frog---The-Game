from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random


global angulo, fAspect,anguloX,anguloY,NUMERO_LIVROS

anguloX=0; anguloY=0;randMax = 1;NUMERO_LIVROS = 16

class Livro:
    r=0.0;g=0.0; b=0.0; pX_Livro=0.0;
    

def chao():
    glColor3f(0.1, 0.6, 0.6);
    glPushMatrix();
    glTranslated(1.5, 0.2, 1.3);
    glScaled(4.0, 0.2, 4.0);
    glutSolidCube(1.0);
    glPopMatrix();

def paredeFundo():
    glColor3f(0.7, 0.72, 1);
    glPushMatrix();
    glTranslated(1.5, 1.10, -0.7);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(4.0, 0.03, 2.0);
    glutSolidCube(1.0);
    glPopMatrix();

def paredeLadoE():
    glColor3f(0.7, 0.72, 1);
    glPushMatrix();
    glTranslated(-0.5, 1.10, 1.3);
    glRotated(90.0, 0.0, 1.0, 0.0)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(4.0, 0.03, 2.0)
    glutSolidCube(1.0)
    glPopMatrix()

def paredeFrente():
    glColor3f(0.7, 0.72, 1);
    glPushMatrix();
    glTranslated(1.5,1.10,3.3)
    glRotated(-90.0, 90.0, 0.0, 0.0);
    glScaled(4.0, 0.03, 2.0)
    glutSolidCube(1.0)
    glPopMatrix()

def paredeLadoD():
    glColor3f(0.7, 0.72, 1);
    glPushMatrix();
    glTranslated(3.5, 1.10, 0.55);
    glRotated(90.0, 0.0, 1.0, 0.0)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(2.5, 0.03, 2.0)
    glutSolidCube(1.0)
    glPopMatrix()

    glColor3f(0.7, 0.72, 1);
    glPushMatrix();
    glTranslated(3.5, 1.10, 3.05);
    glRotated(90.0, 0.0, 1.0, 0.0)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.5, 0.03, 2.0)
    glutSolidCube(1.0)
    glPopMatrix()

    glColor3f(0.7, 0.72, 1);
    glPushMatrix();
    glTranslated(3.5, 1.85, 2.3);
    glRotated(90.0, 0.0, 1.0, 0.0)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1, 0.03, 0.5)
    glutSolidCube(1.0)
    glPopMatrix()

def porta():
#Porta
    glColor3f(0.76,0.5,0.3);
    glPushMatrix();
    glTranslated(3, 0.85, 2.8);
    glRotated(90, 1, 0, 0)
    glScaled(1, 0.03, 1.5)
    glutSolidCube(1.0)
    glPopMatrix()
#Maçaneta
    glColor3f(0.2,0.2,0.2);
    glPushMatrix();
    glTranslated(2.6, 0.85, 2.8);
    glRotated(90, 1, 0, 0)
    glScaled(0.1, 0.1, 0.05)
    glutSolidCube(1.0)
    glPopMatrix()

    
def paineltv():
#Painel
    glColor3f(0.9,0.8,0.8)
    glPushMatrix()
    glTranslated(2.2,1.1,-.66)    
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1.5,0.03,1.5);
    glutSolidCube(1.0);
    glPopMatrix();
#TV
    glColor3f(0,0,0)
    glPushMatrix()
    glTranslated(2.21,1.3,-0.63)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1.3,0.03,0.9)
    glutSolidCube(1.0)
    glPopMatrix()

#Tela
    glColor3f(1,1,1)
    glPushMatrix()
    glTranslated(2.22,1.32,-0.62)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1,0.03,0.7)
    glutSolidCube(1.0)
    glPopMatrix()
#Movel
    glColor3f(0.9,0.8,0.8)
    glPushMatrix()
    glTranslated(2.2,0.5,-.53)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1.5,0.3,0.4)
    glutSolidCube(1.0)
    glPopMatrix()
#PS5 (Atari Edition)
    #parteMeio
    glColor3f(0,0,0)
    glPushMatrix()
    glTranslated(2.5,0.75,-.5)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.05,0.1,0.3)
    glutSolidCube(1.0)
    glPopMatrix()

    #partesBrancas
    glColor3f(1,1,1)
    glPushMatrix()
    glTranslated(2.47,0.75,-.5)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.01,0.15,0.3)
    glutSolidCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslated(2.53,0.75,-.5)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.01,0.15,0.3)
    glutSolidCube(1.0)
    glPopMatrix()

def tapete():
#Parte Amarela
    glColor(1,1,0)
    glPushMatrix()
    glTranslated(2,0.3,2)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1.5,2,0.01)
    glutSolidSphere(0.6,40,10)
    glPopMatrix()

#Parte Azul
    glColor(0,0,1)
    glPushMatrix()
    glTranslated(2,0.31,2)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1.2,1.7,0.01)
    glutSolidSphere(0.55,30,10)
    glPopMatrix()




def sofa():
#Base
    glColor3f(0.76,0.5,0)
    glPushMatrix()
    glTranslated(2.2,0.4,0.5)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1.5,0.5,0.3)
    glutSolidCube(1.0)
    glPopMatrix()

#Encosto
    glColor3f(0.76,0.5,0)
    glPushMatrix()
    glTranslated(2.2,0.6,0.7)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1.5,0.2,0.8)
    glutSolidCube(1.0)
    glPopMatrix()

#Braços
    glColor3f(0.76,0.5,0)
    glPushMatrix()
    glTranslated(1.5,0.5,0.50)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.3,0.6,0.5)
    glutSolidCube(1.0)
    glPopMatrix()

    glColor3f(0.76,0.5,0)
    glPushMatrix()
    glTranslated(2.9,0.5,0.50)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.3,0.6,0.5)
    glutSolidCube(1.0)
    glPopMatrix()  

def estante():
#ParteTras
    glColor3f(0.30, 0.30, 0.40);
    glPushMatrix();
    glTranslated(0.5, 1.15, -0.7);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.7, 0.02, 0.86);
    glutSolidCube(2.0);
    glPopMatrix();
#Lateral traseira
    glPushMatrix();
    glTranslated(-0.2, 1.15, -0.6);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.12, 0.86);
    glutSolidCube(2.0);
    glPopMatrix();
#Lateral frontal
    glPushMatrix();
    glTranslated(1.2, 1.15, -0.6);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.12, 0.86);
    glutSolidCube(2.0);
    glPopMatrix();
#Topo
    glPushMatrix();
    glTranslated(0.5, 1.95, -0.58);
    glScaled(0.7, 0.06, 0.10);
    glutSolidCube(2.0);
    glPopMatrix();
#Meio
    glPushMatrix();
    glTranslated(0.5, 1.15, -0.58);
    glScaled(0.7, 0.06, 0.10);
    glutSolidCube(2.0);
    glPopMatrix();
#Base
    glPushMatrix();
    glTranslated(0.5, 0.35, -0.58);
    glScaled(0.7, 0.06, 0.10);
    glutSolidCube(2.0);
    glPopMatrix();
#CapaJogos
    glColor3f(0,0,1)
    glPushMatrix()
    glTranslated(0.47,1.7,-0.585)
    glScaled(1.25,0.05,0.25)
    glutSolidCube(1.0)
    glPopMatrix()



def livro(x, r, g, b):
    if (r == 0 and g == 0 and b == 0):
        g = 1.0;
    glColor3f(r, g, b);
    glPushMatrix();
    glTranslated(x, 1.47, -0.58);
    glScaled(0.15, 1.0, 0.45);
    glutSolidCube(0.5);
    glPopMatrix();

def Bandeira():

    x = -0.50; y = 1.50; z = 0.20;
    
#Parte Verde
    glColor3f(0,1,0);
    glPushMatrix();
    glTranslated(x, y, z + 0.3);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 1.2, 0.8);
    glutSolidCube(1.0);
    glPopMatrix();

#Parte Amarela
    glColor3f(1,1,0);
    glPushMatrix();
    glTranslated(x+0.01, y, z + 0.3);
    glRotated(45.0, 45.0, 0.0, 0.0);
    glScaled(0.04, 0.55, 0.55);
    glutSolidCube(1.0);
    glPopMatrix();
    
#Parte Azul
    glColor3f(0,0,1)
    glPushMatrix();
    glTranslated(x+0.02, y, z + 0.3);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.02, 0.3, 0.3);
    glutSolidSphere(0.9,20,20);
    glPopMatrix();

#Parte Branca
    glColor(1,1,1)
    glPushMatrix();
    glTranslated(x+0.02, y, z + 0.3);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.04, 0.4, 0.05);
    glutSolidCube(1.0);
    glPopMatrix();

def cama():
#Colchão (Branco)
    glColor3f(1, 1, 1);
    glPushMatrix();
    glTranslated(-0.25, 0.8, 0.7);
    glScaled(0.4, 0.3, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

#Travesseiro (Azul Claro)
    glColor3f(0,1,1);
    glPushMatrix();
    glTranslated(-0.23,1,0.7);
    glScaled(0.3,0.06,0.7);
    glutSolidCube(1.0);
    glPopMatrix();
    
#Cobertor (Vermelho)
    glColor(1,0,0);
    glPushMatrix();
    glTranslated(0.45,0.8,0.7);
    glScaled(1,0.35,0.7);
    glutSolidCube(1.0);
    glPopMatrix();

#Pé esquerdo fundo
    glColor3f(0.5, 0.38, 0.1);	
    glPushMatrix();
    glTranslated(-0.43, 0.45, 0.95);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.06, 0.06, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

#Pé esquerdo frente
    glPushMatrix();
    glTranslated(0.9, 0.45, 0.95);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.06, 0.06, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

#Pé direito fundo
    glPushMatrix();
    glTranslated(-0.43, 0.45, 0.45);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.06, 0.06, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

#Pé direito frente
    glPushMatrix();
    glTranslated(0.9, 0.45, 0.45);
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.06, 0.06, 0.7);
    glutSolidCube(1.0);
    glPopMatrix();

def Lampada():
#Base
    glColor3f(0.4,0.4,0.4)
    glPushMatrix()
    glTranslated(-.25,0.3,2)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.5,0.5,0.5)
    glutSolidCone(0.3,0.5,10,10);
    glPopMatrix();
#Haste
    glPushMatrix()
    glTranslated(-.25,0.8,2)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(0.03,0.03,1.5)
    glutSolidCube(1.0);
    glPopMatrix();
#Suporte
    glPushMatrix()
    glTranslated(-.15,1.5,1.9)
    glRotated(-50.0, 0.0, 90.0, 0.0);
    glScaled(0.5,0.5,0.5)
    glutSolidCone(0.3,0.5,10,10);
    glPopMatrix();
#Lampada
    glColor3f(1,1,0)
    glPushMatrix()
    glTranslated(-.13,1.5,1.88)
    glRotated(-90.0, 1.0, 0.0, 0.0);
    glScaled(1,1,1)
    glutSolidSphere(0.07,20,20)
    glPopMatrix();
    

    
    
    
    
    


def desenhaPrincipal():
    global anguloX, anguloY,livro
    glRotated(anguloX, 0.0, 1.0, 0.0);
    glRotated(anguloY, 1.0, 0.0, 0.0);
    chao();
    paredeFundo();
    paredeLadoE();
    paredeLadoD();
    paredeFrente();
    estante();
    Bandeira();
    cama();
    paineltv();
    sofa();
    tapete();
    Lampada();
    porta();
    for i in range(NUMERO_LIVROS):
        livro(Livros[i].pX_Livro, Livros[i].r, Livros[i].g, Livros[i].b);
    glFlush();

def iluminacao():
    luzAmbiente = [0.3, 0.3, 0.3, 1]
    luzDifusa = [0.5,0.5,0.5, 1];# "cor"
    luzEspecular = [0.3, 0.3, 0.3, 0];# "brilho"
    posicaoLuz1 = [0,0,0,0];
    posicaoLuz2 = [1,0,0,0];
    #{ 50.0, 100.0, 20.0, 1.0 };
    # Capacidade de brilho do material
    especularidade = [0.4, 0.4, 0.4, 0.4];
    especMaterial = 50;
    glClearColor(0.0, 0.0, 0.0, 1.0);
    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH);
    # Define a refletância do material
    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade);
    #// Define a concentração do brilho
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial);
    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente);
    # Define os parâmetros da luz de número 1
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1);
    # Define os parâmetros da luz de número 2
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente);
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa);
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2);
    
    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);#Habilita o uso de iluminação
    glEnable(GL_LIGHT0); # Habilita a luz de número 0
    glEnable(GL_DEPTH_TEST); # Habilita o depth-buffering
    glEnable(GL_NORMALIZE);

def parametrosVisualizacao():
    global fAspect
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    # Especifica a projeção perspectiva
    gluPerspective(angulo, fAspect, 0.1, 500);
    #gluPerspective(angulo, 1, 0.5, 50);
    #glOrtho(-1.8, 1.8, -1.8, 2, 0.8, 200.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    # Especifica posição do observador e do alvo
    #gluLookAt(2.00 + anguloX, 1.00 + anguloY, 2.0, 0.0, 0.5, 0.25, 0.0, 1.0, 0.0);
    gluLookAt(5.0, 5.0, 5.0, 0, 1, 0, 0.0, 1.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

def moveCamera(key, x1, y1):
    global anguloX, anguloY
    if (key == GLUT_KEY_UP):
        anguloY -= 1;
    elif (key == GLUT_KEY_DOWN):
        anguloY += 1;
    elif (key == GLUT_KEY_LEFT):
        anguloX -= 1;
    elif (key == GLUT_KEY_RIGHT):
        anguloX += 1;

    parametrosVisualizacao();
    glutPostRedisplay();

def inicializa():
    global angulo,Livros
    Livros=[]
    iluminacao();
    angulo = 30;
    pX_Livro = -0.12;
    for i in range(NUMERO_LIVROS):
        temp= Livro()
        temp.r=random.random();temp.g=random.random();temp.b=random.random()
        temp.pX_Livro = pX_Livro;
        Livros.append(temp)
        pX_Livro += 0.078;

def alteraTamanhoJanela(w, h):
    global fAspect
    if (h == 0): h = 1; # Para previnir uma divisão por zero
    glViewport(0, 0, w, h);# Especifica o tamanho da viewport
    fAspect = w/h;
    parametrosVisualizacao();

def gerenciaMouse(button, state, x, y):
    global angulo
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo < 170):
                angulo+=5;
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo > 10):
                angulo-=5;
    #printf("%f\n",angulo);
    parametrosVisualizacao();
    glutPostRedisplay();

def GerenciaTeclado(key,x,y):
    if (key==b'1'):
        glEnable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
        
    elif(key==b'2'):
        glEnable(GL_LIGHT2)
        glDisable(GL_LIGHT1)

    parametrosVisualizacao();
    glutPostRedisplay();
        
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(1024, 768);
    glutCreateWindow(b"Ambiente 3D");
    glutDisplayFunc(desenhaPrincipal);
    glutReshapeFunc(alteraTamanhoJanela);
    glutSpecialFunc(moveCamera);
    glutMouseFunc(gerenciaMouse);
    glutKeyboardFunc(GerenciaTeclado)
    inicializa();
    glutMainLoop();

main()
