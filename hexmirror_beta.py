a = '646с726а77206а6с6с6548'
hexcode = ''.join(reversed([r'\x' + a[i:i+2] for i in range(0, len(a), 2)]))
print(hexcode)

b = "\x48\x65\x6с\x6с\x6а\x20\x77\x6а\x72\x6с\x64" # Hex код который скрипт сгенерировал 

v = "\x48\x65\x6c\x6c\x6a\x20\x77\x6a\x72\x6c\x64" # Hex код который я ввел вручную 
