#!/usr/bin/env python3.9

import json
from sys import argv
from pathlib import Path
from pprint import pprint
from collections import defaultdict

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

        raw_papers: dict[str, dict]
        with open(papers_path, 'r') as pf:
            raw_papers = json.load(pf)

        # Especially here, we *want* the schedule
        all_papers: list[Paper] = [Paper(ignore_schedule=False, **v) for (_, v) in raw_papers.items()]

        paired_schedule: defaultdict[str, list[Paper]] = defaultdict(list)

        for p in all_papers:
                paired_schedule['\n'.join(p.schedule)].append(p)

        with open(template_path, 'r') as f:
                empty_template: str = f.read()

        for session, session_papers in paired_schedule.items():
                session_id: str = session.split('\n')[1].split('-')[0]
                session_title: str = session.split('\n')[1].split('-')[1].split(':')[1].lstrip().rstrip()
                session_time: str = session.split('\n')[0] + ',' + '-'.join(session.split('\n')[1].split('-')[2:])

                print(session_id, session_title, session_time)

                result: str = empty_template[:]

                result = result.replace("SESSION", session_id)
                result = result.replace("TITLE", session_title)
                result = result.replace("TIME", session_time)
                result = result.replace("CHAIRS", session_papers[0].chairs)

                for p in session_papers:
                        result += '''

---
                        '''

                        result += f'''
[% .papers %]
{p}
[% / %]
                        '''

                        result += f'''
{{{{ video('{p.yt_full}') }}}}
                        '''

                with open(dest_path / f"{session_id}.md", 'w') as sink:
                        sink.write(result)
