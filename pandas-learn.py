import numpy
import pandas
import pandas as pd

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
    "Column2": ['A', 'B', 'C', 'D'],
    "Column3": [numpy.NaN, 'two', 'three', 'four'],
    "Column4": [40, 20, 30, 20]
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

mean = df["Column1"].mean()
print("mean: ", mean)
print("\ndf:\n", df)
print("df.dropna(axis=1):\n", df.dropna(axis=1))

value_to_fill = df["Column3"].mode()
print("type(value_to_fill):", type(value_to_fill))
print("len(value_to_fill):", len(value_to_fill))
print("value_to_fill:", value_to_fill)
print("value_to_fill[0]:", value_to_fill[0])

print("df['Column3']:", df["Column3"])
print("df['Column3'].fillna(value_to_fill[0]):", df["Column3"].fillna(value_to_fill[0]))
print("df:", df)

print("df.sort_values:", df.sort_values(by="Column4"))
print("df.sort_values:", df.sort_values(by=["Column4", "Column1"], ascending=[True, True]))

print("df['Column2'].replace:", df["Column2"].replace("A", "E"))
print("df['Column1'].apply:", df["Column1"].apply(lambda x : x + 2))

df["Column5"] = df["Column4"] / df["Column1"]
print("df['Column5']:", df["Column5"])

# todo
grouped_df = df.groupby("Column4")
print("type(grouped_df):", type(grouped_df))
print("df.describe:\n", df.describe())
for key, value in grouped_df:
    print("key:", key)
    print("type(value):", type(value), " type(key):", type(key))
    print(value.reset_index())
    # print(grouped_df.get_group(key))

grouped_s = df.groupby("Column4")["Column1"]
print("type(grouped_s):\n", type(grouped_s))
print("grouped_s:\n", grouped_s)
for key, value in grouped_s:
    print("key:", key)
    print("type(value):", type(value), " type(key):", type(key))
    print(value.reset_index())
    # print(grouped_s.get_group(key))

grouped_mean = grouped_s.mean()
print("type(grouped_mean):\n", type(grouped_mean))
print("grouped_mean:\n", grouped_mean)
print("grouped_mean.reset_index:\n", grouped_mean.reset_index())
print("type(grouped_mean.reset_index):\n", type(grouped_mean.reset_index()))

s = pd.Series([1,2])
print("Series s.rename():", s.rename(index={0: "zero", 1: "one"}))

# for key, value in grouped_mean:
#     print("key:", key)
#     print("type(value):", type(value), " type(key):", type(key))
#     print(value.reset_index())

products = {
    "id": [1, 2, 3, 4],
    "name": ["one", "two", "three", "four"],
    "category": ["food", "health", "beauty", "food"]
}

product_ratings = {
    "id": [1, 2, 3, 4],
    "ratings": [5, 4, 5, 3],
    "comments": ["great", "A+", "super", "yummy"]
}

print("df.rename(index):\n", df.rename(index={0: "one", 1: "two", 2: "three", 3: "four"}))
print("df.rename(index, column):\n", df.rename(index={0: "one", 1: "two", 2: "three", 3: "four"}, columns={"Column1": "one", "Column2": "two", "Column3": "three", "Column4": "four", "Column5": "five"}))

product_df = pd.DataFrame(products)
product_ratings_df = pd.DataFrame(product_ratings)
merged_df = product_df.merge(product_ratings_df)
joined_df = product_df.merge(product_ratings_df, on="id")
#
print("merged_df:", merged_df)
print("joined_df:", joined_df)

food_df = merged_df[merged_df["category"] == "food"]
print("food_df:", food_df["ratings"])
print("food_df['ratings']:", food_df["ratings"])
print("food_df['ratings'].mean:", food_df["ratings"].mean())

print("merged_df_mean:\n", merged_df.groupby("category")["ratings"].mean().reset_index().rename(columns={"ratings":"avg_ratings"}))

df = pd.DataFrame({
    'user_id': ['4235', '2342', '1234', '5325', '1342'],
    'gender': ['F', 'F', 'F', 'M', 'M'],
    'total_order': [15, 13, 13, 12, 14]
})

print("df:\n", df)
print("df_average_num_orders by gender:\n", df.groupby("gender")["total_order"].mean().reset_index().rename(columns={"total_order": "average_num_orders"}))

csv_url = "https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv"
titanic = pd.read_csv(csv_url)
print("titanic.head():\n", titanic.head())
titanic_a = titanic.head()
titanic_b = titanic.tail()
print("concatenated titanic:\b", pd.concat([titanic_a, titanic_b], axis=0))