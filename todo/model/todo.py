class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed: bool = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            return self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"

    pass


class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        todo_id: int = len(self.todos) + 1
        new_todo: Todo = Todo(todo_id, title, description, completed=False, tags=[])
        self.todos[todo_id] = new_todo
        return todo_id

    def pending_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> dict[str, int]:
        tag_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return tag_count

    pass
