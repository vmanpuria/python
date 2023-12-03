import pandas

one: int = 1

#series
data0: list[int] = [one, 2, 3, 4, 5]
series = pandas.Series(data0)

print("series:\n", series)
print("type(series): ", type(series))
print("series.count(): ", series.count())

#dataframe
data: dict[str, list[int] or list[str]] = {
    "Column1": [1, 2, 3, 4],
    "Column2": ['A', 'B', 'C', 'D']
}
df = pandas.DataFrame(data)
print("\ndf:\n", df)
column1 = df["Column1"]
print("column1:\n", column1)
print("type(column1): ", type(column1))

row0 = df.iloc[0]
print("row0:\n", row0)
print("type(row0): ", type(row0))
cell0_0 = row0[0]
print("cell0_0: ", cell0_0)
print("type(cell0_0): ", type(cell0_0))

sliced_df = df[0:2]
print("sliced_df:\n", sliced_df)
print("type(sliced_df):", type(sliced_df))

row_0 = df.loc[0]
print("row_0:\n", row_0)
