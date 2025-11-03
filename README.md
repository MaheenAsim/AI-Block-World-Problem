

# 🧱 Block World Goal Stack Planner

## 📖 Overview

This project implements a **Goal Stack Planning (GSP)** algorithm for the **Blocks World problem**, where a robot manipulator autonomously transforms an **initial configuration of blocks** into a **target goal configuration**.

The system simulates intelligent planning behavior by using **predicates**, **preconditions**, and **actions**, following principles of **AI planning and reasoning**.

Developed by **Maheen Asim** and **Julie Zaepfel** at **St. Olaf College**, this project modularizes the Goal Stack Planning algorithm into multiple Python classes for readability, testing, and future extensibility.

---

## 🧩 Project Structure

| File                                 | Description                                                                                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **`main.py`**                        | Entry point of the program — loads input and goal states, runs the planner, and displays results.              |
| **`block.py`**                       | Defines the `Block` class and basic properties of individual blocks.                                           |
| **`state.py`**                       | Manages the current state of the world, representing predicates like `ON`, `ONTABLE`, and `CLEAR`.             |
| **`scene.py`**                       | Handles visual or console-based representation of states.                                                      |
| **`project_01.py`**                  | Core implementation of the Goal Stack Planner — integrates predicates, allowed operations, and planning logic. |
| **`input.txt`**                      | Specifies the **initial state** of the world.                                                                  |
| **`goal.txt`**                       | Specifies the **goal state** configuration.                                                                    |
| **`Block World Paper.docx (1).pdf`** | Research paper accompanying this implementation, describing the algorithm, design, and related work.           |

---

## ⚙️ How It Works

The **Goal Stack Planner** algorithm works as follows:

1. **Initial Setup**

   * Loads the initial and goal states from text files.
   * Initializes the **world state** and an empty **goal stack**.

2. **Goal Decomposition**

   * Pushes compound goals onto the stack.
   * Breaks them down into simpler subgoals.

3. **Action Planning**

   * Checks if preconditions for an action are satisfied.
   * If not, pushes the required predicates back onto the stack.

4. **Execution and State Update**

   * Once all preconditions are satisfied, performs the action.
   * Updates the world state by deleting and adding predicates.

5. **Output**

   * Displays all intermediary states showing how the world transitions from the initial to goal configuration.

---

## 🧠 Core Concepts Implemented

### Predicates

Define conditions of the world:

* `ON(A, B)` → A is on B
* `ONTABLE(A)` → A is on the table
* `CLEAR(A)` → Nothing on top of A
* `HOLDING(A)` → Robot arm holding A
* `ARMEMPTY()` → Arm is free

### Operations

Define actions with preconditions, delete, and add lists:

| Operation       | Preconditions                      | Deletes                  | Adds                     |
| --------------- | ---------------------------------- | ------------------------ | ------------------------ |
| `STACK(A, B)`   | `CLEAR(B)` ∧ `HOLDING(A)`          | `CLEAR(B)`, `HOLDING(A)` | `ARMEMPTY`, `ON(A, B)`   |
| `UNSTACK(A, B)` | `ARMEMPTY`, `ON(A, B)`, `CLEAR(A)` | `ARMEMPTY`, `ON(A, B)`   | `HOLDING(A)`, `CLEAR(B)` |
| `PICKUP(A)`     | `CLEAR(A)`, `ARMEMPTY`             | `ARMEMPTY`               | `HOLDING(A)`             |
| `PUTDOWN(A)`    | `HOLDING(A)`                       | `HOLDING(A)`             | `ONTABLE(A)`, `ARMEMPTY` |

---

## 🧮 Example Run

### Input (`input.txt`)

```
square(A)
triangle(B)
square(C)
square(D)
square(E)
square(F)

on(A, table)
on(B, table)
on(E, table)
on(C, A)
on(D, table)
```

### Goal (`goal.txt`)

```
square(A)
triangle(B)
square(C)
square(D)
square(E)
square(F)

on(A, table)
on(B, table)
on(E, table)
on(C, A)
on(D, C)
```

### Output (Example)

```
Initial state loaded...
Performing UNSTACK(D, table)
Performing STACK(D, C)
Goal achieved successfully!

Final arrangement:
E, B on table
C on A
D on C
```

---

## 🧰 How to Run

### Prerequisites

* Python 3.8+
* No external dependencies required

### Steps

```bash
# 1. Clone or download the repository
git clone https://github.com/<your-username>/block-world-planner.git
cd block-world-planner

# 2. Run the main program
python main.py
```

---

## 🧩 Key Features

* Modular object-oriented design
* Clear separation of **predicates**, **operations**, and **planner logic**
* Readable and extendable code structure
* Step-by-step goal satisfaction trace
* Easily modifiable initial and goal states via text files

---

## 🚀 Future Work

* Add **graphical visualization** for block movements
* Optimize algorithm for **time complexity and scalability**
* Extend to **irregular block shapes** (triangular, cylindrical)
* Integrate reinforcement or heuristic planning approaches

---

## 🧾 References

* Anandraj, J. (2018). *Goal Stack Planning*. [AI - The Future](https://aithefuture.wordpress.com/2018/02/26/goal-stack-planning)
* Slaney, J. & Thiébaux, S. (1996). *Linear Time Near-Optimal Planning in the Blocks World*. [AAAI Conference](https://cdn.aaai.org/AAAI/1996/AAAI96-179.pdf)


