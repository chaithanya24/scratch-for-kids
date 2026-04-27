# Class 6: Cloning & Advanced Techniques — Project Work

> These are the 4 projects for Class 6. Each focuses on cloning and combining concepts.

---

## Project 1: Snowfall Animation
**Goal:** Snowflakes fall from the sky in random positions and sizes.

**Instructions:**
1. Draw a small white circle sprite (snowflake). Add a winter backdrop.
2. Hide the original sprite on green flag
3. Use a `forever` loop to `create clone of [myself]` every 0.2 seconds
4. In `when I start as a clone`: go to random x at top, set random size, show
5. Fall down with slight random horizontal drift
6. Delete the clone when it reaches the bottom

**Concepts practiced:** Clones with randomized properties, natural-looking animation.

---

## Project 2: Balloon Pop Game
**Goal:** Balloons float up from the bottom. Click them to pop them and score points.

**Instructions:**
1. Use the "Balloon1" sprite. Create variable "Score".
2. Hide original, create clones in a `forever` loop
3. Clones start at bottom with random x, size, and color
4. Clones float upward and delete when off screen
5. Add a second `when I start as a clone` script for click detection
6. On click: increase score, play pop sound, animate with ghost effect, delete

**Concepts practiced:** Click detection on clones, ghost effect for pop animation, parallel scripts on clones.

---

## Project 3: Rain of Emojis
**Goal:** Different emoji sprites fall from the sky. Catch the happy faces (+1), avoid the sad faces (-1).

**Instructions:**
1. Create a sprite with 2 costumes: happy face and sad face
2. Add a Player sprite at the bottom that follows the mouse
3. Clones fall from random positions, each randomly picking happy or sad costume
4. If clone touches player: check costume name to decide +1 or -1 score
5. Delete clone after being caught or reaching the bottom

**Concepts practiced:** Costume-based logic, mouse following, positive and negative scoring.

---

## Project 4: Fireworks Display
**Goal:** Click anywhere on the stage to launch a firework that explodes into particles.

**Instructions:**
1. Create a "Launcher" sprite (small arrow/rocket) and a "Particle" sprite (small dot)
2. Launcher: on mouse click, glide from bottom to mouse position, then broadcast [explode]
3. Particle: on receiving [explode], create 20 clones of itself
4. Each particle clone: go to launcher position, pick random direction, move outward
5. Particles fade out using ghost effect and shrink, then delete

**Concepts practiced:** Broadcast triggering clones, particle effects, combining multiple techniques.
