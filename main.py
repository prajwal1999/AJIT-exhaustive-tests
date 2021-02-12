# All possible register combinations for misc instructions
# Author : Prajwal Kamble
# 9 Feb 2021 

import itertools
import random

global_reg = ['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7']
out_reg = ['o0', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7']
local_reg = ['l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7']
in_reg = ['i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7']
window_regs = global_reg + out_reg + local_reg + in_reg # all registers in current window
hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def generate_mulscc_instrs():
    # to get all possible combinations of window registers, taken 3 at a time
    permutations = list(itertools.permutations(window_regs, r=3))
    instrs = []
    for per in permutations:
        instrs.append('mulscc %' + per[0] + ', %' + per[1] + ', %' + per[2] + '\n')
    return instrs

def generate_flush_instrs():
    instrs = []
    for per in window_regs:
        instrs.append('flush %' + per + '\n')
    return instrs

def generate_rd_wr_asr_instrs():
    instrs = []
    for x in range(1, 32):
        for y in window_regs:
            instrs.append(
                'wr %' + y + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'asr' + str(x) + '\n'
            ) # wr %l0, 0xFF, %asr16
    instrs.append('\n')
    for x in range(1, 32):
        for y in window_regs:
            instrs.append(
                'rd %' + 'asr' + str(x) + ', %' + y + '\n'
            ) # rd %asr16, %o0
    return instrs

def generate_rd_wr_psr_instrs():
    instrs = []
    for y in window_regs:
        instrs.append(
            'wr %' + y + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'psr' + '\n'
        ) # wr %l0, 0x0F, %psr
    for y in window_regs:
        instrs.append(
            'rd %' + 'psr, ' + y + '\n'
        ) # rd %psr, %o0
    return instrs

def generate_rd_wr_tbr_instrs():
    instrs = []
    for y in window_regs:
        instrs.append(
            'wr %' + y + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'tbr' + '\n'
        ) # wr %l0, 0x0, %tbr
    for y in window_regs:
        instrs.append(
            'rd %' + 'tbr, ' + y + '\n'
        ) # rd %tbr, %o1
    return instrs

def generate_rd_wr_wim_instrs():
    instrs = []
    for y in window_regs:
        instrs.append(
            'wr %' + y + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'wim' + '\n'
        ) # wr %l0, 0x10, %wim
    for y in window_regs:
        instrs.append(
            'rd %' + 'wim, ' + y + '\n'
        ) # rd %wim, %o0
    return instrs

def generate_rd_wr_y_instrs():
    instrs = []
    for i in window_regs:
        instrs.append(
            'wr %' + i + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'y' + '\n'
        ) # wr %l0, 0xFF, %y
    for y in window_regs:
        instrs.append(
            'rd %' + 'y, ' + i + '\n'
        ) # rd %y, %o1
    return instrs

def generate_save_restore_instrs():
    # to get all possible combinations of window registers, taken 3 at a time
    permutations = list(itertools.permutations(window_regs, r=2))
    instrs = []
    for per in permutations:
        instrs.append(
            'save %' + per[0] + ', 0x' + 
            random.choice(hex_digits) + random.choice(hex_digits) + 
            ', %' + per[1] + '\n'
        ) # save %l0, 0x3, %i0
    for per in permutations:
        instrs.append(
            'restore %' + per[0] + ', 0x' + 
            random.choice(hex_digits) + random.choice(hex_digits) + 
            ', %' + per[1] + '\n'
        ) # restore %l0, 0x3, %o0
    return instrs

def generate_sethi_instrs():
    instrs = []
    for x in window_regs:
        instrs.append(
            'sethi 0x' + random.choice(hex_digits) +
            random.choice(hex_digits) + random.choice(hex_digits) + random.choice(hex_digits) +
            ', %' + x + '\n'
        ) # sethi 0x1234, %l3
    return instrs
if __name__=="__main__":
    main_asm = open('main.s', 'w')
    main_asm.write('! All possible register combinations for misc instructions\n')
    main_asm.write('! Author : Prajwal Kamble\n')
    main_asm.write('! 9 Feb 2021\n\n\n')
    main_asm.writelines(generate_flush_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_mulscc_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_rd_wr_asr_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_rd_wr_asr_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_rd_wr_psr_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_rd_wr_tbr_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_rd_wr_wim_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_rd_wr_y_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_save_restore_instrs())
    main_asm.write('\n\n\n')
    main_asm.writelines(generate_sethi_instrs())
    main_asm.write('\n\n\n')

    other_instr = ['unimp', 'nop', 'stbar']
    for i in range(30):
        main_asm.write(random.choice(other_instr) + '\n')

    main_asm.close()
