import random

def get_13bit_imm():
    number = random.choice(range(0, 2**13))
    hex_number = hex(number)
    return hex_number.split('x')[1]

def write_to_asm(Instructions_Generated):
    asm_file = open('files/main.s', 'w')
    vprj_file = open('files/main.vprj', 'w')
    prologue_file = open('prologue.s', 'r')
    epilogue_file = open('epilogue.s', 'r')
    asm_file.write(prologue_file.read())
    for instr in Instructions_Generated:
        asm_file.write(instr)
        asm_file.write('\n')
        print(instr)
    asm_file.write(epilogue_file.read())
    vprj_file.write('SOURCES = main.s\n\n\n\n')
    vprj_file.write('RESULTS = \n')
    vprj_file.write('g1=0x00000080')
    asm_file.close()
    vprj_file.close()
    prologue_file.close()
    epilogue_file.close()

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

def generate_control_transfer_instr(instr, window_regs):
    pass