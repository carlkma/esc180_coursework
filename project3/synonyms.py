'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''


# ESC180 Project 3
# synonyms.py
# Dec 7, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# NOTE: VERSION 4 - FINAL SUBMISSION (UNLESS UPDATED)


import math
import re


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    denominator_1 = 0
    denominator_2 = 0

    for key in vec1:
        if key in vec2:
            numerator += vec1[key] * vec2[key]
        denominator_1 += vec1[key] ** 2

    for key in vec2:
        denominator_2 += vec2[key] ** 2

    denominator = math.sqrt(denominator_1*denominator_2)
    return numerator / denominator



def build_semantic_descriptors(sentences):
    answer = {}

    for i in range(len(sentences)):
        sentences[i] = [word.lower() for word in sentences[i]]

    for sentence in sentences:
        for word in sentence:
            if word not in answer:
                answer[word] = {}
            descriptor = update_descriptor(answer[word],sentence,word)
            
    return answer
                

def update_descriptor(original, sentence, word_interest):
    for word in sentence:
        if word != word_interest:
            if word not in original:
                original[word] = 1
            else:
                original[word] += 1
    return original


def build_semantic_descriptors_from_files(filenames):
    sentences = []

    for filename in filenames:
        f = open(filename, "r", encoding="latin1")
        text = f.read()
        f.close()

        text = text.lower()
        text = re.sub("[,:;]", " ", text)
        text = re.sub("--?", " ", text)

        text = re.split("[.!?]", text)
        for i in range(len(text)):
            text[i]=text[i].split()
        sentences += text

    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    score = [-1] * len(choices)
    if word in semantic_descriptors:

        descriptors_word = semantic_descriptors[word]

        for i in range(len(choices)):
            if choices[i] in semantic_descriptors:
                descriptors_choice = semantic_descriptors[choices[i]]

                score[i] = similarity_fn(descriptors_word,descriptors_choice)

    return choices[score.index(max(score))]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename, "r", encoding="latin1")
    text = f.read().splitlines()
    f.close()
    total = len(text)
    correct = 0

    for line in text:
        info = line.split()
        word = info[0]
        answer = info[1]
        choices = info[2:]
        
        if most_similar_word(word, choices, semantic_descriptors, similarity_fn) == answer:
            correct += 1
    return correct / total * 100


if __name__ == '__main__':
    sd = build_semantic_descriptors_from_files(["2600-0.txt","pg7178.txt"])
    percentage = run_similarity_test("test.txt", sd, cosine_similarity)
    print(percentage)