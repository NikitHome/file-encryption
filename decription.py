import pyAesCrypt
import os

# функция дешифрования файла
def decryption(file, password):
    # задаем размер буфера
    buffer_size = 512 * 1024
    
    # вызов метода дешифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
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
        # если нашли директорию - дешифруем ее
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else: # в случае НЕ нахождения директории продолжаем сканировать
            walking_by_dirs(path, password)
            
password = input("Введите пароль для шифрования: ")
walking_by_dirs("", password)