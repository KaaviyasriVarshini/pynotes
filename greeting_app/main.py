from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Greeting App")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    """Display the empty greeting form"""
    return templates.TemplateResponse(
        "greeting.html",
        {"request": request, "name": None, "greeting": None}
    )


@app.post("/", response_class=HTMLResponse)
async def create_greeting(request: Request, name: str = Form(...)):
    """Process the form and display greeting"""
    greeting = f"Hello, {name}!"
    return templates.TemplateResponse(
        "greeting.html",
        {"request": request, "name": name, "greeting": greeting}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)