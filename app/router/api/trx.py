"""
In this api, by using request and crypto site,
we get the current price of Tron currency...
"""

from fastapi import APIRouter, Response, status

from requests import post
from bs4 import BeautifulSoup

router = APIRouter(prefix='/api', tags=["Crypto"])

def TRX():
    a = post("https://arzdigital.com/coins/tron/")
    soup = BeautifulSoup(a.content , "html.parser")
    find = soup.find("div", {"class":"arz-coin-page-data__coin-toman-price"}).text.strip()
    return find

@router.get('/tron', status_code=status.HTTP_200_OK)
@router.post('/tron', status_code=status.HTTP_200_OK)
async def tron():
    price = TRX()
    return {
        "success": True,
        "data": {
            "price_tron": price
        }
    }