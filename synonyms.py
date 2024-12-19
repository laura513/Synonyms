# part 1
# a)
import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''
    sum_of_squares = 0.0
    for x in vec.values():
        sum_of_squares += x**2

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    ''' calculates the cosine similarity between two vectors. C
    osine similarity measure the similarity between two
    non-zero vectors of an inner product space that measures
    the cosine of the angle between them. The cosine of 0°
    is 1, and it is less than 1 for any other angle.'''
    dot_product= 0.0
    for i in vec1.keys():
        if i in vec2.keys():
            dot_product += vec1[i]*vec2[i]
    norm1 = norm(vec1)
    norm2 = norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return -1
    else:
        return dot_product/(norm1 * norm2)

# def absvec(value):
#     res = 0
#     for i in range(len(value)):
#         res += (value[i])**2
#     return res
#
# def cosine_similarity(vec1, vec2):
#     sum = 0
#     for i in vec1.keys():
#         if i in vec2.keys():
#             sum += float(vec1[i] * vec2[i])
#     # Convert dict_values to lists
#     vec1_values = list(vec1.values())
#     vec2_values = list(vec2.values())
#     res = float(sum/((absvec(vec1_values)*absvec(vec2_values))**(0.5)))
#     return(res)

# b)
def build_semantic_descriptors(sentences):
    w = {}
    for sentence in sentences:
        words = set(sentence)
        for word in words:
            if word not in w:
                w[word] = {}
            for other_words in words:
                if other_words != word:
                    w[word][other_words] = w[word].get(other_words, 0) + 1
    return w

# c)
def build_semantic_descriptors_from_files(filenames):
    '''reads files, splits them into sentences, and then uses
    build_semantic_descriptors to build descriptors for all
    words across these files.'''
    sentences1 = []
    for filename in filenames:
        file = open(filename, 'r',  encoding="latin1")
        content = file.read().lower()  # Convert to lowercase
        # Remove punctuation
        content = content.replace("\n\n", " ")
        content = content.replace("\n", " ")
        content = content.replace(",", " ")
        content = content.replace("-", " ")
        content = content.replace("--", " ")
        content = content.replace(":", " ")
        content = content.replace(";", " ")
        content = content.replace("!", ".")
        content = content.replace("?", ".")
        content = content.replace("/", " ")

        content_sentences = content.split(".")
        for sentence in content_sentences:
            words = sentence.split(" ")
            word_l = []
            for word in words:
                if word:
                    word_l.append(word)
            sentences1.append(word_l)
    return build_semantic_descriptors(sentences1)



# d)
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    sim = {}
    max_sim = -1
    V1 = semantic_descriptors.get(word, {})
    for choice in choices:
        V2 = semantic_descriptors.get(choice, {})
        res = similarity_fn(V1, V2)
        sim[choice] = res
        if res >= max_sim:
            max_sim = res
    for choice in choices:
        if sim[choice] == max_sim:
            return choice


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''evaluates the synonym detection system. The file contains pairs of words
    (a word and its synonym), followed by a set of choices.'''
    correct = 0
    total = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            if len(words) >= 3:  # Ensure there are enough words in the line
                word, answer, choices = words[0], words[1], words[2:]
                if most_similar_word(word, choices, semantic_descriptors, similarity_fn) == answer:
                    correct += 1
                total += 1
    print(f"Total Tests Passed: {correct} out of {total}")
    return correct / total if total else 0
# #
# filenames = ["2600-0.txt", "2600-1.txt"]
# semantic_descriptors = build_semantic_descriptors_from_files(filenames)
# # print(semantic_descriptors)
# # similarity_score = run_similarity_test('text1.txt', semantic_descriptors, cosine_similarity)
#
# print(run_similarity_test("text1.txt", semantic_descriptors, cosine_similarity))
# print(semantic_descriptors)
# # print(f"Similarity Score: {similarity_score}")
#
# # print(build_semantic_descriptors_from_files(["test.txt"]))
#
# print(run_similarity_test("text1.txt", descriptor, cosine_similarity))




