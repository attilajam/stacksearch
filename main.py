from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel
from search_results import search_math_stackexchange
from typing import List, Dict, Optional
# Create FastAPI app
app = FastAPI(title="Math StackExchange Search")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define search result model
class SearchResult(BaseModel):
    title: str
    link: str

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search")
async def search(problem: str = Form(...)):
    results = search_math_stackexchange(problem)
    return results  # Return the results array directly, not wrapped in an object

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
