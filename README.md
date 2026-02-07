# 📰 Hindu Daily Story - CEO Briefing Automation

**Automated Daily News Briefing for CEOs using The Hindu RSS feeds and AI-generated summaries.**

---

## **Overview**

This project fetches the latest news from The Hindu across multiple categories (National, International, Business, Sci-Tech, Editorial) and generates a cohesive, CEO-ready briefing. It uses a local LLaMA model via Ollama for natural language summarization and sends the output via email.

- News is grouped by theme: **Geopolitics & Policy, Economy & Markets, Technology & Industry, Social/Environment**.
- Each story includes a concise **Implication for business or policy**.
- Adds **fun facts** and a **Thought of the Day** for engagement.
- Emails are formatted in **HTML with styled sections and emojis**.

---

## **Features**

- Fetches news from multiple Hindu RSS feeds.
- Cleans and processes HTML content.
- Categorizes stories intelligently based on keywords.
- Generates polished, fact-based summaries using **Ollama + LLaMA 3**.
- Formats briefing for **email with HTML styling**.
- Sends automated email with daily briefing.
- Can be scheduled with **GitHub Actions** for fully automated daily runs.

---

## **Prerequisites**

- Python 3.11+
- Ollama installed locally (`ollama` CLI)
- RSS feeds accessible from your machine
- Email account for sending updates (Gmail recommended)

**Python dependencies:**

```bash
pip install feedparser requests
