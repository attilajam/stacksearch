# Math StackExchange Search
Search the math stack exchange for a generalized solution for a given math problem. 

This is done by calling the Gemini API to generalize the given problem, then sending it to the Google Custom Search API. Then, the search finds at most 12 of the most upvoted results (question or answer), and shows them to the user. 

# Why should you care
The goal of this project is to improve the learning of math students that are dependent on AI, because of how good it is at taking a problem and giving a straight up explanation. The problem with this, is that you forget how to apply a general formula, or other steps to a similar problem to your own, limiting the growth of your learning. That is where this project comes in, aiming to find generalized problems and solutions from the Math StackExchange, and recommend them based on the given problem.

# Installation
```bash
git clone https://github.com/attilajam/stacksearch.git
cd stacksearch
python -m venv venv
source venv/bin/activate 
pip install fastapi uvicorn jinja2 python-multipart google requests python-dotenv
python main.py
```

# TODO
- [ ] Deploy and host the project on a website
- [X] Swap the Google Custom Search API as it is too expensive. (Swapped to StackExchange API 2.3)
- [ ] Improve the prompt to find better search engine prompts
- [ ] Create a better frontend, allowing users to sign up, etc.
Note: the files for the frontend was generated using AI, and doing minimal debugging of the JavaScript. I do not claim the front-end related files as my own work, I specialize in the backend. 
