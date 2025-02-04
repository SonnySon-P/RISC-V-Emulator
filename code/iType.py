from registersAddressMapping import registersAddressMapping

class iType:
    def process(self, inst, rd, rs1, imm, registers, memory, pc):
        # 讀取暫存器
        temp1 = registers.read(registersAddressMapping.getRegisterAddress(rs1))

        # 計算
        if inst == "addi":
            temp2 = int(temp1) + int(imm)
        elif inst == "slti":
            if int(temp1) < int(imm):
                temp2 = 1
            else:
                temp2 = 0
        elif inst == "sltiu":
            if abs(int(temp1)) < abs(int(imm)):
                temp2 = 1
            else:
                temp2 = 0
        elif inst == "xori":
            temp2 = int(temp1) ^ int(imm)
        elif inst == "ori":
            temp2 = int(temp1) | int(imm)
        elif inst == "andi":
            temp2 = int(temp1) & int(imm)
        elif inst == "slli":
            temp2 = int(temp1) << int(imm)
        elif inst == "srli":
            temp2 = int(temp1) >> int(imm)
        elif inst == "srai":
            if rs1 < 0:
                temp2 = (int(temp1) + (1 << 5)) >> int(imm)  # 如果rs1是負數，則進行算術右移
            else:
                temp2 = int(temp1) >> int(imm)  # 正數則直接進行右移操作
        elif inst == "lb":
            temp2 = memory.read(int(temp1) + int(imm))
        elif inst == "lh":
            temp2 = memory.read(int(temp1) + int(imm))
        elif inst == "lw":
            temp2 = memory.read(int(temp1) + int(imm))
        elif inst == "lbu":
            temp2 = memory.read(int(temp1) + int(imm))
        elif inst == "lhu":
            temp2 = memory.read(int(temp1) + int(imm))
        elif inst == "jalr":
            registers.write(registersAddressMapping.getRegisterAddress(rd), pc + 4)  # 將pc + 4寫入暫存器
            pc = int(temp1) + int(imm)  # 新的pc值

        # 寫入暫存器
        registers.write(registersAddressMapping.getRegisterAddress(rd), temp2)

        return pc + 4