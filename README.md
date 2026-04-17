# Python Automation Toolkit

A collection of Python scripts for web automation, data processing, and productivity enhancement.

## 🎁 Tools Included

### 1. Web Scraper 🌐
- Multi-threaded web scraping
- Support for JavaScript-rendered pages
- Automatic retry and error handling
- Export to CSV/JSON/Excel

### 2. File Organizer 📁
- Auto-organize files by type
- Duplicate file detection
- Batch rename utility

### 3. Email Automation ✉️
- Bulk email sending
- Template support
- Attachment handling

### 4. Data Cleaner 🧹
- CSV/Excel data cleaning
- Missing value handling
- Format standardization

## 🚀 Installation

```bash
pip install python-automation-toolkit
```

## 📚 Usage

```python
from automation_toolkit import WebScraper

# Initialize scraper
scraper = WebScraper(headless=True)

# Scrape data
data = scraper.scrape("https://example.com")
scraper.export(data, "output.csv")
```

## 🧪 Testing

```bash
pytest tests/
```

## 📖 License

MIT

---
Made by [Jonathan Zhang](https://github.com/jonathan7591)
