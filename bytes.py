import re
E = '\033[1;31m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B} @EZ_X4
|{F}[+] TeleGram  : {B} @Theyhates_joker   |
|{F}[+] Tool  : {B}Decode Bytes[1,1000] |
{E}==============================''')
def decode(byte_string):
    """Decode a bytes string like 'bytes([1, 2, ..., 10000])' to the corresponding characters."""
    decode_AHMED = re.findall(r'\d+', byte_string)
    decode_AHMED = list(map(int, decode_AHMED))
    try:
        return bytes(decode_AHMED).decode()
    except UnicodeDecodeError:
        return ''.join(chr(b) for b in decode_AHMED)

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        enc = file.read()    
    try:
        fix_mahos = re.sub(r'bytes\(\[([^\]]+)\]\)', 
                               lambda match: f'"{decode(match.group(0))}"', 
                               enc)
    except:
        fix_mahos = enc
    try:
        fix_mahos = fix_mahos.replace('.decode()', '')
    except:
        fix_mahos = fix_mahos
    try:
        fix_mahos = re.sub(r'bytes\(\[\]\)', '""', fix_mahos)
    except:
        fix_mahos = fix_mahos
    
    new_dec = f"decode_{filename}"
    with open(new_dec, 'w', encoding='utf-8') as fixed_file:
        fixed_file.write(fix_mahos)

    print(f"{F} File Fixed Done !! {new_dec}")

fix_file(filename=input(f"{C}ENTER YOUR file that Encode By Bytes to dec it: {X}"))