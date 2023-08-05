from bs4 import BeautifulSoup
from markdownify import markdownify


def __get_most_relevant_tag(soup):
    """Most relevant, is the deepest parent with the most h1, h2, h3, p tags"""

    def calculate_score(node, depth):
        score = 0
        if node.name and node.name.lower() in ["h1", "h2", "h3", "p"]:
            score += 1 / depth
        if node.children:
            for child in node.children:
                if child.name is not None:
                    score += calculate_score(child, depth + 1)
        return score

    # First remove things we definately don't need.
    for data in soup(["style", "script", "iframe"]):
        data.decompose()

    # Calculate scores for each tag
    tag_scores = {}
    for tag in soup.find_all():
        tag_scores[tag] = calculate_score(tag, 1)

    # Filter out irrelvant tags
    tag_scores = dict(
        filter(
            lambda t: t[0].name
            and t[0].name.lower()
            in [
                "div",
                "span",
                "section",
                "article",
                "body",
                "table",
                "header",
                "main",
                "pre",
                "summary",
            ],
            tag_scores.items(),
        )
    )

    # Normalize scores against the entire DOM
    total_score = sum(tag_scores.values())
    normalized_scores = {tag: score / total_score for tag, score in tag_scores.items()}

    # Return the tag with the highest score.
    return sorted(normalized_scores.items(), key=lambda x: x[1])[-1]


def __replace_link_with_anchor_text(tag):
    """Replaces all links with the text that they contain"""
    for link in tag.find_all("a"):
        link.replace_with(link.text)
    return tag


def __get_well_presented_text(tag):
    """Removes all unessesary images, links etc so that we can have concise text only version"""
    tag = __replace_link_with_anchor_text(tag)
    for t in tag.find_all("img"):
        t.replace_with("")
    return tag


def extract_content(html: str, format="plaintext"):
    soup = BeautifulSoup(html, "html.parser")
    relevant_tag = __get_most_relevant_tag(soup)
    if format == "plaintext":
        return __get_well_presented_text(relevant_tag).get_text()
    if format == "markdown":
        return markdownify(relevant_tag)
    return relevant_tag[0]
