import pandas as pd
import random

random.seed(42)
data = []
for _ in range(200):
    edad = random.randint(15, 80)
    puede_votar = 1 if edad >= 18 else 0
    data.append([edad, puede_votar])

df = pd.DataFrame(data, columns=["edad", "puede_votar"])
df.to_csv("voting_data.csv", index=False)
print("voting_data.csv generado con 200 filas.")
