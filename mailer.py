
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from datetime import datetime

EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""  

def format_story_html(story_text):
    """Convert plain story text into styled HTML for CEO email."""

    
    story_text = story_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    
    story_html = story_text.replace('\n', '<br>')

    story_html = re.sub(
        r"(?:💡\s*Implication:)(.*?)(?=<br>)",
        r'<p style="color:#007bff; font-weight:bold; margin-left:15px;">💡 Implication:\1</p>',
        story_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    story_html = re.sub(
        r"(?:Fun\s*Fact:)(.*?)(?=<br>)",
        r'<div style="background:#fff3cd; padding:10px; border-left:5px solid #ffc107; margin:10px 0;">🐾 Fun Fact:\1</div>',
        story_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    story_html = re.sub(
        r"(?:Thought of the Day:)(.*)$",
        r'<blockquote style="font-style:italic; color:#555; border-left:3px solid #28a745; padding-left:10px;">🧠 Thought of the Day:\1</blockquote>',
        story_html,
        flags=re.IGNORECASE | re.DOTALL
    )

    story_html = story_html.replace("Geopolitics & Policy", "🌍 Geopolitics & Policy")
    story_html = story_html.replace("Economy & Markets", "📊 Economy & Markets")
    story_html = story_html.replace("Industry & Corporate Moves", "🏭 Industry & Corporate Moves")
    story_html = story_html.replace("Technology Shifts", "💻 Technology Shifts")
    story_html = story_html.replace("Social or Local Developments", "🌱 Social or Local Developments")

    return story_html

def send_email(story_text):
    """Send the daily Hindu briefing to the CEO with both plain text and HTML formatting."""
    today_str = datetime.now().strftime("%B %d, %Y")
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = f"📰 Your AI-Generated Hindu Daily Brief - {today_str}"

    story_html = format_story_html(story_text)

    msg.attach(MIMEText(story_text, "plain"))
    msg.attach(MIMEText(story_html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email failed: {e}")
