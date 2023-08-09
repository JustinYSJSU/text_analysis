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
        split_text = text.split() #split the text by any white space (each word separated by space)
        
        #for each word, add to its counter or add a new word to the freq counter
        for word in split_text:
            word = word.rstrip(",.")
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        #sort by the freq of each word, largest to smallest
        sorted_freq = sorted(word_freq.items(), key = lambda x:x[1], reverse=True)

        return dict(sorted_freq)

    def sentiment_analysis_text(self, text):
        pass

    def keyword_analysis_text(self, text):
        pass

    def part_of_speech_analysis_text(self, text):
        pass