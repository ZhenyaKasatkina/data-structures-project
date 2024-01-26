class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next_node = None         # следующий


class LinkedList:
    """Класс для односвязного списка.
    Хранит ссылки на первый и последний узлы списка."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.item_list = []

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и
        добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        node.next_node = self.head
        self.head = node
        if not self.tail:
            self.tail = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и
        добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if self.tail:
            self.tail.next_node = node
        self.tail = node

        if not self.head:
            self.head = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении
        для визуализации данных односвязного списка."""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()

    def to_list(self):
        """Возвращает список с данными,
        содержащимися в односвязном списке `LinkedList`"""
        node = self.head
        while node:
            self.item_list.append(node.data)
            node = node.next_node
        return self.item_list

    def get_data_by_id(self, value):
        """Возвращает первый найденный в
        `LinkedList` словарь с ключом 'id',
        значение которого равно переданному в метод значению."""

        for item in self.to_list():
            try:
                isinstance(item, dict)
                if item['id'] == value:
                    return item
            except (TypeError, KeyError):
                print("Данные не являются словарем или в словаре нет id")
            else:
                if item['id'] == value:
                    return item
