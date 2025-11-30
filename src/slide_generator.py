from pptx import Presentation

class SlideGenerator:
    def __init__(self, template_path):
        print(f"Loading template from: {template_path}")
        self.template_path = template_path
        self.prs = Presentation(template_path)

        # Analyze layouts to find indices
        self.layout_map = {}
        for i, layout in enumerate(self.prs.slide_layouts):
            self.layout_map[layout.name] = i

        # Define default mappings (can be improved in Phase 3)
        # We look for standard names or fall back to indices
        self.TITLE_LAYOUT_IDX = self.layout_map.get("TITLE", 0)
        self.CONTENT_LAYOUT_IDX = self.layout_map.get("TITLE_AND_BODY", 1)

        print(f"  - Title Layout Index: {self.TITLE_LAYOUT_IDX}")
        print(f"  - Content Layout Index: {self.CONTENT_LAYOUT_IDX}")

    def generate(self, slides_data, output_path):
        print(f"Generating presentation to: {output_path}")

        # [Fix] Clearing existing slides caused file corruption (Duplicate name error).
        # For now, we append new slides after the template slides to ensure file validity.
        # self._clear_existing_slides()

        for i, slide_data in enumerate(slides_data):
            # Simple Rule-based Mapping (Phase 2 level)
            # If it's the first slide, use Title Layout
            # Otherwise use Content Layout
            if i == 0:
                layout_idx = self.TITLE_LAYOUT_IDX
            else:
                layout_idx = self.CONTENT_LAYOUT_IDX

            slide_layout = self.prs.slide_layouts[layout_idx]
            slide = self.prs.slides.add_slide(slide_layout)

            # 1. Set Title
            if slide_data["title"] and slide.shapes.title:
                slide.shapes.title.text = slide_data["title"]

            # 2. Set Body
            # Find the body placeholder (usually index 1, or the one that is not title)
            body_placeholder = None
            for shape in slide.placeholders:
                # Placeholder indices: 0 is usually Title, 1 is Body/Subtitle
                # We can also check element.ph_idx
                if shape.placeholder_format.idx > 0:
                    body_placeholder = shape
                    break

            if body_placeholder and slide_data["body"]:
                tf = body_placeholder.text_frame
                tf.clear() # Clear default placeholder text

                for p_idx, para_data in enumerate(slide_data["body"]):
                    p = tf.add_paragraph()
                    # If it's the very first paragraph of the text frame, add_paragraph adds a second one?
                    # No, clear() removes all text but leaves one empty paragraph usually?
                    # Actually tf.clear() removes all text.
                    # But tf.paragraphs[0] exists.
                    # Let's handle the first paragraph separately or just use the list.
                    if p_idx == 0 and len(tf.paragraphs) == 1 and tf.paragraphs[0].text == "":
                        p = tf.paragraphs[0]

                    for run_data in para_data:
                        run = p.add_run()
                        run.text = run_data["text"]
                        if run_data["bold"]:
                            run.font.bold = True
                        if run_data["italic"]:
                            run.font.italic = True

        self.prs.save(output_path)
        print("Generation complete.")

    def _clear_existing_slides(self):
        # Helper to remove all slides from the template presentation
        # Accessing the private _sldIdLst to clear slides
        xml_slides = self.prs.slides._sldIdLst
        slides = list(xml_slides)
        for s in slides:
            xml_slides.remove(s)
        print(f"Cleared {len(slides)} existing slides from template.")
