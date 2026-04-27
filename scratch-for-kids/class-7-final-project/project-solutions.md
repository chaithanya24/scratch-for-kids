# Class 7: Final Project — Project Solutions

> Complete block-by-block solutions for all 4 example projects.

---

## Project 1: Pong Game — Solution

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

---

## Project 2: Animated Story — Solution

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

---

## Project 3: Whack-a-Mole — Solution

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

---

## Project 4: Dance Party — Solution

**Setup:** Add 3-4 dancer sprites (use Scratch's built-in dancer sprites). Add a music loop.

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
