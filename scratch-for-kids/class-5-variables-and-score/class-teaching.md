# Class 5: Variables & Score — Teaching Guide (1 Hour)

> **Topic:** Using variables to track score, lives, and timers  
> **Duration:** 1 hour  
> **Prerequisites:** Classes 1–4 completed

## Learning Objectives
- Understand what variables are and why they're useful
- Create, set, and change variables in Scratch
- Use variables to track score, lives, and timers
- Display variables on the stage

---

## Session Breakdown

### Review & Warm-Up (5 min)
- Quick recap of loops and conditions
- "Today we're going to add something that makes games feel like real games — scores, lives, and timers!"

### What is a Variable? (10 min)

**Simple Explanation:**
- "A variable is like a labeled box. You can put a number or word inside it, look at what's inside, and change what's inside."
- Draw on whiteboard: a box labeled "Score" with the number 0 inside
- "When you catch a fruit, we open the box, take out 0, put in 1. Catch another fruit, take out 1, put in 2."

**Real-life examples:**
- Your age is a variable — it changes every year
- The temperature outside is a variable — it changes every hour
- Your score in a game is a variable — it changes when you earn points

### Creating & Using Variables (15 min)

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

### Guided Project (20 min)

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

### Wrap-Up (5 min)
- "Variables let us remember things — scores, lives, anything we need to track."
- Preview: "Next class we learn cloning — making copies of sprites while the game is running!"
