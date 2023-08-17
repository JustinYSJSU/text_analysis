class AnalysisTools:
    def __init__(self):
        pass

    def analysis_options(self):
        print()
        print("******************")
        print("*ANALYSIS OPTIONS*")
        print("******************")
        print()
        print("1: Word Frequency Analysis: Recieve the top 20 most common words in the text. Ordered from most to least frequent")
        print("2: Translation: Translate your text into another language.")
        print("3: Keyword Analysis: Analyze the keywords in the text. Which words are the most meaningful?")
        print("4: Part of Speech Analysis: Analyze the part of speech of each word in the text")
        print()
        print("**Select your analysis option with the number keys 1 - 4.**")
        
        analysis_choice = input()
        return analysis_choice
    
    def initiate_export(self):
        print("Export?")


    