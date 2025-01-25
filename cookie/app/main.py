from fastapi import FastAPI, Request, Response, Cookie, Form
from fastapi.responses import HTMLResponse,FileResponse, RedirectResponse
from typing import Optional
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory="app/templates")
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    image: str
    data : str

items_db = [
    Item(id=85, name="iPhone 16 Pro", description="沙漠色鈦金屬 iPhone 16 Pro 與 iPhone 16 Pro Max，周圍點綴著星星、煙火與鱗片", price=36900, image="https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/store-card-50-cny-iphone-pro-202501?wid=960&hei=1000", data="假的：D"),
    Item(id=86, name="Apple Watch Series 10", description="鈦金屬金色 Apple Watch Series 10 搭配金色米蘭式錶環，周圍點綴著火花、圓點與金色鱗片", price=13500, image="https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/store-card-50-cny-watch-s10-202501?wid=960&hei=1000",data="假的：D"),
    Item(id=88, name="MacBook Pro", description="打開的銀色 MacBook Pro，展示 Liquid Retina XDR 顯示器、圓角設計與凸出的腳座。周圍點綴著火花、星星、圓點與金色鱗片", price=54900, image="https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/store-card-50-cny-macbook-pro-202501?wid=960&hei=1000&fmt=p-jpg",data="假的：D"),
    Item(id=87, name="flag", description="U can't see me:)", price=9999999999, image="https://img.etimg.com/thumb/msid-87088964,width-300,height-225,imgsize-7052,resizemode-75/1.jpg",data="FLAG_FORMAT{Appl3_st0r3_M45t3r}")

]
@app.get("/")
async def read_items(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": items_db})

@app.get("/flag")
async def rickroll():
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.get("/buy")
async def buy_item( request: Request ,id: Optional[str] = Cookie(None), Product_Prices: Optional[str] = Cookie(None),user: Optional[str] = Cookie(None)):
    html_content = """
        <html>
            <head>
                <meta http-equiv="refresh" content="1;url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" />
            </head>
            <body>
                <p>我不知道你要幹麻，所以送你rickroll：）</p>
            </body>
        </html>
        """
    
    try:
        price = int(Product_Prices)
        id = int(id)
        item = next(i for i in items_db if i.id == id)
        if user != "guest":
            html_content = """
            <html>
                <head>
                    <meta http-equiv="refresh" content="0.1;url=https://www.youtube.com/watch?v=cw9FIeHbdB8" />
                </head>
                <body>
                    <p>Who are you?</p>
                </body>
            </html>
            """
            return HTMLResponse(html_content, status_code=403)
    
        elif price> 0:
            return FileResponse(os.path.join("app/img/","no_money.jpg"), status_code=403)
        elif price < 0:
            return FileResponse(os.path.join("app/img/","I_have_no_money.jpg"), status_code=403)
        elif price == 0:
            return templates.TemplateResponse("test.html", {"request": request, "data": item.data})
    except:
        pass
    return HTMLResponse(html_content, status_code=403)
        

@app.get("/items", response_class=HTMLResponse)
async def get_items(request: Request, response: Response,id: int):
    item = next((i for i in items_db if i.id == id), None)
    if item:
        response =templates.TemplateResponse("final.html", {"request": request, "item": item})
        response.set_cookie(key="id", value=item.id)
        response.set_cookie(key="Product_Prices", value=item.price)
        response.set_cookie(key="user", value="guest")
        return response
    else:
        html_content = """
            <html>
                <head>
                    <meta http-equiv="refresh" content="0;url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" />
                </head>
                <body>
                    <p>對不起我沒做那麼多：）</p>
                </body>
            </html>
            """
        return HTMLResponse(content=html_content)




import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8787)