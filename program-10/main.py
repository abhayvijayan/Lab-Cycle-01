import pandas as pd

data = {
    "Name" : ["Abhay", "Arun", "Nandu", "Ardra", "Krishna"],
    "Marks" : [80, 72, 79, 82, 77],
    "Age" : [21, 20, 23, 21, 21]
}

df = pd.DataFrame(data)
print(df)

# Access Data using key
print("Names Column : \n", df['Name'])

# Access using loc
print("\n First Row : ")
print(df.loc[0])

# Access specific rows using iloc
print("\n First two Rows : ")
print(df.iloc[0:2])

# Add new Column
df['Grade'] = ['A', 'B', 'A', 'B', 'C']
print("updated DF : \n", df)

# Modify values in a column
df['Marks'] = df['Marks'] + 5
print("\nUpdated DF : ")
print(df)

# Filter Rows
print("\nStudents with mark >= 80")
print(df[df["Marks"] >= 80])

# Delete a column
df = df.drop(columns=['Grade'])

print("\nAfter removing column")
print(df)