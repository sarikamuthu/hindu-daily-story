import feedparser
import requests
import re

FEEDS = {
    "National": "https://www.thehindu.com/news/national/feeder/default.rss",
    "International": "https://www.thehindu.com/news/international/feeder/default.rss",
    "Business": "https://www.thehindu.com/business/feeder/default.rss",
    "Sci-Tech": "https://www.thehindu.com/sci-tech/feeder/default.rss",
    "Editorial": "https://www.thehindu.com/opinion/columns/feeder/default.rss"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/rss+xml, application/xml"
}


def clean_html(text):
    if not text:
        return "No summary available."
    text = re.sub("<.*?>", "", text)
    text = re.sub("\s+", " ", text).strip()
    return text


def tag_story(category, title, summary):
    """
    Tag stories into neat categories for email briefing.
    """
    text = (title + " " + summary).lower()

    if any(word in text for word in ["policy", "government", "minister", "law", "election"]):
        return "🌍 Geopolitics & Policy"

    if any(word in text for word in ["market", "economy", "gdp", "inflation", "trade", "stock"]):
        return "📊 Economy & Markets"

    if any(word in text for word in ["startup", "company", "industry", "investment", "business"]):
        return "💻 Technology & Industry"

    if any(word in text for word in ["ai", "technology", "research", "innovation", "science"]):
        return "💻 Technology & Innovation"

    if any(word in text for word in ["war", "china", "us", "global", "international"]):
        return "🌐 Global Affairs"

    if category == "Editorial":
        return "✍️ Expert Opinion"

    return "📰 General Developments"


def fetch_feed_content(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None


def fetch_top_stories(limit=3):
    all_stories = []

    for category, url in FEEDS.items():
        print(f"Fetching {category} news...")

        xml_content = fetch_feed_content(url)
        if not xml_content:
            continue

        feed = feedparser.parse(xml_content)

        if not feed.entries:
            print(f"❌ No entries found for {category}")
            continue

        for entry in feed.entries[:limit]:
            title = entry.get("title", "No Title")
            summary = clean_html(entry.get("summary", ""))

            theme = tag_story(category, title, summary)

           
            all_stories.append({
                "theme": theme,
                "title": title,
                "summary": summary,
                "implication": ""  
            })

    return all_stories
