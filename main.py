import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from typing import Dict
import argparse
import json

# logger config
logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO)

BASE_URL = "https://www.hpmor.com/chapter/"


def crawlChapter(chapter_nr: int) -> Dict[int, str]:
    """
    A function to crawl a specific HPMOR chapter.
    This functions is a blocking function.
    """

    complete_url = urljoin(BASE_URL, str(chapter_nr))
    logging.info(f"Crawling {complete_url}")
    resp = requests.get(complete_url)
    if resp.ok == False:
        logging.warning(
            f"Did not receive HTTP OK status (Code: {resp.status_code} - {resp.reason}!"
        )
        return {}

    raw_text = resp.text
    resp.close()

    soup = BeautifulSoup(raw_text, features="html.parser")
    story_div = soup.find("div", {"id": "storycontent"})
    if story_div == None:
        logging.warning(
            f"Did not receive 'storycontent' div for chapter {chapter_nr}! Check correct chapter number or URL!"
        )
        return {}

    paragraph_dict: Dict[int, str] = {}
    paragraphs = story_div.findChildren("p", recursive=False)
    for i, p in enumerate(paragraphs):
        par_text = p.text
        # clean the result text
        par_text = par_text.replace("\n", " ")
        paragraph_dict[i] = p.text

    return paragraph_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A tool to crawl specific chapters from hpmor.com. The results are saved to a JSON file."
    )
    parser.add_argument(
        "-s",
        "--start_chapter",
        type=int,
        help="An integer to indicate the first chapter that shall be crawled.",
        default=1,
        required=False,
    )
    parser.add_argument(
        "-e",
        "--end_chapter",
        type=int,
        help="An integer to indicate the last chapter that shall be crawled.",
        default=21,
        required=False,
    )
    args = parser.parse_args()

    start_i = args.start_chapter
    end_i = args.end_chapter
    logging.info(f"Crawling chapters {start_i} to {end_i}")
    logging.info("These chapters partly include notes/ mentions from the author (mostly at the start of every chapter)!")

    chapter_dict: Dict[int, Dict[int, str]] = {}

    for i in range(start_i, end_i + 1):
        result = crawlChapter(i)
        if result != {}:
            chapter_dict[i] = result

    with open("crawled.json", "w+") as f:
        json.dump(chapter_dict, f)
