import pandas as pd

def load_data(file_path):
    """Загружает данные из файла CSV"""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Обрабатывает данные: чистка и расчет дополнительных метрик"""
    # Преобразование данных, заполнение пропусков
    df['conversion_rate'] = df['sales'] / df['visits']
    df['average_order_value'] = df['revenue'] / df['sales']
    return df

def aggregate_data(df):
    """Агрегирует данные по месяцам и каналам продаж"""
    df['date'] = pd.to_datetime(df['date'])
    return df.groupby(['channel', pd.Grouper(key='date', freq='M')]).sum().reset_index()
