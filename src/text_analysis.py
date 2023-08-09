from analysis_tools import AnalysisTools
from analyze_text import TextAnalysis

analyzer = AnalysisTools()
text_analyzer = TextAnalysis()

class TextAnalysis():
  def __init__(self):
    pass
  
  def analyze_text(self, user_input):
    print("Please pick an analysis option")
    analysis_choice = analyzer.analysis_options()

    if analysis_choice == "1":
      freq_dict = text_analyzer.word_freq_analysis_text(user_input)
      print()
      print("***Word Frequency Analysis Results***")
      print()
      
      for word, freq in freq_dict.items():
        print(f"{word}: {freq}")

      print()
      most_freq_word = list(freq_dict.keys())[0]
      print(f"The most frequent word is: '{most_freq_word}' with a frequency of {freq_dict[most_freq_word]}")
