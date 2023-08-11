import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import Counter
import time

class TextAnalysis:
 
    def __init__(self):
        pass


    def word_freq_analysis_text(self, text):
        """ Analyze the frequency of words in the given text

        Keyword Arguments:
        text -- the inputted text

        Return Values:
        A dictionary containing each word and its frequency 
        """
        text = text.lower()
        word_freq = {} #hold each word + feq
        split_text = text.splitlines() #split the text by any white space (each word separated by space)
        print("Loading analysis...")
        print()
        #for each word, add to its counter or add a new word to the freq counter
        for line in split_text:
            word_list = line.split()
            for word in word_list: 
                word = word.rstrip(",.")
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
        #sort by the freq of each word, largest to smallest
        sorted_freq = sorted(word_freq.items(), key = lambda x:x[1], reverse=True)
        sorted_freq = dict(sorted_freq)
        print()
        print("***Word Frequency Analysis Results***")
        print()
      
        for word, freq in sorted_freq.items():
          print(f"{word}: {freq}")

        print()
        most_freq_word = list(sorted_freq.keys())[0]
        print(f"The most frequent word is: '{most_freq_word}' with a frequency of {sorted_freq[most_freq_word]}")

    def sentiment_analysis_text(self, text):
        pass

    def keyword_analysis_text(self, text):
        pass

    def part_of_speech_analysis_text(self, text):
         
        #download tools needed for analysis
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        #split the text, then tag each word 
        print("Loading analysis...")
        new_text = word_tokenize(text)
        pos_tags = pos_tag(new_text)
        #count the occurence of each tag in the text
        tag_counts = Counter(tag for word, tag in pos_tags)
        tag_representations = {
            "CC": "Conjunctional Coordinator", 
            "CD": "Cardinal Digit", 
            "DT": "Determiner", 
            "EX": "Existenial", 
            "FW": "Foreign Word", 
            "IN": "Preposition / Conjunction", 
            "JJ": "Adjective",
            "JJR": "Adjective / Comparative", 
            "JJS": "Adjective / Superlative",
            "LS": "List Marker",
            "MD": "Modal",
            "NN": "Singular Noun",
            "NNS": "Plural noun",
            "NNP": "Sigular Proper Noun",
            "NNPS": "Propoer noun plural",
            "POS": "Possessive Ending",
            "PDT": "Predeterminer",
            "WRB": "Abverb of WH (Where, when, why,etc)",
            "WP$": "Possessive of WH (Whose)", 
            "WP": "Pronoun of WH (who, which, what, whose, etc)",
            "WDT": "Determiner of WP", 
            "VBZ": "Verb",
            "VB": "Base Verb", 
            "VBD": "Past tense verb",
            "VBG": "Present tense verb",
            "VBP": "Non-3rd person singular present verb",
            "VBN": "Past participle verb",
            "UH": "Interjection",
            "TO": "To go", 
            "RP": "Particle",
            "RBS": "Adverb",
            "RB": "Adverb",
            "RBR": "Adverb",
            "PRP": "Personal Pronoun",
            "PRP$": "Possessive Pronoun",
            ".": "Period",
            ":": "Colon",
            ",": "Comma",
            "HYPH": "Hyphen", 
            "$": "Dollar",
            "``": "Left Quote",
            "''": "Right Quote",
            "-LRB-": "Left Bracket",
            "-RRB-": "Right Bracket",
            "ADD": "Email",
            "AFX": "Affix",
            "XX": "Unknown",
        }

        print()
        print("***Part of Speech Analysis Results***")
        for tag in tag_counts:
            print(f"{tag_representations[tag]} count: {tag_counts[tag]}")
        print(f"The most common part of speech is: {tag_representations[max(tag_counts, key=tag_counts.get)]}")