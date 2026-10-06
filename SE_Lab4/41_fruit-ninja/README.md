# Software Engineering Lab 4 – Vibe Coding

## Fruit Ninja – Python/Pygame

**Student:** Anand S  
**USN:** PES1UG24AM341  
**Lab:** Software Engineering Lab – 4  
**Project:** Fruit Ninja  
**Technology:** Python, Pygame  
**Project Directory:** `SE_Lab4/41_fruit-ninja`  
**Personal Repository:** `SE_LAB_PES1UG24AM341`

---

## 1. Project Overview

This project is a Python/Pygame-based Fruit Ninja game enhanced as part of Software Engineering Lab 4 using the Vibe Coding approach.

The starter project was extended through four independent tasks:

1. Refine Collision Detection
2. Implement Game Over Screen
3. Add Replay and Difficulty Selection
4. Add Sound Effects

Each task was implemented, tested, committed separately using Git, and pushed to the personal GitHub repository.

---

## 2. Objectives

The objectives of this lab were:

- Improve the existing Fruit Ninja gameplay.
- Make fruit slicing more reliable.
- Add a proper Game Over state.
- Provide replay functionality.
- Add multiple difficulty levels.
- Improve the game experience using sound effects.
- Practice iterative development and debugging.
- Use Git for version control.
- Maintain separate commits for individual tasks.
- Test each feature after implementation.

---

## 3. Technologies Used

- **Programming Language:** Python
- **Game Framework:** Pygame
- **Version Control:** Git
- **Repository Hosting:** GitHub
- **Development Environment:** Visual Studio Code

---

# 4. Tasks Implemented

## Task 1 – Refine Collision Detection

### Prompt

> Improve the collision detection in the Fruit Ninja game so that fruit slicing works reliably, especially when the player performs fast mouse swipes. Use the line segment between the previous mouse position and the current mouse position for collision detection instead of checking only the current mouse position. Also add a small collision margin around the fruit so that fast swipes are detected reliably. Do not change unrelated gameplay features.

### Implementation

The collision detection was improved so that the game checks the line segment between the previous mouse position and the current mouse position.

An additional collision margin was introduced around the fruit to improve detection reliability during fast swipes.

### Result

Fast mouse swipes can reliably detect fruit slicing even when the mouse moves quickly between frames.

### Commit

```text
Task 1: Refine collision detection
```

---

## Task 2 – Implement Game Over Screen

### Prompt

> Implement a proper Game Over screen for the Fruit Ninja game. When the player loses, stop the normal gameplay and display a clear Game Over message/state to the player. The Game Over state should integrate cleanly with the existing game flow and should not affect unrelated functionality.

### Implementation

A proper Game Over state was added.

When the player reaches the Game Over condition:

- Normal gameplay stops.
- A clear Game Over state is displayed.
- The player can proceed to the replay/difficulty selection flow.

### Result

The game now provides clear feedback when the player loses instead of simply stopping gameplay.

### Commit

```text
Task 2: Implement game over screen
```

---

## Task 3 – Add Replay and Difficulty Selection

### Prompt

> Add replay functionality and difficulty selection to the Fruit Ninja game. After Game Over, provide options for Easy, Medium, Hard, and Exit. Make the difficulty levels meaningfully different by changing gameplay parameters such as fruit spawn interval, bomb probability, and object speed. Allow the player to start a new game without restarting the application. Keep the existing gameplay and collision improvements working correctly.

### Implementation

Replay functionality and multiple difficulty levels were added.

Available options:

- Easy
- Medium
- Hard
- Exit

The difficulty level changes gameplay parameters such as:

- Fruit spawning interval
- Bomb probability
- Object speed

Replay allows the player to start a new game without restarting the application.

During development, gameplay, rendering, movement, and collision-related issues were debugged and corrected.

### Result

The game now provides multiple difficulty levels and allows the player to replay after Game Over.

### Commit

```text
Task 3: Add replay and difficulty selection
```

---

## Task 4 – Add Sound Effects

### Prompt

> Add sound effects to the Fruit Ninja game for the major gameplay events. Implement a sound management module and add separate audio feedback for fruit slicing, bomb explosion, and Game Over. Ensure the sounds are triggered at the correct events and do not break the existing gameplay, replay, difficulty selection, or collision detection features.

### Implementation

A dedicated sound management module was added:

```text
game/sound_manager.py
```

The following sound effects were implemented:

- Fruit slicing sound
- Bomb explosion sound
- Game Over sound

The sounds are triggered according to the corresponding gameplay events.

### Result

The game now provides audio feedback for important gameplay events.

### Commit

```text
Task 4: Add sound effects
```

---

# 5. Final Features

