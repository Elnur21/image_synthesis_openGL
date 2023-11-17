from math import cos, sin
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_width, window_height = 500, 500
window_position_x, window_position_y = 0, 0
polygon_order = 8 

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_Scene()
    glFlush()
    glutSwapBuffers()


def draw_regular_polygon():
    # Set color to cyan
    glColor3f(0.0, 1.0, 1.0)

    # Draw using GL_TRIANGLES
    glBegin(GL_TRIANGLES)
    draw_triangles()
    glEnd()

    # Draw using GL_TRIANGLE_STRIP
    glTranslatef(2.0, 0.0, 0.0)  # Shift to the right for the next method
    glBegin(GL_TRIANGLE_STRIP)
    draw_triangle_strip()
    glEnd()

    # Draw using GL_TRIANGLE_FAN
    glTranslatef(-2.0, -2.0, 0.0)  # Shift back to the center and down
    glBegin(GL_TRIANGLE_FAN)
    draw_triangle_fan()
    glEnd()

def draw_triangles():
    for i in range(8):
        angle1 = (2 * math.pi * i) / 8
        angle2 = (2 * math.pi * (i + 1)) / 8

        x1, y1 = 0.0, 0.0
        x2, y2 = math.cos(angle1), math.sin(angle1)
        x3, y3 = math.cos(angle2), math.sin(angle2)

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glVertex2f(x3, y3)

def draw_triangle_strip():
    for i in range(8 + 1):
        angle = (2 * math.pi * i) / 8

        x, y = math.cos(angle), math.sin(angle)

        glVertex2f(x, y)
        glVertex2f(0.0, 0.0)

def draw_triangle_fan():
    glVertex2f(0.0, 0.0)
    for i in range(8 + 1):
        angle = (2 * math.pi * i) / 8

        x, y = math.cos(angle), math.sin(angle)

        glVertex2f(x, y)
    
def render_Scene():
    draw_regular_polygon()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2.0, 4.0, -1.0, 1.0)  # Adjust the view based on the number of primitives
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Function to update and print window information
def update_window_info():
    print("Window Size:", window_width, "x", window_height)
    print("Window Position:", window_position_x, ",", window_position_y)
    print()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Polygons")

    gluOrtho2D(-1, 1, -1, 1)
    

    # Register GLUT callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
