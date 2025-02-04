class RV32IRegisters:
    def __init__(self):
        # 初始化32個暫存器，所有的暫存器初始值為0
        self.registers = [0] * 32  # RV32I有32個暫存器，索引從0到31
    
    def read(self, registerNumber):
        if registerNumber == 0:
            return 0  # x0(zero)暫存器的值始終是0
        elif 0 <= registerNumber < 32:
            return self.registers[registerNumber]
        else:
            print(f"Invalid register number: {registerNumber}. Must be between 0 and 31.")
    
    def write(self, registerNumber, value):
        if registerNumber == 0:
            return  # 不允許對x0(zero)暫存器寫入值
        elif 0 <= registerNumber < 32:
            self.registers[registerNumber] = value
        else:
            print(f"Invalid register number: {registerNumber}. Must be between 0 and 31.")