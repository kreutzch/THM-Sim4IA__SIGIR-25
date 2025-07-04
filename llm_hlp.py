import google.generativeai as genai
from openai import OpenAI
import ast
import re
import os

def next_queries_gpt(input, prompt_text, num_required_queries, prompt_instructions, modelname='gpt-4.1-nano', temperature=0):
    client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

    try:
        messages = [{"role": "user", "content": prompt_text + ' ' + prompt_instructions.replace('%NUMOFQUERIES%', str(num_required_queries)) + ' ' + input}]
        
        response = client.chat.completions.create(
            model = modelname,
            messages = messages,
            temperature = temperature
        )
        content = response.choices[0].message.content.strip()

        try:
            content_c = content.replace('```', '')
            next_queries = ast.literal_eval(content_c)

        except Exception as e:
            content_wo_brackets = content_c.replace('[', '').replace(']', '')
            next_queries = [
                re.sub(r"^\s*(?:[\d]+|[-–])[\.\)-]?\s*'\"`", "", line).strip()
                for line in content_wo_brackets.splitlines()
                if line.strip()
            ]
            
        if num_required_queries + 1 == num_required_queries:
            next_queries = next_queries[1:]

    except Exception as e:
        print(f"[ERROR] OpenAI API call failed: {e}")
        return next_queries, True

    if len(next_queries) != num_required_queries:
        print(f"[WARNING] Mismatch: {num_required_queries} input vs {len(next_queries)} output")
        return next_queries, True

    return next_queries, False

def next_queries_gemini(input, prompt_text, num_required_queries, prompt_instructions, modelname='gemini-2.0-flash', temperature=0):
    genai.configure(api_key = os.environ.get("GOOGLE_API_KEY"))
    gemini_model = genai.GenerativeModel(modelname)

    try:
        messages = [{"role": "user", "parts": prompt_text + ' ' + prompt_instructions.replace('%NUMOFQUERIES%', str(num_required_queries)) + ' ' + input}]
        
        completion = gemini_model.generate_content(
            generation_config = genai.types.GenerationConfig(temperature=temperature),
            contents = messages
        )
        content = completion.text.strip()

        try:
            content_c = content.replace('```', '')
            next_queries = ast.literal_eval(content_c)

        except Exception as e:
            content_wo_brackets = content_c.replace('[', '').replace(']', '')
            next_queries = [
                re.sub(r"^\s*(?:[\d]+|[-–])[\.\)-]?\s*'\"`", "", line).strip()
                for line in content_wo_brackets.splitlines()
                if line.strip()
            ]
            
        if num_required_queries + 1 == len(next_queries):
            next_queries = next_queries[1:]

    except Exception as e:
        print(f"[ERROR] Gemini API call failed: {e}")
        return next_queries, True

    if len(next_queries) != num_required_queries:
        print(f"[WARNING] Mismatch: {num_required_queries} input vs {len(next_queries)} output")
        return next_queries, True

    return next_queries, False
