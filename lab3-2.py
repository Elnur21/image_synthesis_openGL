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
    # Display the current modelview matrix before the translation
    glColor3f(0,1,0)
    # translate the triangl
    glScale(0.05, 1.2, 1.0);
    glBegin(GL_TRIANGLES)
    glVertex3f( -0.8, -0.3, -0.1)
    glVertex3f( -0.3, 0.5, 0.0)
    glVertex3f( 0.2, 0.3, 0.2)
    glEnd()



def print_modelview_matrix():
    modelview_matrix = glGetDoublev(GL_MODELVIEW_MATRIX)
    for i in range(4):
        print(modelview_matrix[i])

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

    # Register GLUT callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == "__main__":
    main()
