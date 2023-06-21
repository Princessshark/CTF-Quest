import hashlib

text = 'Hillary Rodham Clinton'
hashed_text = hashlib.md5(text.encode()).hexdigest()

print(hashed_text)

