def words_sorting(*args):
    word_dict = {}
    total_sum = 0

    for word in args:
        if word not in word_dict:
            word_sum = sum([ord(char) for char in word])
            word_dict[word] = word_sum
            total_sum += word_sum

    if total_sum % 2 != 0:
        sorted_dict = sorted(word_dict.items(), key=lambda x: -x[1])
    else:
        sorted_dict = sorted(word_dict.items())

    result = []
    for word in sorted_dict:
        result.append(f"{word[0]} - {word[1]}")

    return "\n".join([item for item in result])
