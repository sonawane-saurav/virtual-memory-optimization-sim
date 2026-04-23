def compare_algorithms(results, pages):
    """
    Computes performance metrics for each algorithm.

    Args:
        results (dict): {
            "FIFO": faults,
            "LRU": faults,
            "Optimal": faults
        }
        pages (list): page reference string

    Returns:
        dict:
        {
            "FIFO": {
                "page_faults": int,
                "hits": int,
                "fault_rate": float,
                "hit_rate": float
            },
            ...
        }
    """

    total_requests = len(pages)
    comparison = {}

    for algo, faults in results.items():
        hits = total_requests - faults

        fault_rate = faults / total_requests if total_requests > 0 else 0
        hit_rate = hits / total_requests if total_requests > 0 else 0

        comparison[algo] = {
            "page_faults": faults,
            "hits": hits,
            "fault_rate": fault_rate,
            "hit_rate": hit_rate
        }

    return comparison
