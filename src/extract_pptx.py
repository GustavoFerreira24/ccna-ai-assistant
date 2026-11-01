from pathlib import Path
from pptx import Presentation


def clean_text(text: str) -> str:
    lines = []

    for line in text.splitlines():
        cleaned_line = " ".join(line.split())

        if cleaned_line:
            lines.append(cleaned_line)

    return "\n".join(lines)



def extract_slides(file_path: Path, start_slide: int = 1) -> list[dict]:
    presentation = Presentation(file_path)
    documents = []

    for slide_number, slide in enumerate(presentation.slides, start=1):
        if slide_number < start_slide:
            continue

        text_parts = []

        for shape in slide.shapes:
            if shape.has_text_frame:
                text_parts.append(shape.text)

            elif shape.has_table:
                for row in shape.table.rows:
                    cells = [cell.text for cell in row.cells]
                    text_parts.append(" | ".join(cells))

        text = clean_text("\n".join(text_parts))

        if text:
            documents.append({
                "source": file_path.name,
                "slide_number": slide_number,
                "text": text,
            })

    return documents


if __name__ == "__main__":
    file_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "documents"
        / "private"
        / "ITN_Module_1.pptx"
    )

    documents = extract_slides(file_path, start_slide=12)

    print(f"Extracted {len(documents)} slides.\n")

    
    for document in documents:
        if document["slide_number"] in (19, 30):
            print(f"Source: {document['source']}")
            print(f"Slide: {document['slide_number']}")
            print(document["text"])
            print("-" * 50)

