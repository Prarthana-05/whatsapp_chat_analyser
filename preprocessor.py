import pandas as pd
import re

def preprocess_whatsapp(data):
    # 1️⃣ Regex pattern to match timestamps
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s[ap]m\s-\s'
    
    # 2️⃣ Split messages using timestamp pattern
    messages = re.split(pattern, data)[1:]  # skip empty first split
    
    # 3️⃣ Extract timestamps
    timestamps = re.findall(pattern, data)
    
    # 4️⃣ Clean timestamps (remove trailing ' - ')
    timestamps = [ts.strip().rstrip(' -') for ts in timestamps]
    
    # 5️⃣ Create initial DataFrame
    df = pd.DataFrame({'messages_date': timestamps, 'user_messages': messages})
    
    # 6️⃣ Convert timestamps to datetime
    df['date'] = pd.to_datetime(df['messages_date'], format='%d/%m/%y, %I:%M %p', errors='coerce')
    
    # 7️⃣ Split sender and message
    df[['sender', 'message']] = df['user_messages'].str.split(': ', n=1, expand=True)
    
    # 8️⃣ Handle system messages (no sender)
    df['message'] = df['message'].fillna(df['user_messages']).str.strip()
    df['sender'] = df['sender'].where(df['user_messages'].str.contains(': '))
    
    # 9️⃣ Add extra columns for analysis
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    
    #  🔟 Keep only clean columns
    df = df[['date', 'sender', 'message', 'year', 'month', 'day', 'hour', 'minute']]
    
    return df
