class TrackOrders:
    # aqui deve expor a quantidade de estoque

    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dish_qtd_request = {}
        for item in self.orders:
            if item[0] == customer:
                if item[1] not in dish_qtd_request:
                    dish_qtd_request[item[1]] = 1
                else:
                    dish_qtd_request[item[1]] += 1
        return max(dish_qtd_request, key=dish_qtd_request.get)

    def get_never_ordered_per_customer(self, customer):
        exist_dishes = set()
        dishes_ordered_by_customer = set()

        for item in self.orders:
            exist_dishes.add(item[1])

        for item in self.orders:
            if item[0] == customer:
                dishes_ordered_by_customer.add(item[1])
        return exist_dishes - dishes_ordered_by_customer

    def get_days_never_visited_per_customer(self, customer):
        available_days = set()
        days_customer_go_to_snake_bar = set()

        for item in self.orders:
            available_days.add(item[2])

        for item in self.orders:
            if item[0] == customer:
                days_customer_go_to_snake_bar.add(item[2])
        return available_days - days_customer_go_to_snake_bar

    def get_busiest_day(self):
        person_per_day = {}
        for item in self.orders:
            if not item[2] in person_per_day:
                person_per_day[item[2]] = 1
            elif item[2] in person_per_day:
                person_per_day[item[2]] += 1
        return max(person_per_day, key=person_per_day.get)

    def get_least_busy_day(self):
        person_per_day = {}
        for item in self.orders:
            if not item[2] in person_per_day:
                person_per_day[item[2]] = 1
            elif item[2] in person_per_day:
                person_per_day[item[2]] += 1
        return min(person_per_day, key=person_per_day.get)
