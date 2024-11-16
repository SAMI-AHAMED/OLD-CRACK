import os,time
code = input(' [+] Єиτєя Fiℓє Иαмє » ')
ɒєcσɒє = open(code, 'r+')
ɒєcσɒє_content = ɒєcσɒє.read()
ɒєcσɒє.seek(0)
ɒєcσɒє.truncate()
ɒєcσɒє_content = ɒєcσɒє_content.replace('exec', 'print')
ɒєcσɒє.write(ɒєcσɒє_content)
None
os.system('python ' + code + ' > ' + f'''decode_{code}''')
print('ᴛᴏᴏʟ ᴅᴇᴄᴏᴅᴇᴅ & ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ɪɴ ꜰɪʟᴇ')
time.sleep(2)
os.system('clear')
time.sleep(1)

