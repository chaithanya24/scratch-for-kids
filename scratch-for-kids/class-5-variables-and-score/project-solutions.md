# Class 5: Variables & Score — Project Solutions

> Complete block-by-block solutions for all 4 projects.

---

## Project 1: Click Counter Challenge — Solution

**Setup:** Create variables "Score" and "Time".

```
when green flag clicked
set [Score] to (0)
set [Time] to (10)
repeat until <(Time) < (1)>
  wait (1) seconds
  change [Time] by (-1)
end
say (join [Final Score: ] (Score)) for (3) seconds
stop [all]

when this sprite clicked
change [Score] by (1)
start sound [Pop]
go to x: (pick random (-200) to (200)) y: (pick random (-150) to (150))
```

---

## Project 2: Math Quiz — Solution

**Setup:** Create variables "Score", "Number1", "Number2".

```
when green flag clicked
set [Score] to (0)
repeat (5)
  set [Number1] to (pick random (1) to (10))
  set [Number2] to (pick random (1) to (10))
  ask (join (join (Number1) [ + ]) (Number2)) and wait
  if <(answer) = ((Number1) + (Number2))> then
    say [Correct!] for (1) seconds
    change [Score] by (1)
    start sound [Collect]
  else
    say (join [Wrong! The answer was ] ((Number1) + (Number2))) for (2) seconds
    start sound [Oops]
  end
end
say (join [You got ] (join (Score) [ out of 5!])) for (3) seconds
```

---

## Project 3: Virtual Pet — Solution

**Setup:** Create variables "Hunger" (starts at 100) and "Happiness" (starts at 100). Cat sprite.

```
when green flag clicked
set [Hunger] to (100)
set [Happiness] to (100)
forever
  change [Hunger] by (-1)
  change [Happiness] by (-0.5)
  wait (1) seconds
  if <(Hunger) < (1)> then
    say [I'm starving! Game over!] for (3) seconds
    stop [all]
  end
  if <(Happiness) < (1)> then
    say [I'm so sad! Game over!] for (3) seconds
    stop [all]
  end
  if <(Hunger) < (30)> then
    say [I'm hungry...] for (1) seconds
  end
  if <(Happiness) < (30)> then
    think [I'm bored...] for (1) seconds
  end
end

when [f] key pressed
change [Hunger] by (20)
say [Yum!] for (1) seconds
start sound [Chomp]

when [p] key pressed
change [Happiness] by (20)
say [Wheee!] for (1) seconds
next costume
start sound [Pop]
```

---

## Project 4: Coin Collector with Levels — Solution

**Setup:** Cat sprite + Coin sprite. Variables: "Score", "Level", "Speed".

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

**Coin script:**
```
when green flag clicked
set [Score] to (0)
set [Level] to (1)
set [Speed] to (3)
forever
  go to x: (pick random (-200) to (200)) y: (180)
  show
  repeat until <(y position) < (-170)>
    change y by ((0) - (Speed))
    if <touching [Cat]?> then
      change [Score] by (1)
      start sound [Collect]
      hide
      if <((Score) mod (5)) = (0)> then
        change [Level] by (1)
        change [Speed] by (1)
        say (join [Level ] (Level)) for (1) seconds
      end
    end
  end
end
```
