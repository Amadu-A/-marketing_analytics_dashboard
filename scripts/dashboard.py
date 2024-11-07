import pandas as pd

def load_data(filepath):
    """Загружает данные из CSV файла."""
    return pd.read_csv(filepath)

def preprocess_data(data):
    """Проводит предварительную обработку данных."""
    # Добавьте логику очистки и преобразования данных, если необходимо
    data['date'] = pd.to_datetime(data['date'])
    return data

def aggregate_data(data):
    """Агрегирует данные для построения отчетов."""
    return data.groupby(['channel', 'date']).agg(
        total_visits=('visits', 'sum'),
        total_sales=('sales', 'sum'),
        total_revenue=('revenue', 'sum'),
        avg_conversion_rate=('sales', 'mean')
    ).reset_index()
