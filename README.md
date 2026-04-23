# Virtual Memory Optimization Simulator

## Overview

The Virtual Memory Optimization Simulator is a Python-based application designed to demonstrate key concepts of virtual memory management. It simulates demand paging, page replacement algorithms, and memory performance metrics to analyze how different strategies affect system efficiency.

The project provides an interactive interface to input page reference strings and frame sizes, and then visualizes the behavior and performance of multiple page replacement algorithms.

---

## Features

- Simulation of demand paging
- Implementation of page replacement algorithms:
  - FIFO (First-In-First-Out)
  - LRU (Least Recently Used)
  - Optimal Page Replacement
- Performance evaluation including:
  - Page faults
  - Hits
  - Fault rate
  - Hit rate
- Comparative visualization using bar charts
- Step-by-step memory state visualization
- Interactive UI for user input and analysis

---

## Tech Stack

- Python
- Streamlit (for user interface)
- Pandas (for data handling and visualization)

---

## Project Structure
virtual-memory-simulator/
│
├── app/
│ └── app.py # Streamlit UI
│
├── core/
│ ├── fifo.py # FIFO algo implementation
│ ├── lru.py # LRU algo implementation
│ ├── optimal.py # Optimal algo implementation
│ ├── simulator.py # central file for importing algos
│ └── metrics.py # Performance metric calculations
│
└── README.md


---

## How It Works

1. The user provides:
   - A page reference sequence
   - The number of available frames

2. The system runs all three algorithms:
   - FIFO
   - LRU
   - Optimal

3. For each algorithm:
   - Page faults and hits are calculated
   - Memory states are recorded step-by-step

4. Performance metrics are computed and displayed

5. Results are visualized through:
   - Tabular data
   - Graphs
   - Memory state transitions

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/sonawane-saurav/virtual-memory-optimization-simulator.git
cd virtual-memory-optimization-simulator

pip install streamlit pandas
streamlit run app/app.py
```

## Example Input

Page Sequence: 7,0,1,2,0,3,0,4
Frames: 3

## Output

The application provides:
- A performance metrics table comparing algorithms
- A bar chart showing page fault comparison
- A step-by-step memory state table for each algorithm

## Learning Outcomes

- Understanding of virtual memory concepts
- Insight into demand paging and page faults
- Comparison of different page replacement algorithms
- Analysis of performance trade-offs in memory management
- Experience with building simulation-based systems
- Exposure to UI integration with backend logic

## Challenges Faced

- Understanding the working of different page replacement algorithms
- Managing state in Streamlit due to script re-execution
- Structuring the project into modular components
- Integrating backend logic with frontend UI
- Debugging input handling and data flow issues
