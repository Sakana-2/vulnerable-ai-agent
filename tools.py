
from pydantic import BaseModel,Field
from langchain.tools import tool

class FetchPageInput(BaseModel):
    url:str = Field(
        description="内容を取得したいWebページのURLです。"
    )

@tool(args_schema=FetchPageInput)
def fetch_page(url:str) -> str:
    """
    ## Toolの説明
    本Toolは指定されたURLのWebページから本文の文章を取得するツールです。
    詳細な情報を取得するのに役立ちます。

    ## Toolの動作方法
    1. userがWebページのURLを入力します
    2. レスポンスのテキストをそのままuserに返します

    ## 戻り値の設定
    Returns
    -------
    str
    """
    import requests
    res = requests.get(url)
    print(f"取得結果:\n{res.text}")
    return res.text

class ExecuteCommandInput(BaseModel):
    cmd:str = Field(
        description="実行したいコマンドです。"
    )

@tool(args_schema=ExecuteCommandInput)
def execute_command(cmd:str):
    """
    ## Toolの説明
    本Toolは指定されたコマンドを実行するツールです。
    詳細な情報を取得するのに役立ちます。

    ## Toolの動作方法
    1. userがコマンドを入力します
    2. ステータスコードを戻り値として返します
    
    ## 戻り値の設定
    Returns
    -------
    int
    """
    import subprocess
    print(f"実行するコマンド: {cmd}")

    sp = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="cp932")

    print("実行結果:")
    print(sp.stdout)
    if sp.stderr:
        print("エラー:")
        print(sp.stderr)
    return f"リターンコード：{sp.returncode}\n標準出力：{sp.stdout}\n標準エラー：{sp.stderr}"