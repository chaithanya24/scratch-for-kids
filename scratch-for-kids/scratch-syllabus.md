# Scratch Programming for Kids — 7-Class Syllabus (Full Documentation)

> **Age Group:** 7–12 years  
> **Session Length:** 1 hour each  
> **Prerequisites:** None — just a computer with a web browser  
> **Platform:** [Scratch 3.0](https://scratch.mit.edu)

---

## Class 1: Meet Scratch (1 Hour)

### Learning Objectives
- Understand what programming is in simple terms
- Navigate the Scratch interface confidently
- Create and run a simple script using drag-and-drop blocks

### Session Breakdown

#### Introduction (10 min)
- **What is programming?**
  - Analogy: "Imagine you have a robot friend. It only does exactly what you tell it. Programming is writing those instructions."
  - Show a fun example: a finished Scratch game (e.g., a cat chasing a mouse)
- **What is Scratch?**
  - Created by MIT for kids to learn coding
  - Used by millions of kids worldwide
  - No typing needed — just drag and drop

#### Interface Tour (10 min)
Walk kids through each part of the screen:
- **Stage:** The white area on the right where your project plays (480 x 360 pixels)
- **Sprite:** The character on the stage (default is the Scratch Cat)
- **Sprite List:** Below the stage — shows all your sprites
- **Block Palette:** Left side — colored categories of blocks (Motion, Looks, Sound, etc.)
- **Scripts Area:** Middle — where you drag blocks to build your program
- **Green Flag / Stop Sign:** Top of stage — runs and stops your project

**Activity:** Have kids click through each block category and read a few block names out loud.

#### Guided Coding (15 min)
Build this together step by step:

1. Click the **Events** category (yellow) → drag `when green flag clicked` to the scripts area
2. Click **Looks** (purple) → drag `say [Hello!] for [2] seconds` and snap it below
3. Click **Motion** (blue) → drag `move [10] steps` and snap it below
4. Click the **Green Flag** — watch the cat say "Hello!" and move
5. Add `turn [15] degrees` and another `move [10] steps`
6. Click Green Flag again — the cat talks, moves, and turns

**Key Concept:** Blocks run from top to bottom, one after another. This is called **sequence**.

#### Free Exploration (10 min)
Let kids experiment:
- Change the number in `move` to make the cat go farther
- Change the text in `say` to anything they want
- Try adding more blocks from Motion and Looks
- Try clicking the cat sprite on stage and dragging it around

#### Wrap-Up & Discussion (5 min)
- "What did you make the cat do?"
- "What happens if you change the numbers in the blocks?"
- Preview next class: "Next time we'll make our sprites move in cool ways and change how they look!"

---

### Class 1 — Sample Projects & Solutions

#### Project 1: Greeting Cat
**Goal:** Cat walks and greets the user.

```
when green flag clicked
say [Hi! I'm Scratchy!] for (2) seconds
move (100) steps
say [Nice to meet you!] for (2) seconds
```

**What kids learn:** Sequence, say block, move block.

---

#### Project 2: Spinning Star
**Goal:** Add a star sprite that spins in place.

```
when green flag clicked
turn right (45) degrees
turn right (45) degrees
turn right (45) degrees
turn right (45) degrees
```

**Setup:** Delete the cat. Click "Choose a Sprite" → search "Star".

**What kids learn:** Turn block, repetition concept (they'll notice they're repeating the same block — sets up loops for Class 4).

---

#### Project 3: Two Friends Talking
**Goal:** Two sprites have a conversation.

**Sprite 1 (Cat):**
```
when green flag clicked
say [Hey Duck, what's up?] for (2) seconds
wait (2) seconds
say [Me too! Let's play!] for (2) seconds
```

**Sprite 2 (Duck):**
```
when green flag clicked
wait (2) seconds
say [Not much! Just coding!] for (2) seconds
```

**Setup:** Add a second sprite (Duck). Position them on opposite sides of the stage.

**What kids learn:** Multiple sprites can have their own scripts. `wait` block for timing.

---

#### Project 4: Cat's Big Adventure
**Goal:** Cat moves to different spots on the stage.

```
when green flag clicked
go to x: (-200) y: (0)
say [Starting my adventure!] for (2) seconds
glide (1) secs to x: (0) y: (100)
say [I'm on top of the world!] for (2) seconds
glide (1) secs to x: (200) y: (0)
say [What a journey!] for (2) seconds
```

**What kids learn:** `go to` for instant movement, `glide` for smooth movement, x/y coordinates preview.

---

## Class 2: Motion & Looks (1 Hour)

### Learning Objectives
- Use motion blocks to control sprite position, direction, and movement
- Use looks blocks to change appearance, costumes, and size
- Understand the Scratch coordinate system (x, y)

### Session Breakdown

#### Review & Warm-Up (5 min)
- Quick recap: "Last time we made the cat move and talk. Who remembers what the green flag does?"
- Challenge: "Can you make the cat move to the right side of the stage in under 10 seconds? Go!"

#### Motion Blocks Deep Dive (15 min)

**Key Motion Blocks to Teach:**

| Block | What It Does |
|-------|-------------|
| `move (10) steps` | Moves sprite forward in the direction it's facing |
| `turn right (15) degrees` | Rotates sprite clockwise |
| `turn left (15) degrees` | Rotates sprite counter-clockwise |
| `go to x: (0) y: (0)` | Instantly moves sprite to a position |
| `glide (1) secs to x: (0) y: (0)` | Smoothly slides sprite to a position |
| `point in direction (90)` | Sets which way the sprite faces (90 = right, 0 = up, -90 = left, 180 = down) |
| `if on edge, bounce` | Reverses direction when hitting the stage edge |

**Coordinate System Explanation:**
- Draw a simple grid on a whiteboard or show on screen
- Center of stage = x: 0, y: 0
- Right = positive x (up to 240), Left = negative x (down to -240)
- Up = positive y (up to 180), Down = negative y (down to -180)
- **Activity:** Call out positions and have kids guess where on the stage they are: "x: 200, y: 150" → top right corner

#### Looks Blocks Deep Dive (15 min)

**Key Looks Blocks to Teach:**

| Block | What It Does |
|-------|-------------|
| `say [Hello!] for (2) seconds` | Speech bubble that disappears |
| `say [Hello!]` | Speech bubble that stays |
| `think [Hmm...] for (2) seconds` | Thought bubble |
| `switch costume to [costume2]` | Changes the sprite's image |
| `next costume` | Cycles to the next costume |
| `change size by (10)` | Makes sprite bigger (positive) or smaller (negative) |
| `set size to (100) %` | Sets exact size (100% = normal) |
| `show` / `hide` | Makes sprite visible or invisible |
| `change [color] effect by (25)` | Applies visual effects |
| `clear graphic effects` | Removes all effects |

**Costumes Explanation:**
- Click the "Costumes" tab at the top
- Show that the cat has two costumes (legs in different positions)
- Switching between them creates a walking animation
- You can also draw your own costumes or upload images

#### Guided Project (15 min)
Build together: "Dancing Cat"

```
when green flag clicked
go to x: (0) y: (0)
set size to (100) %
forever
  move (10) steps
  next costume
  if on edge, bounce
  change [color] effect by (10)
  wait (0.2) seconds
end
```

Walk through each block and explain what it adds. (Note: `forever` is a preview of loops from Class 4 — just tell kids "this block makes everything inside it repeat over and over.")

#### Free Build Time (10 min)
Kids pick one of the sample projects below or experiment on their own.

---

### Class 2 — Sample Projects & Solutions

#### Project 1: Walking Animation
**Goal:** Make the cat walk back and forth across the stage with a walking animation.

```
when green flag clicked
set rotation style [left-right]
forever
  move (5) steps
  next costume
  if on edge, bounce
  wait (0.1) seconds
end
```

**What kids learn:** `set rotation style` prevents the cat from flipping upside down. Costume switching creates animation.

---

#### Project 2: Growing and Shrinking Sprite
**Goal:** A sprite that grows big, then shrinks back to normal.

```
when green flag clicked
set size to (100) %
repeat (10)
  change size by (10)
  wait (0.1) seconds
end
repeat (10)
  change size by (-10)
  wait (0.1) seconds
end
```

**What kids learn:** `change size by` with positive and negative numbers. `repeat` block preview.

---

#### Project 3: Color Changing Parrot
**Goal:** A parrot that flies across the screen changing colors.

**Setup:** Choose the "Parrot" sprite (it has multiple costumes for wing flapping).

```
when green flag clicked
go to x: (-200) y: (50)
repeat (40)
  move (10) steps
  next costume
  change [color] effect by (5)
  wait (0.05) seconds
end
clear graphic effects
say [I made it!] for (2) seconds
```

**What kids learn:** Graphic effects, combining motion with looks, `clear graphic effects`.

---

#### Project 4: Sprite Parade
**Goal:** Three sprites walk across the stage one after another.

**Setup:** Add 3 sprites (Cat, Dog, Duck). Position them all at x: -200.

**Cat script:**
```
when green flag clicked
go to x: (-200) y: (100)
glide (2) secs to x: (200) y: (100)
say [Cat is here!] for (1) seconds
```

**Dog script:**
```
when green flag clicked
go to x: (-200) y: (0)
wait (1) seconds
glide (2) secs to x: (200) y: (0)
say [Dog is here!] for (1) seconds
```

**Duck script:**
```
when green flag clicked
go to x: (-200) y: (-100)
wait (2) seconds
glide (2) secs to x: (200) y: (-100)
say [Quack!] for (1) seconds
```

**What kids learn:** Multiple sprites, `wait` for staggered timing, `glide` for smooth movement, y-positioning.

---

## Class 3: Events & Sound (1 Hour)

### Learning Objectives
- Understand events as triggers that start scripts
- Use keyboard and mouse events to make interactive projects
- Add and control sounds in Scratch projects
- Use broadcast messages for sprite-to-sprite communication

### Session Breakdown

#### Review & Warm-Up (5 min)
- "Last class we made sprites move and change looks. Today we make them interactive — they'll respond to YOU!"
- Quick challenge: "Make your cat say something when you click the green flag" (review)

#### Events Deep Dive (15 min)

**Key Event Blocks:**

| Block | What It Does |
|-------|-------------|
| `when green flag clicked` | Runs when the green flag is pressed |
| `when [space] key pressed` | Runs when a specific key is pressed |
| `when this sprite clicked` | Runs when you click on the sprite |
| `when backdrop switches to [backdrop1]` | Runs when the background changes |
| `when I receive [message1]` | Runs when a broadcast message is received |
| `broadcast [message1]` | Sends a message to all sprites |
| `broadcast [message1] and wait` | Sends a message and waits for all receivers to finish |

**Teaching Approach:**
- Start with `when green flag clicked` — they already know this one
- Add `when [space] key pressed` — have kids press space and watch something happen
- Add `when this sprite clicked` — click the sprite on stage
- Explain: "Events are like doorbells. When someone presses the doorbell (the event), you go answer the door (the script runs)."

**Activity:** Add 4 different event blocks to the same sprite, each doing something different:
```
when green flag clicked → say [Game starting!]
when [space] key pressed → move (20) steps
when [up arrow] key pressed → change y by (20)
when this sprite clicked → change [color] effect by (25)
```

#### Sound Deep Dive (15 min)

**Key Sound Blocks:**

| Block | What It Does |
|-------|-------------|
| `play sound [Meow] until done` | Plays a sound and waits for it to finish |
| `start sound [Meow]` | Plays a sound without waiting |
| `stop all sounds` | Stops everything playing |
| `change [pitch] effect by (10)` | Changes pitch up or down |
| `set [pitch] effect to (100)` | Sets exact pitch |
| `change volume by (-10)` | Makes quieter or louder |
| `set volume to (100) %` | Sets exact volume |

**Adding Sounds:**
1. Click the "Sounds" tab at the top
2. Click the speaker icon (bottom left) to browse the sound library
3. You can also record your own sound or upload a file
4. Each sprite has its own sounds

**Activity:** Have kids:
1. Go to the Sounds tab
2. Add 3 different sounds from the library
3. Create a script that plays them in sequence

#### Guided Project (15 min)
Build together: "Interactive Pet"

```
when green flag clicked
say [Click me or press keys!] for (3) seconds

when this sprite clicked
start sound [Meow]
change size by (20)
wait (0.3) seconds
change size by (-20)

when [space] key pressed
next costume
start sound [Pop]

when [up arrow] key pressed
change y by (30)
wait (0.3) seconds
change y by (-30)
start sound [Boing]
```

#### Free Build Time (10 min)
Kids pick a sample project or create their own interactive sprite.

---

### Class 3 — Sample Projects & Solutions

#### Project 1: Piano Keyboard
**Goal:** Press different keys to play different musical notes.

**Setup:** Use the Scratch Cat or any sprite.

```
when [1] key pressed
play note (60) for (0.5) beats

when [2] key pressed
play note (62) for (0.5) beats

when [3] key pressed
play note (64) for (0.5) beats

when [4] key pressed
play note (65) for (0.5) beats

when [5] key pressed
play note (67) for (0.5) beats

when [6] key pressed
play note (69) for (0.5) beats

when [7] key pressed
play note (71) for (0.5) beats

when [8] key pressed
play note (72) for (0.5) beats
```

**Note:** You need the "Music" extension. Click "Add Extension" (bottom left) → "Music".

**Note values:** 60 = Middle C, 62 = D, 64 = E, 65 = F, 67 = G, 69 = A, 71 = B, 72 = High C

**What kids learn:** Key events, music extension, note values.

---

#### Project 2: Click the Sprite Game
**Goal:** Sprite appears in random places. Click it before it moves!

```
when green flag clicked
forever
  go to x: (pick random (-200) to (200)) y: (pick random (-150) to (150))
  show
  start sound [Pop]
  wait (1) seconds
  hide
  wait (0.5) seconds
end

when this sprite clicked
say [You got me!] for (0.5) seconds
start sound [Collect]
hide
```

**What kids learn:** `when this sprite clicked`, `pick random`, `show`/`hide`, combining events.

---

#### Project 3: Sound Board
**Goal:** Multiple sprites, each plays a different sound when clicked.

**Setup:** Add 4 sprites (Drum, Guitar, Singer, Bell — or any sprites). Give each a different sound.

**Drum sprite:**
```
when this sprite clicked
start sound [Drum Buzz]
change size by (10)
wait (0.1) seconds
change size by (-10)
```

**Guitar sprite:**
```
when this sprite clicked
start sound [Guitar Strum]
change [color] effect by (25)
wait (0.3) seconds
clear graphic effects
```

**Singer sprite:**
```
when this sprite clicked
start sound [Singer1]
say [La la la!] for (1) seconds
```

**Bell sprite:**
```
when this sprite clicked
start sound [Bell Toll]
turn right (30) degrees
wait (0.2) seconds
turn left (30) degrees
```

**What kids learn:** Each sprite has its own scripts and sounds. Visual feedback on click.

---

#### Project 4: Story with Broadcast Messages
**Goal:** Two characters tell a story using broadcast to coordinate.

**Setup:** Add a "Wizard" and "Dragon" sprite. Add a castle backdrop.

**Wizard script:**
```
when green flag clicked
go to x: (-150) y: (-50)
say [Halt, dragon!] for (2) seconds
broadcast [dragon responds]
wait (3) seconds
say [Then I shall cast a spell!] for (2) seconds
broadcast [spell cast]

when I receive [dragon responds]
think [Hmm, a tough one...] for (2) seconds
```

**Dragon script:**
```
when I receive [dragon responds]
go to x: (150) y: (-50)
say [You cannot stop me!] for (2) seconds

when I receive [spell cast]
repeat (5)
  change [ghost] effect by (20)
  wait (0.3) seconds
end
say [Nooo!] for (1) seconds
hide
```

**What kids learn:** `broadcast` and `when I receive` for coordinating between sprites. Ghost effect for disappearing.

---

## Class 4: Loops & Conditions (1 Hour)

### Learning Objectives
- Understand and use `forever`, `repeat`, and `repeat until` loops
- Understand and use `if` and `if-else` conditional blocks
- Combine loops and conditions to create game logic
- Use sensing blocks to detect collisions and input

### Session Breakdown

#### Review & Warm-Up (5 min)
- "Remember how we kept copying the same block over and over? Today we learn the shortcut — loops!"
- Show the spinning star from Class 1 (4 turn blocks) and ask: "What if we wanted it to spin 100 times?"

#### Loops Deep Dive (15 min)

**Key Loop Blocks:**

| Block | What It Does |
|-------|-------------|
| `forever` | Repeats everything inside it non-stop until you press the stop sign |
| `repeat (10)` | Repeats everything inside it a specific number of times |
| `repeat until <condition>` | Repeats until something becomes true |

**Teaching Approach:**

1. **Repeat block** — Refactor the spinning star:
```
-- Before (Class 1 way):
turn right (45) degrees
turn right (45) degrees
turn right (45) degrees
turn right (45) degrees

-- After (with loop):
repeat (4)
  turn right (45) degrees
end
```
"Same result, way less work. What if we change 4 to 100?"

2. **Forever block** — Make the cat walk forever:
```
forever
  move (5) steps
  if on edge, bounce
end
```
"This never stops until you hit the red stop sign."

3. **Repeat until** — Walk until touching something:
```
repeat until <touching [edge]?>
  move (5) steps
end
say [I reached the edge!] for (2) seconds
```

**Real-life analogy:**
- `repeat 10` = "Brush your teeth 10 times"
- `forever` = "Keep breathing"
- `repeat until` = "Keep walking until you reach the door"

#### Conditions Deep Dive (15 min)

**Key Condition Blocks:**

| Block | What It Does |
|-------|-------------|
| `if <> then` | Runs the code inside only if the condition is true |
| `if <> then / else` | Runs one set of code if true, another if false |

**Key Sensing Blocks (used as conditions):**

| Block | What It Does |
|-------|-------------|
| `<touching [mouse-pointer]?>` | True if sprite touches the mouse |
| `<touching [Sprite2]?>` | True if sprite touches another sprite |
| `<touching color [#ff0000]?>` | True if sprite touches a specific color |
| `<key [space] pressed?>` | True if a key is currently held down |
| `<mouse down?>` | True if mouse button is held |

**Teaching Approach:**

1. **Simple if:**
```
forever
  if <key [right arrow] pressed?> then
    move (5) steps
  end
end
```
"The cat only moves when you hold the right arrow."

2. **If-else:**
```
forever
  if <touching [edge]?> then
    say [I hit the wall!] for (1) seconds
  else
    move (3) steps
  end
end
```

3. **Combining conditions in a loop:**
```
forever
  if <key [right arrow] pressed?> then
    change x by (5)
  end
  if <key [left arrow] pressed?> then
    change x by (-5)
  end
  if <key [up arrow] pressed?> then
    change y by (5)
  end
  if <key [down arrow] pressed?> then
    change y by (-5)
  end
end
```
"Now you can move in all 4 directions!"

#### Guided Project (15 min)
Build together: "Simple Maze"

**Setup:**
- Use the paint editor to draw a simple maze as the backdrop (thick black walls, green start area, red end area)
- Use a small sprite (shrink the cat or use the "Ball" sprite)

**Ball/Cat script:**
```
when green flag clicked
go to x: (-200) y: (150)
set size to (30) %
forever
  if <key [right arrow] pressed?> then
    change x by (3)
  end
  if <key [left arrow] pressed?> then
    change x by (-3)
  end
  if <key [up arrow] pressed?> then
    change y by (3)
  end
  if <key [down arrow] pressed?> then
    change y by (-3)
  end
  if <touching color [#000000]?> then
    go to x: (-200) y: (150)
    say [Oops! Back to start!] for (1) seconds
  end
  if <touching color [#ff0000]?> then
    say [You win!] for (2) seconds
    stop [all]
  end
end
```

#### Wrap-Up (5 min)
- "Loops save us from repeating blocks. Conditions let our program make decisions."
- Preview: "Next class we add scores and lives using variables!"

---

### Class 4 — Sample Projects & Solutions

#### Project 1: Dodge the Obstacles
**Goal:** A sprite moves left/right to dodge falling objects.

**Setup:** Player sprite (Cat) at bottom. Add a "Ball" sprite.

**Cat script:**
```
when green flag clicked
go to x: (0) y: (-150)
forever
  if <key [left arrow] pressed?> then
    change x by (-7)
  end
  if <key [right arrow] pressed?> then
    change x by (7)
  end
end
```

**Ball script:**
```
when green flag clicked
forever
  go to x: (pick random (-200) to (200)) y: (180)
  repeat until <(y position) < (-170)>
    change y by (-5)
  end
end
```

**What kids learn:** `repeat until` with a condition, combining loops with key controls.

---

#### Project 2: Color Touch Game
**Goal:** Sprite changes color when touching different colored areas on the backdrop.

**Setup:** Paint a backdrop with 4 colored quadrants (red, blue, green, yellow).

```
when green flag clicked
forever
  if <key [right arrow] pressed?> then
    change x by (5)
  end
  if <key [left arrow] pressed?> then
    change x by (-5)
  end
  if <key [up arrow] pressed?> then
    change y by (5)
  end
  if <key [down arrow] pressed?> then
    change y by (-5)
  end
  if <touching color [#ff0000]?> then
    say [Red zone!] for (0.5) seconds
    set [color] effect to (0)
  end
  if <touching color [#0000ff]?> then
    say [Blue zone!] for (0.5) seconds
    set [color] effect to (100)
  end
  if <touching color [#00ff00]?> then
    say [Green zone!] for (0.5) seconds
    set [color] effect to (50)
  end
  if <touching color [#ffff00]?> then
    say [Yellow zone!] for (0.5) seconds
    set [color] effect to (150)
  end
end
```

**What kids learn:** Color sensing, multiple if blocks, color effects.

---

#### Project 3: Chase Game
**Goal:** A cat chases the mouse pointer. If it catches it, it says "Got you!"

```
when green flag clicked
forever
  point towards [mouse-pointer]
  move (3) steps
  if <touching [mouse-pointer]?> then
    say [Got you!] for (1) seconds
    go to x: (0) y: (0)
    wait (1) seconds
  end
end
```

**Extension:** Add a second sprite that runs away from the cat:
```
when green flag clicked
forever
  point towards [Cat]
  turn right (180) degrees
  move (2) steps
  if on edge, bounce
end
```

**What kids learn:** `point towards`, combining motion with conditions, simple AI behavior.

---

#### Project 4: Traffic Light Simulator
**Goal:** A traffic light that cycles through red, yellow, green with a walking character that responds.

**Setup:** Create a sprite with 3 costumes (red light, yellow light, green light). Add a person sprite.

**Traffic Light script:**
```
when green flag clicked
forever
  switch costume to [red]
  broadcast [red light]
  wait (3) seconds
  switch costume to [green]
  broadcast [green light]
  wait (3) seconds
  switch costume to [yellow]
  broadcast [yellow light]
  wait (1) seconds
end
```

**Person script:**
```
when green flag clicked
go to x: (-200) y: (-100)

when I receive [green light]
repeat until <(x position) > (200)>
  move (3) steps
  next costume
  wait (0.1) seconds
end
go to x: (-200) y: (-100)

when I receive [red light]
stop [other scripts in sprite]

when I receive [yellow light]
stop [other scripts in sprite]
```

**What kids learn:** Broadcast + conditions, costume switching for state, `stop [other scripts in sprite]`.

---

## Class 5: Variables & Score (1 Hour)

### Learning Objectives
- Understand what variables are and why they're useful
- Create, set, and change variables in Scratch
- Use variables to track score, lives, and timers
- Display variables on the stage

### Session Breakdown

#### Review & Warm-Up (5 min)
- Quick recap of loops and conditions
- "Today we're going to add something that makes games feel like real games — scores, lives, and timers!"

#### What is a Variable? (10 min)

**Simple Explanation:**
- "A variable is like a labeled box. You can put a number or word inside it, look at what's inside, and change what's inside."
- Draw on whiteboard: a box labeled "Score" with the number 0 inside
- "When you catch a fruit, we open the box, take out 0, put in 1. Catch another fruit, take out 1, put in 2."

**Real-life examples:**
- Your age is a variable — it changes every year
- The temperature outside is a variable — it changes every hour
- Your score in a game is a variable — it changes when you earn points

#### Creating & Using Variables (15 min)

**How to create a variable:**
1. Click the "Variables" category (orange)
2. Click "Make a Variable"
3. Name it (e.g., "Score")
4. Choose "For all sprites" (shared) or "For this sprite only" (private)
5. Click OK — new blocks appear!

**Key Variable Blocks:**

| Block | What It Does |
|-------|-------------|
| `set [Score] to (0)` | Puts a specific value in the variable |
| `change [Score] by (1)` | Adds to the current value (use negative to subtract) |
| `(Score)` | The round block — use this to read the variable's value |
| `show variable [Score]` | Shows the variable display on stage |
| `hide variable [Score]` | Hides the variable display |

**Guided Activity — Build a click counter:**
```
when green flag clicked
set [Score] to (0)

when this sprite clicked
change [Score] by (1)
say (join [Score: ] (Score)) for (0.5) seconds
```

**Using variables in conditions:**
```
when green flag clicked
set [Score] to (0)
forever
  if <(Score) > (10)> then
    say [You win! Score over 10!] for (2) seconds
    stop [all]
  end
end
```

**Multiple variables:**
- Create "Score", "Lives", and "Timer"
- Show how each can be displayed on stage independently

#### Guided Project (20 min)
Build together: "Catch the Apple"

**Setup:**
- Keep the Cat sprite at the bottom
- Add an Apple sprite
- Create variables: "Score" and "Lives"

**Cat script:**
```
when green flag clicked
go to x: (0) y: (-150)
forever
  if <key [left arrow] pressed?> then
    change x by (-7)
  end
  if <key [right arrow] pressed?> then
    change x by (7)
  end
end
```

**Apple script:**
```
when green flag clicked
set [Score] to (0)
set [Lives] to (3)
forever
  go to x: (pick random (-200) to (200)) y: (180)
  show
  repeat until <(y position) < (-170)>
    change y by (-4)
    if <touching [Cat]?> then
      change [Score] by (1)
      start sound [Collect]
      hide
    end
  end
  if <(y position) < (-170)> then
    change [Lives] by (-1)
    start sound [Oops]
  end
  if <(Lives) < (1)> then
    say (join [Game Over! Score: ] (Score)) for (3) seconds
    stop [all]
  end
end
```

Walk through each section:
1. Initialize variables at the start
2. Apple falls from random x position
3. If cat catches it → score goes up, apple hides
4. If apple reaches the bottom → lose a life
5. If lives reach 0 → game over

#### Wrap-Up (5 min)
- "Variables let us remember things — scores, lives, anything we need to track."
- Preview: "Next class we learn cloning — making copies of sprites while the game is running!"

---

### Class 5 — Sample Projects & Solutions

#### Project 1: Click Counter Challenge
**Goal:** Click the sprite as many times as you can in 10 seconds.

**Setup:** Create variables "Score" and "Time".

```
when green flag clicked
set [Score] to (0)
set [Time] to (10)
repeat until <(Time) < (1)>
  wait (1) seconds
  change [Time] by (-1)
end
say (join [Final Score: ] (Score)) for (3) seconds
stop [all]

when this sprite clicked
change [Score] by (1)
start sound [Pop]
go to x: (pick random (-200) to (200)) y: (pick random (-150) to (150))
```

**What kids learn:** Timer using a variable, combining click events with variables.

---

#### Project 2: Math Quiz
**Goal:** The sprite asks math questions. Score goes up for correct answers.

**Setup:** Create variables "Score", "Number1", "Number2", "Answer".

```
when green flag clicked
set [Score] to (0)
repeat (5)
  set [Number1] to (pick random (1) to (10))
  set [Number2] to (pick random (1) to (10))
  ask (join (join (Number1) [ + ]) (Number2)) and wait
  if <(answer) = ((Number1) + (Number2))> then
    say [Correct!] for (1) seconds
    change [Score] by (1)
    start sound [Collect]
  else
    say (join [Wrong! The answer was ] ((Number1) + (Number2))) for (2) seconds
    start sound [Oops]
  end
end
say (join [You got ] (join (Score) [ out of 5!])) for (3) seconds
```

**What kids learn:** `ask` and `answer` blocks, operators (addition), variables for dynamic content.

---

#### Project 3: Virtual Pet
**Goal:** A pet with hunger and happiness meters. Feed it and play with it to keep the meters up.

**Setup:** Create variables "Hunger" (starts at 100) and "Happiness" (starts at 100). Add a Cat sprite.

```
when green flag clicked
set [Hunger] to (100)
set [Happiness] to (100)
forever
  change [Hunger] by (-1)
  change [Happiness] by (-0.5)
  wait (1) seconds
  if <(Hunger) < (1)> then
    say [I'm starving! Game over!] for (3) seconds
    stop [all]
  end
  if <(Happiness) < (1)> then
    say [I'm so sad! Game over!] for (3) seconds
    stop [all]
  end
  if <(Hunger) < (30)> then
    say [I'm hungry...] for (1) seconds
  end
  if <(Happiness) < (30)> then
    think [I'm bored...] for (1) seconds
  end
end

when [f] key pressed
change [Hunger] by (20)
say [Yum!] for (1) seconds
start sound [Chomp]

when [p] key pressed
change [Happiness] by (20)
say [Wheee!] for (1) seconds
next costume
start sound [Pop]
```

**What kids learn:** Multiple variables interacting, gradual decrease, key events to modify variables.

---

#### Project 4: Coin Collector with Levels
**Goal:** Collect coins to score points. After 5 coins, speed increases (level up).

**Setup:** Cat sprite + Coin sprite (use "Button2" or draw a circle). Variables: "Score", "Level", "Speed".

**Cat script:**
```
when green flag clicked
go to x: (0) y: (-150)
forever
  if <key [left arrow] pressed?> then
    change x by (-7)
  end
  if <key [right arrow] pressed?> then
    change x by (7)
  end
end
```

**Coin script:**
```
when green flag clicked
set [Score] to (0)
set [Level] to (1)
set [Speed] to (3)
forever
  go to x: (pick random (-200) to (200)) y: (180)
  show
  repeat until <(y position) < (-170)>
    change y by ((0) - (Speed))
    if <touching [Cat]?> then
      change [Score] by (1)
      start sound [Collect]
      hide
      if <((Score) mod (5)) = (0)> then
        change [Level] by (1)
        change [Speed] by (1)
        say (join [Level ] (Level)) for (1) seconds
      end
    end
  end
end
```

**What kids learn:** `mod` operator for level thresholds, variable-driven difficulty, multiple variables working together.

---

## Class 6: Cloning & Advanced Techniques (1 Hour)

### Learning Objectives
- Understand what cloning is and when to use it
- Create, control, and delete clones
- Use broadcast messages for complex sprite communication
- Combine all previous concepts into more sophisticated projects

### Session Breakdown

#### Review & Warm-Up (5 min)
- "We've learned motion, looks, events, sounds, loops, conditions, and variables. That's a LOT! Today we learn one more powerful tool — cloning."
- Quick question: "In the apple catching game, what if we wanted 5 apples falling at the same time? Would we need 5 apple sprites?" (Answer: No — we can use clones!)

#### Cloning Deep Dive (20 min)

**What is a Clone?**
- "A clone is a copy of a sprite that's created while the program is running."
- "It looks the same, acts the same, but it's a separate copy."
- "Think of it like a copy machine — you put in one sprite, and it makes as many copies as you need."

**Key Clone Blocks:**

| Block | What It Does |
|-------|-------------|
| `create clone of [myself]` | Makes a copy of this sprite |
| `create clone of [Sprite2]` | Makes a copy of another sprite |
| `when I start as a clone` | Runs when a new clone is created (like green flag but for clones) |
| `delete this clone` | Removes this clone from the stage |

**Important Rules:**
- Scratch allows a maximum of 300 clones at once
- Clones disappear when you press the stop sign
- Each clone can have its own position, direction, size, and effects
- The original sprite is like the "template" — clones copy from it

**Step-by-step Teaching:**

1. **Basic clone creation:**
```
when green flag clicked
forever
  create clone of [myself]
  wait (1) seconds
end

when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
show
repeat (36)
  change y by (-10)
end
delete this clone
```
"Every second, a new clone appears at the top and falls down."

2. **Clone with behavior:**
```
when I start as a clone
set size to (pick random (50) to (150)) %
set [color] effect to (pick random (0) to (200))
show
repeat until <(y position) < (-170)>
  change y by (-5)
  turn right (5) degrees
end
delete this clone
```
"Each clone is a different size and color!"

3. **Why delete clones?**
- "If you don't delete clones, they pile up and slow down your project."
- "Always delete clones when they're done (off screen, caught by player, etc.)"

#### Broadcast Messages for Complex Games (10 min)

**When to use broadcasts:**
- When one sprite needs to tell other sprites something happened
- When you need to coordinate timing between sprites
- When a game state changes (game over, level up, etc.)

**Pattern: Game State Management**
```
-- In the main game sprite:
when green flag clicked
broadcast [start game]

-- When player loses:
broadcast [game over]

-- In each sprite:
when I receive [start game]
  ... start doing things ...

when I receive [game over]
  stop [other scripts in sprite]
  hide
```

**Activity:** Add broadcasts to the apple game from last class:
- `broadcast [game over]` when lives = 0
- All sprites listen for `[game over]` and stop

#### Guided Project (15 min)
Build together: "Space Shooter"

**Setup:**
- Spaceship sprite at the bottom (use "Rocketship" or draw one)
- Enemy sprite (use "Bug" or "Crab")
- Create variables: "Score"

**Spaceship script:**
```
when green flag clicked
go to x: (0) y: (-150)
set [Score] to (0)
forever
  if <key [left arrow] pressed?> then
    change x by (-7)
  end
  if <key [right arrow] pressed?> then
    change x by (7)
  end
end

when [space] key pressed
create clone of [Bullet]
```

**Bullet sprite (draw a small yellow rectangle):**
```
when green flag clicked
hide

when I start as a clone
go to [Rocketship]
show
repeat until <(y position) > (170)>
  change y by (10)
  if <touching [Enemy]?> then
    change [Score] by (1)
    start sound [Collect]
    delete this clone
  end
end
delete this clone
```

**Enemy sprite:**
```
when green flag clicked
hide
forever
  create clone of [myself]
  wait (pick random (1) to (3))
end

when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
show
repeat until <(y position) < (-170)>
  change y by (-3)
  if <touching [Rocketship]?> then
    broadcast [game over]
    say [Hit!] for (1) seconds
    delete this clone
  end
end
delete this clone
```

**Game Over handler (add to Spaceship):**
```
when I receive [game over]
say (join [Game Over! Score: ] (Score)) for (3) seconds
stop [all]
```

#### Wrap-Up (5 min)
- "Clones let us create many copies of a sprite without adding them manually."
- "Combined with everything else we've learned, you can now build real games!"
- Preview: "Next class is YOUR class — you'll design and build your own project from scratch!"

---

### Class 6 — Sample Projects & Solutions

#### Project 1: Snowfall Animation
**Goal:** Snowflakes fall from the sky in random positions and sizes.

**Setup:** Draw a small white circle sprite (snowflake). Add a winter backdrop.

```
when green flag clicked
hide
forever
  create clone of [myself]
  wait (0.2) seconds
end

when I start as a clone
go to x: (pick random (-240) to (240)) y: (180)
set size to (pick random (20) to (80)) %
show
repeat until <(y position) < (-175)>
  change y by (pick random (-3) to (-1))
  change x by (pick random (-2) to (2))
  turn right (pick random (-5) to (5)) degrees
end
delete this clone
```

**What kids learn:** Clones with randomized properties, natural-looking animation.

---

#### Project 2: Balloon Pop Game
**Goal:** Balloons float up from the bottom. Click them to pop them and score points.

**Setup:** Use the "Balloon1" sprite. Create variable "Score".

```
when green flag clicked
hide
set [Score] to (0)
forever
  create clone of [myself]
  wait (pick random (0.5) to (2))
end

when I start as a clone
go to x: (pick random (-200) to (200)) y: (-180)
set size to (pick random (50) to (100)) %
set [color] effect to (pick random (0) to (200))
show
repeat until <(y position) > (180)>
  change y by (pick random (1) to (4))
  change x by (pick random (-1) to (1))
end
delete this clone

when I start as a clone
wait until <mouse down? and touching [mouse-pointer]?>
change [Score] by (1)
start sound [Pop]
repeat (5)
  change size by (10)
  change [ghost] effect by (20)
end
delete this clone
```

**Note:** The two `when I start as a clone` scripts both run on each clone simultaneously.

**What kids learn:** Click detection on clones, ghost effect for pop animation, parallel scripts on clones.

---

#### Project 3: Rain of Emojis
**Goal:** Different emoji sprites fall from the sky. Catch the happy faces (score +1), avoid the sad faces (score -1).

**Setup:** Create a sprite with 2 costumes: happy face and sad face. Player sprite at bottom. Variable: "Score".

**Emoji sprite:**
```
when green flag clicked
hide
forever
  create clone of [myself]
  wait (0.8) seconds
end

when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
switch costume to (pick random (1) to (2))
show
repeat until <(y position) < (-170)>
  change y by (-4)
  if <touching [Player]?> then
    if <(costume [name]) = [happy]> then
      change [Score] by (1)
      start sound [Collect]
    else
      change [Score] by (-1)
      start sound [Oops]
    end
    delete this clone
  end
end
delete this clone
```

**Player script:**
```
when green flag clicked
set [Score] to (0)
go to x: (0) y: (-150)
forever
  go to x: (mouse x) y: (-150)
end
```

**What kids learn:** Costume-based logic, mouse following, positive and negative scoring.

---

#### Project 4: Fireworks Display
**Goal:** Click anywhere on the stage to launch a firework that explodes into particles.

**Setup:** Draw a small colored dot sprite. Create a "Launcher" sprite (small arrow or rocket).

**Launcher script:**
```
when green flag clicked
hide
forever
  if <mouse down?> then
    go to x: (mouse x) y: (-180)
    show
    glide (0.5) secs to x: (mouse x) y: (mouse y)
    broadcast [explode]
    hide
    wait (0.5) seconds
  end
end
```

**Particle sprite (small colored circle):**
```
when green flag clicked
hide

when I receive [explode]
repeat (20)
  create clone of [myself]
end

when I start as a clone
go to [Launcher]
set [color] effect to (pick random (0) to (200))
set size to (pick random (30) to (80)) %
show
point in direction (pick random (-180) to (180))
repeat (20)
  move (pick random (3) to (8)) steps
  change [ghost] effect by (5)
  change size by (-2)
end
delete this clone
```

**What kids learn:** Broadcast triggering clones, particle effects, combining multiple techniques.

---

## Class 7: Final Project & Show and Tell (1 Hour)

### Learning Objectives
- Plan a project before building it
- Apply all learned concepts independently
- Practice presenting and explaining their work
- Celebrate their achievements and inspire each other

### Session Breakdown

#### Concept Review Game (10 min)

Play a quick review game. The instructor says a concept, kids raise their hand and explain it:

| Concept | Expected Answer |
|---------|----------------|
| Sequence | Blocks run from top to bottom, one after another |
| Loop | Makes blocks repeat (forever, repeat 10, repeat until) |
| Condition | Makes the program decide — if something is true, do this |
| Variable | A named box that stores a number or word |
| Event | Something that triggers a script (green flag, key press, click) |
| Clone | A copy of a sprite made while the program runs |
| Broadcast | A message sent from one sprite to all other sprites |

**Bonus round:** Show a short script on screen and ask "What does this do?"

#### Project Planning (10 min)

**Give kids a planning sheet (on paper or screen):**

```
MY SCRATCH PROJECT PLAN
=======================
Project Name: _______________
Type: [ ] Game  [ ] Animation  [ ] Story  [ ] Other: _____

What does it do? (1-2 sentences):
_________________________________
_________________________________

Sprites I need:
1. _______________
2. _______________
3. _______________

Variables I need:
1. _______________
2. _______________

Controls:
- Arrow keys for: _______________
- Space bar for: _______________
- Mouse for: _______________

Concepts I'll use:
[ ] Loops  [ ] Conditions  [ ] Variables  [ ] Clones  [ ] Broadcasts  [ ] Sounds
```

**Instructor tip:** Walk around and help kids scope their projects. Common mistake: planning something too ambitious. Guide them toward something achievable in 25 minutes.

**Project idea suggestions for kids who are stuck:**

| Project Idea | Difficulty | Key Concepts |
|-------------|-----------|--------------|
| Pong (ball bounces, paddle moves) | Medium | Loops, conditions, variables |
| Animated greeting card | Easy | Looks, sound, events |
| Quiz show (ask questions, track score) | Medium | Variables, conditions, ask/answer |
| Flappy bird style game | Hard | Clones, variables, conditions |
| Dance party (multiple sprites dancing) | Easy | Loops, costumes, sound |
| Whack-a-mole | Medium | Clones, variables, click events |

#### Build Time (25 min)

**Instructor role during build time:**
- Walk around the room
- Help kids who are stuck (guide, don't build for them)
- Encourage kids to help each other
- Remind kids to save their work frequently (File → Save now, or it auto-saves if logged in)

**Common issues and quick fixes:**

| Problem | Solution |
|---------|----------|
| "My sprite won't move" | Check if the script is attached to the right sprite. Check if there's a `forever` loop. |
| "My clone won't appear" | Make sure the original sprite is `hide`-ing and the clone has `show` in `when I start as a clone`. |
| "My variable isn't changing" | Check if you're using `change by` vs `set to`. Make sure the condition that triggers the change is actually being met. |
| "My game is too fast/slow" | Add or adjust `wait` blocks. Change the step size in `move` or `change y by`. |
| "Sprites are overlapping" | Use `go to front layer` or `go back (1) layers` to control which sprite appears on top. |

**5-minute warning:** "Start wrapping up! Make sure your project works when you click the green flag."

#### Show and Tell (15 min)

**Format:**
- Each kid gets 1-2 minutes (adjust based on class size)
- They come to the front (or share screen if virtual)
- Click the green flag and demo their project
- Answer 1-2 questions from classmates

**Presentation template (keep it simple for kids):**
1. "My project is called ___"
2. "It's a ___ (game/animation/story)"
3. "Here's how it works..." (demo)
4. "The hardest part was ___"
5. "I used ___ (concepts) to build it"

**Instructor tips for show and tell:**
- Celebrate every project, no matter how simple
- Point out something specific and positive about each one: "I love how you used clones for the rain effect!"
- Encourage applause after each presentation
- If a project has a bug during the demo, normalize it: "Even professional programmers have bugs! That's totally normal."

---

### Class 7 — Sample Projects & Solutions

These are complete example projects that the instructor can share as inspiration, or that advanced kids can reference during build time.

#### Project 1: Pong Game
**Goal:** Classic Pong — ball bounces around, player controls a paddle, score goes up on each hit.

**Setup:** Draw a "Paddle" sprite (flat rectangle), a "Ball" sprite (small circle). Variable: "Score".

**Paddle script:**
```
when green flag clicked
go to x: (0) y: (-160)
set size to (100) %
forever
  if <key [left arrow] pressed?> then
    change x by (-10)
  end
  if <key [right arrow] pressed?> then
    change x by (10)
  end
end
```

**Ball script:**
```
when green flag clicked
set [Score] to (0)
go to x: (0) y: (0)
point in direction (pick random (30) to (60))
forever
  move (6) steps
  if on edge, bounce
  if <touching [Paddle]?> then
    change [Score] by (1)
    start sound [Pop]
    point in direction ((0) - (direction))
    change y by (10)
  end
  if <(y position) < (-175)> then
    say (join [Game Over! Score: ] (Score)) for (3) seconds
    stop [all]
  end
end
```

**What kids learn:** Bouncing physics, paddle control, game over condition.

---

#### Project 2: Animated Story
**Goal:** A short animated story with scene changes, dialogue, and sound effects.

**Setup:** 3 backdrops (forest, castle, sky). Sprites: Knight, Dragon, Princess.

**Knight script:**
```
when green flag clicked
switch backdrop to [forest]
go to x: (-150) y: (-50)
show
say [I must save the princess!] for (2) seconds
glide (2) secs to x: (150) y: (-50)
say [There's the castle!] for (2) seconds
broadcast [scene 2]

when I receive [scene 2]
switch backdrop to [castle]
go to x: (-150) y: (-50)
say [Dragon! Release the princess!] for (2) seconds
broadcast [dragon appears]
wait (4) seconds
say [Take that!] for (1) seconds
broadcast [dragon defeated]

when I receive [dragon defeated]
wait (2) seconds
broadcast [scene 3]

when I receive [scene 3]
switch backdrop to [sky]
go to x: (-50) y: (-50)
say [You're free, princess!] for (2) seconds
```

**Dragon script:**
```
when green flag clicked
hide

when I receive [dragon appears]
go to x: (150) y: (0)
set size to (150) %
show
say [Never!] for (2) seconds

when I receive [dragon defeated]
start sound [Oops]
repeat (10)
  change [ghost] effect by (10)
  change size by (-5)
end
hide
```

**Princess script:**
```
when green flag clicked
hide

when I receive [scene 3]
go to x: (50) y: (-50)
show
say [Thank you, brave knight!] for (2) seconds
start sound [Collect]
```

**What kids learn:** Scene management with backdrops, broadcast for story sequencing, show/hide for character entrances.

---

#### Project 3: Whack-a-Mole
**Goal:** Moles pop up from holes. Click them to score. They get faster over time.

**Setup:** Draw a backdrop with 6 "holes" (brown ovals). One mole sprite. Variables: "Score", "Speed", "Time".

```
when green flag clicked
hide
set [Score] to (0)
set [Speed] to (1)
set [Time] to (30)
broadcast [start timer]
forever
  create clone of [myself]
  wait ((1.5) - ((Speed) * (0.1)))
  if <(Speed) < (12)> then
    change [Speed] by (0.5)
  end
end

when I receive [start timer]
repeat (30)
  wait (1) seconds
  change [Time] by (-1)
end
broadcast [times up]

when I receive [times up]
say (join [Time's up! Score: ] (Score)) for (3) seconds
stop [all]

when I start as a clone
go to x: (pick random (-150) to (150)) y: (pick random (-100) to (50))
show
set size to (80) %
wait (pick random (0.5) to (1.5))
delete this clone

when I start as a clone
wait until <mouse down? and touching [mouse-pointer]?>
change [Score] by (1)
start sound [Pop]
say [Ouch!] for (0.3) seconds
delete this clone
```

**What kids learn:** Clone-based gameplay, difficulty scaling with variables, timer implementation.

---

#### Project 4: Dance Party
**Goal:** Multiple characters dance to music with synchronized moves.

**Setup:** Add 3-4 dancer sprites (use Scratch's built-in dancer sprites — they have dance costumes). Add a music loop.

**Dancer 1 script:**
```
when green flag clicked
go to x: (-120) y: (-50)
start sound [Dance Celebrate] until done

when green flag clicked
forever
  next costume
  wait (0.3) seconds
end

when green flag clicked
forever
  change [color] effect by (5)
  change size by (3)
  wait (0.3) seconds
  change size by (-3)
  wait (0.3) seconds
end
```

**Dancer 2 script:**
```
when green flag clicked
go to x: (0) y: (-50)
forever
  next costume
  wait (0.3) seconds
end

when green flag clicked
forever
  turn right (10) degrees
  wait (0.1) seconds
end
```

**Dancer 3 script:**
```
when green flag clicked
go to x: (120) y: (-50)
forever
  next costume
  wait (0.3) seconds
end

when green flag clicked
forever
  glide (0.5) secs to x: (120) y: (0)
  glide (0.5) secs to x: (120) y: (-50)
end
```

**Disco Ball sprite (optional):**
```
when green flag clicked
go to x: (0) y: (130)
forever
  turn right (3) degrees
  change [color] effect by (2)
end
```

**What kids learn:** Parallel scripts, music, combining motion and looks for choreography.

---

## Appendix: Tips for Instructors

### General Teaching Tips
- **Show, don't just tell.** Always demo on screen before asking kids to try.
- **Encourage experimentation.** "What happens if you change that number?" is the best question.
- **Normalize bugs.** "Bugs are just puzzles to solve. Even experts have them."
- **Pair struggling kids with confident ones.** Peer teaching reinforces learning for both.
- **Save frequently.** Remind kids to save, or ensure they're logged into Scratch accounts (auto-save).

### Common Kid Questions & Answers
| Question | Answer |
|----------|--------|
| "How do I undo?" | Edit → Undo, or Ctrl+Z (Cmd+Z on Mac) |
| "My sprite disappeared!" | Check if it's hidden (use `show` block). Check if it went off-stage (use `go to x:0 y:0`). |
| "Can I use my own pictures?" | Yes! In the Costumes tab, click the upload icon to add your own images. |
| "Can I share my project?" | Yes! Click "Share" at the top (requires a Scratch account). |
| "How do I add a background?" | Click the backdrop icon (bottom right, next to the sprite chooser). |

### Scratch Account Setup
- Go to [scratch.mit.edu](https://scratch.mit.edu)
- Click "Join Scratch"
- Kids under 13 need a parent email for verification
- Accounts allow saving, sharing, and remixing projects
- If accounts aren't possible, projects can be saved to the computer via File → Save to your computer

### Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| Ctrl/Cmd + Z | Undo |
| Ctrl/Cmd + Shift + Z | Redo |
| Ctrl/Cmd + S | Save |
| Right-click a block | Duplicate, Delete, or Add Comment |
| Hold Shift + Click Green Flag | Turbo Mode (runs faster) |

---

*End of Syllabus*
