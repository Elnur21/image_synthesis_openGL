from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
move = 0.3
speed = 0.01
# Disply callback function
def display():
# Reset background
    glClear(GL_COLOR_BUFFER_BIT)
    # Render scene
    render_Scene()
    # Swap buffers
    glutSwapBuffers()
def idle():
    global move
    move += speed
    if move > 1.0:
        move = -0.3  # Reset the position when it reaches the right end
    time.sleep(0.01)
    glutPostRedisplay()
# Scene render function
def render_Scene():
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3 + move, -0.1, 0.1)
    glVertex3f(0.3 + move, -0.1, 0.0)
    glVertex3f(0 + move, 0.3, -0.2)
    glEnd()


# Initialize GLUT
glutInit()
# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)
# Create the window and give it a title
glutCreateWindow(b"Animating a triangle")
# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)
# Define display callback
glutDisplayFunc(display)
# Define idle callback
glutIdleFunc(idle)
# Begin event loop
glutMainLoop()