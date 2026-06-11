# votacionAFK

Aplicación web de predicción de voto usando Machine Learning supervisado (Regresión Logística).

## Archivos

- `generate_data.py` — Genera dataset sintético con 200 filas (edad 15-80)
- `train.py` — Entrena un modelo de Regresión Logística con scikit-learn
- `app.py` — App Flask con interfaz web dark mode
- `requirements.txt` — flask, scikit-learn, pandas, joblib
- `modelo_voto.pkl` — Modelo entrenado

## Uso

```bash
pip install -r requirements.txt
python generate_data.py
python train.py
python app.py
```
