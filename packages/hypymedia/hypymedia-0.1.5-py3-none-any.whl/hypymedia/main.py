from typing import Callable


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


# (element_name, end_tag)
tags = [
    ("a", True),
    ("abbr", True),
    ("address", True),
    ("area", False),
    ("article", True),
    ("aside", True),
    ("audio", True),
    ("base", False),
    ("blockquote", True),
    ("body", True),
    ("br", False),
    ("button", True),
    ("canvas", True),
    ("caption", True),
    ("circle", True),
    ("cite", True),
    ("code", True),
    ("col", False),
    ("colgroup", True),
    ("data", True),
    ("datalist", True),
    ("dd", True),
    ("del_", True),
    ("details", True),
    ("dialog", True),
    ("div", True),
    ("dl", True),
    ("dt", True),
    ("ellipse", True),
    ("em", True),
    ("embed", False),
    ("fieldset", True),
    ("figcaption", True),
    ("figure", True),
    ("footer", True),
    ("form", True),
    ("h1", True),
    ("h2", True),
    ("h3", True),
    ("h4", True),
    ("h5", True),
    ("h6", True),
    ("head", True),
    ("header", True),
    ("hr", False),
    ("html", True),
    ("iframe", True),
    ("img", False),
    ("input", False),
    ("kbd", True),
    ("label", True),
    ("legend", True),
    ("li", True),
    ("link", False),
    ("main", True),
    ("map", True),
    ("mark", True),
    ("menu", True),
    ("meta", False),
    ("meter", True),
    ("nav", True),
    ("noscript", True),
    ("ol", True),
    ("optgroup", True),
    ("option", True),
    ("output", True),
    ("p", True),
    ("picture", True),
    ("polygon", True),
    ("portal", True),
    ("pre", True),
    ("progress", True),
    ("param", False),
    ("q", True),
    ("rect", True),
    ("s", True),
    ("samp", True),
    ("script", True),
    ("section", True),
    ("select", True),
    ("slot", True),
    ("small", True),
    ("source", False),
    ("span", True),
    ("strong", True),
    ("style", True),
    ("sub", True),
    ("summary", True),
    ("sup", True),
    ("svg", True),
    ("table", True),
    ("tbody", True),
    ("td", True),
    ("template", True),
    ("text", True),
    ("textarea", True),
    ("tfoot", True),
    ("th", True),
    ("thead", True),
    ("time", True),
    ("title", True),
    ("tr", True),
    ("track", False),
    ("u", True),
    ("ul", True),
    ("var", True),
    ("video", True),
    ("wbr", False),
]

for tag in tags:
    globals()[tag[0]] = _el_factory(name=tag[0], end_tag=tag[1])
