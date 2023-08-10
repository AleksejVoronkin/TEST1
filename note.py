import json
import datetime

class Note:
    def __init__(self, id, title, body, created_at, modified_at):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.modified_at = modified_at

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, default=lambda obj: obj.__dict__)

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes_data = json.load(file)
            notes = []
            for note_data in notes_data:
                note = Note(
                    note_data['id'],
                    note_data['title'],
                    note_data['body'],
                    note_data['created_at'],
                    note_data['modified_at']
                )
                notes.append(note)
            return notes
    except FileNotFoundError:
        return []

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modified_at = created_at
    note = Note(len(notes) + 1, title, body, created_at, modified_at)
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def edit_note():
    note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    for note in notes:
        if note.id == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            note.title = new_title
            note.body = new_body
            note.modified_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note.id == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

def list_notes():
    date_filter = input("Введите дату для фильтрации заметок (гггг-мм-дд) или оставьте поле пустым для просмотра всех заметок: ")
    filtered_notes = [note for note in notes if note.created_at[:10] == date_filter] if date_filter else notes
    print("Список заметок:")
    for note in filtered_notes:
        print(f"ID: {note.id}")
        print(f"Заголовок: {note.title}")
        print(f"Тело: {note.body}")
        print(f"Дата создания: {note.created_at}")
        print(f"Дата последнего изменения: {note.modified_at}")
        print()

notes = load_notes()

while True:
    command = input("Введите команду (add, edit, delete, list, exit): ")
    if command == "add":
        add_note()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "list":
        list_notes()
    elif command == "exit":
        break
    else:
        print("Некорректная команда")

print("Выход из программы")