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
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
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
    glutCreateWindow(b"My OpenGL Window")

    gluOrtho2D(-1, 1, -1, 1)
    
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the clear color to white

    # Register GLUT callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
