# Random tests generation for mulscc instruction 
# Author : Prajwal Kamble
# 17 Feb 2021 

import itertools
import random
import json
import os
from shutil import copyfile

global_reg = ['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7']
out_reg = ['o0', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7']
local_reg = ['l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7']
in_reg = ['i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7']
window_regs = global_reg + out_reg + local_reg + in_reg # all registers in current window
hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def init_file(file):
    file.write('! Random tests for verifying MULSCC instructions \n\n')
    file.write('! Author: Prajwal Kamble \n')
    file.write('! 18 Feb 2021 \n')
    file.write('\n\n\n.global main \nmain: \n_start:')

    file.write('    ! Initialize PSR, enable traps.\n')
    file.write('    ! set PSR with ET=1 PS=1 S=1, all other fields=0\n')
    file.write('    mov 0xE0, %l0\n')
    file.write('    wr %l0, %psr\n')
    file.write('    nop\n    nop\n    nop\n\n\n')

    file.write('    !store base of trap table in TBR register\n')
    file.write('    set	trap_table_base, %l0\n')
    file.write('    wr	%l0, 0x0, %tbr\n')
    file.write('    nop\n    nop\n    nop\n\n\n')

    file.write('    !Initialize g1. Upon a trap, g1 should be overwritten by the trap number\n')
    file.write('    mov 0xBAD, %g1\n\n\n\n')

def generate_32bit_hex():
    hex = '0x'
    for i in range(8):
        hex += random.choice(hex_digits)
    return hex

def generate_instr():
    instr = ''
    regs = window_regs
    hold_psr = random.choice(regs)
    instr += '    rd %psr, %' + hold_psr + '\n'
    regs.remove(hold_psr)
    instr += '    mov ' + generate_32bit_hex() + ', %y\n'
    rs1_reg = random.choice(regs)
    instr += '    set' + generate_32bit_hex() + ', %' + rs1_reg + '\n'
    # regs.remove(rs1_reg)
    rs2_reg = random.choice(regs)
    instr += '    set' + generate_32bit_hex() + ', %' + rs2_reg + '\n'
    # regs.remove(rs2_reg)
    rd_reg = random.choice(regs)
    instr += '    mulscc %' + rs1_reg + ', %' + rs2_reg + ', %' + rd_reg + '\n\n'
    
    return instr

if __name__=="__main__":
    if not os.path.isdir('MULSCC'):
        os.mkdir('MULSCC')
    os.chdir('MULSCC')
    copyfile('../clean.sh', 'clean.sh')

    asm_file = open('mulscc.s', 'w')
    vprj_file = open('mulscc.vprj', 'w')

    init_file(asm_file)
    vprj_file.write('SOURCES = mulscc.s\n\n\n\n\n')
    vprj_file.write('RESULTS = \n')

    for i in range(20):
        asm_file.write(generate_instr())

    trap_file = open('../trap_table.s', 'r')
    asm_file.write(trap_file.read())

    trap_file.close()
    asm_file.close()
    vprj_file.close()