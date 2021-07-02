#!/usr/bin/env python3.9

import json
from sys import argv
from pathlib import Path
# from operator import attrgetter

from paper import Paper


if __name__ == "__main__":
    assert len(argv) == 5

    template_path: Path = Path(argv[1])
    assert template_path.exists()

    papers_path: Path = Path(argv[2])
    assert papers_path.exists()

    dest_path: Path = Path(argv[3])

    root_content: Path = Path(argv[4])

    raw_papers: dict[str, dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: dict[str, Paper] = {k: Paper(**v) for (k, v) in raw_papers.items()}

    with open(template_path, 'r') as f:
        empty_template: str = f.read()

    paper: Paper
    for paper in papers.values():
        result: str = empty_template[:]

        result = result.replace("CONF_ID", paper.id)
        result = result.replace("TITLE", paper.title)
        result = result.replace("AUTHORS", ", ".join(paper.authors))
        result = result.replace("ORID", paper.or_id)
        result = result.replace("PDF_URL", paper.pdf)
        result = result.replace("ABSTRACT", paper.sanitized_abstract)
        result = result.replace("SCHEDULE", "<br>".join(paper.schedule))
        result = result.replace("TEASER", paper.yt_teaser)

        if paper.award:
            result = result.replace("AWARD", f"## {paper.award}")
        else:
            result = result.replace("AWARD", "")

        if paper.yt_teaser:
            result = result.replace("EMBEDEDTEASE", f"{{{{ youtube('{paper.yt_teaser}') }}}}")
        else:
            result = result.replace("EMBEDEDTEASE", "")

        result = result.replace("PROCEEDINGS", "")
        # if paper.short:
        # else:
        #     result = result.replace("PROCEEDINGS", f'\n- <a href="{paper.pmlr_url}">Proceedings</a>')

        # slides_path: Path = Path(paper.slides)

        # if not (root_content / paper.slides[1:]).exists():
        #     print(f"\tPaper {paper.id} without slides: {paper.url} {(root_content / paper.slides)}")

        slides_ok: bool = (root_content / paper.slides[1:]).exists()
        video_ok: bool = (root_content / paper.yt_full[1:]).exists()

        # yt_link = paper.yt_teaser if paper.short else paper.yt_full
        yt_link = paper.yt_full

        if video_ok and slides_ok:
            result = result.replace("PRESENTATION", f"{{{{ html_presentation('{yt_link}', '{paper.slides}', 720, 450) }}}}")
            # print(f"\tPaper {paper.id} has both slides or presentation.")
        elif video_ok and not slides_ok:
            result = result.replace("PRESENTATION", f"{{{{ video('{yt_link}') }}}}")
            print(f"\tPaper {paper.id} without slides: {(root_content / paper.slides)}")
        elif not video_ok and slides_ok:
            # result = result.replace("PRESENTATION", f"{{{{ video('{yt_link}') }}}}")
            print(f"\tPaper {paper.id} without video: {(root_content / yt_link)}")
        else:
            result = result.replace("PRESENTATION", "")
            print(f"\tPaper {paper.id} with neither slides or presentation: {(root_content / paper.slides)} {(root_content / yt_link)}")

        oral_text: str
        if paper.oral:
            oral_text = "Oral presentation"
        elif paper.poster:
            oral_text = "Poster presentation"
        elif paper.short:
            oral_text = "Short paper"

        result = result.replace("ORAL", oral_text)

        with open((dest_path / Path(paper.url)).with_suffix(".md"), 'w') as sink:
            sink.write(result)
