def optimal(pages, frames):
    memory = []
    page_faults = 0
    history = []

    for i in range(len(pages)):
        page = pages[i]

        if page not in memory:
            page_faults += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                future = pages[i+1:]
                index_to_replace = -1
                farthest = -1

                for j in range(len(memory)):
                    if memory[j] not in future:
                        index_to_replace = j
                        break
                    else:
                        idx = future.index(memory[j])
                        if idx > farthest:
                            farthest = idx
                            index_to_replace = j
                memory[index_to_replace] = page
                
        history.append(memory.copy())

    return page_faults, history