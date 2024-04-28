import datetime
import random

import requests
from bs4 import BeautifulSoup
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
import os


def build_coach() -> PromptTemplate:
    return PromptTemplate.from_template("""
    You are a CrossFit coach. You are terse and to the point.
    
    The workout of the day is as follows:
    {workout}
    
    Answer questions about the workout and provide guidance to athletes.
    
    Question: {question}
    """)


def summarize_and_format_wod(llm: Ollama, random_wod: str) -> str:
    return llm.invoke(f"""
    Summarize workout in Markdown format, without any scaling options or extra notes and information:
    {random_wod}
    """.strip())


def scrape_crossfit_for_wod(year, month, day) -> str:
    print(f"Scraping CrossFit for WOD for {year}-{month}-{day} from {os.getenv('CROSSFIT_URL')}")
    url = f"{os.getenv('CROSSFIT_URL')}/workout/{year}/{month}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    workouts = soup.select('div.content-container')
    workout = list(workouts)[-day].select('div.content')[0]
    return workout.get_text()


def fetch_wod() -> str:
    # generate some random year between 2006 and 2024
    current_year = datetime.datetime.now().year
    epoch = int(os.getenv("BOT_MEMORY_START_YEAR")) if isinstance(os.getenv("BOT_MEMORY_START_YEAR"), int) else 2006
    year = random.randrange(epoch, current_year + 1)
    month = random.randrange(1, 13)
    last_day_of_month = (datetime.datetime(year, month + 1, 1) - datetime.timedelta(days=1)).day
    day = random.randrange(1, last_day_of_month + 1)
    return scrape_crossfit_for_wod(year, month, day)


def response_generator(llm: Ollama, coach: PromptTemplate, wod: str, question: str):
    output = (coach | llm).stream({"workout": wod, "question": question})
    for word in output:
        yield word
