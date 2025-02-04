class RV32IMemory:
    def __init__(self, size = 1024 * 1024):  # memory大小為1MB
        self.memory = {}  # 使用字典來模擬內存，鍵是位址，值是指令
        self.wordSize = 4  # 每條指令占用4字節
        self.size = size  # 設置內存的大小

        # 初始化內存，將每個位置設置為空字串
        for address in range(0, size, self.wordSize):
            self.memory[address] = ""
    
    def write(self, address, instruction):
        # 檢查位址是否4字節對齊
        if address % self.wordSize != 0:
            print(f"Invalid address 0x{address:X}. Address must be aligned to {self.wordSize} bytes.")
            return

        # 檢查位址是否在內存範圍內
        if address < self.size:
            self.memory[address] = instruction
        else:
            print(f"Memory overflow at address 0x{address:X}. Could not load instruction.")

    def read(self, address):
        # 檢查位址是否4字節對齊
        if address % self.wordSize != 0:
            print(f"Invalid address 0x{address:X}. Address must be aligned to {self.wordSize} bytes.")
            return None
        
        # 檢查位址是否在內存範圍內
        if address < self.size:
            return self.memory.get(address, None)
        else:
            print(f"Invalid address 0x{address:X}. Unable to read instruction.")
            return None

    def get_memory(self):
        # 返回整個記憶體的內容
        return self.memory