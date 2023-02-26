import statistics

def median_avg_errors(values):
    try:
        median = round(statistics.median(values), 2)
    except statistics.StatisticsError:
        median = None
    try:
        avg = round(sum(values) / len(values), 2)
    except ZeroDivisionError:
        avg = None
    return median, avg