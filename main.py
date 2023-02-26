# import re
# import sys
#
# # можно заказать максимум 5 штук (доставщик не довезет больше за один заказ)
# max_pizzas = 5
# # Оплата в USD
# delivery_charge = 3.00
# # Перечень пиццы
# pizzas_available = (
#     {"name": "BBQ",             "price": 15},
#     {"name": "Seafood",          "price": 12},
#     {"name": "Pepperoni",            "price": 10},
#
# )
#
# # Определяет исключение
# class CancelOrder(Exception):
#     pass
#
# # детали заказа
# class Order():
#     def __init__(self):
#         self.pickup = True
#
#         self.name = ""
#         self.address = None
#         self.phone = None
#
#         self.number_pizzas = 0
#         self.pizzas = []
#
#         self.total_cost = 0
#
#
# def get_input(regex, input_message=None, error_message=None, ignore_case=True):
#     """Gets valid input, validated using regular expressions."""
#     while True:
#         # ввод для проверки
#         u_input = input(str(input_message))
#
#         lower = u_input.lower()
#         if lower == "q" or lower == "quit":
#             sys.exit()
#         elif u_input == "c" or u_input == "cancel":
#             raise CancelOrder()
#
#         if ignore_case:
#             if re.match(regex, u_input, re.IGNORECASE):
#                 break
#         else:
#             if re.match(regex, u_input):
#                 break
#
#         if error_message:
#             print(str(error_message))
#
#     return u_input
#
#
# def print_order(order):
#     print("| Name: {}".format(order.name))
#     print("| Order type: {}".format("Pickup" if order.pickup else "Delivery"))
#     if not order.pickup:
#         print("| Адрес доставки: {}".format(order.address))
#         print("| Номер телефона клиента: {}".format(order.phone))
#     print("|\n| Описание заказа:\t\t\t\tPrice each:\tSubtotal:")
#     for pizza in order.pizzas:
#         print("| \t{}x {:<22}\t${:<6.2f}\t\t${:>5.2f}".format(
#             pizza['amount'], pizza['name'],
#             pizza['price'], pizza['price']*pizza['amount']))
#
#     if not order.pickup:
#             print("| \tDelivery charge\t\t\t\t\t$ {:>5.2f}".format(
#                 delivery_charge))
#     print("| {:61}--------".format(""))
#     print("| {:54} Total: ${:.2f}".format("", order.total_cost))
#
#
# print("Кафе Три пиццы")
# print("Администратор")
# print("Введите 'C' чтобы отменить заказ, или 'Q' чтобы выйти из программы")
# print("В качестве вводных данных достаточно ввести одну букву")
# print("Слово в скобках [] - по умолчанию")
#
#
# orders = []
#
# # сортировка пиццы по цене
# pizzas_available = sorted(
#     pizzas_available,
#     key=lambda k: (k["price"], k["name"]))
#
# while True:
#     try:
#         print("\nНовый заказ")
#         order = Order()
#
#         user_input = get_input(
#             r"$|(?:P|D)",
#             "В кафе или с собой?:",
#             "Введите a 'p' (в кафе) or a 'd' (доставка)")
#         if user_input.lower().startswith("d"):
#             order.pickup = False
#
#         order.name = get_input(
#             r"[A-Z]+$",
#             "Введите имя клиента:",
#             "Имя должно содержать только буквы")
#
#         if not order.pickup:
#             order.address = get_input(
#                 r"[ -/\w]+$",
#                 "Адрес доставки:",
#                 "Адрес должен содержать и буквы и цифры (либо только буквы)")
#             order.phone = get_input(
#                 r"\d+$",
#                 "Номер телефона:",
#                 "Номер телефона должен содержать только цифры")
#
#         while True:
#             user_input = get_input(
#                 r"\d$",
#                 "Номер пиццы в заказе:",
#                 "Заказ должен быть более или равен 5 штукам")
#             user_input = int(user_input)
#             if 0 < user_input <= max_pizzas:
#                 order.number_pizzas = user_input
#                 break
#             else:
#                 print("Заказ должен быть больше 5 пиц или равен 0")
#
#
#         print("\nКакую пиццу хотите заказать?")
#         for i, pizza in enumerate(pizzas_available):
#
#             print("{}: {}".format(str(i+1).zfill(2), pizza['name']))
#
#         print("\nEnter your selection number for each pizza you want to buy")
#         for i in range(order.number_pizzas):
#             while True:
#                 string = "Pizza #{} of {}:".format(i+1, order.number_pizzas)
#                 user_input = get_input(
#                     r"\d\d?$",
#                     string,
#                     "Pizza selection number must"
#                     "correspond to those listed above")
#                 user_input = int(user_input)
#                 try:
#                     if user_input == 0:
#                         raise IndexError
#
#                     to_add = pizzas_available[user_input-1]
#
#                     for ordered in order.pizzas:
#                         if to_add["name"] == ordered["name"]:
#                             ordered["amount"] += 1
#                             break
#
#                     else:
#                         order.pizzas.append(to_add)
#                         order.pizzas[-1]["amount"] = 1
#
#                     break
#
#                 except IndexError:
#                     print("Pizza selection number must"
#                         "correspond to those listed above")
#
#         order.total_cost = sum(
#             pizza["price"]*pizza["amount"]
#             for pizza in order.pizzas)
#         if not order.pickup:
#                 order.total_cost += delivery_charge
#
#         # добавить заказ в лист заказов
#         orders.append(order)
#         print("\nOrder saved. Order was:")
#         print_order(order)
#
#         user_input = get_input(
#             r"$|(?:Y|N|O).*",
#             "Would you like to enter another order or view all"
#                 "previous orders? [Yes]/No/Orders:",
#             "Only yes/no or \"orders\" responses allowed")
#         if user_input.lower().startswith("o"):
#             for i, order in enumerate(orders):
#                 print("-" * 73)
#                 print_order(order)
#                 if i == len(orders) + 1:
#                     print("-" * 73)
#         elif user_input.lower().startswith("n"):
#             sys.exit()
#
#     except CancelOrder:
#         try:
#             print("\nЗаказ отменен")
#             user_input = get_input(
#                 r"$|(?:Y|N).*",
#                 "Would you like to enter another order? [Yes]/No",
#                 "Only yes or no responses allowed")
#             if user_input.lower().startswith("n"):
#                 sys.exit()
#
#         except CancelOrder:
#             print("Type 'Q' to exit the program")