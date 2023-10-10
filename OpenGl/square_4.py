from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def square1():
  glBegin(GL_QUADS) #quadrilateral
  glVertex2f(100, 300) # vertex : menggambarkan titik kedalam array, vertex2 (x,y)
  glVertex2f(200, 300)
  glVertex2f(200, 400)
  glVertex2f(100, 400)
  glEnd() # mengakhiri bidang yang dibuat
def square2():
  glBegin(GL_QUADS) #quadrilateral
  glVertex2f(300, 300)
  glVertex2f(400, 300)
  glVertex2f(400, 400)
  glVertex2f(300, 400)
  glEnd()
def square3():
  glBegin(GL_QUADS) #quadrilateral
  glVertex2f(100, 100)
  glVertex2f(200, 100)
  glVertex2f(200, 200)
  glVertex2f(100, 200)
  glEnd()
def square4():
  glBegin(GL_QUADS) #quadrilateral
  glVertex2f(300, 100)
  glVertex2f(400, 100)
  glVertex2f(400, 200)
  glVertex2f(300, 200)
  glEnd()

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
  square1()
  glColor3ub(255, 0, 0) # ubyte
  square2()
  glColor3f(0.0, 1.0, 0.0) #float
  square3()
  glColor3ub(0, 0, 255) # ubyte
  square4()
  glutSwapBuffers()
  
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Ahmad Alif Ramadhan - 222410103010")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop() #memanggil display terus menerus

