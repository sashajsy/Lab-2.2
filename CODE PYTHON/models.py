from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Підключення до існуючої бази даних SQLite
engine = create_engine('sqlite:///loyalty_system1.db')

# Рефлектування для автоматичного завантаження існуючих таблиць
metadata = MetaData()
metadata.reflect(bind=engine)

# Отримуємо посилання на таблиці з існуючої бази даних
Customers = metadata.tables['Customers']
LoyaltyCards = metadata.tables['LoyaltyCards']
Products = metadata.tables['Products']
Orders = metadata.tables['Orders']
Transactions = metadata.tables['Transactions']

# Створення сесії для роботи з базою даних
Session = sessionmaker(bind=engine)
session = Session()
