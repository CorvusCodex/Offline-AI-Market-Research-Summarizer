from utils import run_llama

def market_research(info):
    prompt = f"Summarize this competitor/market information into key insights:\n{info}"
    return run_llama(prompt)

if __name__ == "__main__":
    text = open("market.txt").read()
    print(market_research(text))
