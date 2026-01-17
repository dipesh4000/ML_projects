from urlextract import URLExtract

extractor = URLExtract()
def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    words = []
    for message in df['message']:
        words.extend(message.split())
    num_words = len(words)

    df['message'] = df['message'].apply(lambda x: x.strip())

    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]

    links=[]
    for message in df['message']:
        links.extend(extractor.find_urls(message))


    return num_messages, num_words, num_media_messages, len(links)
def most_busy_users(df):
    x = df['user'].value_counts().head()
    new_df = round((df['user'].value_counts()/df.shape[0])*100, 2).reset_index(
        ).rename(columns={'user':'name', 'count':'percent'})
    return x, new_df

def most_common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df.query('message != ""  and message != "<Media omitted>"')
    temp = temp.reset_index(drop=True)

    words = []
    for message in df['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
        words.extend(message.split())