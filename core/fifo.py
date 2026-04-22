def fifo(pages, frames):
    memory = []                                 # current pages in frames
    queue = []                                  # to track FIFO order
    page_faults = 0                             # page fault count
    history = []                                # stores memory state step-by-step

    for page in pages:
        if page not in memory:                  # PAGE FAULT
            page_faults += 1
        
            if len(memory) < frames:
                memory.append(page)
                queue.append(page)
            else:
                oldest = queue.pop(0)           # memory is not sufficient, remove the oldest one
                memory.remove(oldest)

                memory.append(page)             # add the new page
                queue.append(page)

        history.append(memory.copy())

    return page_faults, history