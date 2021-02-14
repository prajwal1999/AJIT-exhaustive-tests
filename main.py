# All possible register combinations for misc instructions
# Author : Prajwal Kamble
# 9 Feb 2021 

import itertools
import random
import json

global_reg = ['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7']
out_reg = ['o0', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7']
local_reg = ['l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7']
in_reg = ['i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7']
window_regs = global_reg + out_reg + local_reg + in_reg # all registers in current window
hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

statistics_generated = {}

def init_statistics():
    file = open('expected_stats.json', 'r')
    expected_stats = json.load(file)
    for x in expected_stats.keys():
        statistics_generated[x] = 0
    file.close()

def generate_mulscc_instrs():
    # to get all possible combinations of window registers, taken 3 at a time
    permutations = list(itertools.permutations(window_regs, r=3))
    instrs = []
    for per in permutations:
        statistics_generated['mulscc'] += 1
        statistics_generated[per[0]] += 1
        statistics_generated[per[1]] += 1
        statistics_generated[per[2]] += 1
        instrs.append('mulscc %' + per[0] + ', %' + per[1] + ', %' + per[2] + '\n')
        instrs.append('\n\n\n')

    return instrs

def generate_flush_instrs():
    instrs = []
    for per in window_regs:
        statistics_generated['flush'] += 1
        statistics_generated[per] += 1
        instrs.append('flush %' + per + '\n')
        instrs.append('\n\n\n')
    return instrs

def generate_rd_wr_asr_instrs():
    instrs = []
    for x in range(1, 32):
        for y in window_regs:
            statistics_generated["wr"] += 1
            statistics_generated[y] += 1
            statistics_generated["asr"] += 1
            instrs.append(
                'wr %' + y + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'asr' + str(x) + '\n'
            ) # wr %l0, 0xFF, %asr16
    instrs.append('\n')
    for x in range(1, 32):
        for y in window_regs:
            statistics_generated["rd"] += 1
            statistics_generated[y] += 1
            statistics_generated["asr"] += 1
            instrs.append(
                'rd %' + 'asr' + str(x) + ', %' + y + '\n'
            ) # rd %asr16, %o0
    instrs.append('\n\n\n')
    return instrs

def generate_rd_wr_psr_instrs():
    instrs = []
    for i in window_regs:
        statistics_generated["wr"] += 1
        statistics_generated[y] += 1
        statistics_generated["psr"] += 1
        instrs.append(
            'wr %' + i + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'psr' + '\n'
        ) # wr %l0, 0x0F, %psr
    for i in window_regs:
        statistics_generated["rd"] += 1
        statistics_generated[y] += 1
        statistics_generated["psr"] += 1
        instrs.append(
            'rd %' + 'psr, ' + i + '\n'
        ) # rd %psr, %o0
    instrs.append('\n\n\n')
    return instrs

def generate_rd_wr_tbr_instrs():
    instrs = []
    for i in window_regs:
        statistics_generated["wr"] += 1
        statistics_generated[y] += 1
        statistics_generated["tbr"] += 1
        instrs.append(
            'wr %' + i + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'tbr' + '\n'
        ) # wr %l0, 0x0, %tbr
    for i in window_regs:
        statistics_generated["rd"] += 1
        statistics_generated[y] += 1
        statistics_generated["tbr"] += 1
        instrs.append(
            'rd %' + 'tbr %, ' + i + '\n'
        ) # rd %tbr, %o1
    instrs.append('\n\n\n')
    return instrs

def generate_rd_wr_wim_instrs():
    instrs = []
    for i in window_regs:
        statistics_generated["wr"] += 1
        statistics_generated[y] += 1
        statistics_generated["wim"] += 1
        instrs.append(
            'wr %' + i + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'wim' + '\n'
        ) # wr %l0, 0x10, %wim
    for i in window_regs:
        statistics_generated["rd"] += 1
        statistics_generated[y] += 1
        statistics_generated["wim"] += 1
        instrs.append(
            'rd %' + 'wim %, ' + i + '\n'
        ) # rd %wim, %o0
    instrs.append('\n\n\n')
    return instrs

def generate_rd_wr_y_instrs():
    instrs = []
    for i in window_regs:
        statistics_generated["wr"] += 1
        statistics_generated[i] += 1
        statistics_generated["y"] += 1
        instrs.append(
            'wr %' + i + ', 0x' + random.choice(hex_digits) + random.choice(hex_digits) + ', %' + 'y' + '\n'
        ) # wr %l0, 0xFF, %y
    for i in window_regs:
        statistics_generated["rd"] += 1
        statistics_generated[i] += 1
        statistics_generated["y"] += 1
        instrs.append(
            'rd %' + 'y, %' + i + '\n'
        ) # rd %y, %o1
    instrs.append('\n\n\n')
    return instrs

def generate_save_restore_instrs():
    # to get all possible combinations of window registers, taken 3 at a time
    permutations = list(itertools.permutations(window_regs, r=2))
    instrs = []
    for per in permutations:
        statistics_generated["save"] += 1
        statistics_generated[per[0]] += 1
        statistics_generated[per[1]] += 1
        instrs.append(
            'save %' + per[0] + ', 0x' + 
            random.choice(hex_digits) + random.choice(hex_digits) + 
            ', %' + per[1] + '\n'
        ) # save %l0, 0x3, %i0
    for per in permutations:
        statistics_generated["restore"] += 1
        statistics_generated[per[0]] += 1
        statistics_generated[per[1]] += 1
        instrs.append(
            'restore %' + per[0] + ', 0x' + 
            random.choice(hex_digits) + random.choice(hex_digits) + 
            ', %' + per[1] + '\n'
        ) # restore %l0, 0x3, %o0
    instrs.append('\n\n\n')
    return instrs

def generate_sethi_instrs():
    instrs = []
    for x in window_regs:
        statistics_generated["sethi"] += 1
        statistics_generated[x] += 1
        instrs.append(
            'sethi 0x' + random.choice(hex_digits) +
            random.choice(hex_digits) + random.choice(hex_digits) + random.choice(hex_digits) +
            ', %' + x + '\n'
        ) # sethi 0x1234, %l3
    instrs.append('\n\n\n')
    return instrs

def check_statistics():
    file = open('expected_stats.json', 'r')
    expected_stats = json.load(file)
    check_file = open('checked_stats', 'w')
    check_file.write("Entity")
    for i in range(35-6):
        check_file.write(" ")
    check_file.write("Expected Occurences")
    for i in range(35-19):
        check_file.write(" ")
    check_file.write("Generated Occurences")
    for i in range(35-20):
        check_file.write(" ")
    check_file.write("\n\n")

    for x in expected_stats.keys():
        check_file.write(x)
        for i in range(35-len(x)):
            check_file.write(" ")
        check_file.write(str(expected_stats[x]))
        for i in range(35-len(str(expected_stats[x]))):
            check_file.write(" ")
        check_file.write(str(statistics_generated[x]))
        for i in range(35-len(str(statistics_generated[x]))):
            check_file.write(" ")

        if(statistics_generated[x] == expected_stats[x]):
            check_file.write("Success")
        else:
            check_file.write("Failed")
            print("Occurences of " + x + " not Matched: Expected - " + str(expected_stats[x]) + " Got - " + str(statistics_generated[x]))
        check_file.write("\n")

    file.close()
    check_file.close()

if __name__=="__main__":
    init_statistics()
    main_asm = open('main.s', 'w')
    main_asm.write('! All possible register combinations for misc instructions\n')
    main_asm.write('! Author : Prajwal Kamble\n')
    main_asm.write('! 9 Feb 2021\n\n\n')
    main_asm.writelines(generate_flush_instrs())
    main_asm.writelines(generate_mulscc_instrs())
    main_asm.writelines(generate_rd_wr_asr_instrs())
    main_asm.writelines(generate_rd_wr_asr_instrs())
    main_asm.writelines(generate_rd_wr_psr_instrs())
    main_asm.writelines(generate_rd_wr_tbr_instrs())
    main_asm.writelines(generate_rd_wr_wim_instrs())
    main_asm.writelines(generate_rd_wr_y_instrs())
    main_asm.writelines(generate_save_restore_instrs())
    main_asm.writelines(generate_sethi_instrs())
    other_instr = ['unimp', 'nop', 'stbar']
    for i in range(30):
        temp_instr = random.choice(other_instr)
        statistics_generated[temp_instr] += 1
        main_asm.write(temp_instr + '\n')
    main_asm.close()
    check_statistics()
    print("done!")