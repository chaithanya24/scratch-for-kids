# Class 5: Variables & Score — Project Work

> These are the 4 projects for Class 5. Each focuses on using variables.

---

## Project 1: Click Counter Challenge
**Goal:** Click the sprite as many times as you can in 10 seconds.

**Instructions:**
1. Create variables "Score" and "Time"
2. On green flag: set Score to 0, set Time to 10
3. Use a `repeat until` loop that waits 1 second and decreases Time by 1
4. When Time reaches 0, show the final score and stop
5. On sprite click: increase Score by 1, play a sound, move sprite to a random position

**Concepts practiced:** Timer using a variable, combining click events with variables.

---

## Project 2: Math Quiz
**Goal:** The sprite asks math questions. Score goes up for correct answers.

**Instructions:**
1. Create variables "Score", "Number1", "Number2"
2. Use a `repeat (5)` loop for 5 questions
3. Set Number1 and Number2 to random numbers (1–10)
4. Use `ask` block to show the question (e.g., "3 + 7")
5. Use `if` to check if `answer` equals the correct sum
6. Show final score at the end

**Concepts practiced:** `ask` and `answer` blocks, operators (addition), variables for dynamic content.

---

## Project 3: Virtual Pet
**Goal:** A pet with hunger and happiness meters. Feed it and play with it to keep the meters up.

**Instructions:**
1. Create variables "Hunger" (starts at 100) and "Happiness" (starts at 100)
2. In a `forever` loop, gradually decrease both variables
3. If either reaches 0, game over
4. Press "f" to feed (increase Hunger by 20)
5. Press "p" to play (increase Happiness by 20)
6. Add warnings when meters get low (below 30)

**Concepts practiced:** Multiple variables interacting, gradual decrease, key events to modify variables.

---

## Project 4: Coin Collector with Levels
**Goal:** Collect coins to score points. After 5 coins, speed increases (level up).

**Instructions:**
1. Cat sprite at bottom, Coin sprite falls from top
2. Create variables: "Score", "Level", "Speed"
3. Coin falls at the current Speed value
4. When cat catches coin: score +1
5. Every 5 points (use `mod` operator): Level +1, Speed +1
6. Display the level-up message

**Concepts practiced:** `mod` operator for level thresholds, variable-driven difficulty.
