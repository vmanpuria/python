import pandas

one: int = 1

data: list[int] = [one, 2, 3, 4, 5]
series = pandas.Series(data)

print(series)
