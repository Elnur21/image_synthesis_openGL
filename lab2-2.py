from math import cos, sin
import random
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
    pointSize=0
    index=1
    for i in range(150):
        pointSize+=0.05
        index+=3
        colorG=random.random()
        colorR=random.random()
        colorB=random.random()
        glColor3f(colorR, colorB, colorG)
        glPointSize(pointSize)
        glBegin(GL_POINTS)
        angle = index * (3.14159265 / 180.0)
        x = 0 + 0.7 * cos(angle)
        y = 0 + 0.7 * sin(angle)
        glVertex2f(x, y)
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
    glutCreateWindow(b"Big circle with squares")

    gluOrtho2D(-1, 1, -1, 1)
    

    # Register GLUT callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
