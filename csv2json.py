#!/usr/bin/env python3.9

import json
from pprint import pprint
from typing import Optional

from bs4 import BeautifulSoup
import pandas as pd


from paper import Paper, PaperEncoder


if __name__ == "__main__":
        short_file: str = "short_papers.csv"
        long_file: str = "long_papers.csv"
        program_file: str = "program.html"
        output_file: str = "papers.json"

        program_dict: dict[str, tuple[str, str]] = {}  # openreview key: [conf_id, Schedule]

        current_time: Optional[str] = None
        conf_id: str
        openreview_id: str
        with open(program_file, 'r') as f:
                for line in f:
                        if "<h3>" in line:
                                current_time = BeautifulSoup(line, 'html.parser').h3.text
                        elif 'target="_blank">' in line:
                                conf_id = line.split(':')[0]
                                openreview_url = BeautifulSoup(line, 'html.parser').a['href']
                                openreview_id = openreview_url.split("id=")[1]

                                assert current_time is not None
                                program_dict[openreview_id] = (conf_id, current_time)

        # pprint(program_dict)

        df_long_papers: pd.DataFrame
        df_long_papers = pd.read_csv(long_file,
                                     sep=',',
                                     dtype={"number": int,
                                            "forum": str,
                                            "title:": str,
                                            "abstract": str,
                                            "authors": str,
                                            "decision": str})
        # print(df_long_papers)

        orals: list[str] = ["A1", "A2", "A3",
                            "D1", "D2", "D3",
                            "E1", "E2", "E3",
                            "H1", "H2", "H3",
                            "L1", "L2", "L3"]

        papers: list[Paper] = []
        for _, csv_line in df_long_papers.iterrows():
                if csv_line['decision'] == "Reject":
                        continue

                authors: list[str] = csv_line['authors'].split('|')

                or_id: str = csv_line['forum'].split("?id=")[1]
                id_: str
                schedule: str
                id_, schedule = program_dict[or_id]

                oral: bool = id_ in orals

                current_paper: Paper = Paper(id=id_,
                                             title=csv_line['title'],
                                             authors=', '.join(authors),
                                             url=f"papers/{id_}.html",
                                             or_id=or_id,
                                             oral=str(oral),
                                             short="False",
                                             abstract=csv_line['abstract'],
                                             schedule=schedule,
                                             ignore_schedule=True)

                # print(f"{{{{{current_paper.id}}}}}")

                papers.append(current_paper)

        df_short_papers: pd.DataFrame
        df_short_papers = pd.read_csv(short_file,
                                      sep=',',
                                      dtype={"number": int,
                                             "forum": str,
                                             "title:": str,
                                             "abstract": str,
                                             "authors": str,
                                             "decision": str})

        for _, csv_line in df_short_papers.iterrows():
                if csv_line['decision'] == "Reject":
                        continue

                authors = csv_line['authors'].split('|')

                or_id = csv_line['forum'].split("?id=")[1]
                id_
                schedule
                id_, schedule = program_dict[or_id]

                current_paper = Paper(id=id_,
                                      title=csv_line['title'],
                                      authors=', '.join(authors),
                                      url=f"papers/{id_}.html",
                                      or_id=or_id,
                                      oral="False",
                                      short="True",
                                      abstract=csv_line['abstract'],
                                      schedule=schedule,
                                      ignore_schedule=True)

                print(f"{{{{{current_paper.id}}}}}")

                papers.append(current_paper)

        with open(output_file, 'w') as sink:
                json.dump({p.id: p for p in papers}, sink,
                          cls=PaperEncoder, indent=4, sort_keys=True)
