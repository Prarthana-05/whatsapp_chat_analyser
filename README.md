Markdown
# WhatsApp Chat Analyzer

A comprehensive data visualization tool built with **Streamlit** to analyze WhatsApp chat exports. Gain insights into messaging patterns, most active users, emoji usage, and more.

**Live Demo:** [Click Here to View App](https://whatsappchatanalyser-yrt46fzem7ttumwwmn5lwi.streamlit.app/)

---

##  Features
* **Top Statistics:** Total messages, words, media shared, and links.
* **Timelines:** Monthly and daily message frequency charts.
* **Activity Maps:** Identify the busiest days of the week and months of the year.
* **Heatmaps:** Visualize hourly activity patterns across the week.
* **WordCloud & Common Words:** Most used vocabulary (includes Hinglish filtering).
* **Emoji Analysis:** Breakdown of the most frequently used emojis.

---

##  Installation & Setup

**1. Clone the repository:**
```bash
git clone https://github.com/Prarthana-05/whatsapp_chat_analyser.git
cd whatsapp_chat_analyser

2. Install dependencies:
pip install streamlit pandas matplotlib seaborn wordcloud urlextract emoji

3. Run the app:
streamlit run app.py

## Project Structure
app.py: The main Streamlit entry point.

preprocessor.py: Logic for cleaning and parsing raw text data.

helper.py: Functions for statistical analysis and plot generation.

stop_hinglish.txt: Common filler words to ignore in analysis.

---

##  How to Export Chat

1. Open **WhatsApp** on your phone.
2. Open a **chat** or **group**.
3. Tap the **three dots** (Android) or **Name** (iOS) > **More** > **Export Chat**.
4. Select **Without Media**.
5. Upload the resulting `.txt` file to this analyzer dashboard.
