from registersAddressMapping import registersAddressMapping

class rType:
    def process(self, inst, rd, rs1, rs2, registers):
        # 讀取暫存器
        temp1 = registers.read(registersAddressMapping.getRegisterAddress(rs1))
        temp2 = registers.read(registersAddressMapping.getRegisterAddress(rs2))

        # 計算
        if inst == "add":
            temp3 = int(temp1) + int(temp2)
        elif inst == "sub":
            temp3 = int(temp1) - int(temp2)
        elif inst == "sll":
            temp3 = int(temp1) << int(temp2)
        elif inst == "slt":
            if int(temp1) < int(temp2):
                temp3 = 1
            else:
                temp3 = 0
        elif inst == "sltu":
            if abs(int(temp1)) < abs(int(temp2)):
                temp3 = 1
            else:
                temp3 = 0
        elif inst == "xor":
            temp3 = int(temp1) ^ int(temp2)
        elif inst == "srl":
            temp3 = int(temp1) >> int(temp2)
        elif inst == "sra":
            if rs1 < 0:
                temp3 = (int(temp1) + (1 << 5)) >> int(temp2)  # 如果rs1是負數，則進行算術右移
            else:
                temp3 = int(temp1) >> int(temp2)  # 正數則直接進行右移操作
        elif inst == "or":
            temp3 = int(temp1) | int(temp2)
        elif inst == "and":
            temp3 = int(temp1) & int(temp2)

        # 寫入暫存器
        registers.write(registersAddressMapping.getRegisterAddress(rd), temp3)