import pygame

pygame.init()

# screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# colors
BLACK = (0, 0, 0)
DARK_GREY = (50, 50, 50)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)

# font setup
FONT = pygame.font.SysFont("Verdana", 36)

# screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("One Level")

# framerate clock
clock = pygame.time.Clock()

# player constants
PLAYER_SIZE = 40
PLAYER_SPEED = 5
JUMP_FORCE = 150 
GRAVITY = 8 

# level layout
PLATFORMS = [
    pygame.Rect(200, 600, 200, 20),
    pygame.Rect(200, 500, 200, 20),
    pygame.Rect(500, 400, 200, 20),
    pygame.Rect(800, 300, 200, 20),
]
BUTTON = pygame.Rect(820, 280, 40, 20)
DOOR = pygame.Rect(1150, 500, 80, 120)
SPIKES = [
    pygame.Rect(x, 680, 40, 40) for x in range(100, 1200, 40) if not (50 <= x <= 200)
]
FLOOR = pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10)
LEFT_WALL = pygame.Rect(0, 0, 10, SCREEN_HEIGHT)
RIGHT_WALL = pygame.Rect(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT)
CEILING = pygame.Rect(0, 0, SCREEN_WIDTH, 10)

# level text
LEVEL_TEXTS = {
    1: "Welcome to Level 1",
    2: "Watch your step",
    3: "Can you make it?",
    4: "Getting harder",
    5: "Halfway there!",
    6: "Don't give up!",
    7: "Spikes galore",
    8: "Almost there!",
    9: "One more to go!",
    10: "Final challenge",
}

# player
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, SCREEN_HEIGHT - PLAYER_SIZE - 20, PLAYER_SIZE, PLAYER_SIZE)
        self.color = LIGHT_BLUE
        self.x_velocity = 0
        self.y_velocity = 0
        self.on_ground = False

    def move(self, pressed_keys):
        self.x_velocity = 0
        if pressed_keys[pygame.K_LEFT]:
            self.x_velocity = -PLAYER_SPEED
        if pressed_keys[pygame.K_RIGHT]:
            self.x_velocity = PLAYER_SPEED

        # jumping
        if pressed_keys[pygame.K_UP] and self.on_ground:
            self.y_velocity = -JUMP_FORCE
            self.on_ground = False

        # gravity
        self.y_velocity += GRAVITY

        # movement
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity // 10

        # screen boundary failsafe
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # check platform collision
        self.on_ground = False
        for current_platform in PLATFORMS:
            if self.rect.colliderect(current_platform) and self.y_velocity > 0:
                self.rect.bottom = current_platform.top
                self.y_velocity = 0
                self.on_ground = True

        # check floor collision
        if self.rect.colliderect(FLOOR):
            self.rect.bottom = FLOOR.top
            self.y_velocity = 0
            self.on_ground = True

# game states
START_SCREEN = "start"
PLAYING = "playing"
VICTORY = "victory"
current_state = START_SCREEN

# current level
current_level = 1

# obstacle adding
def add_obstacle(level):
    if level == 2:
        SPIKES.append(pygame.Rect(250, 580, 40, 40))  # Add spike to first platform
    elif level == 3:
        PLATFORMS[1].width = 150  # Shrink second platform
        PLATFORMS[0].width = 150  # Shrink first platform
    elif level == 4:
        SPIKES.append(pygame.Rect(870, 280, 40, 40))  # Add spike to fourth platform
    elif level == 5:
        SPIKES.append(pygame.Rect(660, 380, 40, 40))  # Add spike to third platform
    elif level == 6:
        SPIKES.append(pygame.Rect(270, 480, 40, 40))  # Add spike to lower platform
    elif level == 7:
        SPIKES.append(pygame.Rect(1120, 440, 40, 40))  # Add spike to fourth platform
    elif level == 8:
        SPIKES.append(pygame.Rect(1220, 440, 40, 40))  # Add spike to higher platform
    elif level == 9:
        PLATFORMS.append(pygame.Rect(1100, 460, 150, 20))  # Add higher platform
        PLATFORMS.append(pygame.Rect(1060, 650, 150, 20))  # Add higher platform
    elif level == 10:
        SPIKES.append(pygame.Rect(650, 380, 40, 40))  # Add spike to third platform

# helper functions
def draw_text(text, x, y, color):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

def reset_level():
    player.rect.x = 50
    player.rect.y = SCREEN_HEIGHT - PLAYER_SIZE - 20

def handle_quit():
    pygame.quit()
    raise SystemExit

# game loop
player = Player()
button_pressed = False

while True:
    screen.fill(DARK_GREY)

    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            handle_quit()

    if current_state == START_SCREEN:
        # draw start screen
        draw_text("Only One Level", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 3, WHITE)
        draw_text("Press Enter to Play", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 3 + 50, WHITE)
        draw_text("Press Q to Quit", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 3 + 100, WHITE)

        if pressed_keys[pygame.K_RETURN]:
            current_state = PLAYING
        elif pressed_keys[pygame.K_q]:
            handle_quit()

    elif current_state == PLAYING:
        # add obstacles 
        add_obstacle(current_level)

        # draw floor, walls, and ceiling
        pygame.draw.rect(screen, WHITE, FLOOR)
        pygame.draw.rect(screen, WHITE, LEFT_WALL)
        pygame.draw.rect(screen, WHITE, RIGHT_WALL)
        pygame.draw.rect(screen, WHITE, CEILING)

        # draw platforms
        for current_platform in PLATFORMS:
            pygame.draw.rect(screen, WHITE, current_platform)

        # draw spikes
        for spike in SPIKES:
            pygame.draw.rect(screen, RED, spike)

        # draw button
        pygame.draw.rect(screen, PINK, BUTTON)

        # draw door
        pygame.draw.rect(screen, BLACK if not button_pressed else WHITE, DOOR)

        # draw player
        pygame.draw.rect(screen, player.color, player.rect)

        # level counter
        draw_text(f"Level: {current_level}", 50, 10, WHITE)

        # level text
        level_text = LEVEL_TEXTS.get(current_level, "")
        draw_text(level_text, SCREEN_WIDTH // 2 - 200, 50, LIGHT_BLUE)

        # quit button
        draw_text("Quit", 50, 50, WHITE)
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 50 <= mouse_x <= 150 and 50 <= mouse_y <= 100:
                handle_quit()

        # player movement
        player.move(pressed_keys)

        # check if player touches button
        if player.rect.colliderect(BUTTON):
            button_pressed = True

        # check if player touches door
        if button_pressed and player.rect.colliderect(DOOR):
            current_level += 1
            if current_level > 10:
                current_state = VICTORY
            else:
                reset_level()
                button_pressed = False

        # check if player touches spikes
        for spike in SPIKES:
            if player.rect.colliderect(spike):
                reset_level()

    elif current_state == VICTORY:
        draw_text("You Win!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 3, LIGHT_BLUE)
        draw_text("Press Q to Quit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 3 + 50, LIGHT_BLUE)

        if pressed_keys[pygame.K_q]:
            handle_quit()

    pygame.display.flip()
    clock.tick(60)
