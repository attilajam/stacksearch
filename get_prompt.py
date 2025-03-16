import os 
from dotenv import load_dotenv
from google import genai
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
def get_prompt(problem):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"Reword the following math problem into a search prompt that can be used to find an explanation to a similar problem from forums like Math Stack Exchange and etc. The goal of the rewording is to generalize the problem, so that the student can look at one problem, and apply the steps to another, improving their learning. Like for example, if I ask you to find the PDF of X+Y, when X and Y is of the Exponential distribution, you would return \"What is the sum of two random variables of the exponential distribution\". Got it? The math problem that I want you to turn into a search prompt is {problem}. Give up to 3 search prompts and format them in one line separated by a comma, with no symbols around each prompt. This formatting part is the most important."
    )
    return response.text.split(",")

if __name__ == "__main__":
    print(get_prompt("Suppose that Z ∼ N (0, 1) is a standard normal random variable. Use the Z-Table for the following: Use the table to calculate P (Z ≥ −0.25) and P (Z ≥ 1.06). (The table won’t give these answers directly. You should show how you convert these to questions that can be answered with the table."))
