from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def forecast_sales(df, forecast_period=3):
    """Прогнозирует продажи на основе линейной регрессии"""
    df['date_ordinal'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
    model = LinearRegression()

    # Подготовка данных для модели
    X = np.array(df['date_ordinal']).reshape(-1, 1)
    y = df['revenue']

    model.fit(X, y)

    future_dates = np.array(
        [df['date_ordinal'].max() + i * 30 for i in range(1, forecast_period + 1)]
    ).reshape(-1, 1)
    predictions = model.predict(future_dates)

    return predictions
