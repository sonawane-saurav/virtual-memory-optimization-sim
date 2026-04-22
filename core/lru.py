def lru(pages, frames):
    memory = []
    recent = []                                     
    page_faults = 0
    history = []

    for page in pages:
        if page in memory:                          # HIT, update recent usage
            recent.remove(page)
            recent.append(page)
        else:                                       # PAGE FAULT
            page_faults += 1

            if len(memory) < frames:
                memory.append(page)
                recent.append(page)
            else:
                lru_page = recent.pop(0)
                memory.remove(lru_page)

                memory.append(page)
                recent.append(page)
        
        history.append(memory.copy())

    return page_faults, history
