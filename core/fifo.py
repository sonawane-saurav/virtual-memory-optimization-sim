def fifo(pages, frames):
    memory = []                                 # current pages in frames
    queue = []                                  # to track FIFO order
    page_faults = 0                             # page fault count
    history = []                                # stores memory state step-by-step

    