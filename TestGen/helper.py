import random

def get_13bit_imm():
    number = random.choice(range(0, 2**13))
    hex_number = hex(number)
    return hex_number.split('x')[1]

def write_to_asm(Instructions_Generated):
    asm_file = open('main.s', 'w')
    for instr in Instructions_Generated:
        asm_file.write(instr)
        asm_file.write('\n')
        print(instr)
    asm_file.close()

def generate_integer_alu_instr(instr, window_regs):
    temp_instr = instr + ' '
    source1 = random.choice(window_regs)
    dest = random.choice(window_regs)
    i = random.choice([0,1])
    source2 = ''
    if(i):
        source2 = get_13bit_imm()
    else:
        source2 = random.choice(window_regs)
    temp_instr += '%' + source1 + ', %' + source2 + ', %' + dest
    return temp_instr

def generate_data_transfer_instr(instr, window_regs):
    temp_instr = instr + ' '
    source1 = random.choice(window_regs)
    dest = random.choice(window_regs)
    temp_instr += '[%' + source1 + '], %' + dest
    return temp_instr