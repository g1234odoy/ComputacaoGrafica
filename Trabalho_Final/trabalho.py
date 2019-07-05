from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import sys
import png
import math

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0

arq = sys.argv[1]
arqText = sys.argv[2] 
text = int(sys.argv[3])

if text < 0:
    text = 0
if text > 3:
    text = 3


texture = []
def carregaImg():
    reader = png.Reader(filename=arq)
    w, h, pixels, metadata = reader.read_flat()

    if(metadata['alpha']):
        bytesPerPixel = 4
    else:
        bytesPerPixel = 3


    lista = []

    def posicao(linha, coluna):
        return bytesPerPixel*(w*linha+coluna)

    ######## FAZ A GARRAFA INTEIRA NO CONSOLE ########
    lista = []
    for linha in range(1,h-1):
        lista2 = []
        for coluna in range(1,w-1):
            pc = posicao(linha-1,coluna)
            pb = posicao(linha+1,coluna)
            p = posicao(linha,coluna)
            pe = posicao(linha,coluna-1)
            pd = posicao(linha,coluna+1)
            dv = abs(pixels[pc]-pixels[pb])
            dh = abs(pixels[pe]-pixels[pd])
            d = int(max(dv,dh))
            if d > 10:
                d = 255
                lista2.append(1)
            else:
                lista2.append(0)  

        lista.append(lista2)

    ##### TIRA AS LINHAS SÓ COM 0 #####
    numeroLinha = -1
    listaSem0 = []
    for linha in lista:
        numeroLinha += 1
        count = 0
        for elemento in linha:
            if elemento == 1:
                count = count + 1
        if count != 0:
            listaSem0.append(linha)


    ##### ACHA O COMEÇO E O FINAL #####
    comeco = 0
    final = 0
    for linha in listaSem0:
        comeco = 0
        for comeco in range(len(linha)):
            if linha[comeco] == 1:
                for f in range(comeco, len(linha)):
                    if linha[f] != 1:
                        break
                    final = f
                break
        if comeco != 0:
            break


    meio = (comeco+final)/2
    if(meio % 2 != 0):
        meio += 0.5

    maiorDist = float("inf")

    ##### ACHA A MENOR DISTÂNCIA DO INÍCIO DAS LINHAS PARA O PRIMEIRO 1 #####
    for linha in listaSem0:
        for z in range(len(linha)):
            if linha[z] == 1:
                if z < maiorDist:
                    maiorDist = z
                break


    ##### ACHA A TAÇA COM A MENOR DISTÂNCIA DO INÍCIO DAS LINHAS PARA O PRIMEIRO 1 #####
    listaFinal = []       
    for linha in listaSem0:
        listaFinalAux = []
        for g in range(int(maiorDist), int(meio)):
            listaFinalAux.append(linha[g])
        #print(listaFinalAux)
        listaFinal.append(listaFinalAux)

    global t,ft,tamLinha
    tamLinha = len(listaFinal[0])
    t = len(listaFinal)
    ft = []
    for i in range(0,t):
        count = 0
        itens = []
        for item in listaFinal[i]:  
            count += 1
            if item == 1:
                itens.append(count)
        
        if len(itens) != 0:
            if len(itens) == 3:
                ft.append(itens[1])
            else:
                ft.append(itens[0])

    global textInicial, textFinal
    textInicial = text*(t/4)
    textFinal = textInicial + (t/4)

def calcX(a):
    if a == len(ft):
        return 1-float(float(ft[0])/float(tamLinha))
    return 1-float(float(ft[a])/float(tamLinha))

def calcY(a):
    return 4*(1.0-float(float(a)/float(t)))

def calcYTextura(a):
    return float((a-textInicial)/(textFinal-textInicial))

def LoadTextures():
    global texture
    texture = glGenTextures(2)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename=arqText)
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(75.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 10.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,-1.5,-7.0)            

    #glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    #glRotatef(zrot,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, texture[0])

    a0 = 0
    af = t
    p0 = 0
    pf = (2*math.pi)

    a = a0
    while a < af:
        glBegin(GL_QUADS)        
        glColor3f(1,1,1)
        p = p0
        while p < pf:
            if(a >= textInicial and a <= textFinal):
                glTexCoord2f(1-float(p/pf), calcYTextura(a)); glVertex3f(calcX(a)*math.cos(p), calcY(a) , calcX(a)*math.sin(p))
                glTexCoord2f(1-float(p/pf), calcYTextura(a+1)); glVertex3f(calcX(a+1)*math.cos(p), calcY(a+1), calcX(a+1)*math.sin(p))
                glTexCoord2f(1-float((p+math.pi/50)/pf), calcYTextura(a+1)); glVertex3f(calcX(a+1)*math.cos(p+math.pi/50), calcY(a+1), calcX(a+1)*math.sin(p+math.pi/50))
                glTexCoord2f(1-float((p+math.pi/50)/pf), calcYTextura(a)); glVertex3f(calcX(a)*math.cos(p+math.pi/50), calcY(a), calcX(a)*math.sin(p+math.pi/50))   
            else:    
                glVertex3f(calcX(a)*math.cos(p), calcY(a) , calcX(a)*math.sin(p))
                glVertex3f(calcX(a+1)*math.cos(p), calcY(a+1), calcX(a+1)*math.sin(p))
                glVertex3f(calcX(a+1)*math.cos(p+math.pi/50), calcY(a+1), calcX(a+1)*math.sin(p+math.pi/50))
                glVertex3f(calcX(a)*math.cos(p+math.pi/50), calcY(a), calcX(a)*math.sin(p+math.pi/50))
            
            p += (math.pi/50)
        glEnd()
        a += 1
    
    xrot  = xrot + 3.01                # X rotation
    yrot = yrot + 2.01                 # Y rotation
    zrot = zrot + 1.01                 # Z rotation

    glutSwapBuffers()


def main():
    carregaImg()
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(800, 600)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)


    # Initialize our window. 
    InitGL(800, 600)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print("Hit ESC key to quit.")
    main()
