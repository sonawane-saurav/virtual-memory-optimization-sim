import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from core.simulator import fifo, lru, optimal
from core.metrics import compare_algorithms

# Title
st.title("Virtual Memory Optimization Simulator")
