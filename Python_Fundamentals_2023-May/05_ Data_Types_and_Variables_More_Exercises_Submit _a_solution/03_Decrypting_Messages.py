key_number = int(input())
total_line = int(input())
decrypted_txt = ''
for current_line in range(total_line):
    line = ord(input())
    decrypted_txt += chr(line + key_number)
print(decrypted_txt)

