import pandas as pd

def generate_sales_report(df):
    """Создает отчет по продажам с ключевыми показателями"""
    report = df.groupby('channel').agg(
        total_visits=pd.NamedAgg(column='visits', aggfunc='sum'),
        total_sales=pd.NamedAgg(column='sales', aggfunc='sum'),
        total_revenue=pd.NamedAgg(column='revenue', aggfunc='sum'),
        avg_conversion_rate=pd.NamedAgg(column='conversion_rate', aggfunc='mean'),
        avg_order_value=pd.NamedAgg(column='average_order_value', aggfunc='mean')
    )
    return report

def save_report(report, file_path):
    """Сохраняет отчет в Excel"""
    report.to_excel(file_path)
