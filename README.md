**WhatsApp Chat Analyzer**
A comprehensive data visualization tool built with Streamlit to analyze WhatsApp chat exports. Gain insights into messaging patterns, most active users, emoji usage, and more.

**Features**
Top Statistics: Total messages, words, media shared, and links.

Timelines: Monthly and daily message frequency.

Activity Maps: Identify the busiest days of the week and months of the year.

Heatmaps: Hourly activity patterns across the week.

WordCloud & Common Words: Visualize the most used vocabulary (supports Hinglish filtering).

Emoji Analysis: Breakdown of the most frequently used emojis.

**How to Run**
Clone the repository:

Bash
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
Install dependencies:

Bash
pip install streamlit pandas matplotlib seaborn wordcloud urlextract emoji
Run the app:


streamlit run app.py

**Project Structure**
app.py: The main Streamlit entry point.

preprocessor.py: Logic for cleaning and parsing raw text data.

helper.py: Functions for statistical analysis and plot generation.

stop_hinglish.txt: A text file containing common filler words to ignore.

**How to Export Chat**
Open WhatsApp on your phone.

Open a chat or group.

Tap the three dots (Android) or Name (iOS) > More > Export Chat.

Select Without Media.

Upload the .txt file to this analyzer.

https://whatsappchatanalyser-yrt46fzem7ttumwwmn5lwi.streamlit.app/
