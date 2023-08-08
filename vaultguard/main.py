from cryptography.fernet import Fernet
import base64


key = Fernet.generate_key()
password = '1234'
f= Fernet(key)
print(key)
pass1 = f.encrypt(password.encode())
print(pass1)
pass1 = base64.urlsafe_b64encode(pass1).decode()
print(pass1)
pass1 = """Z0FBQUFBQmswS3BhNERVT3JoamlpWEhZd3AtYnhsdVNDdFhEeGt3ZEtsMXJ6TUVGay1YVDRIUlhER0NOQVdoUWJ1QnZiUFNMZFpXNVZJY1piVHljTVJreWtYWlBTcnI3bGc9PQ=="""
pass1 = base64.urlsafe_b64decode(pass1)
print(pass1)
# pass2 = f.decrypt(pass1).decode()
# pass2 = f.decrypt(pass1).decode()
# print(pass2)