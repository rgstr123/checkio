# coding: utf8
import re

def find_word(message):

    words = re.findall(r"\w+", message.lower())
    correlations_word_list = []
    correlations_nums_list = []

    for w1_indx in range(len(words)):
        res_w1_vs_w2 = 0
        for w2_indx in range(len(words)):
            if w1_indx == w2_indx:
                pass
            else:
                # Создаём моножестсво букв, для каждого слова
                set_of_word1 = set(words[w1_indx])
                set_of_word2 = set(words[w2_indx])
                # Создаём мрожества уникальных и общих букв
                unique_letters = set_of_word1.union(set_of_word2)
                common_letters = set_of_word1.intersection(set_of_word2)
                # Записываем результат в переменную
                res_w1_vs_w2 += (len(common_letters) / len(unique_letters)) * 50

                # Если первая буква одинаковая для обоих слов
                if words[w1_indx][0] == words[w2_indx][0]:
                    # Добавляем в переменную 10%
                    res_w1_vs_w2 += 10
                # Если последняя буква одинаковая для обоих слов
                if words[w1_indx][-1] == words[w2_indx][-1]:
                    # Добавляем в переменную 10%
                    res_w1_vs_w2 += 10
                # Если одно слово короче другого
                if len(words[w1_indx]) < len(words[w2_indx]):
                    res_w1_vs_w2 += (len(words[w1_indx])/len(words[w2_indx])) * 30
                else:
                    res_w1_vs_w2 += (len(words[w2_indx])/len(words[w1_indx])) * 30

        # Записываем значение переменной в общий словарь
        correlations_word_list.append(words[w1_indx])
        rnd = round(res_w1_vs_w2, 3)
        correlations_nums_list.append(rnd)

    result_word = ""
    result_nums = 0
    # Пробегаемся по всем результатам и записаваем наибольший(если несколько, то последний)
    for index in range(len(correlations_nums_list)):
        if correlations_nums_list[index] >= result_nums:
            result_nums = correlations_nums_list[index]
            result_word = correlations_word_list[index]
    return result_word

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Friend Fred and friend Ted.") == "friend", "Friend1"
    assert find_word("Speak ........friend and enter...,,,,,..............") == "friend", "Friend2"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
