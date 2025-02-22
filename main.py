# СТЕК
# Создание пустого стека
stack = []
# Добавление элементов в стек
stack.append(1)
stack.append(2)
stack.append(3)
print("Стек после добавления элементов:", stack)
# Удаление элемента из стека (извлекается последний добавленный)
top = stack.pop()
print("Извлечённый элемент:", top)
print("Стек после удаления элемента:", stack)

# ОЧЕРЕДЬ
class Queue:
    def __init__(self):
        self.queue = []  # Инициализация пустого списка для хранения элементов очереди
    def enqueue(self, item):
        """Добавление элемента в конец очереди"""
        self.queue.append(item)
    def dequeue(self):
        """Удаление элемента из начала очереди. Если очередь пуста, генерирует исключение."""
        if self.is_empty():
            raise Exception("Очередь пуста")
        return self.queue.pop(0)
    def is_empty(self):
        """Проверка, пуста ли очередь"""
        return len(self.queue) == 0
    def size(self):
        """Возвращает количество элементов в очереди"""
        return len(self.queue)
# Пример использования:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Очередь после добавления элементов:", q.queue)
    dequeued_item = q.dequeue()
    print("Извлечённый элемент:", dequeued_item)
    print("Очередь после извлечения элемента:", q.queue)

# ГРАФ
# Представление графа в виде списка смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# Функция обхода графа в глубину (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
print("Обход графа в глубину (DFS):")
dfs(graph, 'A')
print()  # для перевода строки

# ДЕРЕВО
# Определение класса для узла дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Создание простого бинарного дерева:
#         1
#        / \
#       2   3
#      / \
#     4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# Функция для обхода дерева в порядке in-order
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)
print("Обход бинарного дерева (in-order):")
inorder_traversal(root)
print()  # для перевода строки



