from typing import List, Optional
from fastapi import HTTPException
from app.schemas.schemas import SiteBase
import requests
import bs4
import csv


class Scraper():
  def google_search(self, keyword: Optional[str] = None) -> List[SiteBase]:
    if keyword is None:
      search_url: str = "https://www.google.com/search"
    else:
      search_url: str = "https://www.google.com/search?q="+keyword
      
    search_response = requests.get(search_url)
    
    soup = bs4.BeautifulSoup(search_response.text, 'lxml')
    parsed_page = soup.select('div.kCrYT>a')
    
    if len(parsed_page) == 0:
      raise HTTPException(status_code=404, detail="Not found")
    
    items: List = []
    rank: int = 1
    for site in parsed_page:
      try:
        item = {
            'rank': rank,
            'title': site.select('h3.zBAuLc')[0].text,
            'url': site.get('href').split('&sa=U&')[0].replace('/url?q=', '')
        }
        rank += 1
        items.append(item)
      except (IndexError, TypeError) as e:
          print(e)
          raise HTTPException(status_code=500, detail="IndexError or TypeError occurred")
      except:
          print('想定外のエラー')
          raise HTTPException(status_code=500, detail="Unexpected error occurred")
        
    return items
  
  def save_csv(self, items):
    csvlist = [["", "検索結果リスト"]]
    num = 0
    for item in items:
      csvlist.append([num, item["title"]])
      num += 1

    try:
        with open("./csv-output/output1.csv", "a") as f:
            writecsv = csv.writer(f, lineterminator='\n')
            writecsv.writerows(csvlist)
    except FileNotFoundError as e:
        print(e)
        raise HTTPException(status_code=500, detail="File not found")
    except csv.Error as e:
        print(e)
        raise HTTPException(status_code=500, detail="Unexpected error occurred")
    return 