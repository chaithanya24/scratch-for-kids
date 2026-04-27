# Class 1: Meet Scratch — Teaching Guide (1 Hour)

> **Topic:** Introduction to Scratch and Programming  
> **Duration:** 1 hour  
> **Age Group:** 7–12 years  
> **Prerequisites:** None  
> **Platform:** [Scratch 3.0](https://scratch.mit.edu)

## Learning Objectives
- Understand what programming is in simple terms
- Learn how a computer works and executes tasks
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

### How Does a Computer Work? (5 min)

Before we start coding, let's understand what's happening inside the computer when we give it instructions!

**A computer has 4 main parts that work together — like a team:**

#### 1. Input (The Ears & Eyes) 👀👂
- This is how the computer receives information from YOU
- Examples: keyboard, mouse, microphone, camera, touchscreen
- "When you press a key or click the mouse, that's INPUT — you're telling the computer something"

#### 2. CPU — The Brain 🧠
- CPU stands for "Central Processing Unit"
- It's the brain of the computer — it thinks and makes decisions
- It reads your instructions (the program) and figures out what to do
- "When you tell Scratch to move the cat 10 steps, the CPU calculates where the cat should go"
- The CPU is VERY fast — it can do billions of calculations per second!

#### 3. Memory (The Notebook) 📝
- **RAM (short-term memory):** Like a whiteboard — stores what the computer is working on RIGHT NOW. When you turn off the computer, it gets erased.
- **Storage (long-term memory):** Like a filing cabinet — stores your files, games, and programs permanently. Your Scratch projects are saved here!
- "When you create a variable called 'Score' in Scratch, the computer stores that number in memory"

#### 4. Output (The Mouth & Hands) 🖥️🔊
- This is how the computer shows you the results
- Examples: screen (monitor), speakers, printer
- "When the cat moves on the Scratch stage or says 'Hello!' — that's OUTPUT"

#### How They Work Together — Step by Step

Here's what happens when you click the Green Flag in Scratch:

1. **INPUT:** You click the green flag with your mouse
2. **CPU:** The brain reads your blocks from top to bottom: "First say Hello, then move 10 steps"
3. **MEMORY:** The computer remembers where the cat is, what it's saying, and any variables
4. **OUTPUT:** The cat appears on screen, shows a speech bubble, and moves!

**Kid-friendly analogy — The Restaurant:**
- **Input** = The customer (you) gives an order to the waiter
- **CPU** = The chef reads the order and cooks the food
- **Memory** = The recipe book and the counter where food is being prepared
- **Output** = The finished meal is served to you on a plate

**Key point:** "A program is just a list of instructions. The computer reads them one by one, from top to bottom, and does exactly what they say. That's why the ORDER of your Scratch blocks matters!"

### Interface Tour (10 min)

Walk kids through each part of the screen:

- **Stage:** The white area on the right where your project plays (480 x 360 pixels)
- **Sprite:** The character on the stage (default is the Scratch Cat)
- **Sprite List:** Below the stage — shows all your sprites
- **Block Palette:** Left side — colored categories of blocks (Motion, Looks, Sound, etc.)
- **Scripts Area:** Middle — where you drag blocks to build your program
- **Green Flag / Stop Sign:** Top of stage — runs and stops your project

**Activity:** Have kids click through each block category and read a few block names out loud.

### Sprites, Costumes, Stages & Backdrops (10 min)

These are the 4 building blocks of every Scratch project. Let's learn each one!

#### What is a Sprite? 🎭

A **sprite** is any character or object in your project. It's the "actor" on your stage.

- The default sprite is the **Scratch Cat** — but you can have as many sprites as you want
- Each sprite has its own scripts (code), costumes, and sounds
- Sprites can move, talk, change appearance, and interact with each other

**How to add a sprite:**
1. Look at the bottom-right of the screen — you'll see the **Sprite List**
2. Hover over the blue cat icon with a "+" sign
3. You get 4 options:
   - 🔍 **Choose a Sprite** — pick from Scratch's library (hundreds of characters, animals, objects)
   - 🎨 **Paint** — draw your own sprite
   - 🎲 **Surprise** — get a random sprite
   - 📁 **Upload** — use your own image file

**How to delete a sprite:**
- Right-click the sprite in the Sprite List → click "delete"
- Or click the sprite, then click the trash can icon

**Sprite properties (shown below the stage):**
- **Name:** You can rename your sprite (click the name to edit)
- **Position:** Shows the x and y coordinates
- **Show/Hide:** The eye icon toggles visibility
- **Size:** 100 = normal, 200 = double size, 50 = half size
- **Direction:** Which way the sprite is facing (90 = right)

#### What are Costumes? 👗

A **costume** is what a sprite looks like. Each sprite can have multiple costumes — like different outfits!

- The Scratch Cat has **2 costumes** (legs in different positions)
- Switching between costumes quickly creates **animation** (like a flipbook)
- Click the **"Costumes" tab** at the top to see and edit costumes

**What you can do in the Costumes tab:**
- See all costumes for the selected sprite
- Click a costume to switch to it
- **Draw a new costume** using the paint editor
- **Upload** an image as a costume
- **Duplicate** a costume and modify it
- **Delete** costumes you don't need
- Use the paint tools to edit: brush, eraser, fill, text, shapes

**Fun facts about costumes:**
- Some sprites have LOTS of costumes (dancers have 4+, letters have uppercase/lowercase)
- The `next costume` block cycles through all costumes in order
- The `switch costume to [name]` block jumps to a specific costume
- Costume names matter — you can use them in your code!

#### What is the Stage? 🎬

The **stage** is the background area where your project plays — think of it as the "theater" where your sprites perform.

- The stage is **480 pixels wide** and **360 pixels tall**
- The center of the stage is position **(0, 0)**
- The stage is always behind all sprites (it's the back layer)
- The stage can have its own scripts too! (useful for game timers, score displays, etc.)

**The stage is NOT a sprite** — it's special:
- It can't move or change size
- It can't use motion blocks
- But it CAN use looks, sound, event, control, sensing, and variable blocks
- It has its own scripts area (click the stage icon to select it)

#### What are Backdrops? 🖼️

A **backdrop** is a costume for the stage — it's the background image of your project.

- Just like sprites have costumes, the stage has **backdrops**
- You can have multiple backdrops and switch between them (great for scene changes in stories!)
- The default backdrop is plain white

**How to add a backdrop:**
1. Look at the bottom-right corner — next to the sprite chooser, there's a **backdrop icon** (looks like a small landscape)
2. Hover over it for 4 options:
   - 🔍 **Choose a Backdrop** — pick from Scratch's library (outdoor scenes, rooms, patterns, etc.)
   - 🎨 **Paint** — draw your own backdrop
   - 🎲 **Surprise** — get a random backdrop
   - 📁 **Upload** — use your own image

**Switching backdrops in code:**
- `switch backdrop to [name]` — instantly changes the background
- `next backdrop` — cycles to the next one
- `when backdrop switches to [name]` — triggers a script when the backdrop changes (great for stories!)

**How sprites and backdrops work together:**
- Backdrops set the **scene** (forest, space, classroom, underwater)
- Sprites are the **characters and objects** in that scene
- Changing the backdrop = changing the scene (like acts in a play)

#### Quick Reference: Sprites vs Stage

| Feature | Sprite | Stage |
|---------|--------|-------|
| Can move? | ✅ Yes | ❌ No |
| Has costumes? | ✅ Yes (called "costumes") | ✅ Yes (called "backdrops") |
| Has scripts? | ✅ Yes | ✅ Yes |
| Has sounds? | ✅ Yes | ✅ Yes |
| Can change size? | ✅ Yes | ❌ No |
| Can be duplicated? | ✅ Yes | ❌ No |
| Uses motion blocks? | ✅ Yes | ❌ No |
| Position on stage? | x, y coordinates | Always fills the background |

**Activity:** Have kids:
1. Add 2 new sprites from the library (an animal and an object)
2. Add a backdrop (try "Blue Sky" or "Beach Malibu")
3. Click the Costumes tab on the cat — see the 2 costumes
4. Click the Backdrops tab on the stage — see the backdrop they added
5. Try renaming a sprite by clicking its name

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
