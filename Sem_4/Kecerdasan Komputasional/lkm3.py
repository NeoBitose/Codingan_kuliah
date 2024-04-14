import pandas

df = pandas.read_csv('iris.csv')

Vlama = df[["sepal.length","sepal.width","petal.length","petal.width"]]
Vmin = Vlama.min()
Vmax = Vlama.max()

Vbaru = (Vlama-Vmin)/(Vmax-Vmin)
Vbaru = Vbaru.join(df['variety'])

print('SETOSA')
sepal_length_setosa = Vbaru[Vbaru.variety == 'Setosa'] ['sepal.length'].mean()
print("Sepal length : ", sepal_length_setosa)
sepal_width_setosa = Vbaru[Vbaru.variety == 'Setosa'] ['sepal.width'].mean()
print("Sepal width : ", sepal_width_setosa)
petal_length_setosa = Vbaru[Vbaru.variety == 'Setosa'] ['petal.length'].mean()
print("Petal length : ", petal_length_setosa)
petal_width_setosa = Vbaru[Vbaru.variety == 'Setosa']['petal.width'].mean()
print("Petal width : ", petal_width_setosa)

print('\nVERSICOLOR')
sepal_length_versicolor = Vbaru[Vbaru.variety == 'Versicolor'] ['sepal.length'].mean()
print("Sepal length : ", sepal_length_versicolor)
sepal_width_versicolor = Vbaru[Vbaru.variety == 'Versicolor']['sepal.width'].mean()
print("Sepal width : ", sepal_width_versicolor)
petal_length_versicolor = Vbaru[Vbaru.variety == 'Versicolor']['petal.length'].mean()
print("Petal length : ", petal_length_versicolor)
petal_widthversicolor = Vbaru[Vbaru.variety == 'Versicolor']['petal.width'].mean()
print("Petal width : ", petal_widthversicolor)

print('\nVIRGINICA')
sepal_length_virginica = Vbaru[Vbaru.variety == 'Virginica']['sepal.length'].mean()
print("Sepal length : ", sepal_length_virginica)
sepal_width_virginica = Vbaru[Vbaru.variety == 'Virginica']['sepal.width'].mean()
print("Sepal width : ", sepal_width_virginica)
petal_length_virginica = Vbaru[Vbaru.variety == 'Virginica']['petal.length'].mean()
print("Petal length : ", petal_length_virginica)
petal_widthvirginica = Vbaru[Vbaru.variety == 'Virginica']['petal.width'].mean()
print("Petal width : ", petal_widthvirginica)

# df = pandas.read_csv('iristesting.csv')
# print("Nilai data asli sebelum normalisasi \n", df)

# Vlama = df[["sepal.length","sepal.width","petal.length","petal.width"]]
# Vmin = Vlama.min()
# Vmax = Vlama.max()

# Vbaru = (Vlama-Vmin)/(Vmax-Vmin)
# Vbaru = Vbaru.join(df['variety'])
# print(Vbaru.to_string())


