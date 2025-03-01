data_notes = {
    'username': 'Ivanov', 'title': 'Zametka', 'content': 'Kupit tetrad',
    "status": 'в работе', 'created_date': "10-11-2024", 'issue_date': "10-12-2024"
}
data_docs = (
    'Имя пользователя', 'Заголовок заметки', 'Описание заметки',
    'Статус заметки', 'Дата создания заметки', 'Дата истечения заметки'
)

for i, value in enumerate(data_notes.values()):
    print(data_docs[i], value)

