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
        print("2: Translation: Translate your text into another language. Results are automatically exported to a .txt file")
        print("3: Keyword Analysis: Analyze the keywords in the text. Which words are the most meaningful?")
        print("4: Part of Speech Analysis: Analyze the part of speech of each word in the text")
        print()
        print("**Select your analysis option with the number keys 1 - 4.**")
        
        analysis_choice = input()
        return analysis_choice
    
    def initiate_export(self):
        print("Would you like to export your results to a .txt file? If you translated, prees 'N'.  Y / N")
        user_choice = input()
        user_choice = user_choice.upper()
        
        if user_choice == "Y":
          return True
    
        return False
    
    def export(self, results):
        export_name = input("Please give a name to your export file (no '.txt' needed):")
        export_file = open(f"{export_name}.txt", "w", encoding='utf-8')
        export_file.write(results)


    