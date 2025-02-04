import argparse
from readFile import readFile
from RV32IMemory import RV32IMemory
from cpuCore import cpuCore

parser = argparse.ArgumentParser()
parser.add_argument("file", help = "Please enter the RISC-V file name")
args = parser.parse_args()
fileName = args.file

try:
    with open(fileName, "r", encoding="utf-8") as file:
        # 將檔案匯入RV32IMemory
        memory = RV32IMemory()  # 創建memory實例
        fileProcessor = readFile(file, memory)  # 執行readFile
        fileProcessor.read()  # 讀取檔案

    # 執行RISC-V CPU
    core = cpuCore()  # 創建cpu實例
    core.implementation(memory)  # 執行core

except FileNotFoundError:
    print(f"Error: The file {fileName} does not exist.")
except Exception as e:
    print(f"An error has occurred: {e}")