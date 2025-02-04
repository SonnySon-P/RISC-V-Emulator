from registersAddressMapping import registersAddressMapping

class sType:
    def process(self, inst, rs2, imm, rs1, registers, memory):
        # 讀取暫存器
        temp1 = registers.read(registersAddressMapping.getRegisterAddress(rs1))
        temp2 = registers.read(registersAddressMapping.getRegisterAddress(rs2))

        # 計算
        if inst == "sb":
            memory.write(int(imm) + int(temp1), temp2)
        elif inst == "sh":
            memory.write(int(imm) + int(temp1), temp2)
        elif inst == "sw":
            memory.write(int(imm) + int(temp1), temp2)