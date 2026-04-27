# Class 3: Events & Sound — Project Solutions

> Complete block-by-block solutions for all 4 projects.

---

## Project 1: Piano Keyboard — Solution

**Setup:** Add the "Music" extension. Click "Add Extension" (bottom left) → "Music".

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

**Note values:** 60 = Middle C, 62 = D, 64 = E, 65 = F, 67 = G, 69 = A, 71 = B, 72 = High C

---

## Project 2: Click the Sprite Game — Solution

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

---

## Project 3: Sound Board — Solution

**Setup:** Add 4 sprites (Drum, Guitar, Singer, Bell). Give each a different sound.

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

---

## Project 4: Story with Broadcast Messages — Solution

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
