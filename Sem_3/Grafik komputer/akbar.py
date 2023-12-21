from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# ... [Your existing code up to the global variables]

width_area = 1900
height_area = 1000

ball_speed = [1.0, 0.5]
player_speed = 10.0

player_height = 100
player_width = 20

# state_ball_pos = [width_area / 2, height_area / 2]
# state_left_player_pos = [40, height_area / 2 - player_height / 2]
# state_right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]

ball_pos = [width_area / 2, height_area / 2]
left_player_pos = [40, height_area / 2 - player_height / 2]
right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]

left_score = 0
right_score = 0

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()
    
def player_right(a, b, c, d) :
  draw_rect(a, b, c, d)
  
def player_left(a, b, c, d) :
  draw_rect(a, b, c, d)

def ball(a, b, c, d) :
  draw_rect(a, b, c, d)

def move_player(key, x, y) :
  global left_player_pos, right_player_pos, player_height, height_area, player_speed
  if key == b'w':
    if left_player_pos[1] < height_area - player_height :
      left_player_pos[1] += player_speed
  elif key == b's':
    if left_player_pos[1] > 0:
      left_player_pos[1] -= player_speed
  elif key == b'o':
    if right_player_pos[1] < height_area - player_height :
      right_player_pos[1] += player_speed
  elif key == b'l':
    if right_player_pos[1] > 0:
      right_player_pos[1] -= player_speed

def move_ball() :
  global right_score, left_score, ball_pos, ball_speed, left_player_pos, right_player_pos, player_width, player_height, width_area
  ball_pos[0] += ball_speed[0]
  ball_pos[1] += ball_speed[1]
  if ball_pos[1] < 0 or ball_pos[1] > height_area:
    ball_speed[1] = -ball_speed[1]
  if (
    left_player_pos[0] < ball_pos[0] < left_player_pos[0] + player_width
    and left_player_pos[1] < ball_pos[1] < left_player_pos[1] + player_height
  ) or (
    right_player_pos[0] - player_width < ball_pos[0] < right_player_pos[0]
    and right_player_pos[1] < ball_pos[1] < right_player_pos[1] + player_height
  ):
    ball_speed[0] = -ball_speed[0]
    
  if ball_pos[0] < 0 :
    right_score += 1
    ball_speed = [1.0, 0.5]
    ball_pos = [width_area / 2, height_area / 2]
    left_player_pos = [40, height_area / 2 - player_height / 2]
    right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]
    print(f"right : {right_score}")
  elif ball_pos[0] > width_area :
    left_score += 1
    ball_speed = [1.0, 0.5]
    ball_pos = [width_area / 2, height_area / 2]
    left_player_pos = [40, height_area / 2 - player_height / 2]
    right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]    
    print(f"left : {left_score}")

# Add a function to draw text on the screen for scores
def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))

def iterate(): 
    glViewport(0, 0, 1900, 1000) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() 
    glOrtho(0.0, 1900, 0.0, 1000, 0.0, 1.0)  
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global player_height, player_width, left_player_pos, right_player_pos
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # objek
    draw_text(20,20, "Selamat datang")
    player_right(right_player_pos[0] - player_width, right_player_pos[1], player_width, player_height )
    player_left(left_player_pos[0], left_player_pos[1], player_width, player_height )
    ball(ball_pos[0] - 5, ball_pos[1] - 5, 30, 30)
    move_ball()
    
    glutSwapBuffers()

def move_player(key, x, y):
    global left_player_pos, right_player_pos, player_height, height_area, player_speed

    if key == b'w':
        if left_player_pos[1] < height_area - player_height:
            left_player_pos[1] += player_speed
    elif key == b's':
        if left_player_pos[1] > 0:
            left_player_pos[1] -= player_speed
    elif key == b'o':
        if right_player_pos[1] < height_area - player_height:
            right_player_pos[1] += player_speed
    elif key == b'l':
        if right_player_pos[1] > 0:
            right_player_pos[1] -= player_speed



glutInit()
glutKeyboardFunc(move_player)    
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1900, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("KELOMPOK E - GAMEPONG")

glutDisplayFunc(showScreen)
glutKeyboardFunc(move_player)
glutIdleFunc(showScreen)

# def main_loop():
#     glutPostRedisplay()  
#     glutMainLoopEvent()  

