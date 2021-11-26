# ESC180 Lab 9
# lab9.py
# Nov 26, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)

# Problem 1

def get_word_count(list_of_words):
    word_counts = {}
    for word in list_of_words:
        if word not in word_counts.keys():
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts

notes_underground = open("notes_underground.txt", encoding="latin-1").read().split()
word_counts = get_word_count(notes_underground)

test = {"sick": 1, "man.": 3, "at": 1, "what": 1, "nothing": 1, "do": 1, "is": 1, "me.": 1,
"I": 5, "ails": 1, "an": 1, "am": 3, "know": 2, "disease,": 1, "not": 1, "liver": 1,
"believe": 1, "all": 1, "my": 2, "certain": 1, "However,": 1, "and": 1, "for": 1,
"unattractive": 1, "spiteful": 1, "about": 1, "a": 2, "diseased.": 1}

print(test==word_counts)

def top10(L):
    largest = [-1] * 10
    for integer in L:
        if integer > min(largest):
            largest[largest.index(min(largest))] = integer
    return largest

def get_ten_most_frequent(word_counts):
    items = list(word_counts.items())
    for i in range(len(items)):
        items[i] = tuple(reversed(items[i]))

    sorted_items = sorted(items, reverse=True)
    return sorted_items[:10]

pride = open("pride.txt", encoding="latin-1").read().split()
word_counts = get_word_count(pride)
print(get_ten_most_frequent(word_counts))

# Problem 2 - See hello.html

# Problem 3
import urllib.request


def get_n_search_results(keyword):

    template = "search results</span>"
    keyword = keyword.replace(" ", "+")
    url = "https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p=%s&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1" % keyword
    f = urllib.request.urlopen(url)
    page = f.read().decode("utf-8")
    f.close()
    end = page.find(template)
    start = 0
    for i in range(end, 0 , -1):
        if page[i] == ">":
            start = i
            break
    output = page[start+1:end-1]
    print(output)
    number = int(output.split()[1].replace(",",""))
    return number

print()
print("Problem 3a")
number = get_n_search_results("u of t")
print(number)

def choose_variant(variants):
    i_max = -1
    n_max = -1
    for i in range(len(variants)):
        number = get_n_search_results(variants[i])
        if number > n_max:
            i_max = i
            n_max = number
    return variants[i_max], n_max

variants = ["top ranked school uoft", "top ranked school waterloo"]

print()
print("Problem 3b")
print(choose_variant(variants))

