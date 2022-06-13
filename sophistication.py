import string
import spacy
from textstat.textstat import textstatistics


#info on readability and NLP: 
#https://www.geeksforgeeks.org/readability-index-pythonnlp/



#generates a list of the easy words from given txt file
def generate_easy_words_list(easy_words):
    with open(easy_words, 'r') as f:
        for line in f:
            easy_words_list = line.split(" ") #split file by spaces
            
            #iterate through list to remove whitespace 
            #and make all words lowercase
            for i in range(len(easy_words_list)):
                easy_words_list[i] = (easy_words_list[i].strip()).lower()
    return easy_words_list

#returns number of easy and difficult words from a given essay
#parameters are 2 txt file names
def difficult_words(essay, easy_words):
    with open(essay, 'r') as essay:
        total_easy = 0
        total_hard = 0
        
        for line in essay:
            #remove whitespace and line breaks, make everything lowercase
            line = (line.strip()).lower()
            
            #remove punctuation (doesn't remove apostrophes)
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            line = line.split(" ") #generates a list of words
            
            #call function to generate a list of easy words from txt file
            easy_words_list = generate_easy_words_list(easy_words)

            
            for word in line: #categorize each word as easy or hard
            
                word = word.replace('’', "'") #weird string formatting
                
                #omits numbers and blanks
                if word in easy_words_list:
                    total_easy +=1 #counts easy words
                elif word != "" and  not(str.isdigit(word)):
                    total_hard += 1 #counts hard words
        return total_easy, total_hard

#creates list of sentences from a string of text
def break_sentences(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return list(doc.sents)

#determines average sentence length from a given essay
#parameter is an essay as a string of text
def avg_sentence(essay_str):
    #call sentences_list function
    sentences_list = break_sentences(essay_str)
    
    #count number of words and number of sentences
    total_words = 0
    total_sentences = 0
    for sentence in sentences_list:
        words = (str(sentence)).split()
        if len(words) != 0:
            total_sentences += 1
            total_words += len(words)
    
    return total_words / total_sentences

def syllables_count(word):
    return textstatistics().syllable_count(word)

def avg_syllables_per_word(text):
    syllable = syllables_count(text)
    words = word_count(text)
    ASPW = float(syllable) / float(words)
    return ASPW

def word_count(text):
    sentences = break_sentences(text)
    words = 0
    for sentence in sentences:
        words += len([token for token in sentence])
    return words


easy_words = "dale_chall_easy_words.txt" #list of 3,000 easy words
essay = "testessay.txt" #trial essay for the program



#make the txt essay file into a string
text_file = open(essay, "r")
essay_string = text_file.read()
text_file.close()


#Essay Analysis:

easy_words, hard_words = difficult_words(essay, easy_words)

print("Easy words: ", easy_words, " Hard words: ",hard_words)

avg_sentence_length = avg_sentence(essay_string)

print("Average sentence length: ",avg_sentence_length)

avg_syllables = avg_syllables_per_word(essay_string)

print("Average syllables: ", avg_syllables)






