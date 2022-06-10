from typing import Dict, List
from django.conf import settings
import httpx
import httpx
class StocksService:
    BASE_URL = 'https://dev.kwayisi.org/apis/gse'

    def live(self) -> List[Dict]:
        response = httpx.get(f"{self.BASE_URL}/live")
        return response.json()

    def live_for_symbol(self, symbol:str) -> Dict:
        return httpx.get(f"{self.BASE_URL}/live/{symbol}").json()
    
    def equities(self) -> List[Dict]:
        return httpx.get(f"{self.BASE_URL}/equities").json()
    
    def equities_for_symbol(self, symbol) -> Dict:
        return httpx.get(f"{self.BASE_URL}/equities/{symbol}").json()
    

    

    