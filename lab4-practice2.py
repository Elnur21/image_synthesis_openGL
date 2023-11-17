from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initial window size
window_width = 800
window_height = 600

def draw_cube():
    glutSolidCube(10.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Set the view
    gluLookAt(2, -4, -2, 0, 0, 0, 0, 1, 0)
    
    # Draw a cube
    draw_cube()
    
    glutSwapBuffers()

def reshape(width, height):
    # Set the new window size
    global window_width, window_height
    window_width = width
    window_height = height

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Experiment with gluPerspective parameters
    gluPerspective(45.0, width/height, 2.0, 10.0)

    # Set the view
    gluLookAt(2, -4, -2, 0, 0, 0, 0, 1, 0)

    glutPostRedisplay()

def keyboard(key, x, y):
    if key == b'\x1b':  # Escape key
        sys.exit(0)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b"OpenGL Cube Example")

glEnable(GL_DEPTH_TEST)

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)

glutMainLoop()
