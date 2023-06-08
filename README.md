# crawler - Python webcrawler

A very simple webcrawler built on `requests` and `beautifulsoup4`. This project's code is mainly taken from a different project with a much narrower scope on the type of websites to be scraped. This project will be expanded over time to offer better support for more generalized webscraping

## Setup

1. Clone this repository locally!
2. Install all the dependencies, ideally in a virtual environment
   ```bash
   python3 -m venv venv
   source ./venv/bin/activate
   pip install -r requirements.txt
   ```
3. Create a folder to store the downloaded websites in
   ```bash
   mkdir websites
   ```
4. Run the crawler. In this example, the crawler will download the entire website tree into the `websites/skunichetty_dev` folder
   ```bash
   python3 -m crawler www.skunichetty.dev websites/skunichetty_dev
   ```
