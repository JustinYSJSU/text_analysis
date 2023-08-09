from text_analysis import TextAnalysis

def main():
  print("************************************")
  print("*Welcome to the Text Analysis tool!*")
  print("************************************")

  print()
  print("Press 'T' to input your own text via keyboard")
  print("Press 'F' to input a path to a file")
  print()

  user_choice = input("Enter here: ")
  user_text_file = ""
  if(user_choice == 'T'):
    user_text_file = input("Enter your text here: ")
    text_analyzer = TextAnalysis()
    print()
    text_analyzer.analyze_text(user_text_file)


  if(user_choice == 'F'):
    user_text_file = input("Enter your file path here: ")
    
if __name__ == "__main__":
  main()