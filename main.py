from agent import create_agent
from util import get_message


def normalize_message(message):
    if isinstance(message, dict):
        return message
    return {
        "role": getattr(message, "role", None) or getattr(message, "type", None),
        "content": getattr(message, "content", None),
    }


if __name__ == "__main__":
    agent = create_agent()
    message = get_message()
    history = []
    while True:
        res = agent.invoke(
                input={
                    "messages": history + [message]
                }
            )
        
        print(res["messages"][-1].content)

        history = res["messages"]
        message = get_message()
