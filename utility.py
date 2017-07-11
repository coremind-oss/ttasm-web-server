from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from django.utils import timezone
import pytz


def encrypt_data (message, public_key):
    key = RSA.importKey(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_data = cipher.encrypt(message.encode('utf-8'))
    return encrypted_data

def decrypt_data (message, private_key):
    key = RSA.importKey(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_data = cipher.decrypt(message)
    return decrypted_data

def get_base_date(tz_string):
    tz_info = pytz.timezone(tz_string)
    current_time_utc = timezone.now()
    return current_time_utc.astimezone(tz_info).date()