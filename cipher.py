import random as r 

class Cipher(object):
    def __init__(self):
        pass

    def encrypt(self, message, shift):
        encrypted_message = ''
        for i in range(len(message)):
            index = ord(message[i])
            if type(shift) == int:
                encrypted_message = encrypted_message + chr((index + shift) % 255)
            elif type(shift) == list:
                encrypted_message = encrypted_message + chr((index + shift[i]) % 255)
        return encrypted_message

    def decrypt(self, ciphertext, shift):
        decrypted_message = ''
        for i in range(len(ciphertext)):
            index = ord(ciphertext[i])
            if type(shift) == int:
                decrypted_message = decrypted_message + chr((index - shift) % 255)
            elif type(shift) == list:
                decrypted_message = decrypted_message + chr((index - shift[i]) % 255)
        return decrypted_message

    def one_time_pad(self, message):
        pad = []
        for letter in message:
            pad.append(r.randint(0, 255))
        return pad
