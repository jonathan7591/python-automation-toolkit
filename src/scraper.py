"""Web Scraper Module"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict

class WebScraper:
    """Simple web scraper with data export capabilities."""
    
    def __init__(self, headers=None):
        self.session = requests.Session()
        self.session.headers.update(headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape(self, url: str) -> Dict:
        """Scrape single page."""
        response = self.session.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        return {
            'title': soup.title.string if soup.title else '',
            'links': [a['href'] for a in soup.find_all('a', href=True)],
            'text': soup.get_text(),
        }
    
    def export(self, data: Dict, filename: str):
        """Export data to file."""
        if filename.endswith('.json'):
            import json
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        elif filename.endswith('.csv'):
            df = pd.DataFrame([data])
            df.to_csv(filename, index=False)

if __name__ == "__main__":
    scraper = WebScraper()
    data = scraper.scrape("https://example.com")
    print(f"Title: {data['title']}")
    print(f"Links found: {len(data['links'])}")
