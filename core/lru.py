def lru(pages, frames):
    memory = []
    recent = []                                     
    page_faults = 0
    history = []
