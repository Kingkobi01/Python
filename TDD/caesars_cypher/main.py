
import string


def encrypt(message, shiftvalue=1):
    if not isinstance(message, str):
        message = str(message)
    chars = string.ascii_letters + string.digits + string.punctuation + " "
    encrypted_message_list = [chars[(chars.find(char) + shiftvalue) % len(chars)]
                              for char in message]
    encrypted_message = "".join(encrypted_message_list)
    return encrypted_message
