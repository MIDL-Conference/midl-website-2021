#!/usr/bin/env python3.9

import json


class Paper():
    def __init__(self, id: str, title: str, authors: str, url: str, or_id: str, oral: str, short: str,
                 abstract: str, schedule: str = "", slides: str = "", yt_teaser: str = "",
                 yt_full: str = "", ignore_schedule: bool = False, award: str = "",
                 pdf: str = "", pmlr_url=""):
        self.id: str = id
        self.title: str = title
        self.authors: list[str] = authors.split(', ')
        self.url: str = url
        self.or_id: str = or_id
        self.oral: bool = oral == "True"
        self.short: bool = short == "True"
        self.poster: bool = (not self.short) and (not self.oral)
        self.abstract: str = abstract
        self.slides: str = slides
        self.yt_teaser: str = yt_teaser
        self.yt_full: str = yt_full
        self.award: str = award

        self.pmlr_url: str = pmlr_url
        assert not (self.short and self.pmlr_url)

        self.pdf: str
        self.pdf = f'https://openreview.net/pdf?id={self.or_id}' if not pdf else pdf

        # if self.short:
        # else:
        #     pmlr_id: str = self.pmlr_url.split('/')[-1].replace(".html", "")
        #     self.pdf_url = f"http://proceedings.mlr.press/v121/{pmlr_id}/{pmlr_id}.pdf"

        self.schedule: list[str]
        if not schedule:
            self.schedule = []
        else:
            self.schedule = schedule.split('\n')

        assert not (self.oral and self.short)
        if self.short:
            assert not self.oral

        # if not ignore_schedule:
        #     try:
        #         if not self.oral:
        #             assert len(self.schedule) == 1
        #         else:
        #             assert len(self.schedule) == 2
        #     except AssertionError:
        #         print(self.id, self.schedule)

        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        self.sanitized_abstract = sanitized_abstract

        # self.__class__.__name__: str = "Paper"

    def __str__(self) -> str:
        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        sanitized_abstract = repr(sanitized_abstract)

        return f'''{{{{ paper({repr(self.title)},
        \'{f'{", ".join(self.authors)}'}\',
        openreview=\'{f'https://openreview.net/forum?id={self.or_id}'}\',
        pdf=\'{self.pdf}\',
        id='{self.id}',
        paper='{self.url}',
        proceedings='{self.pmlr_url}',
        abstract={sanitized_abstract})
}}}}'''
        # teaser=\'{f'https://youtu.be/{self.yt_teaser}' if self.yt_teaser else ""}\',
        # video=\'{self.yt_full if self.yt_full else ""}\',


class PaperEncoder(json.JSONEncoder):
    def default(self, paper):
        if isinstance(paper, Paper):
            return {"id": str(paper.id),
                    "title": paper.title,
                    "authors": ", ".join(paper.authors),
                    "url": paper.url,
                    "pdf": paper.pdf,
                    "or_id": paper.or_id,
                    "oral": str(paper.oral),
                    "short": str(paper.short),
                    "abstract": paper.abstract,
                    "schedule": "\n".join(paper.schedule),
                    "slides": paper.slides,
                    "yt_teaser": paper.yt_teaser,
                    "yt_full": paper.yt_full,
                    "award": paper.award,
                    "pmlr_url": paper.pmlr_url}

        return json.JSONEncoder.default(self, paper)
