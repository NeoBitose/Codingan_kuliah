from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_table():
    # Lapangan pingpong
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.5, 0.0)  # Warna hijau
    glVertex3f(-1.0, -0.1, -1.0)
    glVertex3f(1.0, -0.1, -1.0)
    glVertex3f(1.0, -0.1, 1.0)
    glVertex3f(-1.0, -0.1, 1.0)
    glEnd()

def draw_net():
    # Net pingpong
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)  # Warna putih
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glEnd()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 2.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    draw_table()
    draw_net()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow("Lapangan Pingpong 3D")
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(draw_scene)
    glutIdleFunc(draw_scene)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1.0, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glutMainLoop()

if __name__ == "__main__":
    main()
