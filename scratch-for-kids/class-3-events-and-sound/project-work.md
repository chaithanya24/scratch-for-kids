# Class 3: Events & Sound — Project Work

> These are the 4 projects for Class 3. Each focuses on events and sound.

---

## Project 1: Piano Keyboard
**Goal:** Press different keys to play different musical notes.

**Instructions:**
1. You need the "Music" extension — click "Add Extension" (bottom left) → "Music"
2. Add a `when [1] key pressed` event block for each key (1 through 8)
3. Under each, add `play note (X) for (0.5) beats` with different note values
4. Note values: 60 = Middle C, 62 = D, 64 = E, 65 = F, 67 = G, 69 = A, 71 = B, 72 = High C

**Concepts practiced:** Key events, music extension, note values.

---

## Project 2: Click the Sprite Game
**Goal:** Sprite appears in random places. Click it before it moves!

**Instructions:**
1. Use a `forever` loop to keep the sprite moving
2. Inside the loop: `go to` a random position, `show`, `wait`, then `hide`
3. Add a separate `when this sprite clicked` script that says something and plays a sound
4. Use `pick random` for x (-200 to 200) and y (-150 to 150)

**Concepts practiced:** `when this sprite clicked`, `pick random`, `show`/`hide`, combining events.

---

## Project 3: Sound Board
**Goal:** Multiple sprites, each plays a different sound when clicked.

**Instructions:**
1. Add 4 sprites (Drum, Guitar, Singer, Bell — or any you like)
2. Give each sprite a different sound from the sound library
3. Add a `when this sprite clicked` script to each
4. Add visual feedback (size change, color change, or rotation) when clicked

**Concepts practiced:** Each sprite has its own scripts and sounds, visual feedback on click.

---

## Project 4: Story with Broadcast Messages
**Goal:** Two characters tell a story using broadcast to coordinate.

**Instructions:**
1. Add a "Wizard" and "Dragon" sprite, plus a castle backdrop
2. Wizard speaks first, then uses `broadcast [dragon responds]`
3. Dragon has a `when I receive [dragon responds]` script to reply
4. Wizard broadcasts `[spell cast]` and Dragon fades away using the ghost effect
5. Use `wait` blocks to time the dialogue

**Concepts practiced:** `broadcast` and `when I receive` for coordinating between sprites, ghost effect.
