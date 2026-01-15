import pandas as pd
import re
def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'date': dates})
    df['date'] = (df['date'].str.replace(' - ', '', regex=False).pipe(pd.to_datetime, format='%d/%m/%y, %H:%M'))
    df = df[1:]
    df[['user', 'message']] = df['user_message'].str.split(':', n=1, expand=True)
    df['user'] = df['user'].apply(lambda x: x.replace('`', "Dipesh"))
    df['user'] = df['user'].apply(lambda x: x.split()[0])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df.drop(columns=['user_messages','date'], inplace=True)
    return df