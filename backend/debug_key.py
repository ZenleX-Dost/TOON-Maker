import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

target_models = ['gemini-1.5-flash', 'gemini-pro', 'gemini-1.0-pro']
available_models = []
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        available_models.append(m.name)

with open('debug_output.txt', 'w') as f:
    f.write("Checking availability of target models:\n")
    for target in target_models:
        # Check both with and without 'models/' prefix
        found = False
        for avail in available_models:
            if target in avail:
                f.write(f"[OK] Found {target} as {avail}\n")
                found = True
                break
        if not found:
            f.write(f"[FAIL] Could not find {target}\n")

    f.write("\nAll available generateContent models:\n")
    for m in available_models:
        f.write(f"{m}\n")
    print("Output written to debug_output.txt")
