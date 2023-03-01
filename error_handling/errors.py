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

def file_reading_value_errors(value):
    try:
        value = float(value)
        return value
    except ValueError:
        pass


# def numpy_errors(slope, intercept):
#     try:
#         slope, intercept = np.polyfit(league_levels, values, 1)
