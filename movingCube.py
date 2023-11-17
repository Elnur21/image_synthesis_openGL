from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

cube_rotation_x = 20.0  # Initial x-axis rotation angle
cube_rotation_y = 20.0  # Initial y-axis rotation angle

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Apply rotations around x and y axes
    glRotatef(cube_rotation_x, 1.0, 0.0, 0.0)
    glRotatef(cube_rotation_y, 0.0, 1.0, 0.0)

    render_Scene()

    glutSwapBuffers()


def render_Scene():
# Multi-colored side - FRONT
    glBegin(GL_POLYGON)
    glColor3f( 1.0, 0.0, 0.0 )
    glVertex3f( 0.5, -0.5, -0.5 ) # Point P1 is red
    glColor3f( 0.0, 1.0, 0.0 )
    glVertex3f( 0.5, 0.5, -0.5 ) # Point P2 is green
    glColor3f( 0.0, 0.0, 1.0 )
    glVertex3f( -0.5, 0.5, -0.5 ) # Point P3 is blue
    glColor3f( 1.0, 0.0, 1.0 )
    glVertex3f( -0.5, -0.5, -0.5 ) # Point P4 is purple
    glEnd()
    # White side - BACK
    glBegin(GL_POLYGON)
    glColor3f( 1.0, 1.0, 1.0 )
    glVertex3f( 0.5, -0.5, 0.5 )
    glVertex3f( 0.5, 0.5, 0.5 )
    glVertex3f( -0.5, 0.5, 0.5 )
    glVertex3f( -0.5, -0.5, 0.5 )
    glEnd()
    # Purple side - RIGHT
    glBegin(GL_POLYGON)
    glColor3f( 1.0, 0.0, 1.0 )
    glVertex3f( 0.5, -0.5, -0.5 )
    glVertex3f( 0.5, 0.5, -0.5 )
    glVertex3f( 0.5, 0.5, 0.5 )
    glVertex3f( 0.5, -0.5, 0.5 )
    glEnd()
    # Green side - LEFT
    glBegin(GL_POLYGON)
    glColor3f( 0.0, 1.0, 0.0 )
    glVertex3f( -0.5, -0.5, 0.5 )
    glVertex3f( -0.5, 0.5, 0.5 )
    glVertex3f( -0.5, 0.5, -0.5 )
    glVertex3f( -0.5, -0.5, -0.5 )
    glEnd()
    # Blue side - TOP
    glBegin(GL_POLYGON)
    glColor3f( 0.0, 0.0, 1.0 )
    glVertex3f( 0.5, 0.5, 0.5 )
    glVertex3f( 0.5, 0.5, -0.5 )
    glVertex3f( -0.5, 0.5, -0.5 )
    glVertex3f( -0.5, 0.5, 0.5 )
    glEnd()
    # Red side - BOTTOM
    glBegin(GL_POLYGON)
    glColor3f( 1.0, 0.0, 0.0 )
    glVertex3f( 0.5, -0.5, -0.5 )
    glVertex3f( 0.5, -0.5, 0.5 )
    glVertex3f( -0.5, -0.5, 0.5 )
    glVertex3f( -0.5, -0.5, -0.5 )
    glEnd()


def keyPressed(key, x, y):
    global cube_rotation_x, cube_rotation_x
    step = 5.0

    if key == b'q':
        cube_rotation_x += step
    elif key == b'a':
        cube_rotation_x -= step

    if key == b'w':
        cube_rotation_x += step
    elif key == b's':
        cube_rotation_x -= step
    glutPostRedisplay()

def specialKeyPressed(key, x, y):
    global cube_rotation_x, cube_rotation_y
    step = 5.0

    if key == GLUT_KEY_LEFT:
        cube_rotation_y -= step
    elif key == GLUT_KEY_RIGHT:
        cube_rotation_y += step
    elif key == GLUT_KEY_UP:
        cube_rotation_x -= step
    elif key == GLUT_KEY_DOWN:
        cube_rotation_x += step

    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Rotating Cube")
gluOrtho2D(-1, 1, -1, 1)
glutDisplayFunc(display)
glutKeyboardFunc(keyPressed)
glutSpecialFunc(specialKeyPressed) 
glutMainLoop()

