from langchain.text_splitter import RecursiveCharacterTextSplitter,Language


# this is python code and you can write js or html and mardon langauge etc just change mentioend with like python or js or markdown
Text = """
       numbers = [10, 25, 7, 42, 19]           
       largest = max(numbers)
       print("The largest number is:", largest)

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 30,
    chunk_overlap = 0


)

result = splitter.split_text(Text)
print(len(result))
print(result)

print(result[0])