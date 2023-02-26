import statistics

def median_avg_errors(values):
    try:
        median = round(statistics.median(values), 2)
    except statistics.StatisticsError:
        median = 0
    try:
        avg = round(sum(values) / len(values), 2)
    except ZeroDivisionError:
        avg = 0
    return median, avg