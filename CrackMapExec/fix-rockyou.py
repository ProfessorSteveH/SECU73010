input_file = 'rockyou.txt'
output_file = 'rockyou_utf8.txt'

print("[*] Converting file to clean UTF-8...")

with open(input_file, 'r', encoding='latin-1') as f:
    text = f.read()

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"[+] Done! Cleaned file saved as: {output_file}")
