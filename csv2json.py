#!/usr/bin/env python3.9

import json

import pandas as pd


from paper import Paper, PaperEncoder


if __name__ == "__main__":
        input_file: str = "long_papers.csv"
        output_file: str = "papers.json"

        df_papers: pd.DataFrame
        df_papers = pd.read_csv(input_file,
                                sep=',',
                                dtype={"number": int,
                                       "forum": str,
                                       "title:": str,
                                       "abstract": str,
                                       "authors": str,
                                       "decision": str})

        # print(df_papers)

        papers: list[Paper] = []
        for _, csv_line in df_papers.iterrows():
                if csv_line['decision'] == "Reject":
                        continue

                id_: str = f"L{csv_line['number']:03d}"
                authors: list[str] = csv_line['authors'].split('|')
                or_id: str = csv_line['forum'].split("?id=")[1]

                current_paper: Paper = Paper(id=csv_line['number'],
                                             title=csv_line['title'],
                                             authors=', '.join(authors),
                                             url=f"papers/{id_}.html",
                                             or_id=or_id,
                                             oral="False",
                                             short="False",
                                             abstract=csv_line['abstract'],
                                             ignore_schedule=True)

                # print(current_paper)

                papers.append(current_paper)

        with open(output_file, 'w') as sink:
                json.dump({p.id: p for p in papers}, sink,
                          cls=PaperEncoder, indent=4, sort_keys=True)
