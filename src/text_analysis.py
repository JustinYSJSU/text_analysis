from analysis_tools import AnalysisTools
from analyze_text import TextAnalysis

analyzer = AnalysisTools()
text_analyzer = TextAnalysis()

class TextAnalysis():
  def __init__(self):
    pass
  
  def analyze_text(self, user_input):
    results = ""
    print("Please pick an analysis option")
    analysis_choice = analyzer.analysis_options()
    if analysis_choice == "1":
        results = text_analyzer.word_freq_analysis_text(user_input)

    if analysis_choice == "2":
        results = text_analyzer.translate_text(user_input)

    if analysis_choice == "3": 
       results = text_analyzer.keyword_analysis_text(user_input)
           
    if analysis_choice == "4":
        results = text_analyzer.part_of_speech_analysis_text(user_input)

    export = analyzer.initiate_export()

    if export:
       analyzer.export(results)
