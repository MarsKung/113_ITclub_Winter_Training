import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
    <head>

</head>
    <style>
    /* static/style.css */
body {
    margin: 0;
    padding: 0;
    background: #0a0a0a;
    color: #0f0;
    font-family: 'Courier New', monospace;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    overflow: hidden;
    position: relative;
}

body::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        linear-gradient(90deg, #0a0a0a 21px, transparent 1%) center,
        linear-gradient(#0a0a0a 21px, transparent 1%) center,
        #000;
    background-size: 22px 22px;
    opacity: 0.2;
}

h1 {
    font-size: 3em;
    text-align: center;
    margin: 20px;
    position: relative;
    color: #0f0;
    text-shadow: 0 0 10px #0f0;
    letter-spacing: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
}

h1:hover {
    text-shadow: 0 0 20px #0f0, 0 0 30px #0f0, 0 0 40px #0f0;
    transform: scale(1.1);
}

h1::before {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 100%;
    color: #0f0;
    overflow: hidden;
    border-right: 2px solid #0f0;
    animation: typing 6s steps(30) infinite;
}

p {
    font-size: 1.2em;
    text-align: center;
    margin: 20px;
    color: #0f0;
    opacity: 0.8;
    max-width: 600px;
    line-height: 1.6;
    position: relative;
}

img {
    max-width: 100%;
    height: auto;
    border: 2px solid #0f0;
    box-shadow: 0 0 20px #0f0;
    transition: all 0.3s ease;
}

img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px #0f0;
}

@keyframes typing {
    0%, 90%, 100% {
        width: 0;
    }
    30%, 60% {
        width: 100%;
    }
}

@keyframes flicker {
    0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100% {
        opacity: 0.99;
        text-shadow: -1px -1px 0 #0f0, 1px -1px 0 #0f0, -1px 1px 0 #0f0, 1px 1px 0 #0f0;
    }
    20%, 21.999%, 63%, 63.999%, 65%, 69.999% {
        opacity: 0.4;
        text-shadow: none;
    }
}

.container {
    position: relative;
    z-index: 1;
    padding: 20px;
    background: rgba(0, 20, 0, 0.2);
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 255, 0, 0.1);
    backdrop-filter: blur(5px);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.1);
    }
    to {
        box-shadow: 0 0 30px rgba(0, 255, 0, 0.3);
    }
}

.binary-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    opacity: 0.1;
    font-family: monospace;
    font-size: 14px;
    overflow: hidden;
    z-index: 0;
}

.binary-bg::after {
    content: "01101000 01100001 01100011 01101011 01100101 01110010 00100000 01100101 01110100 01101000 01101001 01100011 01110011";
    position: absolute;
    top: 0;
    left: 0;
    white-space: pre;
    animation: scroll 20s linear infinite;
}

@keyframes scroll {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(-50%);
    }
}
    </style>
    <body>
        <h1>where's the flag?</h1>
        <img src="/readimg?filename=welcome.png" alt="" />
        <p>Find the file named flag</p>
    </body>
    </html>
    """

@app.get("/readimg")
def read_file(filename: str):
    url = os.path.join("app/img/", filename)
    return FileResponse(url)



# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8787)