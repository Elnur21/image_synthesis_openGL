from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

cube_size = 0.2

angle = 0.0

def draw_cube(axis, color):
    glColor3fv(color)
    glPushMatrix()
    glTranslatef(*axis)  
    glutSolidCube(cube_size)  
    glPopMatrix()

def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 5, 5, 0, 0, 0, 0, 0, 1)

    glRotatef(angle, 1, 1, 1)  

    draw_cube((1, 0, 0), (1, 0, 0))  
    draw_cube((0, 1, 0), (0, 1, 0)) 
    draw_cube((0, 0, 1), (0, 0, 1))  

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def timer(value):
    global angle
    angle += 0.2  
    angle %= 360  
    glutPostRedisplay()  
    glutTimerFunc(17, timer, 0)  


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutCreateWindow(b"OpenGL Cubes Example")
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutTimerFunc(17, timer, 0)  
glutMainLoop()


