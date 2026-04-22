'''
Hits = Total Pages - Page Faults
Fault Rate = Page Faults / Total Pages
Hit Rate = Hits / Total Pages
'''

def calculate_metrics(pages, page_faults):
    total = len(pages)
    hits = total - page_faults

    fault_rate = page_faults / total
    hit_rate = hits / total

    return {
        "total_pages" : total,
        "page_faults" : page_faults,
        "hits" : hits,
        "fault_rate" : fault_rate,
        "hit_rate" : hit_rate
    }

def compare_algorithms(results, pages):
      comparison = {}

    for name, faults in results.items():
        comparison[name] = calculate_metrics(pages, faults)

    return comparison
