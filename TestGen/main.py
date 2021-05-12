import json
import random
from helper import write_to_asm, generate_integer_alu_instr, generate_data_transfer_instr, generate_control_transfer_instr

global_reg = ['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7']
out_reg = ['o0', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7']
local_reg = ['l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7']
in_reg = ['i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7']
window_regs = global_reg + out_reg + local_reg + in_reg # all registers in current window
hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

Register_File_Local = {}
Instructions_Generated = []
Instruction_Count = 0


def generate_instr(instrs_set):
    global Instructions_Generated
    global Instruction_Count
    instr_group = random.choice(list(instrs_set.keys()))
    instrs = instrs_set[instr_group]
    instr = random.choice(list(instrs.keys()))
    if(instr_group == "integer_alu"):
        Instructions_Generated.append(generate_integer_alu_instr(instr, window_regs))
        Instruction_Count += 1
    if(instr_group == "data_transfer"):
        Instructions_Generated.append(generate_data_transfer_instr(instr, window_regs))
        Instruction_Count += 1
    # if(instr_group == "control_transfer"):
    #     Instructions_Generated.append(generate_control_transfer_instr(instr, window_regs))
    #     Instruction_Count += 1


if __name__=="__main__":
    instr_file = open('instrs.json', 'r')
    reg_file = open('reg_file.json', 'r')
    Register_File_Local = json.load(reg_file)

    instrs_set = json.load(instr_file)
    instr_file.close()
    reg_file.close()

    for i in range(5):
        generate_instr(instrs_set)
    write_to_asm(Instructions_Generated)