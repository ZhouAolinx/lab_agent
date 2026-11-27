import bcrypt

plain_text = "123456".encode("utf-8")
hash_pwd = bcrypt.hashpw(plain_text, bcrypt.gensalt(12))
print(hash_pwd.decode("utf-8"))
