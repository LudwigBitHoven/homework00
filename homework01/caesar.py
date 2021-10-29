import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ''
    for i in text:
        if i.isalpha():
            #Если shift выходит за пределы алфавита в большую сторону (с учетом регистров)
            #shift % 26 позволяет работать со сдвигом превышающим длину латинского алфавита
            if ord(i) + shift % 26 > 122 and i.islower() or ord(i) + shift % 26 > 90 and i.isupper():
                ciphertext += chr(ord(i) + shift % 26 - 26)
            #Если shift выходит за пределы алфавита в меньшую сторону (с учетом регистров)
            elif shift < 0 and (ord(i) + shift % 26 < 97 and i.islower() or ord(i) + shift % 26 < 65 and i.isupper()):
                ciphertext += chr(ord(i) + shift % 26 + 26)
            #Если shift в пределах алфавита - занести в результативную строку
            else:
                ciphertext += chr(ord(i) + shift % 26)
        #Если символ не буква - занести в результативную строку
        else:
            ciphertext += chr(ord(i))
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    #Функция идентична encrypt_caesar, но shift берется с противоположным знаком
    shift = -shift
    ciphertext = ''
    for i in text:
        if i.isalpha():
            if ord(i) + shift % 26 > 122 and i.islower() or ord(i) + shift % 26 > 90 and i.isupper():
                ciphertext += chr(ord(i) + shift % 26 - 26)
            elif shift < 0 and (ord(i) + shift % 26 < 97 and i.islower() or ord(i) + shift % 26 < 65 and i.isupper()):
                ciphertext += chr(ord(i) + shift % 26 + 26)
            else:
                ciphertext += chr(ord(i) + shift % 26)
        else:
            ciphertext += chr(ord(i))
    return ciphertext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
