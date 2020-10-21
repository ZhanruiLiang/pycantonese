import pytest

from pycantonese import segment
from pycantonese.word_segmentation import Segmenter


@pytest.mark.parametrize(
    "chars, segmenter, expected",
    [
        ("廣東話容唔容易學？", None, ["廣東話", "容", "唔容易", "學", "？"]),
        (
            "廣東話容唔容易學？",
            Segmenter(allow={"容唔容易"}),
            ["廣東話", "容唔容易", "學", "？"],
        ),
        (
            "廣東話容唔容易學？",
            Segmenter(disallow={"廣東話"}),
            ["廣東", "話", "容", "唔容易", "學", "？"],
        ),
        (
            "廣東話容唔容易學？",
            Segmenter(max_word_length=2),
            ["廣東", "話", "容", "唔", "容易", "學", "？"],
        ),
    ],
)
def test_segment(chars, segmenter, expected):
    actual = segment(chars, cls=segmenter)
    assert actual == expected
