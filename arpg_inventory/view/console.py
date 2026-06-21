class ConsoleView:
    def show_menu(self):
        print("\n=== ARPG INVENTORY & TRADE MANAGER ===")
        print("1. Add Item to Stash (Добавить предмет в тайник)")
        print("2. Show All Items (Показать весь инвентарь)")
        print("3. Filter Items by Category (Фильтр по категории)")
        print("4. Get Last Looted Item (Показать последний выбитый лут)")
        print("5. Exit (Выйти)")
        return input("Select an option (1-5): ").strip()

    def get_item_input(self):
        print("\n--- Adding New Item ---")
        name = input("Enter item name (e.g., Chaos Orb, Leather Belt): ").strip()
        while not name:
            print("Error: Name cannot be empty!")
            name = input("Enter item name: ").strip()

        category = input("Enter category (Currency, Ring, Gloves, Weapon): ").strip()
        while not category:
            print("Error: Category cannot be empty!")
            category = input("Enter category: ").strip()

        # Валидация ввода для уникального ID (должно быть целым числом)
        while True:
            id_input = input("Enter unique Item ID (integer): ").strip()
            if id_input.isdigit():
                item_id = int(id_input)
                break
            print("Error: ID must be a positive number! Try again.")

        # Добавим одну базовую характеристику для простоты
        stat_name = input("Enter property name (e.g., cold_resistance, value_in_chaos): ").strip()
        
        # Валидация числового значения характеристики
        while True:
            stat_val_input = input(f"Enter value for {stat_name} (integer): ").strip()
            if stat_val_input.isdigit():
                stat_value = int(stat_val_input)
                break
            print("Error: Value must be a number! Try again.")

        properties = {stat_name: stat_value}
        return item_id, name, category, properties

    def show_items(self, items):
        if not items:
            print("\nYour stash is empty.")
            return
        print("\n--- Current Inventory ---")
        for item in items:
            print(item)

    def get_category_for_filter(self):
        return input("\nEnter category name to filter by (e.g., Currency): ").strip()

    def show_message(self, message):
        print(f"\n[INFO] {message}")