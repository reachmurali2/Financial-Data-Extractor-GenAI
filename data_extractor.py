'''
This module processes financial text using a Large Language Model(LLM) from langchain_groq
It takes financial text as input, extracts Revenue (Actual & Expected) and EPS (Actual & Expected),
and returns a structured JSON response.
'''

from langchain_groq import ChatGroq                          # Imports ChatGroq to use Groq's LLM.import
from langchain_core.prompts import PromptTemplate            # Imports PromptTemplate to format prompts for the model
from langchain_core.output_parsers import JsonOutputParser   # Imports JsonOutPutParser to convert the LLM's response into structured JSON
from langchain_core.exceptions import OutputParserException  # Imports OutputParserException to handle errors in JSON parsing
from dotenv import load_dotenv                               # Loads environment variables from a .env file.

load_dotenv()
llm=ChatGroq(model_name='llama-3.3-70b-versatile'api_key = api_key)           # Creates an instance of the LLM (Llama 3.3-70B)/Chatgroq

# Mock function to extract financial data (replace with actual function)
def extract(article_text):                                   # Defines the extracts function, which takes a financial news as input
    prompt="""                                               # Defines a structured prompt to instruct the model on extracting financial data.
    From the below news article, extract revenue and eps in JSON format containing the
    following keys: 'revenue_actual', 'revenue_expected', 'eps_actual', 'eps_expected'.
    Each values should have a unit such as million or billion.
    only return the valid JSON. No preamble.
    
    Article
    =======
    {article}                                                # Placeholder where the financial article text will be inserted.
    """
    pt = PromptTemplate.from_template(prompt)                # Converts the string prompt into a structured PromptTemplate/pt is a PromptTemplate object created from a string template.
    global llm                                               # Ensures llm is accessible globally within the script.

    chain = pt|llm                                           # pt|llm creates a streamlined LangChain pipeline. The formatted prompt from PromptTemplate(pt) is sent to the LLM(llm). The LLM processes the prompt and returns a response.
    response = chain.invoke({'article':article_text})        # Sends the Financial article to the LLM and gets a response.
    parser=JsonOutputParser()                                # Initializes a JSON parser to process the model's response.

    try:                                                     # starts error handling for potential parsing issues.
        res = parser.parse(response.content)                 # Parses the response into structured JSON.
    except OutputParserException:                            # Catches exceptions if parsing fails.
        raise OutputParserException("Context too big. Unable to parse jobs.")  # Raises an error if the response cannot be parsed.
    return res                                               # Returns the extracted financial data in JSON format.