The completed Fruit Ninja game contains:

- Improved fruit collision detection
- Reliable fast-swipe slicing
- Game Over screen
- Replay functionality
- Easy difficulty
- Medium difficulty
- Hard difficulty
- Difficulty-based gameplay changes
- Fruit slicing sound
- Bomb explosion sound
- Game Over sound

---

# 6. Project Structure

The main project is located inside:

```text
SE_Lab4/
└── 41_fruit-ninja/
```

The sound functionality includes:

```text
game/
└── sound_manager.py
```

The remaining project files are part of the Fruit Ninja starter project and its updated implementation.

---

# 7. How to Run the Project

## Step 1 – Navigate to the Project

```bash
cd SE_Lab4/41_fruit-ninja
```

## Step 2 – Install Pygame

```bash
pip install pygame
```

## Step 3 – Run the Game

Run the main Python entry-point file of the project:

```bash
python main.py
```

> If the starter project uses a different entry-point filename, run that existing main Python file instead.

---

# 8. Testing

The complete game was tested after implementing all four tasks.

## 8.1 Collision Detection Testing

Fast mouse swipes were tested to verify that fruits could be sliced correctly.

**Status:** Passed

## 8.2 Game Over Testing

The game was played until the Game Over condition was reached.

**Status:** Passed

## 8.3 Replay Testing

Replay functionality was tested after Game Over.

**Status:** Passed

## 8.4 Difficulty Testing

The following difficulty levels were tested:

- Easy
- Medium
- Hard

**Status:** Passed

## 8.5 Sound Testing

The following sound effects were tested:

- Fruit slicing
- Bomb explosion
- Game Over

**Status:** Passed

## 8.6 Final Integration Testing

All implemented features were tested together after completing Task 4.

**Status:** Passed

---

# 9. Before Implementation Video

The following video shows the original/starter version of the Fruit Ninja project before implementing the Lab 4 tasks.

## Before Video

**Insert / Embed Before Video Here**

<br><br><br><br>

**Before Video Link:**  
[Watch Before Implementation Video](./Before_Modifying.mp4)

---

# 10. After Implementation Video

The following video shows the final Fruit Ninja project after completing all four Lab 4 tasks.

## After Video

**Insert / Embed After Video Here**

<br><br><br><br>

**After Video Link:**  
[Watch After Implementation Video](./After_Modifying.mp4)

---

# 11. Git Version Control

Git was used to maintain the project and track the implementation of each task.

Each task was committed separately.

### Task 1

```text
Task 1: Refine collision detection
```

### Task 2

```text
Task 2: Implement game over screen
```

### Task 3

```text
Task 3: Add replay and difficulty selection
```

### Task 4

```text
Task 4: Add sound effects
```

All task changes were pushed to the personal GitHub repository.

---

# 12. Development Workflow

The following workflow was followed:

```text
Starter Project
      |
      v
Task 1 – Collision Detection
      |
      v
Testing
      |
      v
Git Commit & Push
      |
      v
Task 2 – Game Over Screen
      |
      v
Testing
      |
      v
Git Commit & Push
      |
      v
Task 3 – Replay & Difficulty
      |
      v
Debugging & Testing
      |
      v
Git Commit & Push
      |
      v
Task 4 – Sound Effects
      |
      v
Testing
      |
      v
Git Commit & Push
      |
      v
Final Integration Testing
      |
      v
Before / After Videos
```

---

# 13. Final Task Status

| Task | Feature | Status |
|------|---------|--------|
| Task 1 | Refine Collision Detection | Completed |
| Task 2 | Game Over Screen | Completed |
| Task 3 | Replay Functionality | Completed |
| Task 3 | Difficulty Selection | Completed |
| Task 4 | Sound Effects | Completed |
| Final | Integration Testing | Completed |

---

# 14. Lab 4 Deliverables

The completed Lab 4 work consists of:

1. **Before Video** – Original/starter project demonstration.
2. **After Video** – Final project demonstration after implementing all tasks.
3. **Updated Source Code** – Fruit Ninja project containing all four implemented tasks.
4. **Separate Git Commits** – Individual commits for each task.
5. **Vibe Coding Chat History** – The four prompts used to implement the four tasks.

---

# 15. Conclusion

The Fruit Ninja project was successfully enhanced through four independent Vibe Coding tasks.

The final application includes improved collision detection, a proper Game Over screen, replay functionality, multiple difficulty levels, and sound effects.

Each task was implemented and tested independently, committed separately using Git, and pushed to the personal repository.

The complete project was finally integration-tested and all implemented features were verified successfully.

## Final Status

**LAB 4 – VIBE CODING: COMPLETED SUCCESSFULLY**
