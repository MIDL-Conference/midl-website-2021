#!/usr/bin/env python3.8

import json
import re
from sys import argv
from pathlib import Path
from typing import Dict, List, Match, Pattern

from paper import Paper


if __name__ == "__main__":
    assert len(argv) == 4

    template_path: Path = Path(argv[1])
    assert template_path.exists()

    papers_path: Path = Path(argv[2])
    assert papers_path.exists()

    # mode: str = argv[3]
    # assert mode in ["short", "full"]

    dest_path: Path = Path(argv[3])

    raw_papers: Dict[str, Dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: Dict[int, Paper] = {int(k): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

    template: str
    with open(template_path, 'r') as f:
        template = f.read()
    filled = template[:]

    regexp: Pattern = re.compile("{{[OSP]([0-9]+)}}")
    matches: List[Match] = list(regexp.finditer(template))

    print(len(matches))
    # print(matches)
    for m in matches:
        # id = m[1][2:-2]
        int_id: int = int(m[1])
        # print(m[0], int_id)
        # print(papers[int_id])

        filled = filled.replace(m[0], str(papers[int_id]))

    with open(dest_path, 'w') as sink:
        sink.write(filled)
