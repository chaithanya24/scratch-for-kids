# Class 4: Loops & Conditions — Teaching Guide (1 Hour)

> **Topic:** Repeating actions and making decisions  
> **Duration:** 1 hour  
> **Prerequisites:** Classes 1–3 completed

## Learning Objectives
- Understand and use `forever`, `repeat`, and `repeat until` loops
- Understand and use `if` and `if-else` conditional blocks
- Combine loops and conditions to create game logic
- Use sensing blocks to detect collisions and input

---

## Session Breakdown

### Review & Warm-Up (5 min)
- "Remember how we kept copying the same block over and over? Today we learn the shortcut — loops!"
- Show the spinning star from Class 1 (4 turn blocks) and ask: "What if we wanted it to spin 100 times?"

### Loops Deep Dive (15 min)

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

### Conditions Deep Dive (15 min)

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

3. **Combining conditions in a loop — 4-direction movement:**
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

### Guided Project (15 min)

Build together: "Simple Maze"

**Setup:**
- Use the paint editor to draw a simple maze as the backdrop (thick black walls, green start area, red end area)
- Use a small sprite (shrink the cat or use the "Ball" sprite)

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

### Wrap-Up (5 min)
- "Loops save us from repeating blocks. Conditions let our program make decisions."
- Preview: "Next class we add scores and lives using variables!"
