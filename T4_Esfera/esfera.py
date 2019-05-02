from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

a0 = (-math.pi)/2
af = (math.pi)/2
p0 = 0
pf = (2*math.pi)
r = 3
def px(a):
    return r*math.cos(a)

def py(a):
    return r*math.sin(a)

def qx(r2,p):
    return r2*math.cos(p)
    
def qz(r2,p):
    return r2*math.sin(p)

def Esfera():
    a = a0
    while a < af:
        glBegin(GL_POINTS)
        glVertex3f(px(a),py(a),0)
        glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        p = p0
        while p < pf:
            glVertex3f(qx(px(a),p), py(a), qz(px(a),p))
            p += (math.pi/50)
        glEnd()
        a += (math.pi/50)
        
def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Esfera()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
    
#PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Rede")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(75,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()