#!/usr/bin/env python3.9

import json


class Paper():
    def __init__(self, id: str, title: str, authors: str, url: str, or_id: str, oral: str, short: str,
                 abstract: str, schedule: str = "", slides: str = "", video: str = "",
                 ignore_schedule: bool = False, award: str = "",
                 pdf: str = "", pmlr_url="", youtube_video_id: str = "", cloudflare_video_id: str = "",
                 chairs: str = ""):
        self.id: str = id
        self.title: str = title
        self.authors: list[str] = authors.split(', ')
        self.url: str = url
        self.or_id: str = or_id
        self.oral: bool = oral == "True"
        self.short: bool = short == "True"
        self.poster: bool = (not self.short) and (not self.oral)
        self.abstract: str = abstract.replace('\r\n', '\n').replace('\r','\n').strip()
        self.slides: str = slides
        self.video: str = video
        self.youtube_video_id: str = youtube_video_id
        self.award: str = award
        self.cloudflare_video_id: str = cloudflare_video_id
        self.chairs: str = chairs

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
        sanitized_abstract = sanitized_abstract.replace('\r', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        self.sanitized_abstract = sanitized_abstract

        # self.__class__.__name__: str = "Paper"

    def __str__(self) -> str:
        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('\r', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        sanitized_abstract = repr(sanitized_abstract)

        return f'''{{{{ paper({repr(self.title)},
        \'{f'{", ".join(self.authors)}'}\',
        openreview=\'{f'https://openreview.net/forum?id={self.or_id}'}\',
        pdf=\'{self.pdf}\',
        id='{self.id}',
        paper='{self.url}',
        proceedings='{self.pmlr_url}',
        video=\'{"https://www.youtube.com/watch?v=" + self.youtube_video_id if self.youtube_video_id else self.video}\',
        abstract={sanitized_abstract})
}}}}'''
        # teaser=\'{f'https://youtu.be/{self.yt_teaser}' if self.yt_teaser else ""}\',


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
                    "video": paper.video,
                    "award": paper.award,
                    "pmlr_url": paper.pmlr_url,
                    "youtube_video_id": paper.youtube_video_id,
                    "cloudflare_video_id": paper.cloudflare_video_id,
                    "chairs": paper.chairs}

        return json.JSONEncoder.default(self, paper)
