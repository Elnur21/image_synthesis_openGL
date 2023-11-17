from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def background():
    glClearColor(0.5, 0.5, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def perspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    _, _, width, height = glGetDoublev(GL_VIEWPORT)
    gluPerspective(45, width / height, 0.1, 100.0)

def lookat():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

def light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(0.0, 0.0, 10.0, 1.0))

def depth():
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

def material(color, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color)
    glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(shininess))

def drawCone(radius, height, slices, stacks):
    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glutSolidCone(radius, height, slices, stacks)
    glPopMatrix()

def drawSphere(radius, slices, stacks):
    glutSolidSphere(radius, slices, stacks)

def display():
    background()
    perspective()
    lookat()
    light()
    depth()

    sphere_color = GLfloat_4(1.0, 0.843, 0.0, 1.0)
    material(sphere_color, 128.0)
    drawSphere(1, 50, 50)

    material(sphere_color, 128.0)
    glPushMatrix()
    glTranslatef(0, 0, 1)
    drawCone(1, 2, 50, 10)
    glPopMatrix()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Cone and circle")
glutDisplayFunc(display)
glutMainLoop()
