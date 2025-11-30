# 開發任務與執行順序 (Development Plan)

本文件列出開發「簡報自動化設計系統」所需的步驟與任務清單。

## 第一階段：概念驗證與基礎建設 (Phase 1: POC & Infrastructure)

**目標**: 確認 `python-pptx` 能夠讀取內容並套用範本。

1. **環境建置**:
   - [V] 安裝 Python 環境。
   - [V] 安裝 `python-pptx`。
2. **POC 腳本開發**:
   - [V] 任務 1.1: 撰寫腳本讀取一個簡單的「內容 PPT」，印出每一頁的文字內容。
   - [V] 任務 1.2: 撰寫腳本讀取一個「範本 PPT」，列出所有可用的版面配置 (Layouts) 名稱。
   - [V] 任務 1.3: 嘗試建立一個新 PPT，使用範本中的某個版面，並填入 "Hello World" 文字。

## 第二階段：核心邏輯開發 (Phase 2: Core Logic Implementation)

**目標**: 完成基本的「文字內容」遷移功能。

3. **內容解析器 (Content Parser)**:
   - [V] 開發 `ContentExtractor` 類別，將每一頁的結構 (標題、內文列表) 轉換為結構化資料 (JSON/Dict)。
4. **合成引擎 (Composition Engine)**:
   - [V] 開發 `SlideGenerator` 類別。
   - [V] 實作「標題對標題」(Title-to-Title) 的映射邏輯。
   - [V] 實作「內文對內文」(Body-to-Body) 的映射邏輯。
   - [V] 處理基本的文字格式保留 (粗體、斜體)。

## 第三階段：智慧映射與版面選擇 (Phase 3: Intelligent Mapping)

**目標**: 讓程式能根據內容多寡自動選擇版面，而非固定使用同一種。

5. **版面選擇邏輯**:
   - [ ] 實作規則：若只有標題 -> 使用「標題投影片 (Title Slide)」或「章節頁 (Section Header)」。
   - [ ] 實作規則：若有標題 + 少量文字 -> 使用「標題及物件 (Title and Content)」。
   - [ ] 實作規則：若有標題 + 兩欄文字 -> 使用「兩欄內容 (Two Content)」。
6. **溢出處理**:
   - [ ] 偵測文字是否過多，若過多則自動縮小字級或拆分為兩頁 (選用)。

## 第四階段：進階功能 (Phase 4: Advanced Features - Optional)

**目標**: 處理圖片與 AI 整合。

7. **圖片處理**:
   - [ ] 支援從內容頁提取圖片並放入範本對應的圖片佔位符。
8. **AI 整合 (LLM)**:
   - [ ] 串接 LLM API。
   - [ ] 任務：利用 LLM 解析非結構化內容 (如純文字方塊堆疊)，轉換為標準 JSON 結構 (解決內容檔結構混亂問題)。
   - [ ] 任務：請 AI 讀取頁面文字，建議該頁面的「視覺重點」或「適合的版面類型」。
   - [ ] 任務：請 AI 幫忙精簡文字以符合版面限制。

## 第五階段：介面與封裝 (Phase 5: UI & Packaging)

**目標**: 讓一般使用者方便使用。

9. **CLI 工具**:
   - [ ] 製作命令列介面 `python main.py input.pptx template.pptx output.pptx`。
10. **(選用) 簡單 GUI**:
    - [ ] 使用 Streamlit 或 Tkinter 製作簡單的檔案上傳介面。
