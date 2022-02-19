def predict_genre(answers):
    genres=[]
    if answers[0] == 'Believe in Hardwork':
        genres.append('country')
        genres.append('pop')
    elif answers[0] == 'Believe in Smartwork':
        genres.append('indie')
    if answers[1] == 'Partying':
        genres.append('rock')
        genres.append('indie')
    elif answers[1] == 'Listen to music while reading book':
        genres.append('jazz')
        genres.append('blues')
        genres.append('soul')
        genres.append('drum-and-bass')
    if answers[2] == 'Yes':
        genres.append('dance')
        genres.append('hip-hop')
        genres.append('heavy-metal')
    return set(genres)