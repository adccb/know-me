def normalize_data(key, data):
    if key == 'fear' or key == 'sleep_quality':
        return data / 20
    if key == 'ideation':
        return data / 2
    else:
        return data

