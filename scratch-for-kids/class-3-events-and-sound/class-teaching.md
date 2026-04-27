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

### Broadcasting: How Sprites Talk to Each Other (10 min)

Broadcasting is one of the most powerful concepts in Scratch. It's how sprites send messages to each other — like a walkie-talkie system!

#### The Sender and Receiver Pattern

In real life, communication always has two parts:
- A **Sender** — the person who sends the message
- A **Receiver** — the person who gets the message and acts on it

Scratch broadcasting works the same way:
- **Sender:** The sprite that uses `broadcast [message]` — it shouts a message to everyone
- **Receiver:** Any sprite that has `when I receive [message]` — it hears the message and runs its script

#### How Broadcasting Works — Step by Step

1. **Sprite A** runs `broadcast [start dancing]`
2. The message `"start dancing"` goes out to ALL sprites at the same time
3. **Any sprite** that has `when I receive [start dancing]` will run its script
4. Sprites that DON'T have that block just ignore the message

**Key rules:**
- One sender can trigger MANY receivers (1-to-many communication)
- The sender doesn't need to know who's listening
- Multiple sprites can listen for the same message
- A sprite can be both a sender AND a receiver
- Messages are just text labels — you create them and name them anything you want

#### Real-Life Analogies for Kids

**📻 Radio Station Analogy:**
- The `broadcast` block is like a radio station — it sends a signal out to everyone
- The `when I receive` block is like a radio tuned to that station — only radios tuned to the right channel hear it
- If you're not tuned in, you don't hear anything

**📬 Post Office Analogy:**
- `broadcast [message]` = putting a letter in EVERY mailbox in town
- `when I receive [message]` = checking your mailbox and reading the letter
- If you don't check your mailbox (no `when I receive` block), you never know the letter arrived

**🏫 School Announcement Analogy:**
- `broadcast` = the principal makes an announcement over the loudspeaker
- `when I receive` = students in the classroom hear it and follow the instruction
- "All students go to the gym" — every classroom hears it, but only students respond

#### Types of Broadcast

| Block | What It Does | When to Use |
|-------|-------------|-------------|
| `broadcast [message]` | Sends the message and immediately continues to the next block | When the sender doesn't need to wait |
| `broadcast [message] and wait` | Sends the message and WAITS until all receivers finish their scripts | When things need to happen in order (like a story) |

#### Common Broadcasting Patterns

**Pattern 1: Scene Changes (Story)**
```
-- Narrator sprite:
broadcast [scene 2]

-- All sprites listen:
when I receive [scene 2]
  switch backdrop to [castle]
  go to x: (100) y: (0)
  show
```

**Pattern 2: Game Events**
```
-- When player loses:
broadcast [game over]

-- Score sprite listens:
when I receive [game over]
  say [Final Score: ...] for (3) seconds

-- Enemy sprite listens:
when I receive [game over]
  stop [other scripts in sprite]
  hide
```

**Pattern 3: Chain Reaction (Conversation)**
```
-- Sprite A says something, then tells Sprite B to respond:
say [Hello!] for (2) seconds
broadcast [B's turn]

-- Sprite B waits for its turn:
when I receive [B's turn]
say [Hi back!] for (2) seconds
broadcast [A's turn again]
```

#### Creating a New Message

1. Drag a `broadcast` block into the scripts area
2. Click the dropdown arrow on the block
3. Click "New message"
4. Type a name (e.g., "start game", "player wins", "next level")
5. Click OK — now this message appears in all `broadcast` and `when I receive` dropdowns

**Naming tips:**
- Use descriptive names: `game over` is better than `message1`
- Use action words: `start dancing`, `show score`, `next scene`
- Keep them short but clear

#### Activity: Build a Simple Broadcast Chain

Have kids build this:

**Sprite 1 (Cat):**
```
when green flag clicked
say [Watch this!] for (2) seconds
broadcast [do a trick]
```

**Sprite 2 (Dog):**
```
when I receive [do a trick]
turn right (360) degrees
say [Ta-da!] for (2) seconds
broadcast [take a bow]
```

**Sprite 1 (Cat) — second script:**
```
when I receive [take a bow]
say [Great job!] for (2) seconds
```

Ask kids: "Who is the sender? Who is the receiver? Can a sprite be both?"

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
