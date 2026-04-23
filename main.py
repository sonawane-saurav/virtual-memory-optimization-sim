'''
from core.fifo import fifo

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

faults, history = fifo(pages, frames)

print("Page Faults:", faults)
print("Memory States:")

for step in history:
    print(step)
'''


'''
from core.lru import lru

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

faults, history = lru(pages, frames)

print("\nLRU Page Faults:", faults)
for step in history:
    print(step)
'''


'''
from core.optimal import optimal

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

faults, history = optimal(pages, frames)

print("\nOptimal Page Faults:", faults)
for step in history:
    print(step)
'''

'''
from core.fifo import fifo
from core.lru import lru
from core.optimal import optimal
from core.metrics import compare_algorithms

pages = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3

fifo_faults, _ = fifo(pages, frames)
lru_faults, _ = lru(pages, frames)
opt_faults, _ = optimal(pages, frames)

results = {
    "FIFO": fifo_faults,
    "LRU": lru_faults,
    "Optimal": opt_faults
}

comparison = compare_algorithms(results, pages)

print("\nCOMPARISON")
for algo, data in comparison.items():
    print(f"\n{algo}:")
    for key, value in data.items():
        print(f"{key}: {value}")
'''


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
