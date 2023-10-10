from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def logo_polygon():
  
  # glColor3f(1.0, 1.0, 0.0)
  glBegin(GL_QUADS) 
  glVertex2f(130, 135)
  glVertex2f(145, 120)
  glVertex2f(145, 85)
  glVertex2f(100, 125)
  glEnd() 
  
  # glColor3f(1.0, 0.0, 0.0)
  glBegin(GL_POLYGON)
  glVertex2f(100, 270)
  glVertex2f(125, 215)
  glVertex2f(130, 170)
  glVertex2f(130, 135)
  glVertex2f(100, 125)
  glEnd()
  
  # glColor3f(0.0, 0.0, 1.0)
  glBegin(GL_QUADS) 
  glVertex2f(125, 215)
  glVertex2f(170, 175)
  glVertex2f(155, 140)
  glVertex2f(130, 170)
  glEnd() 
  
  # glColor3f(0.0, 1.0, 0.0)
  glBegin(GL_POLYGON)
  glVertex2f(195, 240)
  glVertex2f(195, 90)
  glVertex2f(170, 65)
  glVertex2f(155, 20)
  glVertex2f(155, 140)
  glVertex2f(170, 175)
  glEnd()
  
  # glColor3f(0.0, 1.0, 0.0)
  glBegin(GL_POLYGON)
  glVertex2f(205, 240)
  glVertex2f(230, 175)
  glVertex2f(245, 140)
  glVertex2f(245, 20)
  glVertex2f(230, 65)
  glVertex2f(205, 90)
  glEnd()
  
  # glColor3f(0.0, 0.0, 1.0)
  glBegin(GL_QUADS) 
  glVertex2f(230, 175)
  glVertex2f(275, 215)
  glVertex2f(270, 170)
  glVertex2f(245, 140)
  glEnd()
  
  # glColor3f(1.0, 0.0, 0.0)
  glBegin(GL_POLYGON)
  glVertex2f(300, 270)
  glVertex2f(300, 125)
  glVertex2f(270, 135)
  glVertex2f(270, 170)
  glVertex2f(275, 215)
  glEnd()
  
  # glColor3f(1.0, 1.0, 0.0)
  glBegin(GL_QUADS) 
  glVertex2f(270, 135)
  glVertex2f(300, 125)
  glVertex2f(255, 85)
  glVertex2f(255, 120)
  glEnd()
  

def iterate(): 
  glViewport(0, 0, 500, 500) 
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  glColor3f(1.0, 1.0, 0.0)
  logo_polygon()
  glutSwapBuffers()
  
def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  glColor3f(1.0, 1.0, 0.0)
  glTranslatef(150.0, 100.0, 0)
  logo_polygon()
  glutSwapBuffers()
  
def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  glColor3f(1.0, 1.0, 0.0)
  glScale(0.5, 0.5, 0)
  logo_polygon()
  glutSwapBuffers()
  
def showScreen():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  glColor3f(1.0, 1.0, 0.0)
  glRotate(10, 0, 0, 1)
  logo_polygon()
  glutSwapBuffers()
  
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Ahmad Alif Ramadhan - 222410103010")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

