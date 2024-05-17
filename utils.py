from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu

# import os


def generate_xiaohongshu(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(
                       model="gpt-3.5-turbo",
                       #model="gpt-4-0125-preview",
                       openai_api_key="sk-eIxdgzUkkdfvcLSYD9306822213945Bf859f2cB63d3c5d18",
                       #openai_api_key="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"
                       base_url="https://api.aigc369.com/v1"
                       )
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result

#print(generate_xiaohongshu("大模型",  "sk-eIxdgzUkkdfvcLSYD9306822213945Bf859f2cB63d3c5d18"))
