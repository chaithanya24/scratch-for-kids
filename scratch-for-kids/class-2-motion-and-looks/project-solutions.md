# Class 2: Motion & Looks — Project Solutions

> Complete block-by-block solutions for all 4 projects.

---

## Project 1: Walking Animation — Solution

```
when green flag clicked
set rotation style [left-right]
forever
  move (5) steps
  next costume
  if on edge, bounce
  wait (0.1) seconds
end
```

---

## Project 2: Growing and Shrinking Sprite — Solution

```
when green flag clicked
set size to (100) %
repeat (10)
  change size by (10)
  wait (0.1) seconds
end
repeat (10)
  change size by (-10)
  wait (0.1) seconds
end
```

---

## Project 3: Color Changing Parrot — Solution

**Setup:** Choose the "Parrot" sprite.

```
when green flag clicked
go to x: (-200) y: (50)
repeat (40)
  move (10) steps
  next costume
  change [color] effect by (5)
  wait (0.05) seconds
end
clear graphic effects
say [I made it!] for (2) seconds
```

---

## Project 4: Sprite Parade — Solution

**Setup:** Add 3 sprites (Cat, Dog, Duck). Position them all at x: -200.

**Cat script:**
```
when green flag clicked
go to x: (-200) y: (100)
glide (2) secs to x: (200) y: (100)
say [Cat is here!] for (1) seconds
```

**Dog script:**
```
when green flag clicked
go to x: (-200) y: (0)
wait (1) seconds
glide (2) secs to x: (200) y: (0)
say [Dog is here!] for (1) seconds
```

**Duck script:**
```
when green flag clicked
go to x: (-200) y: (-100)
wait (2) seconds
glide (2) secs to x: (200) y: (-100)
say [Quack!] for (1) seconds
```
