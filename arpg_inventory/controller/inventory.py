import json
import os
import sys

# Добавляем путь, чтобы Python увидел папку model
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.item import Item

class InventoryController:
    def __init__(self):
        self.items = []              # Главный список всех предметов
        self.loot_history = []       # Стек для истории лута
        self.filepath = "data.json"  # Файл для сохранения базы данных

    def add_item(self, item):
        self.items.append(item)
        # Добавляем название предмета в стек (наверх)
        self.loot_history.append(item.name)
        self.save_data()

    def get_last_looted(self):
        # Достаем последний добавленный предмет из стека
        if len(self.loot_history) > 0:
            return self.loot_history.pop()
        return "History is empty."

    def filter_by_category(self, category_name):
        # Фильтрация списка по категории
        filtered_list = []
        for item in self.items:
            if item.category.lower() == category_name.lower():
                filtered_list.append(item)
        return filtered_list

    def save_data(self):
        # Превращаем объекты в словари и сохраняем в JSON
        print(f"DEBUG: Saving to {os.path.abspath(self.filepath)}")

        data_to_save = []
        for item in self.items:
            data_to_save.append(item.to_dict())
            
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, indent=4)

    def load_data(self):
        # Загружаем предметы из файла, если он существует
        if not os.path.exists(self.filepath):
            return

        with open(self.filepath, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                self.items = []
                for item_data in data:
                    item_object = Item.from_dict(item_data)
                    self.items.append(item_object)
            except json.JSONDecodeError:
                # Если файл пустой или сломан
                self.items = []