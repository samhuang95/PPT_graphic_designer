from src.content_extractor import ContentExtractor
from src.slide_generator import SlideGenerator
import os

def main():
    input_pptx = "input.pptx"
    ref_pptx = "ref.pptx"
    output_pptx = "output_phase3.pptx"

    if not os.path.exists(input_pptx) or not os.path.exists(ref_pptx):
        print("Error: Input or Template file not found.")
        return

    # 1. Extract Content
    extractor = ContentExtractor()
    content_data = extractor.extract(input_pptx)

    # 2. Generate Slides with Intelligent Mapping
    generator = SlideGenerator(ref_pptx)
    generator.generate(content_data, output_pptx)

    print(f"Success! Output saved to {output_pptx}")

if __name__ == "__main__":
    main()
