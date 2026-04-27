# Class 2: Motion & Looks — Teaching Guide (1 Hour)

> **Topic:** Controlling sprite movement and appearance  
> **Duration:** 1 hour  
> **Prerequisites:** Class 1 completed

## Learning Objectives
- Use motion blocks to control sprite position, direction, and movement
- Use looks blocks to change appearance, costumes, and size
- Understand the Scratch coordinate system (x, y)

---

## Session Breakdown

### Review & Warm-Up (5 min)
- Quick recap: "Last time we made the cat move and talk. Who remembers what the green flag does?"
- Challenge: "Can you make the cat move to the right side of the stage in under 10 seconds? Go!"

### Motion Blocks Deep Dive (15 min)

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

### Looks Blocks Deep Dive (15 min)

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

### Guided Project (15 min)

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

### Free Build Time (10 min)

Kids pick one of the sample projects or experiment on their own.
