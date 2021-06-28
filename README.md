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
