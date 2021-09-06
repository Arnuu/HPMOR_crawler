# HPMOR_crawler
A python crawler for the "Harry Potter - Methods of rationality" fan fiction.

## Attention
The text is uncleaned and could contain notes and comments from the authors.
One has to look at the json entries to find these notes.

## Installation
- create virtual environment with *virtualenv*
    - `python3 -m virtualenv env`
- activate virtual environment
    - `source env/bin/activate`
- download required packages
    - `pip3 -r requirements.txt`
## Usage
Specify which chapters this script should download with:
`python3 main.py -s START_CHAPTER -e END_CHAPTER`

The output is saved to a JSON file called: *crawled.json*.

```
usage: main.py [-h] [-s START_CHAPTER] [-e END_CHAPTER] [-t]

A tool to crawl specific chapters from hpmor.com. The results are saved to a JSON file.

optional arguments:
  -h, --help            show this help message and exit
  -s START_CHAPTER, --start_chapter START_CHAPTER
                        An integer to indicate the first chapter that shall be crawled.
  -e END_CHAPTER, --end_chapter END_CHAPTER
                        An integer to indicate the last chapter that shall be crawled.
  -t, --dump-as-txt     If this flag is set, the text is saved as a .txt file instead of a json file.
```
