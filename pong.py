# Implementation of classic arcade game Pong

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
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right == True:
        ball_vel = [random.randrange(1, 4), -(random.randrange(2, 3))]
    else:
        ball_vel = [-(random.randrange(1, 4)), -(random.randrange(2, 3))]
    pass

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    global ball_pos, ball_vel
    score1 = 0
    score2 = 0
    paddle1_pos = 200
    paddle2_pos = 200
    paddle1_vel = 0
    paddle2_vel = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(1,3), random.randrange(-3,-1)]
    pass
def score_to_text(x):
    global score1, score2
    x = str(x)
    return x
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    c.draw_text("Mr. John Hammond: " + score_to_text(score1), [25,25], 16, "Red")
    c.draw_text("Mr. Dennis Nedry: " + score_to_text(score2), [(WIDTH / 2) + 25, 25], 16, "Green")
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel) > HALF_PAD_HEIGHT and (paddle1_pos + paddle1_vel) < (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos = paddle1_pos + paddle1_vel
    if (paddle2_pos + paddle2_vel) > HALF_PAD_HEIGHT and (paddle2_pos + paddle2_vel) < (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos = paddle2_pos + paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line([4, (40 + paddle1_pos)], [4, (paddle1_pos - 40)], PAD_WIDTH, "White")
    c.draw_line([(WIDTH - HALF_PAD_WIDTH), (40 + paddle2_pos)], [(WIDTH - HALF_PAD_WIDTH), (paddle2_pos - 40)], PAD_WIDTH, "White")
    
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -(ball_vel[1])
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -(ball_vel[1])
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] + BALL_RADIUS) >= (paddle1_pos - HALF_PAD_HEIGHT + 10) and (ball_pos[1] + BALL_RADIUS) <= (paddle1_pos + HALF_PAD_HEIGHT + 10):
            ball_vel[0] = -(ball_vel[0]) * 1.1
        else:
            right = True
            score2 += 1
            ball_init(right)        
    elif ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if (ball_pos[1] + BALL_RADIUS) >= (paddle2_pos - HALF_PAD_HEIGHT + 10) and (ball_pos[1] + BALL_RADIUS) <= (paddle2_pos + HALF_PAD_HEIGHT + 10):
            ball_vel[0] = -(ball_vel[0]) * 1.1
        else:
            right = False
            score1 += 1
            ball_init(right)
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 4, "White", "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc =2
    if key == simplegui.KEY_MAP["W"]:
        paddle1_vel -= acc
        return paddle1_vel
    if key == simplegui.KEY_MAP["S"]:
        paddle1_vel += acc
        return paddle1_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
        return paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
        return paddle2_vel
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["W"] or key == simplegui.KEY_MAP["S"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
label = frame.add_label("Welcome...")
label = frame.add_label("to Jurassic Park Pong!")
label = frame.add_label("")
label = frame.add_label("First Match:")
label = frame.add_label("")
label = frame.add_label("Mr. Hammond")
label = frame.add_label("Versus")
label = frame.add_label("Mr. Nedry")
label = frame.add_label("")
label = frame.add_label('Left uses "W and S"')
label = frame.add_label('Right uses "Up and Down"')
label = frame.add_label("")
label = frame.add_label("Good Luck!")
frame.add_button("Start the Game!", init, 100)                     
                        

                     

# start frame
frame.start()

