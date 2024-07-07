import requests
from bs4 import BeautifulSoup
import time
import os

def find_jobs(job_title, familiar_skill):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_title}"
    
    # Handling potential errors from requesting
    try:
        html_text = requests.get(url).text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 
    
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    os.makedirs("posts", exist_ok=True)  # Create the 'posts' directory if it doesn't exist
    
    for index, job in enumerate(jobs):
        pub_date_element = job.find("span", class_="sim-posted")
        job_pub_date = pub_date_element.span.text
        if "few" in job_pub_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.strip()
            skills = job.find("span", class_="srp-skills").text.strip()
            more_info = job.header.h2.a["href"]
            if familiar_skill.lower() in skills.lower():  # Case-insensitive comparison
                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f"File saved: {index}.txt")

if __name__ == "__main__":
    print("Enter the job title you're looking for:")
    job_title = input("> ")
    print("Enter a skill you are familiar with:")
    familiar_skill = input("> ")
    
    while True:
        find_jobs(job_title, familiar_skill)
        time_wait = 10
        print(f"Waiting for {time_wait} minutes...")
        time.sleep(time_wait * 60)
