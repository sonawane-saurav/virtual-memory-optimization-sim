import pandas as pd
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from core.simulator import fifo, lru, optimal
from core.metrics import compare_algorithms
from core.workloads import (
    sequential_workload,
    looping_workload,
    random_workload,
    locality_workload
)

# -------------------------------
# Highlight Function (NEW)
# -------------------------------
def highlight_faults(states):
    fault_indices = []
    prev = None

    for i, state in enumerate(states):
        if prev is None or state != prev:
            fault_indices.append(i)
        prev = state

    def highlight(row):
        if row.name in fault_indices:
            return ['background-color: #ffcccc'] * len(row)
        return [''] * len(row)

    return highlight


# Title
st.title("Virtual Memory Optimization Simulator")

# -------------------------------
# Workload Selection
# -------------------------------
st.subheader("Workload Selection")

workload_type = st.selectbox(
    "Select Workload Type",
    ["Manual Input", "Sequential", "Looping", "Random", "Locality"]
)

frames = st.number_input("Enter number of frames", min_value=1, value=3, step=1)

pages = []

# -------------------------------
# Input Handling
# -------------------------------
if workload_type == "Manual Input":
    page_input = st.text_input(
        "Enter page sequence (comma separated)",
        "7,0,1,2,0,3,0,4"
    )
    try:
        pages = [int(x.strip()) for x in page_input.split(",")]
    except:
        st.error("Invalid input format!")

elif workload_type == "Sequential":
    n = st.slider("Length", 5, 20, 10)
    pages = sequential_workload(n)

elif workload_type == "Looping":
    cycles = st.slider("Cycles", 1, 10, 3)
    pages = looping_workload(cycles)

elif workload_type == "Random":
    n = st.slider("Length", 5, 20, 10)
    max_page = st.slider("Max Page Number", 3, 10, 5)
    pages = random_workload(n, max_page)

elif workload_type == "Locality":
    n = st.slider("Length", 5, 20, 10)
    pages = locality_workload(n)

# Show pages
if pages:
    st.write("Page Sequence:", pages)

# -------------------------------
# Run Simulation
# -------------------------------
if st.button("Run Simulation") and pages:

    fifo_faults, fifo_states = fifo(pages, frames)
    lru_faults, lru_states = lru(pages, frames)
    opt_faults, opt_states = optimal(pages, frames)

    st.session_state["pages"] = pages
    st.session_state["fifo"] = (fifo_faults, fifo_states)
    st.session_state["lru"] = (lru_faults, lru_states)
    st.session_state["opt"] = (opt_faults, opt_states)

# -------------------------------
# Display Results
# -------------------------------
if "fifo" in st.session_state:

    pages = st.session_state["pages"]
    fifo_faults, fifo_states = st.session_state["fifo"]
    lru_faults, lru_states = st.session_state["lru"]
    opt_faults, opt_states = st.session_state["opt"]

    st.subheader("Results")

    st.info(f"Total Page Requests: {len(pages)}")

    # Metrics
    results = {
        "FIFO": fifo_faults,
        "LRU": lru_faults,
        "Optimal": opt_faults
    }

    comparison = compare_algorithms(results, pages)

    data = []
    for algo, metrics in comparison.items():
        data.append({
            "Algorithm": algo,
            "Page Faults": metrics["page_faults"],
            "Hits": metrics["hits"],
            "Fault Rate": round(metrics["fault_rate"], 3),
            "Hit Rate": round(metrics["hit_rate"], 3)
        })

    df = pd.DataFrame(data)

    st.subheader("Performance Metrics")
    st.table(df)

    # Best Algorithm
    best_algo = min(results, key=results.get)
    st.success(f"Best Performing Algorithm: {best_algo}")

    # Graph
    st.subheader("Page Fault Comparison")

    chart_data = pd.DataFrame({
        "Algorithm": ["FIFO", "LRU", "Optimal"],
        "Page Faults": [fifo_faults, lru_faults, opt_faults]
    })

    st.bar_chart(chart_data.set_index("Algorithm"))

    # Fault Rate Graph
    st.subheader("Fault Rate Comparison")

    fault_rate_data = pd.DataFrame({
        "Algorithm": ["FIFO", "LRU", "Optimal"],
        "Fault Rate": [
            fifo_faults / len(pages),
            lru_faults / len(pages),
            opt_faults / len(pages)
        ]
    })

    st.line_chart(fault_rate_data.set_index("Algorithm"))

    # -------------------------------
    # Memory Visualization
    # -------------------------------
    algo_choice = st.selectbox(
        "Choose Algorithm to Visualize",
        ["FIFO", "LRU", "Optimal"]
    )

    if algo_choice == "FIFO":
        states = fifo_states
    elif algo_choice == "LRU":
        states = lru_states
    else:
        states = opt_states

    state_df = pd.DataFrame(states)
    state_df.columns = [f"Frame{i+1}" for i in range(state_df.shape[1])]

    st.subheader(f"{algo_choice} Memory States")

    styled_df = state_df.style.apply(highlight_faults(states), axis=1)
    st.dataframe(styled_df)

# -------------------------------
# Concepts Section
# -------------------------------
st.header("Concepts Explained")

st.subheader("Memory Allocation")
st.write("""
Memory is divided into fixed-size frames.
Pages are loaded dynamically into these frames based on demand.
This represents how operating systems allocate memory in paging systems.
""")

st.subheader("Fragmentation")
st.write("""
Paging avoids external fragmentation because memory is divided into fixed-size frames.

However, internal fragmentation may occur when a page does not completely fill a frame.

This simulator focuses on page replacement, so fragmentation is explained conceptually.
""")
