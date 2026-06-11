import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("voting_data.csv")
X = df[["edad"]]
y = df["puede_votar"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "modelo_voto.pkl")
print("Modelo entrenado y guardado como modelo_voto.pkl")
