# 簡報自動化設計系統規格書 (Specification)

## 1. 專案概述 (Project Overview)

本專案旨在開發一套自動化工具，能夠將使用者提供的「純內容簡報 (Content PPT)」與「設計範本 (Template PPT)」進行結合，自動生成一份既保有原始內容又具備專業設計風格的最終簡報。

## 2. 核心功能 (Core Features)

### 2.1 輸入 (Input)

1. **內容來源檔 (Content Source)**: 一個 .pptx 檔案，包含使用者想要呈現的文字、條列式重點，通常無特殊排版或僅有基本預設排版。
2. **設計範本檔 (Design Template)**: 一個 .pptx 檔案，包含母片 (Slide Masters)、版面配置 (Layouts)、字型設定、配色方案及背景設計。

### 2.2 處理核心 (Processing Core)

1. **內容解析 (Content Parsing)**:
   - 提取內容檔中每一頁的標題 (Title)。
   - 提取內文 (Body Text)、條列項目 (Bullets)。
   - (進階) 提取圖片、表格或圖表。
2. **範本分析 (Template Analysis)**:
   - 識別範本中的可用版面配置 (例如：標題頁、圖文版面、純文字版面)。
   - 識別版面中的佔位符 (Placeholders) 類型與位置。
3. **智慧映射 (Intelligent Mapping)**:
   - **規則式映射 (Rule-based)**: 根據內容多寡與類型，自動選擇最合適的範本版面 (例如：內容只有標題 -> 選擇「章節標題頁」)。
   - **AI 輔助 (Optional)**: 利用 LLM (如 GPT) 分析文字語意，決定該頁面適合的視覺呈現方式 (例如：將條列式文字轉化為並排的圖卡佈局)，或進行文字摘要以適應版面。
4. **合成生成 (Generation)**:
   - 建立新投影片，套用選定的範本版面。
   - 將解析出的內容填入對應的佔位符中。
   - 處理字體大小自動調整 (Auto-fit) 以避免溢出。

### 2.3 輸出 (Output)

- 一個完整的 .pptx 檔案，內容源自輸入檔，視覺風格源自範本檔。

## 3. 技術架構 (Technical Architecture)

### 3.1 程式語言與函式庫

- **語言**: Python 3.x
- **核心庫**: `python-pptx` (用於讀寫 PowerPoint 檔案)
- **AI 整合 (選用)**: OpenAI API 或 Azure OpenAI (用於內容理解與版面推薦)

### 3.2 系統流程

1. Load Content PPTX -> Extract Slides Data (Text, Images).
2. Load Template PPTX -> Analyze Layouts.
3. For each slide in Content:
   a. Analyze content structure (e.g., Title + 3 bullet points).
   b. Select matching Layout from Template.
   c. Create new slide using Template Layout.
   d. Copy content to new slide placeholders.
4. Save Result PPTX.

## 4. 限制與邊界條件 (Constraints)

- 內容檔需具備基本的結構 (如使用標準的標題與內文框)，若使用者使用純文字方塊隨意堆疊，解析難度會增加。(解決方案：可引入 LLM 進行語意分析，將非結構化的版面元素重組為結構化資料，以識別標題與內文)。
- 複雜物件 (如 SmartArt、複雜群組圖形) 的轉移可能受限於 `python-pptx` 的支援度。
