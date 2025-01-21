from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()
FLAG = "FLAG_FROMAT{P47H_7r4v3r54l_K1Ng}"

@app.get("/robots.txt", response_class=PlainTextResponse)
def read_robots_txt():
    return '''User-agent: *
Disallow:/items/'''

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>FastAPI HTML Response</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <!--Do U know robots.txt?-->
        </body>
    </html>
    """
    return html_content


@app.get("/items", response_class=PlainTextResponse)
def hello_item():
    
    return '''Enter a number after the slash to search for that item'''

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 87:
        html_content = f"""
        <html>
            <head>
                <meta http-equiv="refresh" content="0;url=/" />
            </head>
            <body>
                <p>{FLAG}</p>
                <p>Redirecting to <a href="/">home</a></p>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    else:
        return f'''Item{item_id} is cool! but there is no flag here:('''