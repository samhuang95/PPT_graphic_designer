import os
import json
import google.generativeai as genai
from dotenv import load_dotenv



class AIProcessor:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Warning: GEMINI_API_KEY not found in .env file. AI features will be disabled.")
            self.model = None
            return

        try:
            genai.configure(api_key=api_key)
            # Use gemini model as it is available and capable
            model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
            self.model = genai.GenerativeModel(model_name)
            print(f"AI Processor initialized with Gemini model ({model_name}).")
        except Exception as e:
            print(f"Failed to initialize Gemini API: {e}")
            self.model = None

    def structure_slide_content(self, raw_text_list):
        """
        將雜亂的文字列表傳給 LLM，請它分析並回傳結構化的 JSON (Title, Body)。
        """
        if not self.model:
            return {"title": "", "body": raw_text_list}

        combined_text = "\n".join(raw_text_list)

        prompt = f"""
        You are a professional presentation designer.
        I have extracted some text from a PowerPoint slide, but the structure is lost.
        Please analyze the text and identify which part is likely the 'Title' and which parts are the 'Body' content.

        Raw Text from Slide:
        ---
        {combined_text}
        ---

        Instructions:
        1. Identify the most suitable text for the slide Title.
        2. Organize the rest of the text into a list of Body points.
        3. Return ONLY a valid JSON object. Do not include any markdown formatting or explanations.

        JSON Structure:
        {{
            "title": "The identified title",
            "body": ["point 1", "point 2", "point 3"]
        }}
        """

        try:
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()

            # 清理可能存在的 Markdown 標記 (```json ... ```)
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]

            data = json.loads(response_text.strip())
            return data

        except Exception as e:
            print(f"Error during AI processing: {e}")
            # 發生錯誤時的回退機制：第一行當標題，其餘當內文
            if raw_text_list:
                return {"title": raw_text_list[0], "body": raw_text_list[1:]}
            return {"title": "", "body": []}
