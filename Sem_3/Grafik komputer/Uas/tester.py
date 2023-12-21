import sys
import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *

# Global variables
window_size = (800, 600)
ball_pos = [window_size[0] / 2, window_size[1] / 2]
ball_speed = [2.0, 1.5]
paddle_speed = 8.0
paddle_height = 100
paddle_width = 10
left_paddle_pos = [10, window_size[1] / 2 - paddle_height / 2]
right_paddle_pos = [window_size[0] - 20, window_size[1] / 2 - paddle_height / 2]

# Function to draw a rectangle
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# Function to update the game state
def update():
    global ball_pos, ball_speed, left_paddle_pos, right_paddle_pos

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check collision with top and bottom walls
    if ball_pos[1] < 0 or ball_pos[1] > window_size[1]:
        ball_speed[1] = -ball_speed[1]

    # Check collision with paddles
    if (
        left_paddle_pos[0] < ball_pos[0] < left_paddle_pos[0] + paddle_width
        and left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + paddle_height
    ) or (
        right_paddle_pos[0] - paddle_width < ball_pos[0] < right_paddle_pos[0]
        and right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + paddle_height
    ):
        ball_speed[0] = -ball_speed[0]

    # Update paddles
    keys = glfw.get_key(window, 0)
    if keys == glfw.PRESS:
        if keys == glfw.KEY_UP and right_paddle_pos[1] < window_size[1] - paddle_height:
            right_paddle_pos[1] += paddle_speed
        elif keys == glfw.KEY_DOWN and right_paddle_pos[1] > 0:
            right_paddle_pos[1] -= paddle_speed

    # Move the left paddle automatically (you can replace this with your own AI logic)
    if left_paddle_pos[1] + paddle_height / 2 < ball_pos[1]:
        left_paddle_pos[1] += paddle_speed
    elif left_paddle_pos[1] + paddle_height / 2 > ball_pos[1]:
        left_paddle_pos[1] -= paddle_speed

# Function to render the game
def render():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw paddles
    glColor3f(1.0, 1.0, 1.0)
    draw_rect(left_paddle_pos[0], left_paddle_pos[1], paddle_width, paddle_height)
    draw_rect(right_paddle_pos[0] - paddle_width, right_paddle_pos[1], paddle_width, paddle_height)

    # Draw ball
    draw_rect(ball_pos[0] - 5, ball_pos[1] - 5, 10, 10)

    glfw.swap_buffers(window)

# Initialize GLFW
if not glfw.init():
    sys.exit()

# Create a windowed mode window and its OpenGL context
window = glfw.create_window(window_size[0], window_size[1], "Pong", None, None)
if not window:
    glfw.terminate()
    sys.exit()

# Make the window's context current
glfw.make_context_current(window)

# Set the projection matrix
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, window_size[0], 0, window_size[1], -1, 1)
glMatrixMode(GL_MODELVIEW)

# Set the clear color
glClearColor(0, 0, 0, 1)

# Set up the game loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    update()
    render()

    if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(window, True)

# Terminate GLFW
glfw.terminate()
