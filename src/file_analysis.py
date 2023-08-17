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
      file_analyzer.word_freq_analysis_file(file)
  
    if analysis_choice == "2":
      file_analyzer.translate_file(file)
      
    if analysis_choice == "3":
       file_analyzer.keyword_analysis_file(file)
       
    if analysis_choice == "4":
      file_analyzer.part_of_speech_analysis_file(file)