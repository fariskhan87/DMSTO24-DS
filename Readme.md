# DMSTO24-DS

This repository contains assignments and solutions for the **DMSTO24 Data Structures course**. Each assignment file (`uppgift`) is accompanied by a corresponding test file located in the `tests` directory to ensure correctness and validate the implementation.

## Repository Structure

### Branch: `upifgth01`

The branch is organized as follows:

```
DMSTO24-DS/
├── uppgift1.py
├── uppgift2.py
├── uppgift3.py
├── uppgift4.py
├── uppgift5.py
├── uppgift6.py
├── uppgift7.py
├── uppgift8.py
├── uppgift9.py
├── uppgift10.py
├── uppgift11.py
├── uppgift12.py
├── tests/
│   ├── test_uppgift1.py
│   ├── test_uppgift2.py
│   ├── test_uppgift3.py
│   ├── test_uppgift4.py
│   ├── test_uppgift5.py
│   ├── test_uppgift6.py
│   ├── test_uppgift7.py
│   ├── test_uppgift8.py
│   ├── test_uppgift9.py
│   ├── test_uppgift10.py
│   ├── test_uppgift11.py
│   ├── test_uppgift12.py
└── README.md
```

### Assignment Files and Descriptions

1. **`uppgift1.py`**
   - *Description:* Implements basic data structures such as arrays and linked lists, along with fundamental operations like insertion, deletion, and search.

2. **`uppgift2.py`**
   - *Description:* Focuses on stack and queue implementations, including applications like balancing parentheses and expression evaluation.

3. **`uppgift3.py`**
   - *Description:* Introduces binary tree structures, covering insertion, deletion, and traversal algorithms (in-order, pre-order, post-order).

4. **`uppgift4.py`**
   - *Description:* Explores graph data structures, including representations (adjacency list/matrix) and traversal methods like depth-first search (DFS) and breadth-first search (BFS).

5. **`uppgift5.py`**
   - *Description:* Delves into sorting algorithms such as quicksort, mergesort, and heapsort, analyzing their time and space complexities.

6. **`uppgift6.py`**
   - *Description:* Examines hashing techniques, hash table implementations, and collision resolution strategies like chaining and open addressing.

7. **`uppgift7.py`**
   - *Description:* Studies dynamic programming concepts, solving problems like the knapsack problem and Fibonacci sequence computations.

8. **`uppgift8.py`**
   - *Description:* Investigates greedy algorithms with applications in optimization problems, including activity selection and Huffman coding.

9. **`uppgift9.py`**
   - *Description:* Focuses on graph algorithms for shortest paths, such as Dijkstra's and Bellman-Ford algorithms, and their practical applications.

10. **`uppgift10.py`**
    - *Description:* Explores advanced tree structures like AVL trees and red-black trees, emphasizing self-balancing properties and operations.

11. **`uppgift11.py`**
    - *Description:* Introduces network flow algorithms, including the Ford-Fulkerson method, with applications in maximizing flow in networks.

12. **`uppgift12.py`**
    - *Description:* Covers computational geometry topics, such as convex hull algorithms and their use cases in computer graphics and GIS.

### Test Files

Each assignment has a corresponding test file located in the `tests` directory:

- **`tests/test_uppgift1.py`** to **`tests/test_uppgift12.py`**
  - *Description:* Contains unit tests for the respective assignment file, covering various cases to ensure the correctness and robustness of the implementations.

## How to Use

### Clone the Repository

```bash
git clone -b upifgth01 https://github.com/fariskhan87/DMSTO24-DS.git
cd DMSTO24-DS
```

### Run the Tests

Ensure you have Python installed along with `pytest`. To run the tests:

```bash
pip install pytest
pytest
```

This will execute all test files in the `tests` directory and display the results.

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request to the `upifgth01` branch with a detailed description of the changes.
