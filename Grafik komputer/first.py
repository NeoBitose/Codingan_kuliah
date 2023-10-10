from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# def square1():
#   glBegin(GL_QUADS) #quadrilateral
#   glVertex2f(100, 300) # vertex : menggambarkan titik kedalam array, vertex2 (x,y)
#   glVertex2f(200, 300)
#   glVertex2f(200, 400)
#   glVertex2f(100, 400)
#   glEnd() # mengakhiri bidang yang dibuat
# def square2():
#   glBegin(GL_QUADS) #quadrilateral
#   glVertex2f(300, 300)
#   glVertex2f(400, 300)
#   glVertex2f(400, 400)
#   glVertex2f(300, 400)
#   glEnd()
# def square3():
#   glBegin(GL_QUADS) #quadrilateral
#   glVertex2f(100, 100)
#   glVertex2f(200, 100)
#   glVertex2f(200, 200)
#   glVertex2f(100, 200)
#   glEnd()
# def square4():
#   glBegin(GL_QUADS) #quadrilateral
#   glVertex2f(300, 100)
#   glVertex2f(400, 100)
#   glVertex2f(400, 200)
#   glVertex2f(300, 200)
#   glEnd()

def liness():
  glLineWidth(1)
  
  glBegin(GL_LINES)
  glVertex2f(100, 270)
  glVertex2f(125, 215)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(125, 215)
  glVertex2f(170, 175)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(170, 175)
  glVertex2f(195, 240)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(195, 240)
  glVertex2f(195, 90)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(195, 90)
  glVertex2f(170, 65)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(170, 65)
  glVertex2f(155, 20)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(155, 20)
  glVertex2f(155, 140)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(155, 140)
  glVertex2f(130, 170)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(130, 170)
  glVertex2f(130, 135)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(130, 135)
  glVertex2f(145, 120)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(145, 120)
  glVertex2f(145, 85)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(145, 85)
  glVertex2f(100, 125)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(100, 125)
  glVertex2f(100, 270)
  glEnd()
  
  
  
  glBegin(GL_LINES)
  glVertex2f(205, 240)
  glVertex2f(230, 175)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(230, 175)
  glVertex2f(275, 215)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(275, 215)
  glVertex2f(300, 270)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(300, 270)
  glVertex2f(300, 125)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(300, 125)
  glVertex2f(255, 85)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(255, 85)
  glVertex2f(255, 120)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(255, 120)
  glVertex2f(270, 135)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(270, 135)
  glVertex2f(270, 170)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(270, 170)
  glVertex2f(245, 140)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(245, 140)
  glVertex2f(245, 20)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(245, 20)
  glVertex2f(230, 65)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(230, 65)
  glVertex2f(205, 90)
  glEnd()
  
  glBegin(GL_LINES)
  glVertex2f(205, 90)
  glVertex2f(205, 240)
  glEnd()
  

def predator():
  glBegin(GL_POLYGON)
  glVertex2f(100, 270.0)
  glVertex2f(120.5, 210.5)
  glVertex2f(170, 170.5)
  glVertex2f(190.5, 240)
  glVertex2f(190.5, 90)
  glVertex2f(170, 60.5)
  glVertex2f(150.5, 20)
  glVertex2f(150.5, 140)
  glVertex2f(130, 170)
  glVertex2f(130, 130.5)
  glVertex2f(140.5, 120)
  glVertex2f(140.5, 80.5)
  glVertex2f(100, 120.5)
#   glEnd()
  # glBegin(GL_POLYGON)
  glVertex2f(200.5, 240)
  glVertex2f(230, 170.5)
  glVertex2f(270.5, 210.5)
  glVertex2f(300, 270)
  glVertex2f(300, 120.5)
  glVertex2f(250.5, 80.5)
  glVertex2f(250.5, 120)
  glVertex2f(270, 130.5)
  glVertex2f(270, 170)
  glVertex2f(240.5, 140)
  glVertex2f(240.5, 20)
  glVertex2f(230, 60.5)
  glVertex2f(200.5, 90)
  
  # glEnd()

def polygons():
  
  glBegin(GL_POLYGON)
  glVertex2f(100, 270)
  glVertex2f(125, 215)
  glVertex2f(170, 175)
  glVertex2f(195, 240)
  glVertex2f(195, 90)
  glVertex2f(170, 65)
  glVertex2f(155, 20)
  glVertex2f(155, 140)
  glVertex2f(130, 170)
  glVertex2f(130, 135)
  glVertex2f(145, 120)
  glVertex2f(145, 85)
  glVertex2f(100, 125)
  # glVertex2f(100, 270)
  glEnd()
  
  # glBegin(GL_POLYGON)
  # glVertex2f(205, 240)
  # glVertex2f(230, 175)
  # glVertex2f(275, 215)
  # glVertex2f(300, 270)
  # glVertex2f(300, 125)
  # glVertex2f(255, 85)
  # glVertex2f(255, 120)
  # glVertex2f(270, 135)
  # glVertex2f(270, 170)
  # glVertex2f(245, 140)
  # glVertex2f(245, 20)
  # glVertex2f(230, 65)
  # glVertex2f(205, 90)
  # glVertex2f(205, 240)
  # glEnd()



def iterate(): #menyiapkan media output
  glViewport(0, 0, 500, 500) # membuat ukuran viewport (x,y,w,h)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity() # merubah matrix menjadi matrix identitas
  glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  glColor3f(1.0, 1.0, 0.0) #float
  # square1()
  # glColor3ub(255, 0, 0) # ubyte
  # square2()
  # glColor3f(0.0, 1.0, 0.0) #float
  # square3()
  # glColor3ub(0, 0, 255) # ubyte
  # square4()
  liness()
  glutSwapBuffers()
  
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Ahmad Alif Ramadhan - 222410103010")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop() #memanggil display terus menerus

