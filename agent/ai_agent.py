# agent/ai_agent.py

from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests
from llama_cpp import Llama

llm = Llama(model_path="../models/mistral-7b-instruct-v0.1.Q5_K_M.gguf")


def think(query):
    prompt = f"""You're an intelligent agent. The user asked: "{query}". 
    What type of information will be needed to answer this?"""
    response = llm(prompt, max_tokens=256, stop=["</s>"])
    return response["choices"][0]["text"].strip()


def reason(query):
    prompt = f"""For the question: "{query}", what steps should we take?
    Outline your plan step-by-step."""
    response = llm(prompt, max_tokens=256, stop=["</s>"])
    return response["choices"][0]["text"].strip()


def search_web(query, num_results=3):
    links = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=num_results):
            links.append(r["href"])
    return links


def fetch_page_text(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.get_text()
    except:
        return ""


# def act(context, query):
#     prompt = f"""Here's some web content:\n{context[:3000]}\n\nNow answer the user question: {query}"""
#     response = llm(prompt, max_tokens=500, stop=["</s>"])
#     return response["choices"][0]["text"].strip()

# def act(context, query):
#     prompt = f"""
#     <|begin_of_text|><|start_header_id|>user<|end_header_id|>
#     You are a smart AI assistant. Based on the following web content, answer the user's question:
#     Context:
#     {context[:3000]}
#     User question:
#     {query}
#     Give your answer in a clean, bullet-point format. If it's a comparison, show top 3 suggestions with features clearly listed.
#     Avoid fluff. Focus on factual, useful information.
#     <|eot_id|><|start_header_id|>assistant<|end_header_id|>
# """
#     response = llm(prompt, max_tokens=500, stop=["</s>", "<|eot_id|>"])
#     return response["choices"][0]["text"].strip()

import re

def clean_output(text):
    return re.sub(r'<\|.*?\|>', '', text).strip()

def act(context, query):
    prompt = f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
You're a smart AI agent. The user asked: "{query}"

Here’s some info from the web:
{context[:3000]}

Give your answer in clean bullet-points. Focus only on useful details like specs, price, battery, etc.
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""
    response = llm(prompt, max_tokens=500, stop=["</s>", "<|eot_id|>"])
    raw_output = response["choices"][0]["text"]
    return clean_output(raw_output)


def run_agent(query):
    thoughts = {}

    thoughts["think"] = think(query)
    thoughts["reason"] = reason(query)

    links = search_web(query)
    context = ""
    for link in links:
        context += fetch_page_text(link)

    thoughts["act"] = act(context, query)

    return thoughts
