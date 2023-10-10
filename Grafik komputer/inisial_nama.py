from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def ileft():
  glBegin(GL_QUADS) 
  glVertex2f(250, 500) 
  glVertex2f(350, 500)
  glVertex2f(200, 50)
  glVertex2f(100, 50)
  glEnd() 
def icenter():
  glBegin(GL_QUADS)
  glVertex2f(260, 260)
  glVertex2f(340, 260)
  glVertex2f(360, 190)
  glVertex2f(240, 190)
  glEnd()
def iright():
  glBegin(GL_QUADS)
  glVertex2f(300, 400)
  glVertex2f(350, 500)
  glVertex2f(500, 50)
  glVertex2f(400, 50)
  glEnd()
  
def iterate():
  glViewport(0, 0, 600, 600) 
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  glColor3ub(242, 135, 5)
  icenter()
  glColor3ub(4, 217, 57)
  iright()
  glColor3ub(34, 103, 242)
  ileft()
  glutSwapBuffers()
  
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Ahmad Alif Ramadhan - 222410103010")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

