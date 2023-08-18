import os
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import Counter
from rake_nltk import Rake
import time
from googletrans import Translator, constants
from pprint import pprint

class FileAnalysis:
    file = None

    def __init__(self):
       pass
        
    def verify_file(self, filepath):
        try:
            file = open(filepath, "r", encoding="utf-8") #file exists
        except OSError as e:
            print("File not found") #does not exist 
        return file
            
    def word_freq_analysis_file(self, file):
        """ Analyze the frequency of words in the given text

        Keyword Arguments:
        file -- the inputted file

        Return Values:
        A dictionary containing each word and its frequency 
        """
        results = " "
        data = file.read() #read file, then split it like text 
        split_text = data.splitlines()

        word_freq = {} #hold each word + feq

        #for each word, add to its counter or add a new word to the freq counter
        print("Loading analysis...")
        print()
        for line in split_text:
            word_list = line.split()
            for word in word_list:
                word = word.lower()
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
          results += f"{word}: {freq}"
          results += "\n"

        results += "\n"

        print()
        most_freq_word = list(sorted_freq.keys())[0]
 
        print(f"The most frequent word is: '{most_freq_word}' with a frequency of {sorted_freq[most_freq_word]}")
        results += f"The most frequent word is: '{most_freq_word}' with a frequency of {sorted_freq[most_freq_word]}"
        return results

    def translate_file(self, file):
        data = file.read() #read file, then split it like text 
        split_text = data.splitlines()
        translator = Translator()
        print()
        print("***SUPPORTED LANGUAGES***")
        pprint(constants.LANGUAGES)
        destination_lang = input("Please enter the language code you want to translate to: ")
        file_name = input("Please enter the name of the .txt to export to (no .txt needed): ")
        translated_file = open(f"{file_name}.txt", "w", encoding='utf-8')

        print()
        print("Translating. Please wait...")
        for line in split_text:
            translation = translator.translate(line, dest=destination_lang)
            translation_encoded = translation.text
            translated_file.write(translation_encoded + '\n')
        translated_file.close()
        print("Translation complete!")
        return translated_file

    def keyword_analysis_file(self, file):
        results = ""
        nltk.download('stopwords')
        data = file.read()
        tokens = word_tokenize(data)
        r = Rake()
        data = ' '.join(tokens)
        r.extract_keywords_from_text(data)
        keywords = r.get_ranked_phrases_with_scores()[:10]
        for score, word in keywords:
            print(f"Score: {score:.2f}, Keyword: {word}")
            results += f"Score: {score:.2f}, Keyword: {word}"
            results += "\n"
        return results

    def part_of_speech_analysis_file(self, file):
        """ Analyze the parts of speech of each word in the text.

        Keyword Arguments:
        file -- the inputted file

        """
        results = ""
        data = file.read() #read file, then split it like text 
        #download tools needed for analysis
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        #split the text, then tag each word 
        
        print("Loading analysis...")
        new_text = word_tokenize(data)
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
            "NNP": "Singular Proper Noun",
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
            "(": "Left Parenthesis",
            ")": "Right Parenthesis"
        }

        print()
        print("***Part of Speech Analysis Results***")
        for tag in tag_counts:
            print(f"{tag_representations[tag]} count: {tag_counts[tag]}")
            results += f"{tag_representations[tag]} count: {tag_counts[tag]}"
            results += "\n"
        results += f"The most common part of speech is: {tag_representations[max(tag_counts, key=tag_counts.get)]}"
        return results