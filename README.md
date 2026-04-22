# Virtual Memory Optimization Simulator

A Python-based simulator to demonstrate core Operating System concepts such as demand paging, page faults, and memory allocation strategies. The project analyzes how virtual memory techniques impact system performance and resource utilization.


## Features

- Simulation of **demand paging**
- Tracking and analysis of **page faults**
- Implementation of **page replacement algorithms** (FIFO, LRU)
- Simulation of **memory allocation strategies**
- Analysis of **internal and external fragmentation**
- Interactive UI using Streamlit


## Tools

- Python
- Streamlit


## Concepts Covered

- Virtual Memory
- Demand Paging
- Page Fault Handling
- Page Replacement Algorithms (FIFO, LRU)
- Memory Allocation
- Internal & External Fragmentation


## How It Works

1. User inputs:
   - Number of frames
   - Page reference string
2. Simulator processes:
   - Applies selected page replacement algorithm
   - Tracks page faults
3. Displays:
   - Page table visualization
   - Page fault count
   - Performance insights


## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
