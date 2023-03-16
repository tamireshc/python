from src.track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    qtd_inventory_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
            }

    def __init__(self):
        self.tracKOrdersInstance = TrackOrders()
        self.MINIMUM_INVENTORY_COPY = self.MINIMUM_INVENTORY.copy()
        self.qtd_inventory_to_buy_COPY = self.qtd_inventory_to_buy.copy()

    def add_new_order(self, customer, order, day):
        for item in self.INGREDIENTS[order]:
            if self.MINIMUM_INVENTORY_COPY[item] == 0:
                return False
            else:
                self.MINIMUM_INVENTORY_COPY[item] -= 1
                self.qtd_inventory_to_buy_COPY[item] += 1

            self.tracKOrdersInstance.add_new_order(customer, order, day)

    def get_quantities_to_buy(self):
        return self.qtd_inventory_to_buy_COPY

    def get_available_dishes(self):
        available_dishes = set(self.INGREDIENTS.keys())
        for dish in self.INGREDIENTS.items():
            for item in dish[1]:
                if self.MINIMUM_INVENTORY_COPY[item] == 0:
                    available_dishes.discard(dish[0])
        return available_dishes
