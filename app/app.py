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
