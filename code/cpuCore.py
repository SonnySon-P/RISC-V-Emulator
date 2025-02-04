from RV32IRegisters import RV32IRegisters
from instructionTyple import instructionTyple
from rType import rType
from iType import iType
from sType import sType
from bType import bType
from uType import uType
from jType import jType
from otherType import otherType

class cpuCore:
    def __init__(self):
        self.pc = 0

    def implementation(self, memory):
            registers = RV32IRegisters()  # 創建registers實例

            # 開始執行指令
            while True:
                # 讀取當前程序計數器(pc)地址的指令
                instruction = memory.read(self.pc)

                # 如果該地址沒有指令或超出了有效範圍，則停止執行
                if instruction == "" or instruction is None:
                    break

                # 查詢並顯示指令的類型
                instructionType = instructionTyple.getInstructionType(instruction[0])

                # 指令集解析
                if instructionType == "R":
                    # 假設指令R-type是類似add x1, x2, x3格式
                    inst = instruction[0]  # 指令名稱
                    rd = instruction[1]    # 目標寄存器
                    rs1 = instruction[2]   # 暫存器1
                    rs2 = instruction[3]   # 暫存器2
                    r = rType()  # 創建rType實例
                    r.process(inst, rd, rs1, rs2, registers)  
                elif instructionType == "I":
                    # 假設指令I-type是類似addi a7, a7, 5格式
                    inst = instruction[0]  # 指令名稱
                    rd = instruction[1]    # 目標暫存器
                    rs1 = instruction[2]   # 暫存器
                    imm = instruction[3]   # 立即數
                    i = iType()  # 創建iType實例
                    self.pc = i.process(inst, rd, rs1, imm, registers, memory, self.pc) - 4
                elif instructionType == "S":
                    # 假設指令S-type是類似sw x5, 0(x6)格式
                    inst = instruction[0]  # 指令名稱
                    rs2 = instruction[1]   # 暫存器2，儲存的是資料
                    imm = instruction[2]   # 立即數
                    rs1 = instruction[3]   # 暫存器1，儲存的是記憶體位址
                    s = sType()  # 創建sType實例
                    s.process(inst, rd, rs1, imm, registers, memory)
                elif instructionType == "B":
                    # 假設指令B-type是類似beq x1, x2, 4格式
                    inst = instruction[0]  # 指令名稱
                    rs1 = instruction[1]   # 暫存器1
                    rs2 = instruction[2]   # 暫存器2
                    imm = instruction[3]   # 立即數
                    b = bType()  # 創建bType實例
                    self.pc = b.process(inst, rs1, rs2, imm, registers, self.pc) - 4
                elif instructionType == "U":
                    # 假設指令U-type是類似lui a7, 0格式
                    inst = instruction[0]  # 指令名稱
                    rd = instruction[1]    # 目標寄存器
                    imm = instruction[2]   # 立即數
                    u = uType()  # 創建uType實例
                    u.process(inst, rd, imm, registers, self.pc)
                elif instructionType == "J":
                    # 假設指令J-type是類似jal x1, 100格式
                    inst = instruction[0]  # 指令名稱
                    rd = instruction[1]    # 目標寄存器
                    imm = instruction[2]   # 立即數
                    j = jType()  # 創建jType實例
                    self.pc = j.process(inst, rd, imm, registers, self.pc) - 4
                elif instructionType == "Unknown":
                    # 雖然ecall屬於I-type，但在此先暫時將之分開
                    o = otherType()  # 創建otherType實例
                    o.process(registers)
                
                # 每執行一條指令，程序計數器遞增4
                self.pc = self.pc + 4