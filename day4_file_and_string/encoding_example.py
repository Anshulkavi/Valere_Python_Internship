
Encoding in Python
Encoding is about converting text (Unicode) into bytes, especially for file writing or network transfer.
Decoding is reversal of encoding
Common encodings:
"utf-8" (default & recommended)

"ascii" (limited to basic characters)

"utf-16" (uses more bytes, supports wider range)

text = "Hello, नमस्ते"
encoded_text = text.encode("utf-8") 
print(encoded_text) # b'Hello, \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87'

decoded_text = encoded_text.decode("utf-8")
print(decoded_text)


# Error Handling in Encoding and Decoding
text1 = "Hello 😊"

#ascii doesn't support emoji, so this will raise unless we handle error
encoded = text.encode("ascii", errors="ignore") #removes unsupported chars
print(encoded) #b'Hello, '

encoded = text.encode("ascii", errors= "replace") # replaces with ?
print(encoded) 

#Encoding in flie Writing

#save with utf-16
with open("data.txt", "w", encoding="utf-16") as f:
    f.write("नमस्ते")

#Read with utf-16
with open("data.txt","r",  encoding="utf-16") as f:
    text = (f.read())
    print(type(text))  <class 'str'>

# Reading as binary
with open("data.txt", "rb") as f:
    raw = f.read()
    print(type(raw))   # <class 'bytes'>
