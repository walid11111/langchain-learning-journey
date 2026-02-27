from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel
import os

load_dotenv()

print(os.getenv("GROK_API_KEY"))


# Ist component 
prompt1=PromptTemplate(
    template='geneate a simple notes from the folowwing text \n {text}',
    input_variable=['text']
)

prompt2=PromptTemplate(
    template="generate a five question answers from the following text \n {text}",
    input_varaible=['text']
)

prompt3=PromptTemplate(
    template='merge the provided notes and quiz in a single Document \n notes ->{notes} and {quiz}',
    input_variable=['notes','quiz']
)

# second component
model1=ChatGroq(                 # second component 
    model="llama-3.3-70b-versatile"
)

model2=ChatGroq(
    model="llama-3.1-8b-instant"
)

# 3rd component 
parser=StrOutputParser()



# now parrallel chain logic
parallel_chain=RunnableParallel(    # RunnableParrallel is a kind of Runnable that help to to execute multiple chains parrallel
    {
        'notes': prompt1 | model1 | parser,
        'quiz': prompt2 | model2 | parser
    }
)

merge_chain= prompt3 | model1 | parser

chain = parallel_chain | merge_chain 


text="""   Artificial Intelligence (AI) is one of the most transformative technologies of the 21st century. It refers to the simulation of human intelligence by machines, particularly computer systems, that can perform tasks traditionally requiring human cognition. These tasks include problem-solving, decision-making, natural language understanding, speech recognition, and learning from experience. AI is not a single technology, but rather a broad field that includes subdomains such as Machine Learning (ML), Deep Learning, Natural Language Processing (NLP), Robotics, and Computer Vision.

The history of AI dates back to the 1950s, when pioneers like Alan Turing and John McCarthy laid the foundation for intelligent systems. Early AI research focused on symbolic reasoning and rule-based systems, but the limitations of computing power and data availability slowed progress. The recent explosion of big data, improved algorithms, and advanced hardware such as GPUs and LPUs has reignited rapid developments in AI. Today, AI is used in almost every field — from healthcare and finance to education, entertainment, and transportation.

One of the most significant breakthroughs in AI is Machine Learning, which allows computers to learn patterns from data without explicit programming. Deep Learning, a subset of ML, uses artificial neural networks with multiple layers to analyze complex data like images, videos, and natural language. This has enabled technologies such as facial recognition, self-driving cars, language translation, and generative AI systems like ChatGPT. NLP has made it possible for machines to understand and generate human-like language, making chatbots, voice assistants, and automated translators widely accessible.


"""
Result= chain.invoke({'text':text})
print(Result)


chain.get_graph().print_ascii()


