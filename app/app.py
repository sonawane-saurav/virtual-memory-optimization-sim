import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from core.simulator import fifo, lru, optimal
from core.metrics import compare_algorithms

# Title
st.title("Virtual Memory Optimization Simulator")

# Inputs
page_input = st.text_input("Enter page sequence (comma separated)", "7,0,1,2,0,3,0,4")
frames = st.number_input("Enter number of frames", min_value=1, value=3, step=1)

# Run Simulation
if st.button("Run Simulation"):
    try:
        pages = [int(x.strip()) for x in page_input.split(",")]

        fifo_faults, fifo_states = fifo(pages, frames)
        lru_faults, lru_states = lru(pages, frames)
        opt_faults, opt_states = optimal(pages, frames)

        # Store results in session
        st.session_state["pages"] = pages
        st.session_state["fifo"] = (fifo_faults, fifo_states)
        st.session_state["lru"] = (lru_faults, lru_states)
        st.session_state["opt"] = (opt_faults, opt_states)

    except:
        st.error("Invalid input! Please enter numbers like: 7,0,1,2")

# Display Results
if "fifo" in st.session_state:

    pages = st.session_state["pages"]
    fifo_faults, fifo_states = st.session_state["fifo"]
    lru_faults, lru_states = st.session_state["lru"]
    opt_faults, opt_states = st.session_state["opt"]

    st.subheader("Results")

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

    df = pd.DataFrame(data)

    st.subheader("Performance Metrics")
    st.table(df)

    # Graph
    st.subheader("Page Fault Comparison")

    chart_data = pd.DataFrame({
        "Algorithm": ["FIFO", "LRU", "Optimal"],
        "Page Faults": [fifo_faults, lru_faults, opt_faults]
    })

    st.bar_chart(chart_data.set_index("Algorithm"))

    # Memory Visualization
    algo_choice = st.selectbox(
        "Choose Algorithm to Visualize",
        ["FIFO", "LRU", "Optimal"]
    )

    if algo_choice == "FIFO":
        state_df = pd.DataFrame(fifo_states)
    elif algo_choice == "LRU":
        state_df = pd.DataFrame(lru_states)
    else:
        state_df = pd.DataFrame(opt_states)

    state_df.columns = [f"Frame{i+1}" for i in range(state_df.shape[1])]

    st.subheader(f"{algo_choice} Memory States")
    st.dataframe(state_df)
