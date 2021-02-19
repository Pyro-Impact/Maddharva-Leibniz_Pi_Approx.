def approxpi(series):
    result = 0
    for i in range(1, series + 1):
        result += ((-1) ** (i - 1)) / (2 * i - 1)
    return result * 4


print(approxpi(380000))
# requires around 380000 iterations to get the first 5 digits of pi after the decimal correct.
