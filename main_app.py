import numpy as np
import scipy

import app_part2, app_part1
import langchain, langchain_core, langchain_groq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import dotenv
from dotenv import load_dotenv
from app_part1 import fetch_product_details
from app_part2 import calculation_reorder
from langchain.agents import create_agent
load_dotenv()
api_key=os.environ.get('GROQ_API_KEY')
extractor_llm=ChatGroq(model='openai/gpt-oss-20b', api_key=api_key, temperature=0.2)
prompt=ChatPromptTemplate.from_messages([('system','''You are a helpful shop assistant.
                                                    Please use the tools available to answer the user's query.
                                                    Please do not answer any queries other than those about reordering of products.'''),
                                                    ('user','{question}')])
parser=StrOutputParser()
agent=create_agent(model=extractor_llm, tools=[fetch_product_details, calculation_reorder], system_prompt=('''You are a helpful shop assistant.
                                                    Please use the tools available to answer the user's query.
                                                    Please do not answer any queries other than those about reordering of products.'''))
product='P1050'
user_question=f'Should I place an order for {product}?\nIf so, for how many pieces? I want a 95% confidence of the item being in stock.'
result=agent.invoke({'messages':[('user',user_question)]})
print(result['messages'][-1].content)

