import os
import re
import codecs
import pathlib
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
script = pathlib.Path(sys.argv[1]).absolute()

def read_file(name):
    with open(name, 'rb') as file:
        return file.read()

def write_file(name, cont):
    with open(name, 'wb') as file:
        file.write(cont)

def hexdump(var):
    return var.hex(sep=' ').upper()

def unhexdump(var):
    return codecs.decode(var, 'hex')

mainscript = hexdump(read_file(script))
find_opcode = re.sub(r'(30\s+\d+\s+\d+\s+\d+\s+)(40\s+\d+\s+\d+\s+\d+)(\s+51\s+\d+\s+\d+\s+\d+)', r'\g<1>54 00 00 80\g<3>', mainscript)
not_space = find_opcode.replace(' ', '')
final_script = unhexdump(not_space)
write_file(script.stem + '-unprot.lua', final_script)