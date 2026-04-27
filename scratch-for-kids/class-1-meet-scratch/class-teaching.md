# Class 1: Meet Scratch — Teaching Guide (1 Hour)

> **Topic:** Introduction to Scratch and Programming  
> **Duration:** 1 hour  
> **Age Group:** 7–12 years  
> **Prerequisites:** None  
> **Platform:** [Scratch 3.0](https://scratch.mit.edu)

## Learning Objectives
- Understand what programming is in simple terms
- Navigate the Scratch interface confidently
- Create and run a simple script using drag-and-drop blocks

---

## Session Breakdown

### Introduction (10 min)

**What is programming?**
- Analogy: "Imagine you have a robot friend. It only does exactly what you tell it. Programming is writing those instructions."
- Show a fun example: a finished Scratch game (e.g., a cat chasing a mouse)

**What is Scratch?**
- Created by MIT for kids to learn coding
- Used by millions of kids worldwide
- No typing needed — just drag and drop

### Interface Tour (10 min)

Walk kids through each part of the screen:

- **Stage:** The white area on the right where your project plays (480 x 360 pixels)
- **Sprite:** The character on the stage (default is the Scratch Cat)
- **Sprite List:** Below the stage — shows all your sprites
- **Block Palette:** Left side — colored categories of blocks (Motion, Looks, Sound, etc.)
- **Scripts Area:** Middle — where you drag blocks to build your program
- **Green Flag / Stop Sign:** Top of stage — runs and stops your project

**Activity:** Have kids click through each block category and read a few block names out loud.

### Understanding the Scratch Stage: The 2D Coordinate System (5 min)

Before we start coding, let's understand how Scratch knows WHERE to put things on the stage. It uses a **2D graph** — just like the ones in math class, but way more fun because we use it to move characters around!

#### The X Axis and Y Axis

```
                        y-axis
                          ↑
                          |  (0, 180) ← top center
                   180 ---|
                          |
                          |
         (-240, 0)        |          (240, 0)
  ← ─────────────────── (0,0) ──────────────────── → x-axis
                          |
                          |
                          |
                  -180 ---|
                          |  (0, -180) ← bottom center
                          ↓
```

- **X axis** = the horizontal line (left ↔ right)
  - Goes from **-240** (far left) to **+240** (far right)
  - Positive numbers → right side
  - Negative numbers → left side

- **Y axis** = the vertical line (up ↕ down)
  - Goes from **-180** (very bottom) to **+180** (very top)
  - Positive numbers → upper half
  - Negative numbers → lower half

- **Origin (0, 0)** = the exact center of the stage

**Kid-friendly explanation:** "Think of the stage like a treasure map. To find any spot, you need two numbers: how far left or right (x), and how far up or down (y)."

#### The 4 Quadrants

The X and Y axes divide the stage into 4 sections called **quadrants**:

```
              y-axis
                ↑
                |
   QUADRANT 2   |   QUADRANT 1
   x: negative  |   x: positive
   y: positive  |   y: positive
   (-x, +y)     |   (+x, +y)
                |
  ──────────── (0,0) ──────────── → x-axis
                |
   QUADRANT 3   |   QUADRANT 4
   x: negative  |   x: positive
   y: negative  |   y: negative
   (-x, -y)     |   (+x, -y)
                |
                ↓
```

| Quadrant | X value | Y value | Position on Stage | Example Point |
|----------|---------|---------|-------------------|---------------|
| **Quadrant 1** (top-right) | Positive (+) | Positive (+) | Upper right area | (150, 100) |
| **Quadrant 2** (top-left) | Negative (−) | Positive (+) | Upper left area | (-150, 100) |
| **Quadrant 3** (bottom-left) | Negative (−) | Negative (−) | Lower left area | (-150, -100) |
| **Quadrant 4** (bottom-right) | Positive (+) | Negative (−) | Lower right area | (150, -100) |

#### Key Points on the Stage

```
  (-240, 180)─────────────────────────────(240, 180)
       |                                       |
       |            SCRATCH STAGE              |
       |                                       |
       |              (0, 0)                   |
       |             ← center →                |
       |                                       |
       |                                       |
  (-240,-180)─────────────────────────────(240,-180)
```

| Location | Coordinates |
|----------|-------------|
| Center | (0, 0) |
| Top-left corner | (-240, 180) |
| Top-right corner | (240, 180) |
| Bottom-left corner | (-240, -180) |
| Bottom-right corner | (240, -180) |
| Top center | (0, 180) |
| Bottom center | (0, -180) |
| Left center | (-240, 0) |
| Right center | (240, 0) |

#### Fun Activity: "Where Am I?"

The instructor calls out coordinates, and kids point to where on the stage that would be:

1. **(0, 0)** → "Center! Right in the middle."
2. **(200, 150)** → "Top-right area — Quadrant 1"
3. **(-200, 150)** → "Top-left area — Quadrant 2"
4. **(-200, -150)** → "Bottom-left area — Quadrant 3"
5. **(200, -150)** → "Bottom-right area — Quadrant 4"
6. **(0, 180)** → "Very top, middle"
7. **(-240, 0)** → "Far left, halfway up"

**Reverse game:** Point to a spot on the stage and ask kids to guess the coordinates!

**Tip for kids:** "If you ever forget, just hover your mouse over the stage — Scratch shows the x and y position at the bottom right!"

---

### Guided Coding (15 min)

Build this together step by step:

1. Click the **Events** category (yellow) → drag `when green flag clicked` to the scripts area
2. Click **Looks** (purple) → drag `say [Hello!] for [2] seconds` and snap it below
3. Click **Motion** (blue) → drag `move [10] steps` and snap it below
4. Click the **Green Flag** — watch the cat say "Hello!" and move
5. Add `turn [15] degrees` and another `move [10] steps`
6. Click Green Flag again — the cat talks, moves, and turns

**Key Concept:** Blocks run from top to bottom, one after another. This is called **sequence**.

### Free Exploration (10 min)

Let kids experiment:
- Change the number in `move` to make the cat go farther
- Change the text in `say` to anything they want
- Try adding more blocks from Motion and Looks
- Try clicking the cat sprite on stage and dragging it around

### Wrap-Up & Discussion (5 min)

- "What did you make the cat do?"
- "What happens if you change the numbers in the blocks?"
- Preview next class: "Next time we'll make our sprites move in cool ways and change how they look!"
