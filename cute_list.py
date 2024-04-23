'''Программа для разделения ссылок в файле'''
# Открываем исходный файл для чтения
with open("output.txt", "r") as input_file:
    # Читаем все строки из исходного файла
    lines = input_file.readlines()

    # Определяем количество строк в каждом файле
    chunk_size = 20

    # Разбиваем строки на части по chunk_size
    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]

    # Записываем каждую часть в отдельный файл
    for i, chunk in enumerate(chunks):
        with open(f"output_file_{i+1}.txt", "w") as output_file:
            output_file.writelines(chunk)
