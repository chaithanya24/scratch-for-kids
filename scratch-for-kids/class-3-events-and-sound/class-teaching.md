# Class 3: Events & Sound — Teaching Guide (1 Hour)

> **Topic:** Making interactive projects with events and sound  
> **Duration:** 1 hour  
> **Prerequisites:** Classes 1–2 completed

## Learning Objectives
- Understand events as triggers that start scripts
- Use keyboard and mouse events to make interactive projects
- Add and control sounds in Scratch projects
- Use broadcast messages for sprite-to-sprite communication

---

## Session Breakdown

### Review & Warm-Up (5 min)
- "Last class we made sprites move and change looks. Today we make them interactive — they'll respond to YOU!"
- Quick challenge: "Make your cat say something when you click the green flag" (review)

### Events Deep Dive (15 min)

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

### Sound Deep Dive (15 min)

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

### Guided Project (15 min)

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

### Free Build Time (10 min)

Kids pick a sample project or create their own interactive sprite.
