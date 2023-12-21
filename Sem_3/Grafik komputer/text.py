from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_letter_p():
    glColor3fv((1, 1, 1))  # White color
    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)

    glVertex2f(-0.5, 0.5)
    glVertex2f(0.0, 0.5)

    glVertex2f(0.0, 0.5)
    glVertex2f(0.0, 0.2)

    glVertex2f(0.0, 0.2)
    glVertex2f(-0.2, 0.2)

    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.2, -0.2)

    glVertex2f(-0.2, -0.2)
    glVertex2f(0.0, -0.2)

    glVertex2f(0.0, -0.2)
    glVertex2f(0.0, -0.5)

    glVertex2f(0.0, -0.5)
    glVertex2f(-0.5, -0.5)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_letter_p()
    glutSwapBuffers()

def reshape(width, height):
  glViewport(0, 0, width, height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, 1900, 0.0, 1000, 0.0, 1.0) 
  glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Letter P in PyOpenGL")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glutMainLoop()

if __name__ == "__main__":
    main()
