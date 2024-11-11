from sqlalchemy import select, func
from models import session, Customers, LoyaltyCards, Products, Orders, Transactions

# Функція для відображення всіх даних з таблиці
def view_table_data(table):
    stmt = select(table)
    result = session.execute(stmt)
    for row in result:
        print(row)

# JOIN-запит для об'єднання даних з таблиць Orders, Customers і Transactions
def get_orders_with_transactions():
    stmt = select(
        Orders.c.OrderID,
        Customers.c.Name,
        Orders.c.TotalAmount,
        Transactions.c.PointsEarned
    ).select_from(
        Orders.join(Customers, Orders.c.CustomerID == Customers.c.CustomerID).
        join(Transactions, Orders.c.OrderID == Transactions.c.OrderID)
    )
    result = session.execute(stmt)
    for row in result:
        print(row)


def get_high_value_orders(min_amount):
    stmt = select(Orders).where(Orders.c.TotalAmount > min_amount)
    result = session.execute(stmt)
    for row in result:
        print(row)

# Агрегатна функція для підрахунку загальної кількості бонусних балів
def get_total_bonus_points():
    stmt = select(func.sum(LoyaltyCards.c.BonusPoints))
    result = session.execute(stmt).scalar()
    print(f"Загальна кількість бонусних балів: {result}")

# Меню для вибору операцій
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Показати всі клієнти")
        print("2. Показати всі бонусні картки")
        print("3. Показати всі товари")
        print("4. Показати всі замовлення")
        print("5. Показати замовлення та транзакції")
        print("6. Показати замовлення з сумою більше 10")
        print("7. Загальна кількість бонусних балів")
        print("0. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            view_table_data(Customers)
        elif choice == '2':
            view_table_data(LoyaltyCards)
        elif choice == '3':
            view_table_data(Products)
        elif choice == '4':
            view_table_data(Orders)
        elif choice == '5':
            get_orders_with_transactions()
        elif choice == '6':
            get_high_value_orders(10)
        elif choice == '7':
            get_total_bonus_points()
        elif choice == '0':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
