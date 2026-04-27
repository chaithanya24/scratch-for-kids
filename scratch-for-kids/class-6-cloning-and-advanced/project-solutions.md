# Class 6: Cloning & Advanced Techniques — Project Solutions

> Complete block-by-block solutions for all 4 projects.

---

## Project 1: Snowfall Animation — Solution

**Setup:** Draw a small white circle sprite (snowflake). Add a winter backdrop.

```
when green flag clicked
hide
forever
  create clone of [myself]
  wait (0.2) seconds
end

when I start as a clone
go to x: (pick random (-240) to (240)) y: (180)
set size to (pick random (20) to (80)) %
show
repeat until <(y position) < (-175)>
  change y by (pick random (-3) to (-1))
  change x by (pick random (-2) to (2))
  turn right (pick random (-5) to (5)) degrees
end
delete this clone
```

---

## Project 2: Balloon Pop Game — Solution

**Setup:** Use the "Balloon1" sprite. Create variable "Score".

```
when green flag clicked
hide
set [Score] to (0)
forever
  create clone of [myself]
  wait (pick random (0.5) to (2))
end

when I start as a clone
go to x: (pick random (-200) to (200)) y: (-180)
set size to (pick random (50) to (100)) %
set [color] effect to (pick random (0) to (200))
show
repeat until <(y position) > (180)>
  change y by (pick random (1) to (4))
  change x by (pick random (-1) to (1))
end
delete this clone

when I start as a clone
wait until <mouse down? and touching [mouse-pointer]?>
change [Score] by (1)
start sound [Pop]
repeat (5)
  change size by (10)
  change [ghost] effect by (20)
end
delete this clone
```

**Note:** The two `when I start as a clone` scripts both run on each clone simultaneously.

---

## Project 3: Rain of Emojis — Solution

**Setup:** Create a sprite with 2 costumes: happy face and sad face. Player sprite at bottom. Variable: "Score".

**Emoji sprite:**
```
when green flag clicked
hide
forever
  create clone of [myself]
  wait (0.8) seconds
end

when I start as a clone
go to x: (pick random (-200) to (200)) y: (180)
switch costume to (pick random (1) to (2))
show
repeat until <(y position) < (-170)>
  change y by (-4)
  if <touching [Player]?> then
    if <(costume [name]) = [happy]> then
      change [Score] by (1)
      start sound [Collect]
    else
      change [Score] by (-1)
      start sound [Oops]
    end
    delete this clone
  end
end
delete this clone
```

**Player script:**
```
when green flag clicked
set [Score] to (0)
go to x: (0) y: (-150)
forever
  go to x: (mouse x) y: (-150)
end
```

---

## Project 4: Fireworks Display — Solution

**Setup:** Draw a small colored dot sprite (Particle). Create a "Launcher" sprite (small arrow or rocket).

**Launcher script:**
```
when green flag clicked
hide
forever
  if <mouse down?> then
    go to x: (mouse x) y: (-180)
    show
    glide (0.5) secs to x: (mouse x) y: (mouse y)
    broadcast [explode]
    hide
    wait (0.5) seconds
  end
end
```

**Particle sprite (small colored circle):**
```
when green flag clicked
hide

when I receive [explode]
repeat (20)
  create clone of [myself]
end

when I start as a clone
go to [Launcher]
set [color] effect to (pick random (0) to (200))
set size to (pick random (30) to (80)) %
show
point in direction (pick random (-180) to (180))
repeat (20)
  move (pick random (3) to (8)) steps
  change [ghost] effect by (5)
  change size by (-2)
end
delete this clone
```
