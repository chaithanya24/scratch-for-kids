# Class 4: Loops & Conditions — Project Work

> These are the 4 projects for Class 4. Each focuses on loops and conditional logic.

---

## Project 1: Dodge the Obstacles
**Goal:** A sprite moves left/right to dodge falling objects.

**Instructions:**
1. Place the Cat at the bottom of the stage
2. Add a "Ball" sprite
3. Cat uses `forever` loop with `if key pressed` to move left/right
4. Ball uses `forever` loop: goes to random x at top, then `repeat until` it reaches the bottom
5. Ball resets to top and repeats

**Concepts practiced:** `repeat until` with a condition, combining loops with key controls.

---

## Project 2: Color Touch Game
**Goal:** Sprite changes color when touching different colored areas on the backdrop.

**Instructions:**
1. Paint a backdrop with 4 colored quadrants (red, blue, green, yellow)
2. Use arrow keys to move the sprite around
3. Inside a `forever` loop, add `if touching color` blocks for each color
4. Each color triggers a different `say` message and `set color effect`

**Concepts practiced:** Color sensing, multiple if blocks, color effects.

---

## Project 3: Chase Game
**Goal:** A cat chases the mouse pointer. If it catches it, it says "Got you!"

**Instructions:**
1. Use `point towards [mouse-pointer]` inside a `forever` loop
2. Add `move` steps after pointing
3. Add an `if touching [mouse-pointer]` condition
4. When caught: say something, go back to center, wait, then resume

**Extension:** Add a second sprite that runs away from the cat using `point towards` + `turn 180 degrees`.

**Concepts practiced:** `point towards`, combining motion with conditions, simple AI behavior.

---

## Project 4: Traffic Light Simulator
**Goal:** A traffic light that cycles through red, yellow, green with a walking character that responds.

**Instructions:**
1. Create a sprite with 3 costumes (red light, yellow light, green light)
2. Use a `forever` loop to cycle through costumes with `wait` blocks
3. `broadcast` a message for each light color
4. Add a person sprite that walks on green and stops on red/yellow
5. Use `when I receive` blocks on the person sprite

**Concepts practiced:** Broadcast + conditions, costume switching for state, `stop [other scripts in sprite]`.
