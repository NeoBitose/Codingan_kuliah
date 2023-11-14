from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def liness():
  
  glLineWidth(2)
  
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
  
  # ================================
  
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
  glVertex2f(100, 270)
  glEnd()
  
  glBegin(GL_POLYGON)
  glVertex2f(205, 240)
  glVertex2f(230, 175)
  glVertex2f(275, 215)
  glVertex2f(300, 270)
  glVertex2f(300, 125)
  glVertex2f(255, 85)
  glVertex2f(255, 120)
  glVertex2f(270, 135)
  glVertex2f(270, 170)
  glVertex2f(245, 140)
  glVertex2f(245, 20)
  glVertex2f(230, 65)
  glVertex2f(205, 90)
  glVertex2f(205, 240)
  glEnd()

def logo_polygon():
  
  glBegin(GL_QUADS) 
  glVertex2f(130, 135)
  glVertex2f(145, 120)
  glVertex2f(145, 85)
  glVertex2f(100, 125)
  glEnd() 
  
  glBegin(GL_POLYGON)
  glVertex2f(100, 270)
  glVertex2f(125, 215)
  glVertex2f(130, 170)
  glVertex2f(130, 135)
  glVertex2f(100, 125)
  glEnd()
  
  glBegin(GL_QUADS) 
  glVertex2f(125, 215)
  glVertex2f(170, 175)
  glVertex2f(155, 140)
  glVertex2f(130, 170)
  glEnd() 
  
  glBegin(GL_POLYGON)
  glVertex2f(195, 240)
  glVertex2f(195, 90)
  glVertex2f(170, 65)
  glVertex2f(155, 20)
  glVertex2f(155, 140)
  glVertex2f(170, 175)
  glEnd()
  
  glBegin(GL_POLYGON)
  glVertex2f(205, 240)
  glVertex2f(230, 175)
  glVertex2f(245, 140)
  glVertex2f(245, 20)
  glVertex2f(230, 65)
  glVertex2f(205, 90)
  glEnd()
  
  glBegin(GL_QUADS) 
  glVertex2f(230, 175)
  glVertex2f(275, 215)
  glVertex2f(270, 170)
  glVertex2f(245, 140)
  glEnd()
  
  glBegin(GL_POLYGON)
  glVertex2f(300, 270)
  glVertex2f(300, 125)
  glVertex2f(270, 135)
  glVertex2f(270, 170)
  glVertex2f(275, 215)
  glEnd()
  
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
  # polygons()
  # liness()
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

