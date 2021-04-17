import pygame as pg

'''REQUIRED FUNCTIONS'''
def visuals():
	window.fill(WHITE)
	pg.draw.rect(window, LIGHT_GREY, player1)
	pg.draw.rect(window, LIGHT_GREY, player2)
	pg.draw.ellipse(window, LIGHT_GREY, ball)
	pg.draw.aaline(window, LIGHT_GREY,(w/2,0), (w/2,h))
	
def player1_animation():
	player1.y += player_speed
	if player1.top <= 0:
		player1.top = 0
	if player1.bottom > h:
		player1.bottom = h

def player2_ai():
	if player2.top < ball.y:
		player2.top += player2_speed
	if player2.top > ball.y:
		player2.top -= player2_speed
	if player2.bottom > h:
		player2.bottom = h

def ball_animation():
	global ball_speed_x, ball_speed_y
	ball.x += ball_speed_x
	ball.y += ball_speed_y
	
	if ball.top < 0 or ball.bottom >= h:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= w:
		ball_speed_x *= -1

	if ball.colliderect(player1) or ball.colliderect(player2):
		ball_speed_x *= -1

# GAME INITIALIZATION
pg.init()

# CONFIGS
w, h = 600, 400
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)

# SCREEN
window = pg.display.set_mode((w, h))
pg.display.set_caption('Ping-pong')
pg.display.set_icon(pg.image.load("ping-pong.jpg"))

# SPRITES
ball = pg.Rect(w/2 - 15,h/2 - 15,30,30)
player1 = pg.Rect(w - 20,h/2 - 70,10,140)
player2 = pg.Rect(10, h/2 - 70,10,140)

# SPEEDS
ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
player2_speed = 7

# VARS
game = True
clock = pg.time.Clock()
FPS = 60

# MAIN LOOP
while game:
	# HANDLING INPUT
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game = False

		# DOWN
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_DOWN:
				player_speed += 7
			if event.key == pg.K_UP:
				player_speed -= 7
		
		# UP
		if event.type == pg.KEYUP:
			if event.key == pg.K_DOWN:
				player_speed -= 7
			if event.key == pg.K_UP:
				player_speed += 7	

	# START
	ball_animation()
	visuals()
	player1_animation()
	player2_ai()
	
	# UPDATE
	clock.tick(FPS)
	pg.display.update()
