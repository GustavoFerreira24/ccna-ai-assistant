from pptx import Presentation
from pptx.util import Inches

from src.extract_pptx import clean_text, extract_slides


def test_clean_text():
    text = "  Network Components  \n\n   Host Roles   \n"

    result = clean_text(text)

    assert result == "Network Components\nHost Roles"


def test_extract_slides(tmp_path):
    file_path = tmp_path / "sample.pptx"

    presentation = Presentation()

    # First slide: should be skipped
    slide1 = presentation.slides.add_slide(presentation.slide_layouts[6])
    textbox = slide1.shapes.add_textbox(Inches(1), Inches(1), Inches(5), Inches(1))
    textbox.text = "Instructor notes"

    # Second slide: contains a table
    slide2 = presentation.slides.add_slide(presentation.slide_layouts[6])
    table = slide2.shapes.add_table(
        2, 2, Inches(1), Inches(1), Inches(5), Inches(2)
    ).table

    table.cell(0, 0).text = "LAN"
    table.cell(0, 1).text = "WAN"
    table.cell(1, 0).text = "Local"
    table.cell(1, 1).text = "Wide"

    presentation.save(file_path)

    documents = extract_slides(file_path, start_slide=2)

    assert len(documents) == 1
    assert documents[0]["source"] == "sample.pptx"
    assert documents[0]["slide_number"] == 2
    assert "LAN | WAN" in documents[0]["text"]
    assert "Local | Wide" in documents[0]["text"]

    all_documents = extract_slides(file_path)

    assert len(all_documents) == 2
    assert all_documents[0]["slide_number"] == 1
