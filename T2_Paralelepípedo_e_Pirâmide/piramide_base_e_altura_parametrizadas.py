from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

b = int(sys.argv[1]) if len(sys.argv) > 1 else 3
h = int(sys.argv[2]) if len(sys.argv) > 2 else 2

anguloBase = (2*math.pi)/b

vertices = (
    (0,h,0),
    )

linhas = ()
faces = ()
angulo = 2*math.pi
for x in range(0, b):
    vertices += (((math.cos(angulo),0, -math.sin(angulo))),)
    linhas = ((0,x+1),)
    angulo -= anguloBase

    if(x+1 == b):
        linhas += ((b,1),)
        faces += ((0,b,1),)
    else:
        linhas += ((x+1,x+2),)
        faces += ((0,x+1,x+2),)
    

for x in range(0, b):
    if(x+1 == b):
        faces += ((b+1,b,1),)
    else:
        faces += ((b+1,x+1,x+2),)
    #linhas += ((b,x+1),)        
    # v -a + f =2
    
vertices += ((0,0,0),)


cores = ( (1,0,0),(1,1,0),(1,1,1),(1,0,1),(0,1,1),(1,0,0))

def Cubo():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        if i % 6 == 0:
            i = 0
            
        glColor3fv(cores[i])
        
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
		
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glRotatef(2,1,3,0)
    glRotatef(4,3,5,0)
    Cubo()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


