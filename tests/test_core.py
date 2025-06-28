import pytest

from aar_doc.core import DescriptionTags


class TestDescriptionTags:
    @pytest.mark.parametrize(
        ("text", "want"),
        [
            (
                """
                Logging configuration.
                See: https://example.com/docs/common/logging
                ***defaults_prefix:"__"***
                """,
                "\n                Logging configuration.\n                See: https://example.com/docs/common/logging",
            ),
            (
                """
                Logging configuration.
                See: https://example.com/docs/common/logging
                ***defaults_prefix:"__" foo_tag:"brenson asdfdf"***
                """,
                "\n                Logging configuration.\n                See: https://example.com/docs/common/logging",
            ),
            (
                'Logging configuration. See: https://example.com/docs/common/logging ***defaults_prefix:"__" foo_tag:"brenson asdfdf"***',
                "Logging configuration. See: https://example.com/docs/common/logging",
            ),
            (
                'Logging configuration. ***defaults_prefix:"__" foo_tag:"brenson asdfdf"*** See: https://example.com/docs/common/logging',
                "Logging configuration. See: https://example.com/docs/common/logging",
            ),
            (
                "Logging configuration. See: https://example.com/docs/common/logging",
                "Logging configuration. See: https://example.com/docs/common/logging",
            ),
        ],
    )
    def test_replace(self, text, want):
        assert DescriptionTags(text).replace() == want

    @pytest.mark.parametrize(
        ("text", "want"),
        [
            (
                [
                    "A list value",
                    "with a list description with a rather long description, maybe too long.",
                ],
                {},
            ),
            (
                [
                    "A list value",
                    'with a list description with a rather long description, maybe too long. ***defaults_prefix:"__"***',
                ],
                {"defaults_prefix": "__"},
            ),
            (
                [
                    'A list value ***defaults_prefix:"ff" foo_tag:"brenson asdfdf"******',
                    'with a list description with a rather long description, maybe too long. ***defaults_prefix:"__"***',
                ],
                {"defaults_prefix": "__", "foo_tag": "brenson asdfdf"},
            ),
            (
                """
                Logging configuration.
                See: https://example.com/docs/common/logging
                ***defaults_prefix:"__"***
                """,
                {"defaults_prefix": "__"},
            ),
            (
                """
                Logging configuration.
                See: https://example.com/docs/common/logging
                ***defaults_prefix:"__" foo_tag:"brenson asdfdf"***
                """,
                {"defaults_prefix": "__", "foo_tag": "brenson asdfdf"},
            ),
            (
                'Logging configuration. ***defaults_prefix:"__" foo_tag:"brenson asdfdf"*** See: https://example.com/docs/common/logging',
                {"defaults_prefix": "__", "foo_tag": "brenson asdfdf"},
            ),
            (
                'Logging configuration. See: https://example.com/docs/common/logging ***defaults_prefix:"__" foo_tag:"brenson asdfdf"***',
                {"defaults_prefix": "__", "foo_tag": "brenson asdfdf"},
            ),
            (
                "Logging configuration. See: https://example.com/docs/common/logging",
                {},
            ),
        ],
    )
    def test_parse_tags(self, text, want):
        assert DescriptionTags(text)._tags == want

    @pytest.mark.parametrize(
        ("text", "want"),
        [
            (
                """
                Logging configuration.
                See: https://example.com/docs/common/logging
                ***defaults_prefix:"__"***
                """,
                {"defaults_prefix": "__"},
            ),
            (
                """
                Logging configuration.
                See: https://example.com/docs/common/logging
                ***defaults_prefix:"__" foo_tag:"brenson asdfdf"***
                """,
                {"defaults_prefix": "__"},
            ),
            (
                'Logging configuration. See: https://example.com/docs/common/logging ***defaults_prefix:"ff" foo_tag:"brenson asdfdf"***',
                {"defaults_prefix": "ff"},
            ),
            (
                "Logging configuration. See: https://example.com/docs/common/logging",
                {"defaults_prefix": ""},
            ),
        ],
    )
    def test_tags(self, text, want):
        tags = DescriptionTags(text)
        assert tags.defaults_prefix == want["defaults_prefix"]
