from registersAddressMapping import registersAddressMapping

class uType:
    def process(self, inst, rd, imm, registers, pc):
        if inst == "lui":
            # 寫入寄存器
            registers.write(registersAddressMapping.getRegisterAddress(rd), int(imm))
        elif inst == "auipc":
            # 寫入寄存器
            registers.write(registersAddressMapping.getRegisterAddress(rd), pc + (int(imm) << 12))