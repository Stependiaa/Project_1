def most_frequent_word(words):
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    highest_frequency = 0
    winner = None
    for word, frequency in frequencies.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            winner = word
    return winner



def text_to_dict(text):
    i = 0
    dictionary = {}
    result = {}
    for k in text.split('\n')[1:-1]:
        row = k.split(';')
        dictionary[i] = {'Brand': row[0], 'Model': row[1], 'aggregateRating/ratingValue': row[2], 'aggregateRating/reviewCount': row[3], 'offers/price': row[4], 'offers/priceCurrency': row[5], 'depth': row[6], 'width': row[7]}
        result.update(dictionary)
        i += 1
    return result



