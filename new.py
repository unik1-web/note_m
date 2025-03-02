def collect_input_data(input_fields, field_prompts):
    """Collects input data from the user based on provided fields and prompts."""
    data_notes = {}
    for i, key in enumerate(input_fields):
        if i in [4, 5]:
            data_notes[key] = input(f'Введите {field_prompts[i]} {field_prompts[6]}: ')
        elif i == 1:
            data_notes[key] = []
            for j in range(1, 4):
                data_notes[key].append(input(f'Введите {field_prompts[i]} номер {j}: '))
        else:
            data_notes[key] = input(f'Введите {field_prompts[i]}: ')
    return data_notes

def display_data(field_prompts, data_notes):
    """Displays the collected data to the user."""
    print("\nВы ввели следующие данные:")
    for i, value in enumerate(data_notes.values()):
        print(field_prompts[i], value)

# Example Usage (assuming data_key and data_docs are defined elsewhere)
# For demonstration, let's define them here:
data_key = ['field1', 'field2', 'field3', 'field4', 'field5', 'field6']
data_docs = ['Описание 1', 'Описание 2', 'Описание 3', 'Описание 4', 'Описание 5', 'Описание 6', 'Описание 7']

input_data = collect_input_data(data_key, data_docs)
display_data(data_docs, input_data)

