from normcap.ocr.models import TessArgs


def test_ocr_result(ocr_result):
    """Check if calulated properties are working correctely."""
    assert isinstance(ocr_result.text, str)
    assert ocr_result.text.count("\n") == 0
    assert ocr_result.text.count(" ") >= 2
    assert ocr_result.text.startswith("one")

    assert isinstance(ocr_result.lines, str)
    lines = ocr_result.lines.splitlines()
    assert len(lines) == 2
    assert lines[0] == "one two"

    assert ocr_result.num_blocks == 2
    assert ocr_result.num_pars == 3
    assert ocr_result.num_lines == 2

    assert ocr_result.mean_conf == 30
    ocr_result.words = []
    assert ocr_result.mean_conf == 0

    assert ocr_result.best_scored_magic is None
    ocr_result.magic_scores = {"email": 1.0, "url": 0.7, "paragraph": 0}
    assert ocr_result.best_scored_magic == "email"


def test_tess_args_jpn():
    tess_args = TessArgs(
        path="./tessdata", lang="jpn", oem=111, psm=222, version="4.1.1"
    )
    config = tess_args.to_config_str()
    assert '--tessdata-dir "./tessdata"' in config
    assert "-c preserve_interword_spaces=1" in config
    assert "--oem 111" in config
    assert "--psm 222" in config
    assert tess_args.is_language_without_spaces()


def test_tess_args_eng():
    tess_args = TessArgs(path=None, lang="eng", oem=111, psm=222, version="4.1.1")
    config = tess_args.to_config_str()
    assert "--oem 111" in config
    assert "--psm 222" in config
    assert "--tessdata-dir" not in config
    assert "-c preserve_interword_spaces=1" not in config
    assert not tess_args.is_language_without_spaces()
