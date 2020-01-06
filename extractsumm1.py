import re 
import nltk
import heapq

with open('text.txt', 'r') as file:
    data = file.read().replace('\n', '')

#print(data)

#data_cleanerData = re.sub(r'[^0-9]',' ',data)
#data_cleanedData = re.sub(r'\s+',' ', data)

#print(data_cleanedData)

data_cleanedData = re.sub(r'[^a-zA-Z.[^0-9]]',' ',data)
data_cleanedData = re.sub(r'\s+',' ', data_cleanedData)

#print(data_cleanedData)

#creating sentence tokens
sentences_tokens = nltk.sent_tokenize(data_cleanedData)

words_tokens = nltk.word_tokenize(data_cleanedData)


# calculating the frequency

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = dict()

for word in words_tokens:
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word]=1
        else:
            word_frequencies[word]+=1

#print(word_frequencies) 

# calculating weigth frequency

max_freq_word = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_freq_word

#print(word_frequencies)

#calculatng sentence score with each word weighted frequency

sentences_scores = dict()
#print(type(word_frequencies),type(sentences_scores))
for sentence in sentences_tokens:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word_frequencies.keys():
            if (len(sentence.split(' '))<30):
                if sentence not in sentences_scores.keys():
                    sentences_scores[sentence]=word_frequencies[word]
                else:
                    sentences_scores[sentence]+=word_frequencies[word]

#print(sentences_scores)

summary = heapq.nlargest(10, sentences_scores, key=sentences_scores.get)

final_summary=""
final_summary = final_summary.join(summary)
print(final_summary)
