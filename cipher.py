class Cipher(object):
    def __init__(self):
        pass

    def encrypt(self, message, shift):
        encrypted_message = ''
        for letter in list(message):
            index = ord(letter)
            encrypted_message = encrypted_message + chr(index + shift)
        return encrypted_message

    def decrypt(self, ciphertext, shift):
        decrypted_message = ''
        for letter in list(ciphertext):
            index = ord(letter)
            decrypted_message = decrypted_message + chr(index - shift)
        return decrypted_message
