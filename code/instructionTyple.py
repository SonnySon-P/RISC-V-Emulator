class instructionTyple:
    # 定義指令名稱到指令類型的映射(以下為RV32I指令集，並不包含虛擬指令)
    instructionTypleContent = {
        # R-type Instructions
        "add": "R",  # 加法
        "sub": "R",  # 減法
        "sll": "R",  # 邏輯左移
        "slt": "R",  # 小於比較
        "sltu": "R", # 無符號小於比較
        "xor": "R",  # 異或
        "srl": "R",  # 邏輯右移
        "sra": "R",  # 算術右移
        "or": "R",   # 或操作
        "and": "R",  # 與操作

        # I-type Instructions
        "addi": "I",  # 加立即數
        "slti": "I",  # 小於比較立即數
        "sltiu": "I", # 無符號小於比較立即數
        "xori": "I",  # 異或立即數
        "ori": "I",   # 或立即數
        "andi": "I",  # 與立即數
        "slli": "I",  # 邏輯左移立即數
        "srli": "I",  # 邏輯右移立即數
        "srai": "I",  # 算術右移立即數
        "lb": "I",    # 載入字節
        "lh": "I",    # 載入半字
        "lw": "I",    # 載入字
        "lbu": "I",   # 載入無符號字節
        "lhu": "I",   # 載入無符號半字
        "jalr": "I",  # 跳轉並鏈接
        #fence
        #ecall
        #ebreak

        # S-type Instructions
        "sb": "S",    # 存儲字節
        "sh": "S",    # 存儲半字
        "sw": "S",    # 存儲字

        # B-type Instructions
        "beq": "B",   # 等於
        "bne": "B",   # 不等於
        "blt": "B",   # 小於
        "bge": "B",   # 大於等於
        "bltu": "B",  # 無符號小於
        "bgeu": "B",  # 無符號大於等於

        # U-type Instructions
        "lui": "U",   # 加載上位立即數
        "auipc": "U", # 加載上位立即數並加到pc

        # J-type Instructions
        "jal": "J"    # 跳轉並鏈接
    }

    @classmethod
    def getInstructionType(cls, instruction):
        # 查詢並返回指令類型
        return cls.instructionTypleContent.get(instruction, "Unknown")