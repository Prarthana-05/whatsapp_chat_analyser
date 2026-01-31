from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'].str.contains('<Media omitted>', na=False)].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['sender'].value_counts().head()
    df_percent = round((df['sender'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'sender': 'percent'})
    return x, df_percent

def create_wordcloud(selected_user, df):
    try:
        with open('stop_hinglish.txt', 'r') as f:
            stop_words = f.read()
    except FileNotFoundError:
        stop_words = ""

    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    temp = df[df['sender'].notna()]
    temp = temp[~temp['message'].str.contains('<Media omitted>', na=False)]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    combined_text = temp['message'].str.cat(sep=" ")
    
    if not combined_text.strip():
        return wc.generate("NoData")
        
    return wc.generate(combined_text)

def most_common_words(selected_user, df):
    try:
        with open('stop_hinglish.txt', 'r') as f:
            stop_words = f.read()
    except FileNotFoundError:
        stop_words = ""

    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    temp = df[df['sender'].notna()]
    temp = temp[~temp['message'].str.contains('<Media omitted>', na=False)]

    words = []
    for message in temp['message']:
        for word in str(message).lower().split():
            if word not in stop_words:
                words.append(word)

    return pd.DataFrame(Counter(words).most_common(20))

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    return pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

def monthly_timeline(selected_user, df):
    # .copy() prevents SettingWithCopyWarning
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user].copy()
    else:
        df = df.copy()

    df['month_num'] = df['date'].dt.month
    
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user].copy()
    else:
        df = df.copy()

    df['only_date'] = df['date'].dt.date
    
    return df.groupby('only_date').count()['message'].reset_index()

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]
    
    return df['date'].dt.day_name().value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user].copy()
    else:
        df = df.copy()

    if df.empty:
        return pd.DataFrame()

    df['day_name'] = df['date'].dt.day_name()
    df['period'] = df['hour'].apply(lambda x: f"{x:02d}-{(x+1)%24:02d}")

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap