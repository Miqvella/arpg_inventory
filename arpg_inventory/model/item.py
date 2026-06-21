class Item:
    def __init__(self, item_id, name, category, properties):
        self.item_id = item_id          # Уникальный номер предмета
        self.name = name                # Название (например "Сфера Хаоса")
        self.category = category        # Например ("Валюта", "Кольцо", "Перчатки")
        self.properties = properties    # Характеристики (словарь: {"сопротивление_холоду": 34, "интеллект": 15})

    # Метод для подготовки к сохранению в файл (JSON)
    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "properties": self.properties
        }
    # Метод для загрузки предмета из файла (JSON)
    @classmethod
    def from_dict(cls, data):
        return cls(
            item_id=data["item_id"],
            name=data["name"],
            category=data["category"],
            properties=data["properties"]
        )
    # То как предмет будет красиво выглядеть на экране
    def __str__(self):
        return f"[{self.category}] {self.name} | Статы: {self.properties}"