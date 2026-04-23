import random

def sequential_workload(n):
    """
    Generates sequential page references: 0 → n-1
    Example: n=5 → [0, 1, 2, 3, 4]
    """
    return list(range(n))


def looping_workload(cycles):
    """
    Repeats a fixed pattern multiple times.
    Example pattern: [1, 2, 3]
    """
    base_pattern = [1, 2, 3]
    return base_pattern * cycles


def random_workload(n, max_page):
    """
    Generates random page references between 0 and max_page.
    """
    return [random.randint(0, max_page) for _ in range(n)]


def locality_workload(n):
    """
    Simulates locality of reference:
    Reuses a small working set frequently.
    """
    base = [1, 2, 3, 4]
    result = base.copy()

    for _ in range(n - len(base)):
        result.append(random.choice(base))

    return result
