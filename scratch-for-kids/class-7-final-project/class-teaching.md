# Class 7: Final Project & Show and Tell — Teaching Guide (1 Hour)

> **Topic:** Independent project building and presentation  
> **Duration:** 1 hour  
> **Prerequisites:** Classes 1–6 completed

## Learning Objectives
- Plan a project before building it
- Apply all learned concepts independently
- Practice presenting and explaining their work
- Celebrate their achievements and inspire each other

---

## Session Breakdown

### Concept Review Game (10 min)

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

### Project Planning (10 min)

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

### Build Time (25 min)

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

### Show and Tell (15 min)

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