# glutTimerFunc(1000 // 60, main_loop, 0)  
glutMainLoop() 



# width_area = 1900
# height_area = 1000

# ball_speed = [1.0, 0.5]
# player_speed = 10.0

# player_height = 100
# player_width = 20

# # state_ball_pos = [width_area / 2, height_area / 2]
# # state_left_player_pos = [40, height_area / 2 - player_height / 2]
# # state_right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]

# ball_pos = [width_area / 2, height_area / 2]
# left_player_pos = [40, height_area / 2 - player_height / 2]
# right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]

# left_score = 0
# right_score = 0

# def draw_rect(x, y, width, height):
#     glBegin(GL_QUADS)
#     glVertex2f(x, y)
#     glVertex2f(x + width, y)
#     glVertex2f(x + width, y + height)
#     glVertex2f(x, y + height)
#     glEnd()
    
# def player_right(a, b, c, d) :
#   draw_rect(a, b, c, d)
  
# def player_left(a, b, c, d) :
#   draw_rect(a, b, c, d)

# def ball(a, b, c, d) :
#   draw_rect(a, b, c, d)

# def move_player(key, x, y) :
#   global left_player_pos, right_player_pos, player_height, height_area, player_speed
#   if key == b'w':
#     if left_player_pos[1] < height_area - player_height :
#       left_player_pos[1] += player_speed
#   elif key == b's':
#     if left_player_pos[1] > 0:
#       left_player_pos[1] -= player_speed
#   elif key == b'o':
#     if right_player_pos[1] < height_area - player_height :
#       right_player_pos[1] += player_speed
#   elif key == b'l':
#     if right_player_pos[1] > 0:
#       right_player_pos[1] -= player_speed

# def move_ball() :
#   global right_score, left_score, ball_pos, ball_speed, left_player_pos, right_player_pos, player_width, player_height, width_area
#   ball_pos[0] += ball_speed[0]
#   ball_pos[1] += ball_speed[1]
#   if ball_pos[1] < 0 or ball_pos[1] > height_area:
#     ball_speed[1] = -ball_speed[1]
#   if (
#     left_player_pos[0] < ball_pos[0] < left_player_pos[0] + player_width
#     and left_player_pos[1] < ball_pos[1] < left_player_pos[1] + player_height
#   ) or (
#     right_player_pos[0] - player_width < ball_pos[0] < right_player_pos[0]
#     and right_player_pos[1] < ball_pos[1] < right_player_pos[1] + player_height
#   ):
#     ball_speed[0] = -ball_speed[0]
    
#   if ball_pos[0] < 0 :
#     right_score += 1
#     ball_speed = [1.0, 0.5]
#     ball_pos = [width_area / 2, height_area / 2]
#     left_player_pos = [40, height_area / 2 - player_height / 2]
#     right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]
#     print(f"right : {right_score}")
#   elif ball_pos[0] > width_area :
#     left_score += 1
#     ball_speed = [1.0, 0.5]
#     ball_pos = [width_area / 2, height_area / 2]
#     left_player_pos = [40, height_area / 2 - player_height / 2]
#     right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]    
#     print(f"left : {left_score}")
# def iterate(): #menyiapkan media output
#   glViewport(0, 0, 1900, 1000) # membuat ukuran viewport (x,y,w,h)
#   glMatrixMode(GL_PROJECTION)
#   glLoadIdentity() # merubah matrix menjadi matrix identitas
#   glOrtho(0.0, 1900, 0.0, 1000, 0.0, 1.0)  
#   glMatrixMode(GL_MODELVIEW)
#   glLoadIdentity()
  
# def showScreen():
#   global player_height, player_width, left_player_pos, right_player_pos
#   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#   glLoadIdentity()
#   iterate()
#   # objek
#   player_right(right_player_pos[0] - player_width, right_player_pos[1], player_width, player_height )
#   player_left(left_player_pos[0], left_player_pos[1], player_width, player_height )
#   ball(ball_pos[0] - 5, ball_pos[1] - 5, 30, 30)
#   move_ball()
  
#   glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(1900, 1000)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow("KELOMPOK E - GAMEPONG")
# glutDisplayFunc(showScreen)
# glutKeyboardFunc(move_player)
# glutIdleFunc(showScreen)
# glutMainLoop() #memanggil display terus menerus