#!/usr/bin/env python3.9

import json
from sys import argv
from pathlib import Path
from typing import Dict

from paper import Paper


if __name__ == "__main__":
    assert len(argv) == 2

    papers_path: Path = Path(argv[1])
    assert papers_path.exists()

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[str, Paper] = {k: Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

    for paper in papers.values():
        if paper.short:
            continue
        first_author: str = paper.authors[0].split(' ')[-1]
        det: str = "Oral presentation" if paper.oral else "Splotlight presentation"
        print("\n>>>")
        print(f"MIDL 2021, {paper.id}, {first_author} et al. {det}")
        print(f"{paper.id} - {paper.title}\n\n{', '.join(paper.authors)}")
        print(f"\nConference page: https://2021.midl.io/{paper.url}")
        print(f"PDF: https://openreview.net/pdf?id={paper.or_id}")
        print(f"\nAbstract: {paper.sanitized_abstract}")
