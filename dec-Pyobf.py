import subprocess, tempfile
def DEC_PYOBFUSCATE(CODE):
    try:
        _A_ = []
        for _B_ in CODE.decode().split('\n'):
            if 'lambda' in _B_ and not '**' in _B_:continue
            _A_.append(_B_.strip())
        FUNC = r"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
try:
    if not 'exec' == pyobfuscate[0][1]:
        print('Try Another Method :)')
        input('Press Enter to Exit')
        exit()
    try:
        def a(i):return unpad(AES.new(__import__('hashlib').sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0]).encode()).digest()[:24], AES.MODE_CBC, i[:AES.block_size]).decrypt(i[AES.block_size:]), AES.block_size).decode()
        print(a(pyobfuscate[1][2]))
    except:
        def a(i):return unpad(AES.new(__import__('hashlib').sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0][:-1]).encode()).digest()[:24], AES.MODE_CBC, i[:AES.block_size]).decrypt(i[AES.block_size:]), AES.block_size).decode()
        print(a(pyobfuscate[1][2]))
except:
    def a(i, j):
        i = __import__('base64').b85decode(i)
        j, c = b(j, i[:8])
        return AES.new(j, AES.MODE_CFB, c).decrypt(i[8:]).decode()
    def b(i, j):
        k = __import__('hashlib').pbkdf2_hmac('sha256', i.encode(), j, 100000)
        return (k[:16], k[16:])
    print(a(list(obfuscate.values())[0], list(obfuscate.keys())[0][1:-1]))
"""
        with tempfile.NamedTemporaryFile(suffix='hhhhh.py', delete=False) as _C_:_C_.write(('\n'.join(_A_)+FUNC).encode())
        R = subprocess.run(['python', _C_.name], capture_output=True, text=True)
        return R.stdout
    except UnicodeDecodeError:
        return None
FL = input("</> 𝙴𝙽𝚃𝙴𝚁 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴: ")
with open(FL, 'rb') as file:
    C = file.read()
R = DEC_PYOBFUSCATE(C)
from rich.console import Console
from rich.syntax import Syntax
console = Console()
def show_code_with_result(file_path: str, result: str, temp: bool):
    with open(file_path, "r") as file:
        source_code = file.read()
    syntax = Syntax(source_code, "python", line_numbers=True)
    import os;os.system("clear");console.print(R)
show_code_with_result(FL, R, temp=False)