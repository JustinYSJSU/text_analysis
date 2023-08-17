from text_analysis import TextAnalysis
from file_analysis import FileAnalysis

def main():
  print("************************************")
  print("*Welcome to the Text Analysis tool!*")
  print("************************************")

  print()
  print("***PLEASE NOTE: Unless you are translating, your input text / file MUST be in ENGLISH.***")
  print("Press 'T' to input your own text via keyboard")
  print("Press 'F' to input a path to a file")
  print()

  user_choice = input("Enter here: ")
  user_choice = user_choice.upper()

  user_text_file = ""
  if(user_choice == 'T'):
    user_text_file = input("Enter your text here: ")
    text_analyzer = TextAnalysis()
    print()
    text_analyzer.analyze_text(user_text_file)

  if(user_choice == 'F'):
    user_text_file = input("Enter your file path here: ")
    file_analyzer = FileAnalysis()
    print()
    file_analyzer.analyze_file(user_text_file)
    
if __name__ == "__main__":
  main()