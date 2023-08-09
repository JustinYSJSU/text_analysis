from analysis_tools import AnalysisTools

analyzer = AnalysisTools()

class TextAnalysis():
  def __init__(self):
    pass
  
  #Given user input from main.py, check if a path exists 
  #If so, they have provided a file. If not, they have provided text
  def analyze_text(user_input, self):
    print("Please pick an analysis option")
    analysis_choice = analyzer.analysis_options()