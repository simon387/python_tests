from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

giocatori = read_csv('giocatori.csv')
X = giocatori.drop(columns=['videogame'])
y = giocatori['videogame']

modello = DecisionTreeClassifier()
modello.fit(X.values, y.values)
previsione = modello.predict([[0,31], [1,16]])
print(previsione)