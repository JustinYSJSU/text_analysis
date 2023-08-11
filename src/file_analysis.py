from analysis_tools import AnalysisTools
from analyze_file import FileAnalysis

analyzer = AnalysisTools()
file_analyzer = FileAnalysis()

class FileAnalysis():
  def __init__(self):
    pass
  
  def analyze_file(self, filepath):
    print("Please pick an analysis option")
    analysis_choice = analyzer.analysis_options()
    file = file_analyzer.verify_file(filepath)
    if analysis_choice == "1":
      freq_dict = file_analyzer.word_freq_analysis_file(file)
      print()
      print("***Word Frequency Analysis Results***")
      print()
      
      for word, freq in freq_dict.items():
        print(f"{word}: {freq}")

      print()
      most_freq_word = list(freq_dict.keys())[0]
      print(f"The most frequent word is: '{most_freq_word}' with a frequency of {freq_dict[most_freq_word]}")
