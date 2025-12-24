# PPT Graphic Designer

這是一個自動化 PowerPoint 生成工具，利用 Google Gemini AI 將雜亂的投影片內容重新結構化，並套用指定的設計模板。

## 功能特色

*   **AI 內容重組**: 使用 Gemini AI 分析原始投影片的雜亂文字，自動識別標題與內文。
*   **智慧排版**: 根據內容多寡自動選擇合適的版面配置（例如：單欄或雙欄）。
*   **模板套用**: 支援讀取參考投影片 (`ref.pptx`) 的母片樣式，確保輸出風格一致。

## 快速開始 (Quick Start)

### 1. 環境準備

確保您已安裝 Python 3.8 或以上版本。

安裝必要的 Python 套件：

```bash
pip install python-pptx google-generativeai python-dotenv
```

### 2. 設定 API Key

在專案根目錄建立一個 `.env` 檔案，並填入您的 Google Gemini API Key：

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash  # 可選，預設使用 gemini-2.0-flash
```

### 3. 準備檔案

請在專案根目錄準備以下兩個檔案：

*   `input.pptx`: 包含原始內容的投影片（格式不拘，AI 會讀取其中的文字）。
*   `ref.pptx`: 作為設計模板的投影片（需包含 Title, Section Header, Content 等基本版面）。

### 4. 執行程式

執行主程式 `main_phase4.py`：

```bash
python main_phase4.py
```

程式執行完畢後，將會生成 `output_phase4_ai.pptx`。

## 專案結構

*   `main_phase4.py`: 主程式入口，整合 AI 處理與投影片生成。
*   `src/ai_processor.py`: 負責與 Google Gemini API 溝通，進行內容結構化。
*   `src/slide_generator.py`: 負責讀取模板並生成最終投影片。
*   `check_models.py`: 用於檢查 API Key 是否有效及列出可用模型。
