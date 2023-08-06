import oneai
import pytest
from tests.constants import DOCUMENT, URL_INPUT


def test_custom_text():
    pipeline = oneai.Pipeline(
        [
            oneai.Skill("enhance", text_attr="custom_text"),
        ]
    )
    output = pipeline.run(DOCUMENT)
    assert (
        hasattr(output, "custom_text")
        and output.custom_text is not None
        and hasattr(output.custom_text, "text")
        and output.custom_text.text is not None
    )


def test_custom_labels():
    pipeline = oneai.Pipeline(
        [
            oneai.Skill("enhance", labels_attr="custom_labels"),
        ]
    )
    output = pipeline.run(DOCUMENT)
    assert hasattr(output, "custom_labels") and output.custom_labels is not None


def test_custom_text_and_labels():
    pipeline = oneai.Pipeline(
        [
            oneai.Skill(
                "enhance", text_attr="custom_text", labels_attr="custom_labels"
            ),
        ]
    )
    output = pipeline.run(DOCUMENT)
    assert hasattr(output, "custom_text") and output.custom_text is not None
    assert (
        hasattr(output.custom_text, "custom_labels")
        and output.custom_text.custom_labels is not None
    )


def test_custom_within_pipeline():
    pipeline = oneai.Pipeline(
        [
            oneai.skills.Summarize(),
            oneai.Skill(
                "enhance", text_attr="custom_text", labels_attr="custom_labels"
            ),
            oneai.skills.Proofread(),
            oneai.skills.Anonymize(),
        ]
    )
    output = pipeline.run(DOCUMENT)
    assert hasattr(output.summary, "custom_text")
    assert hasattr(output.summary.custom_text, "text")
    assert hasattr(output.summary.custom_text, "custom_labels")
    assert hasattr(output.summary.custom_text, "proofread")
    assert hasattr(output.summary.custom_text.proofread, "replacements")


def test_modify_predefined_skill():
    pipeline = oneai.Pipeline([oneai.skills.HtmlToArticle(labels_attr="magic_labels")])
    output = pipeline.run(URL_INPUT)
    assert (
        hasattr(output.html_article, "magic_labels")
        and output.html_article.magic_labels
    )


def test_init_skill():
    attrs = ["prompt_fields", "prompt", "temperature"]
    skill = oneai.skills.GPT()
    assert all(hasattr(skill, a) for a in attrs)
    # should not crash - allow params not defined explicitly in SDK
    with pytest.warns(UserWarning):
        skill.fake_param = "fake"
