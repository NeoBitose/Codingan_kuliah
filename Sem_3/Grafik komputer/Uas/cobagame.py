from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import time

width_area = 1900
height_area = 1000

ball_speed = []
player_speed = 0

player_height = 100
player_width = 20

ball_pos = [width_area / 2, height_area / 2]
left_player_pos = [40, height_area / 2 - player_height / 2]
right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]

left_score = 0
right_score = 0

splash_screen = True 
level = 0

def draw_rect(x, y, width, height):
  glBegin(GL_QUADS)
  glVertex2f(x, y)
  glVertex2f(x + width, y)
  glVertex2f(x + width, y + height)
  glVertex2f(x, y + height)
  glEnd()

def draw_text(x, y, text, font):
  glColor3f(1.0, 1.0, 1.0)
  glRasterPos2f(x, y)
  for character in text:
    glutBitmapCharacter(font, ord(character))
    
def player_right(a, b, c, d) :
  glColor3f(0.0, 0.0, 0.0)
  draw_rect(a, b, c, d)
  
def player_left(a, b, c, d) :
  glColor3f(0.0, 0.0, 0.0)
  draw_rect(a, b, c, d)

def ball(a, b, c, d) :
  glColor3f(1.0, 1.0, 0.0)
  draw_rect(a, b, c, d)

def key_func(key, x, y) :
  global left_player_pos, right_player_pos, player_height, height_area, player_speed, level, ball_speed, player_speed, game_over, main_kembali
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
  elif key == b'1':
    level = 1
    ball_speed = [1.0, 0.5]
    player_speed = 10
  elif key == b'2':
    level = 2
    ball_speed = [2.0, 1]
    player_speed = 20
  elif key == b'3':
    level = 3
    ball_speed = [3.0, 1.5]
    player_speed = 30

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
    right_player_pos[0] - player_width - player_width < ball_pos[0] < right_player_pos[0]
    and right_player_pos[1] < ball_pos[1] < right_player_pos[1] + player_height
  ):
    ball_speed[0] = -ball_speed[0]
    
  if ball_pos[0] < 0 :
    right_score += 1
    if ball_speed[0] < 0 :
      ball_speed[0] - 0.2
    else:
      ball_speed[0] + 0.2
    if ball_speed[1] < 0 :
      ball_speed[1] - 0.2
    else:
      ball_speed[1] + 0.2
    ball_pos = [width_area / 2, height_area / 2]
    left_player_pos = [40, height_area / 2 - player_height / 2]
    right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]
    print(f"right : {right_score}")
  elif ball_pos[0] > width_area :
    left_score += 1
    if ball_speed[0] < 0 :
      ball_speed[0] - 0.2
    else:
      ball_speed[0] + 0.2
    if ball_speed[1] < 0 :
      ball_speed[1] - 0.2
    else:
      ball_speed[1] + 0.2
    ball_pos = [width_area / 2, height_area / 2]
    left_player_pos = [40, height_area / 2 - player_height / 2]
    right_player_pos = [width_area - 40, height_area / 2 - player_height / 2]    
    print(f"left : {left_score}")

def splash():
  image_path = "splash.png"  # Replace with the actual path to your image file
  image = Image.open(image_path)
  image_data = image.tobytes("raw", "RGBA", 0, -1)
  width_area, height_area = image.size
  glDrawPixels(width_area, height_area, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

def game():
  player_right(right_player_pos[0] - player_width, right_player_pos[1], player_width, player_height )
  player_left(left_player_pos[0], left_player_pos[1], player_width, player_height )
  ball(ball_pos[0] - 5, ball_pos[1] - 5, 30, 30)
  move_ball()

def gameover():
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_QUADS)
  glVertex2f(0,0)
  glVertex2f(1900,0)
  glVertex2f(1900, 1000)
  glVertex2f(0,1000)
  glEnd()
  
def lapangan() :
  glColor3f(1.0, 1.0, 1.0)
  glBegin(GL_QUADS)
  glVertex2f(0,0)
  glVertex2f(1900,0)
  glVertex2f(1900, 1000)
  glVertex2f(0,1000)
  glEnd()
  
  glBegin(GL_QUADS)
  glColor3ub(3,82,27)
  glVertex2f(10,10)
  glVertex2f(945,10)
  glVertex2f(945,495)
  glVertex2f(10,495)
  glEnd()
  
  glBegin(GL_QUADS)
  glColor3ub(3,82,27)
  glVertex2f(955,10)
  glVertex2f(1890,10)
  glVertex2f(1890,495)
  glVertex2f(955,495)
  glEnd()
  
  glBegin(GL_QUADS)
  glColor3ub(3,82,27)
  glVertex2f(10,505)
  glVertex2f(945,505)
  glVertex2f(945,990)
  glVertex2f(10,990)
  glEnd()
  
  glBegin(GL_QUADS)
  glColor3ub(3,82,27)
  glVertex2f(955,505)
  glVertex2f(1890,505)
  glVertex2f(1890,990)
  glVertex2f(955,990)
  glEnd()
    
def iterate(): #menyiapkan media output
  global width_area, height_area
  glViewport(0, 0, width_area, height_area) # membuat ukuran viewport (x,y,w,h)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity() # merubah matrix menjadi matrix identitas
  glOrtho(0.0, width_area, 0.0, height_area, 0.0, 1.0)  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  
def showScreen():
  global player_height, player_width, left_player_pos, right_player_pos, splash_screen, level, main_kembali, game_over, right_score, left_score, width_area, height_area
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  iterate()
  # objek 
  lapangan()
  
  
  # if splash_screen == True:
  #   splash()
  #   if level == 1 or level == 2 or level == 3:
  #     splash_screen = False
  #   elif level == 0:
  #     splash_screen = True
  # else:
  #   if right_score == 10 or left_score == 10:
  #     right_score = 0
  #     left_score = 0
  #     level = 0
  #     time.sleep(3)
  #     splash_screen = True
  #     draw_text(0, 0, "")
      
  #   elif right_score < 10 or left_score < 10:
  #     lapangan()
  #     game()
  #     draw_text(20, 960, f"Skor Permainan {left_score} : {right_score}", GLUT_BITMAP_TIMES_ROMAN_24)
    
  glutSwapBuffers()
  
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width_area, height_area)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("KELOMPOK E - GAMEPONG")
glutDisplayFunc(showScreen)
glutKeyboardFunc(key_func)
glutIdleFunc(showScreen)
glutMainLoop() 
