from typing import Callable
from html_list import tags


def atts_factory(attributes: dict) -> str:
    """Check k, v pairs and stringify them.
    If value is `True` then return just the key without the value.
    """
    return " ".join(f'{k}="{v}"' if v is not True else k for k, v in attributes.items())


## TAG BUILDER
def _el_factory(name: str, end_tag: bool = True) -> Callable:
    if end_tag:
        return lambda c="", a={}: _element(name, c, a)
    else:
        return lambda a={}: _element(name, attributes=a, end_tag=end_tag)


def _element(
    tag: str, content: list | str = "", attributes: dict = None, end_tag: bool = True
):
    """Build a HTML tag with attributes and content."""

    attributes = attributes or {}
    # if content is a list of HTML, join it
    content = "".join(content) if isinstance(content, list) else content

    head = f"<{tag}"
    atts = f" {atts_factory(attributes)}>" if attributes else ">"
    tail = f"{content}</{tag}>" if end_tag else ""

    return f"{head}{atts}{tail}"


# Inject HTML tag elements into Global. ☢️
for tag in tags:
    globals()[tag[0]] = _el_factory(name=tag[0], end_tag=tag[1])
