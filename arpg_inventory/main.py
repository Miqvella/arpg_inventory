import sys
import os

from model.item import Item
from controller.inventory import InventoryController
from view.console import ConsoleView

def main():
    controller = InventoryController()
    view = ConsoleView()

    # Загружаем сохраненный лут из файла data.json при старте программы
    controller.load_data()
    view.show_message("Inventory loaded successfully from data.json.")

    while True:
        choice = view.show_menu()

        if choice == "1":
            # 1. Добавление предмета
            item_id, name, category, properties = view.get_item_input()
            new_item = Item(item_id, name, category, properties)
            controller.add_item(new_item)
            view.show_message(f"Item '{name}' added to stash and saved!")

        elif choice == "2":
            # 2. Показ всех предметов
            view.show_items(controller.items)

        elif choice == "3":
            # 3. Фильтрация
            category = view.get_category_for_filter()
            filtered = controller.filter_by_category(category)
            view.show_items(filtered)

        elif choice == "4":
            # 4. Проверка стека (последний добавленный лут)
            last_item = controller.get_last_looted()
            print(f"\nLast looted item from history stack: {last_item}")

        elif choice == "5":
            # 5. Выход
            view.show_message("Exiting program. GG!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()