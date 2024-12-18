# final-game

Initially my plan was to make a cyberpunk rpg, but I soon realised that I was in over my head. That project is retired for now, along with the original sprites and soundtrack I had for it, and I hope to return to it once I have the appropriate experience. I instead created a simple 2d platformer that makes me feel very nostalgic for early flash games. I hope you enjoy.

# Pseudocode

Initialize pygame and required modules
Set screen dimensions and create window
Load and configure sounds
Define colors and font
Initialize player constants, level layout, and texts
Define the Player class with attributes and movement logic
Define game states and current level
Define helper functions for drawing text, resetting level, and quitting game

Game loop:

Clear the screen
Get pressed keys

Handle quit event

If game state is START_SCREEN:
  Display start screen text
  If Enter key is pressed, change state to PLAYING
  If Q key is pressed, quit game

If game state is PLAYING:
    Add level-specific obstacles
    Draw level elements
    Display level counter and level-specific text
    Handle quit button click

Update player movement
  Check for collision:
    If player touches spikes, play death sound and reset level
    If player touches the button, play button press sound and activate button
    If player touches the door and button is pressed, play level cleared sound, advance level, reset level if not last level
    Check if player lands on platforms or floor, apply gravity or reset position if necessary

If game state is VICTORY:
    Display victory screen text
    If Q key is pressed, quit game

Update display
Set frame rate
