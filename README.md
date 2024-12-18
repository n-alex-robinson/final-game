# final-game

Initially my plan was to make a cyberpunk rpg, but I soon realised that I was in over my head. That project is retired for now, along with the original sprites and soundtrack I had for it, and I hope to return to it once I have the appropriate experience. I instead created a simple 2d platformer that makes me feel very nostalgic for early flash games. I hope you enjoy.

# Pseudocode

Initialize pygame and required modules<br />
Set screen dimensions and create window<br />
Load and configure sounds<br />
Define colors and font<br />
Initialize player constants, level layout, and texts<br />
Define the Player class with attributes and movement logic<br />
Define game states and current level<br />
Define helper functions for drawing text, resetting level, and quitting game<br />
<br />
Game loop:<br />
<br />
Clear the screen<br />
Get pressed keys<br />
<br />
Handle quit event<br />
<br />
If game state is START_SCREEN:<br />
  Display start screen text<br />
  If Enter key is pressed, change state to PLAYING<br />
  If Q key is pressed, quit game<br />
<br />
If game state is PLAYING:<br />
    Add level-specific obstacles<br />
    Draw level elements<br />
    Display level counter and level-specific text<br />
    Handle quit button click<br />
<br />
Update player movement<br />
  Check for collision:<br />
    If player touches spikes, play death sound and reset level<br />
    If player touches the button, play button press sound and activate button<br />
    If player touches the door and button is pressed, play level cleared sound, advance level, reset level if not last level<br />
    Check if player lands on platforms or floor, apply gravity or reset position if necessary<br />

If game state is VICTORY:
    Display victory screen text
    If Q key is pressed, quit game

Update display
Set frame rate
