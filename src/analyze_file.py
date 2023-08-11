import os

class FileAnalysis:
    file = None

    def __init__(self):
       pass
        
    def verify_file(self, filepath):
        try:
            file = open(filepath, "r") #file exists
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
        data = file.read() #read file, then split it like text 
        split_text = data.splitlines()

        word_freq = {} #hold each word + feq

        #for each word, add to its counter or add a new word to the freq counter
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

        return dict(sorted_freq)

    def sentiment_analysis_file(self, file):
        pass

    def keyword_analysis_file(self, file):
        pass

    def part_of_speech_analysis_file(self, file):
        pass