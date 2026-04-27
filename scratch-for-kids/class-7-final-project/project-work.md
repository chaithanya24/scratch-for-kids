# Class 7: Final Project — Project Work

> These are 4 example projects kids can use as inspiration or follow step-by-step during build time.

---

## Project 1: Pong Game
**Goal:** Classic Pong — ball bounces around, player controls a paddle, score goes up on each hit.

**Instructions:**
1. Draw a "Paddle" sprite (flat rectangle) and a "Ball" sprite (small circle)
2. Create a "Score" variable
3. Paddle: use arrow keys to move left/right at the bottom
4. Ball: starts at center, moves in a random direction
5. Ball bounces off edges. If it touches the paddle, score +1 and reverse direction
6. If ball goes below the paddle (y < -175), game over

**Concepts used:** Loops, conditions, variables, motion.

---

## Project 2: Animated Story
**Goal:** A short animated story with scene changes, dialogue, and sound effects.

**Instructions:**
1. Add 3 backdrops (forest, castle, sky)
2. Add sprites: Knight, Dragon, Princess
3. Use `broadcast` messages to transition between scenes
4. Knight narrates and moves between scenes
5. Dragon appears in scene 2 and fades away when defeated (ghost effect)
6. Princess appears in the final scene

**Concepts used:** Broadcasts, backdrops, show/hide, ghost effect, glide.

---

## Project 3: Whack-a-Mole
**Goal:** Moles pop up from holes. Click them to score. They get faster over time.

**Instructions:**
1. Draw a backdrop with 6 "holes" (brown ovals)
2. Create one mole sprite
3. Create variables: "Score", "Speed", "Time" (30 second timer)
4. Use clones — each clone appears at a random hole position
5. Clones show briefly then disappear. Click to score.
6. Speed increases over time. Game ends when timer hits 0.

**Concepts used:** Clones, variables, click events, timer, difficulty scaling.

---

## Project 4: Dance Party
**Goal:** Multiple characters dance to music with synchronized moves.

**Instructions:**
1. Add 3-4 dancer sprites (use Scratch's built-in dancer sprites)
2. Add a music loop (Dance Celebrate or similar)
3. Each dancer: use `forever` loop with `next costume` for dancing animation
4. Add unique movements to each dancer (spinning, bouncing, color changing)
5. Optional: add a disco ball sprite that spins and changes color

**Concepts used:** Parallel scripts, music, loops, costumes, motion + looks combined.
