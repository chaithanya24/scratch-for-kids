# Class 2: Motion & Looks — Project Work

> These are the 4 projects for Class 2. Each focuses on motion and looks blocks.

---

## Project 1: Walking Animation
**Goal:** Make the cat walk back and forth across the stage with a walking animation.

**Instructions:**
1. Use `set rotation style [left-right]` so the cat doesn't flip upside down
2. Put movement and costume switching inside a `forever` loop
3. Add `if on edge, bounce` so the cat turns around at the edges
4. Add a small `wait` to control animation speed

**Concepts practiced:** Rotation style, costume switching for animation, forever loop preview.

---

## Project 2: Growing and Shrinking Sprite
**Goal:** A sprite that grows big, then shrinks back to normal.

**Instructions:**
1. Start by setting the size to 100%
2. Use a `repeat (10)` block with `change size by (10)` to grow
3. Add a small `wait` between each size change
4. Use another `repeat (10)` block with `change size by (-10)` to shrink

**Concepts practiced:** `change size by` with positive and negative numbers, `repeat` block preview.

---

## Project 3: Color Changing Parrot
**Goal:** A parrot that flies across the screen changing colors.

**Instructions:**
1. Choose the "Parrot" sprite (it has multiple costumes for wing flapping)
2. Start the parrot at the left side of the stage: `go to x: (-200) y: (50)`
3. Use a `repeat` loop combining `move`, `next costume`, and `change [color] effect`
4. End with `clear graphic effects` and a `say` block

**Concepts practiced:** Graphic effects, combining motion with looks, `clear graphic effects`.

---

## Project 4: Sprite Parade
**Goal:** Three sprites walk across the stage one after another.

**Instructions:**
1. Add 3 sprites (Cat, Dog, Duck)
2. Position them all at x: -200 but at different y values (100, 0, -100)
3. Use `glide` blocks to move each across the stage
4. Use `wait` blocks on the 2nd and 3rd sprites so they start after the previous one
5. Add `say` blocks at the end of each glide

**Concepts practiced:** Multiple sprites, `wait` for staggered timing, `glide` for smooth movement, y-positioning.
