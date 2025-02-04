# RISC-V Emulator

基於RV32I指令集，設計並實現了一個能夠執行RISC-V組合語言的CPU模擬器。

## 壹、基本說明
**動機：**
隨著近期RISC-V處理器市佔率的穩步提升，我一直希望能深入了解這項技術。回顧過去在學習計算機組織與結構課程時，曾經接觸過另一種精簡指令集架構-MIPS，因此我決定藉由開發一個RISC-V組合語言模擬器，來快速掌握不同指令集的結構與用途。

**目的：**
此程式基於RV32I指令集進行開發(不包含虛擬指令集)，可以通過讀取組合語言檔案(.asm)，執行數位邏輯運算，幫助我深入理解RISC-V指令集的各種細節。

**開發環境：**
* 程式語言：Python
* 程式編輯器：Visual Studio Code

**使用相依套件：**
以下是開發該軟體所使用的Python套件：
* re（能使用正則表達式，來清楚釐清組合語言的語法，不需要安裝）

**檔案說明：**
```bash
.
|-- README.md
|-- 執行畫面.png  # 軟體執行畫面
\-- app  # 開發程式資料夾
      |-- MotionPlanningExample.java  # 主程式
      |-- MenuBar.java  # 設置MenuBar模組
      |-- PolygonPanel.java  # 繪製圖形模組
      |-- AStar.java  # A＊演算法模組
      |-- CheckCollisions.java  # 檢驗碰撞模組
      \-- SmoothPath.java  # 平滑化路徑模組
```
