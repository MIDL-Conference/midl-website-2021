#!/usr/bin/env python3.9

import json
from typing import Dict

from bs4 import BeautifulSoup

from paper import Paper, PaperEncoder


if __name__ == "__main__":
        paper_json: str = "papers.json"
        pmlr_file: str = "pmlr143.html"

        raw_papers: Dict[str, Dict]
        with open(paper_json, 'r') as pf:
                raw_papers = json.load(pf)
        papers: Dict[str, Paper] = {v["title"].lower(): Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()}

        with open(pmlr_file, 'r') as f:
                pmlr_soup = BeautifulSoup(f.read(), 'html.parser')

        for div in pmlr_soup.find_all("div", {"class": "paper"}):
                title: str = div.find("p", {"class": "title"}).get_text()

                san_title: str = title.replace('\n', '').lower()

                if san_title not in papers.keys():
                        if san_title == "preface":
                                continue
                        elif san_title == 'beyond pixel-wise supervision for segmentation: a few global shape descriptors might be surprisingly good!':
                                san_title = 'Beyond pixel-wise supervision: semantic segmentation with higher-order shape descriptors'.lower()
                        elif san_title == 'understanding and visualizing generalization in unets':
                                san_title = "Understanding and Visualizing Generalization UNets".lower()
                        elif san_title == 'learning the latent heat diffusion process through structural brain network from longitudinal ββ-amyloid data':
                                san_title = "Learning the Latent Heat Diffusion Process through Structural Brain Network from Longitudinal \u03b2-Amyloid Data".lower()
                        else:
                                print(title)

                url: str = div.find("p", {"class": "links"}).find_all('a', href=True)[0]['href']
                assert url[-4:] == "html"

                papers[san_title].pmlr_url = url

        with open(paper_json, 'w') as sink:
                json.dump({p.id: p for p in papers.values()}, sink, cls=PaperEncoder, indent=4, sort_keys=True)
