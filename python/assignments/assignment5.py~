# Implementation of classic arcade game Pong
# Saurabh Patel
# Contact : skpatel@syr.edu

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[1,1]
score1=0
score2 = 0
score1_pos = [50,50]
score2_pos = [550,50]
paddle1_vel=0
paddle2_vel=0
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2

direction_right= False

#update padle positions
def update_padle_pos():
    global paddle1_pos, paddle2_pos,paddle1_vel, paddle2_vel
    if paddle1_pos > (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos = paddle1_pos - 1
    elif paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = paddle1_pos + 1
    else:
        paddle1_pos += paddle1_vel
    if paddle2_pos > (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos = paddle2_pos - 1
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = paddle2_pos + 1
    else:
        paddle2_pos += paddle2_vel

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if(direction) :
        ball_vel[0] = random.randrange(2, 3)
    else :
        ball_vel[0] = (-1) * random.randrange(2, 3)
    # we always need to go up side thats why here always we need to use minus sign    
    ball_vel[1] = (-1) * random.randrange(2, 3)

# update ball position and all
def update_ball_pos():
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    top_touch = (ball_pos[1] <= BALL_RADIUS) 
    bottom_touch = (ball_pos[1]>=(HEIGHT-BALL_RADIUS)-1)

    if top_touch or bottom_touch:
        ball_vel[0] =  ball_vel[0]
        ball_vel[1] = -ball_vel[1] 
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,direction_right,score1,score2  # these are numbers
    score1 = 0
    score2 = 0
    direction_right = False;
    direction = random.randint(0, 1)
    if direction == 1 :
        direction_right = True
    else :
        direction_right = False
    spawn_ball(direction_right)
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,direction_right,paddle1_top,paddle1_bottom,paddle2_top,paddle2_bottom
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Orange")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Orange")
        
    # update ball
    update_ball_pos()
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    update_padle_pos()
    
    # draw paddles
    # draw left hand side paddle
    paddle1_top=paddle1_pos-HALF_PAD_HEIGHT
    paddle1_bottom=paddle1_pos+HALF_PAD_HEIGHT
    paddle2_top=paddle2_pos-HALF_PAD_HEIGHT
    paddle2_bottom=paddle2_pos+HALF_PAD_HEIGHT
    
    canvas.draw_line([HALF_PAD_WIDTH,  paddle1_top],[HALF_PAD_WIDTH,  paddle1_bottom], PAD_WIDTH, "Orange")
    # draw right hand side paddle
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH,  paddle2_top],[WIDTH-HALF_PAD_WIDTH, paddle2_bottom], PAD_WIDTH, "Orange")

    
    # determine whether paddle and ball collide
    # determine its collide with left or right side.
    collide_right = (ball_pos[0] >= ((WIDTH-PAD_WIDTH)-BALL_RADIUS)-1)
    collide_left = (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH)
    # determine its collide with paddle or gutter.
    onpaddle1 = (paddle1_top <= ball_pos[1] <= paddle1_bottom) and (collide_left) #left
    onpaddle2 = (paddle2_top <= ball_pos[1] <= paddle2_bottom) and (collide_right) #right
    onpaddle_right = onpaddle2 and collide_right
    onpaddle_left = onpaddle1 and collide_left
    onpaddle = onpaddle_right or onpaddle_left
    
  	# its on paddle
    if(onpaddle) :
        ball_vel[0] = (-1.2)*ball_vel[0]
        ball_vel[1] = (1.2)*ball_vel[1]
    # its in gutter, increase score level    
    else :
        if collide_right :
            direction_right=False
            score1 = score1 +1
            spawn_ball(direction_right)
        if collide_left :
            direction_right=True
            score2 = score2 +1
            spawn_ball(direction_right)
    # draw scores
    canvas.draw_text(str(score1), score1_pos, 36, "Green")
    canvas.draw_text(str(score2), score2_pos, 36, "Green")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel=paddle1_vel-5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel=paddle1_vel+5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel=paddle2_vel+5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel=paddle2_vel-5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel=0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel=0

def restart_button_handler():
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Restart Game", restart_button_handler, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()

