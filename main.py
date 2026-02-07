#!/usr/bin/env python3
from rss_scout import fetch_top_stories
from storyteller import generate_story
from mailer import send_email

if __name__ == "__main__":
    print("Fetching news...")
    news_list = fetch_top_stories()  

    news_blob = "\n".join(
        f"[{story.get('theme','General')}] {story.get('title','No Title')}: {story.get('summary','No summary')}"
        for story in news_list
    )


    print("\nGenerating story...\n")
    story = generate_story(news_blob)

    print(story)

    print("\nSending email...\n")
    send_email(story)
