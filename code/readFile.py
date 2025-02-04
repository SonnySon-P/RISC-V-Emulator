import re

class readFile:
    def __init__(self, file, memory):
        self.file = file
        self.memory = memory
        self.address = 0  # 用來跟蹤內存地址

    def processLine(self, line: str) -> list:
        # 去掉註解部分，註解從"#"開始到行末
        lineSplit = line.split("#")
        line = lineSplit[0]  # 取註解前的部分

        # 使用正則表達式替換逗號和小括號
        rePunc = re.compile(r"[(),]")
        line = rePunc.sub(" ", line)
        
        # 使用正則表達式替換多餘的空格
        reSpace = re.compile(r"\s+")
        line = reSpace.sub(" ", line)
        
        # 去除字串前後的空白並根據空格分割
        pl = line.strip().split(" ")
        
        return pl if pl else None  # 如果結果非空，返回列表，否則返回None
    
    def read(self):
        insideCode = False  # 用來標記是否進入程式碼區塊
        for line in self.file:
            line = self.processLine(line)  # 去除註解，並格式化每行指令
            
            # 從_start:以下開始讀取
            if line is not None:
                if line[0].startswith("_start:"):  # 檢查_start:標記
                    insideCode = True  # 開始讀取指令
                    continue  # 跳過_start:行本身

                if insideCode == True and line[0] != "":
                    self.memory.write(self.address, line)  # 將指令寫入記憶體
                    self.address = self.address + self.memory.wordSize  # 更新內存地址