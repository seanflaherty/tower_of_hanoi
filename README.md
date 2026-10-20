# Tower of Hanoi (`tower_of_hanoi`)

> A Python implementation solving the classic Tower of Hanoi mathematical puzzle using recursion and data structures. Part of the [freeCodeCamp](https://www.freecodecamp.org/) Python Certification curriculum.

## 📌 Overview

The **Tower of Hanoi** is a classic mathematical puzzle consisting of three rods and a number of disks of varying diameters. The objective of the puzzle is to move the entire stack of disks from a source rod to a destination rod, following three fundamental rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one stack and placing it on top of another stack or on an empty rod.
3. No larger disk may be placed on top of a smaller disk.

This repository contains Python solutions demonstrating recursive problem-solving, stack manipulation, and state tracing for $N$ disks.

---

## ✨ Features

* **Recursive Solver:** Solves the puzzle in the minimal $2^n - 1$ moves.
* **Step-by-Step Visualization:** Prints or outputs the state of the rods after every move.
* **Configurable Disks:** Allows users to specify any number of disks $N$.

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.x** installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/seanflaherty/tower_of_hanoi.git
   ```

2. **Navigate into the directory:**
   ```bash
   cd tower_of_hanoi
   ```

---

## 💡 Usage Example

To run the solver script directly:

```bash
python tower_of_hanoi.py
```

### Example Code Snippet

```python
def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary
        hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks from auxiliary to target
        hanoi(n - 1, auxiliary, target, source)

# Solve for 3 disks
hanoi(3, 'A', 'C', 'B')
```

---

## 🧪 Algorithmic Complexity

| Parameter | Value |
| :--- | :--- |
| **Optimal Moves** | $2^n - 1$ |
| **Time Complexity** | $\mathcal{O}(2^n)$ |
| **Space Complexity** | $\mathcal{O}(n)$ (Call stack depth) |

---

## 🧪 Running Tests

To run the test suite with **pytest**, execute:

```bash
pytest
```

## 🛠️ Built With

* **Language:** [Python 3](https://www.python.org/)
* **Testing:** [pytest](https://docs.pytest.org/)
* **Platform:** [freeCodeCamp](https://www.freecodecamp.org/) Python Certification
* **Focus:** Recursion.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.