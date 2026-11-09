
from pathlib import Path
from html import escape

blog_dir = Path("blog")
projects = Path("Projects.html")

html = projects.read_text(encoding="utf-8")

for file in sorted(blog_dir.glob("*.txt"), reverse=True):
    text = file.read_text(encoding="utf-8").strip()

    if not text:
        continue

    lines = text.splitlines()

    title = lines[0].strip()

    image = ""
    body_lines = []

    for line in lines[1:]:
        if line.startswith("image:"):
            image = line.replace("image:", "", 1).strip()
        else:
            body_lines.append(line)

    body = "<br>\n".join(body_lines).strip()

    image_html = ""

    if image:
        image_html = f'<img src="{escape(image)}" alt="">\n'

    post = f"""
<article>
    <h2>{escape(title)}</h2>
    {image_html}
    <p>{body}</p>
</article>
"""

    html = html.replace(
        "<!-- POSTS -->",
        "<!-- POSTS -->\n" + post,
        1
    )

projects.write_text(html, encoding="utf-8")