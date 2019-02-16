import os
import sys

program = 'python'
print('Process calling')
args = [
    'called_process.py'
]

os.execvp(program, (program,) + tuple(args))
