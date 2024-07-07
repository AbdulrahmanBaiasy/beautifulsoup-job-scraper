# TimesJobs Job Scraper

This Python script scrapes recent job postings from TimesJobs.com based on a provided job title and skill. It saves matching job details to individual text files in the "posts" folder.


[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)


## Introduction

This web scraper is designed to help you quickly find relevant job postings by filtering based on your skills. It automates the process of checking for new listings at regular intervals.

## Technologies Used

* Python 3
* Requests (for fetching web pages)
* BeautifulSoup4 (for parsing HTML)
* lxml (HTML parser for BeautifulSoup)
* os (for file/directory operations)

## Setup Guide

1. **Clone or Download:**
   - Clone this repository to your local machine 
      ```bash
      git clone [https://github.com/AbdulrahmanBaiasy/beautifulsoup-job-scraper]
      cd beautifulsoup-job-scraper
      ```


2. **Install dependencies:**
   - Excute the following command: 
      ```bash
      pip install -r requirements.txt
      ``` 

3. **Run the Script:**
   - Execute the following command:
      ```bash
      python main.py
      ```

4. **Provide Input:**
   - You'll be prompted to enter:
      - The `job title` you are looking for.
      - A `skill` you are familiar with (this helps filter results).

5. **Let it Run:**
   - The script will start scraping TimesJobs and saving matching jobs to the `posts` folder in the same directory.

6. **Review Results:**
   - Check the `posts` folder for text files containing details of the relevant jobs.

## Customization

- **Job Title and Skill:** Change the input values when prompted to search for different jobs.
- **Update Interval:** Modify the `time_wait` variable in the script to adjust how often it checks for new postings.

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional features.

## License

This project is licensed under the MIT License 

## Disclaimer

This script is intended for personal use and educational purposes. Please use it responsibly and respect the terms of service of TimesJobs.com.
