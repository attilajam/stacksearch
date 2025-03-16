import requests
from get_prompt import get_prompt

import os 
from dotenv import load_dotenv
import json
load_dotenv()
API_KEY = os.environ.get("GOOGLE_SEARCH_API_KEY")
link = "https://www.googleapis.com/customsearch/v1"
link = "https://api.stackexchange.com/2.3/search?order=desc&sort=votes&intitle=parameter&site=math"
def search_math_stackexchange(problem):
    search_results = []
    for i in get_prompt(problem):
        link = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=votes&q={i}&site=math"
        response = requests.get(link).json()
        for i in response["items"][:12]:
            search_results.append({"title":i["title"], "link":i["link"]})

    return search_results

    

def search_google_for_math_stackexchange(problem):
    links = []
    for i in get_prompt(problem):
        response = requests.get(f"{link}?q={i}&key={API_KEY}&cx=1721c743e83c24dd6")

        result = response.json()
        questions = []
        answers = []

        for item in result["items"]:
            pagemap = item.get("pagemap", {})
            
            if "question" in pagemap and pagemap["question"]:
                question_data = pagemap["question"][0]
                try:
                    if "upvotecount" in question_data and question_data["upvotecount"]:
                        upvotes = int(question_data["upvotecount"])
                        questions.append({
                            "title": item["title"],
                            "link": item["link"],
                            "upvotes": upvotes
                        })
                except (ValueError, TypeError):
                    pass
            
            if "answer" in pagemap:
                for answer_data in pagemap["answer"]:
                    try:
                        if "upvotecount" in answer_data and answer_data["upvotecount"]:
                            upvotes = int(answer_data["upvotecount"])
                            answers.append({
                                "title": item["title"],  # Use the question title for the answer
                                "link": item["link"],    # Link to the question containing this answer
                                "upvotes": upvotes
                            })
                    except (ValueError, TypeError):
                        pass

        questions.sort(key=lambda x: x["upvotes"], reverse=True)
        answers.sort(key=lambda x: x["upvotes"], reverse=True)

        links = []

        for q in questions[:6]:
            links.append({"title": q["title"], "link": q["link"]})

        for a in answers[:6]:
            links.append({"title": a["title"], "link": a["link"]})
            return links
if __name__ == "__main__":
    links = search_math_stackexchange("Find the integral of x e ^ x")
    print(links)
