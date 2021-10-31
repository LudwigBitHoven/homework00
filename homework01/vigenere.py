def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    res = ""
    key = keyword.upper()
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if (
                ord(plaintext[i]) + ord(key[i % len(key)]) > 187
                and plaintext[i].islower()
                or ord(plaintext[i]) + ord(key[i % len(key)]) > 155
                and plaintext[i].isupper()
            ):
                res += chr(ord(plaintext[i]) + ord(key[i % len(key)]) - ord("a") - 26)
            else:
                res += chr(ord(plaintext[i]) + ord(key[i % len(key)]) - ord("A"))
        else:
            res += plaintext[i]
    return res


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    res = ""
    a = ciphertext
    key = keyword.upper()
    for i in range(len(a)):
        if a[i].isalpha():
            if (
                ord(a[i]) - ord(key[i % len(key)]) < 32
                and a[i].islower()
                or ord(a[i]) - ord(key[i % len(key)]) < 0
                and a[i].isupper()
            ):
                res += chr(ord(a[i]) - ord(key[i % len(key)]) + 65 + 26)
            else:
                res += chr(ord(a[i]) - ord(key[i % len(key)]) + 65)
        else:
            res += a[i]
    return res