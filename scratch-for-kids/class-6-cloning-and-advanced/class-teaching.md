# Class 6: Cloning & Advanced Techniques — Teaching Guide (1 Hour)

> **Topic:** Creating clones and combining all concepts  
> **Duration:** 1 hour  
> **Prerequisites:** Classes 1–5 completed

## Learning Objectives
- Understand what cloning is and when to use it
- Create, control, and delete clones
- Use broadcast messages for complex sprite communication
- Combine all previous concepts into more sophisticated projects

---

## Session Breakdown

### Review & Warm-Up (5 min)
- "We've learned motion, looks, events, sounds, loops, conditions, and variables. That's a LOT! Today we learn one more powerful tool — cloning."
- Quick question: "In the apple catching game, what if we wanted 5 apples falling at the same time? Would we need 5 apple sprites?" (Answer: No — we can use clones!)

### Cloning Deep Dive (20 min)

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

### Broadcast Messages for Complex Games (10 min)

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

### Guided Project (15 min)

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

### Wrap-Up (5 min)
- "Clones let us create many copies of a sprite without adding them manually."
- "Combined with everything else we've learned, you can now build real games!"
- Preview: "Next class is YOUR class — you'll design and build your own project from scratch!"
