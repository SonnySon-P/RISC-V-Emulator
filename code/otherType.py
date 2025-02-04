from registersAddressMapping import registersAddressMapping

class otherType:
    def process(self, registers):
        # 讀取暫存器
        temp1 = registers.read(registersAddressMapping.getRegisterAddress("a7"))
        
        # System Call
        if temp1 == 1:
            temp2 = registers.read(registersAddressMapping.getRegisterAddress("a0"))
            print(temp2)

        elif temp1 == 5:
            # 從螢幕讀取數值
            temp2 = input()

            # 寫入暫存器
            registers.write(registersAddressMapping.getRegisterAddress("a0"), temp2)
        elif temp1 == 10:
            # 結束
            exit(0)