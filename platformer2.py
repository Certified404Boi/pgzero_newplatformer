# this script is for pgzero

guy = Actor("art") # declare the actors
ground = Actor("floor")

# variables
speedy = 0
falling = 99
speedx = 0
guy.pos = 400, 400
ground.pos = 400, 700
WIDTH = 800
HEIGHT = 800

def draw():
    screen.clear()
    guy.draw()
    ground.draw()
    
def update():
	global speedy, speedx, falling # declare global variables
	
	# vertical movement
	speedy -= 1
	falling += 1
	guy.y -= speedy
	touching = guy.colliderect(ground)
	if touching:
		guy.y += speedy
		speedy = 0
		falling = 0
		if keyboard.up:
			speedy = 25
	
	# horizontal movement
	if keyboard.left:
		speedx -= 1.5
	if keyboard.right:
		speedx += 1.5
	guy.x += speedx
	speedx *= 0.8
	
	# screen fencing
	if guy.x > 800:
		guy.x = 800
		speedx = 0
	if guy.x < 0:
		guy.x = 0
		speedx = 0
			
