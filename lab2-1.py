from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_width, window_height = 0, 0
window_position_x, window_position_y = 0, 0

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_Scene()
    glFlush()
    glutSwapBuffers()

def render_Scene():
    # Draw the first point (red)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = i * (3.14 / 180.0)
        x = -0.4 + 0.03 * cos(angle)
        y = 0.5 + 0.03*sin(angle)
        z = 0.0
        glVertex3f(x, y, z)
    glEnd()
    # Draw the second point (green)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = i * (3.14 / 180.0)
        x = -0.2 + 0.06 * cos(angle)
        y = -0.4 + 0.06*sin(angle)
        z = 0.0
        glVertex3f(x, y, z)
    glEnd()
    # Draw the third point (blue)
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = i * (3.14 / 180.0)
        x = 0.5 + 0.06 * cos(angle)
        y = 0.2 + 0.06*sin(angle)
        z = 0.0
        glVertex3f(x, y, z)
    glEnd()

# GLUT callback function for window resize
def reshape(width, height):
    global window_width, window_height
    window_width, window_height = width, height
    update_window_info()

# Function to update and print window information
def update_window_info():
    print("Window Size:", window_width, "x", window_height)
    print("Window Position:", window_position_x, ",", window_position_y)
    print()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Circles")

    gluOrtho2D(-1, 1, -1, 1)
    

    # Register GLUT callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
