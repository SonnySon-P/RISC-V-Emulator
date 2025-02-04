from registersAddressMapping import registersAddressMapping

class bType:
    def process(self, inst, rs1, rs2, imm, registers, pc):
        # 讀取暫存器
        temp1 = registers.read(registersAddressMapping.getRegisterAddress(rs1))
        temp2 = registers.read(registersAddressMapping.getRegisterAddress(rs2))

        # 計算
        if inst == "beq":
            if int(temp1) == int(temp2):
                return pc + int(imm)
        elif inst == "bne":
            if int(temp1) != int(temp2):
                return pc + int(imm)
        elif inst == "blt":
            if int(temp1) < int(temp2):
                return pc + int(imm)
        elif inst == "bge":
            if int(temp1) >= int(temp2):
                return pc + int(imm)
        elif inst == "bltu":
            if abs(int(temp1)) < abs(int(temp2)):
                return pc + int(imm)
        elif inst == "bgeu":
            if abs(int(temp1)) >= abs(int(temp2)):
                return pc + int(imm)