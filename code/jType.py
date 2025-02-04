from registersAddressMapping import registersAddressMapping

class jType:
    def process(self, inst, rd, imm, registers, pc):
        # 計算
        if inst == "jal":
            # 寫入暫存器
            registers.write(registersAddressMapping.getRegisterAddress(rd), pc + 4)

            # 轉跳位址
            return int(imm)