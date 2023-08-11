import re
text = input() # bu ikisini lower() yapabilirsin falg olarak ignorecase yerine ama oburu daha guzel duruyo :P
word = input() # ve bunu

pattern = r"\b" + re.escape(word) + r"\b"  # bu ne ki?    matches = re.findall(rf"\b{word}\b", text)
count = len(re.findall(pattern, text, re.IGNORECASE))
print(count)

# re.escape: metin icinde escape edilmesi gerekebilcek karakterleri escape ediyo