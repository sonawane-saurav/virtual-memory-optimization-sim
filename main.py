from core.fifo import fifo
from core.lru import lru
from core.optimal import optimal
from core.metrics import compare_algorithms
print("\nFrame Variation")

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frame_sizes = [2, 3, 4, 5]

for f in frame_sizes:
    fifo_faults, _ = fifo(pages, f)
    lru_faults, _ = lru(pages, f)
    opt_faults, _ = optimal(pages, f)

    print(f"\nFrames = {f}")
    print(f"FIFO: {fifo_faults}, LRU: {lru_faults}, Optimal: {opt_faults}")