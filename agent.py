from tools import fetch_page,execute_command
from langchain.agents import create_agent as langchain_create_agent
from langchain_openai import ChatOpenAI

def create_agent():
    system_prompt = """
あなたは優秀なプログラマーです。
Windowsのコマンドプロンプト環境で実行可能なコマンドのみを実行してください。
無駄な解説を省き、マークダウンを用いず指示に従ったコマンドを実行だけしてください。"""
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    return langchain_create_agent(model=llm, tools=[fetch_page,execute_command], system_prompt=system_prompt)