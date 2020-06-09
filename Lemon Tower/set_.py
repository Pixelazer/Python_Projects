# Platformer by Aryan Takalkar
# Game settings

# Varibles & Settings 

# Define window size (length/height)
width = 500
height = 600
size = (width, height)

FPS = 60
Title = "Lemon Tower"

FontName = "Fixedsys"

HS_file = "highscore.txt"

# Define colors in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 125, 155)

# Player Settings
playerAcceleration = 0.5
playerFriction = -0.1
playerGravity = 0.8
playerJumpHeight = 20

# Platforms that appear on start
startingPlatforms = [(0, height - 40, width, 40), 
                     ((width/2 - 50), (height*3/4), 100, 20),
                     ((0), (height*1/2), 100, 20),
                     (width - 100, (height*1/2), 100, 20),
                     ((width/2 - 50), 100, 100, 20),
                     ((width/2 - 50), 300, 100, 20),
                     ]

# Spritesheet file name
SPRITESHEET = "spritesheet_jumper.png"