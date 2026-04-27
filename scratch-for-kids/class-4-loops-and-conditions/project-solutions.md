# Class 4: Loops & Conditions — Project Solutions

> Complete block-by-block solutions for all 4 projects.

---

## Project 1: Dodge the Obstacles — Solution

**Setup:** Player sprite (Cat) at bottom. Add a "Ball" sprite.

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

**Ball script:**
```
when green flag clicked
forever
  go to x: (pick random (-200) to (200)) y: (180)
  repeat until <(y position) < (-170)>
    change y by (-5)
  end
end
```

---

## Project 2: Color Touch Game — Solution

**Setup:** Paint a backdrop with 4 colored quadrants (red, blue, green, yellow).

```
when green flag clicked
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
  if <touching color [#ff0000]?> then
    say [Red zone!] for (0.5) seconds
    set [color] effect to (0)
  end
  if <touching color [#0000ff]?> then
    say [Blue zone!] for (0.5) seconds
    set [color] effect to (100)
  end
  if <touching color [#00ff00]?> then
    say [Green zone!] for (0.5) seconds
    set [color] effect to (50)
  end
  if <touching color [#ffff00]?> then
    say [Yellow zone!] for (0.5) seconds
    set [color] effect to (150)
  end
end
```

---

## Project 3: Chase Game — Solution

```
when green flag clicked
forever
  point towards [mouse-pointer]
  move (3) steps
  if <touching [mouse-pointer]?> then
    say [Got you!] for (1) seconds
    go to x: (0) y: (0)
    wait (1) seconds
  end
end
```

**Extension — Second sprite that runs away from the cat:**
```
when green flag clicked
forever
  point towards [Cat]
  turn right (180) degrees
  move (2) steps
  if on edge, bounce
end
```

---

## Project 4: Traffic Light Simulator — Solution

**Setup:** Create a sprite with 3 costumes (red light, yellow light, green light). Add a person sprite.

**Traffic Light script:**
```
when green flag clicked
forever
  switch costume to [red]
  broadcast [red light]
  wait (3) seconds
  switch costume to [green]
  broadcast [green light]
  wait (3) seconds
  switch costume to [yellow]
  broadcast [yellow light]
  wait (1) seconds
end
```

**Person script:**
```
when green flag clicked
go to x: (-200) y: (-100)

when I receive [green light]
repeat until <(x position) > (200)>
  move (3) steps
  next costume
  wait (0.1) seconds
end
go to x: (-200) y: (-100)

when I receive [red light]
stop [other scripts in sprite]

when I receive [yellow light]
stop [other scripts in sprite]
```
