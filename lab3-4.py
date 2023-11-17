from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_Scene()
    glutSwapBuffers()

def render_Scene():
    # Perform a translation to shift the first/red triangle to the bottom
    glPushMatrix()
    glTranslated(0.0, -0.3, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, -0.1, -0.8)
    glVertex3f(0.3, -0.1, -1)
    glVertex3f(0, 0.3, -0.9)
    glEnd()
    glPopMatrix()

    # Perform a translation to shift the second/yellow triangle to the top
    glPushMatrix()
    glTranslated(0.0, 0.3, 0.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, 0.2, 0.0)
    glVertex3f(-0.7, 0.5, 0.0)
    glVertex3f(-0.5, 0.7, 0.0)
    glEnd()
    glPopMatrix()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Two Triangles Shifting")
gluOrtho2D(-1, 1, -1, 1)
glutDisplayFunc(display)
glutMainLoop()

