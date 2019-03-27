from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import math
import random

b = int(sys.argv[1]) if len(sys.argv) > 1 else 3
h = int(sys.argv[2]) if len(sys.argv) > 2 else 2

anguloBase = (2*math.pi)/b
angulo = 0

vertices = ()

linhas = ()
faces = ()
angulo = 2*math.pi
for x in range(0, b):
    vertices += ((math.cos(angulo), 0, -math.sin(angulo)),)
    angulo -= anguloBase

angulo = 2*math.pi

for x in range(0, b):
    vertices += ((math.cos(angulo), h, -math.sin(angulo)),)
    angulo -= anguloBase

for x in range(0, b):
    if(x+1 == b): 
        linhas += ((x,0),)
    else:
        linhas += ((x,x+1),)

for x in range(0+b, b+b):
    if(x+1 == b+b): 
        linhas += ((x,b),)
    else:
        linhas += ((x,x+1),)

faces = ()
for x in range(0, b):
    if(x+1 == b): 
        linhas += ((x,(2*b)-1),)
        faces += ((x,0,b,(2*b)-1),)
    else:
        linhas += ((x,b+x),)
        faces += ((x,x+1,b+1+x,b+x),)


bases = ()
for i in range(0,2):
  aux = ()
  for x in range(0+(i*b), b+(i*b)):
    aux += ((x,))        
  bases += ((aux),)


cores = ( (1,0,0),(1,1,0),(1,1,1),(1,0,1) )

def Cubo():

    
    glBegin(GL_QUADS)
    
    i = 0
    
    for face in faces:
        if i % 3 == 0:
            i = 0
            
        glColor3fv(cores[i])
        
        for vertex in face:
            glVertex3fv(vertices[vertex])
            
        i = i+1
    glEnd()

    
    i = 0
    for face in bases:
        glBegin(GL_POLYGON)
        glColor3fv(cores[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
        glEnd()
    
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(4,3,5,0)
    #glRotatef(2,1,3,0)
    Cubo()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PARALELEPIPEDO")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


