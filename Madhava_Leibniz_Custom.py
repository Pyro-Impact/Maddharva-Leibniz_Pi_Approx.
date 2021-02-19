def approxpi(series):
    result = 1
    for i in range(0, series + 1):
        result = result - (1 / (3 + 4 * i)) + (1 / (5 + 4 * i))
    return result * 4


print(approxpi(69000))
# requires around 69000 iterations to get the first 5 digits of pi after the decimal correct.
