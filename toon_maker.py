"""
TOON-Maker: Normal to Master to TOON Format Converter
Supports English and French
Implements AI-powered prompt expansion and TOON format conversion using Google Gemini
"""

import os
import google.generativeai as genai
from typing import Dict, Any, List

class ToonMaker:
    def __init__(self, language: str = "en"):
        self.language = language
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.model = None
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            # Try to initialize with preferred model, fallback to others
            # Updated for Nov 2025 available models
            models_to_try = [
                'gemini-2.5-flash', 
                'gemini-2.0-flash', 
                'gemini-pro-latest',
                'gemini-1.5-flash',
                'gemini-pro'
            ]
            for model_name in models_to_try:
                try:
                    self.model = genai.GenerativeModel(model_name)
                    # Test the model with a simple generation to ensure it works
                    self.model.generate_content("Test")
                    print(f"Successfully initialized with model: {model_name}")
                    break
                except Exception as e:
                    print(f"Failed to initialize {model_name}: {e}")
                    self.model = None
            
            if not self.model:
                 print("Warning: Could not initialize any Gemini model. Please check your API Key.")
        else:
            print("Warning: GEMINI_API_KEY not found. Falling back to simple mode.")

        self.translations = {
            "en": {
                "ORIGINAL_PROMPT": "ORIGINAL PROMPT",
                "MASTER_PROMPT": "MASTER PROMPT",
                "TOON_FORMAT": "TOON FORMAT",
                "ERROR": "Error: API Key missing or invalid."
            },
            "fr": {
                "ORIGINAL_PROMPT": "PROMPT ORIGINAL",
                "MASTER_PROMPT": "PROMPT MAÎTRE",
                "TOON_FORMAT": "FORMAT TOON",
                "ERROR": "Erreur: Clé API manquante ou invalide."
            }
        }

    def expand_to_master(self, prompt: str) -> str:
        """
        Expand a simple prompt into a comprehensive master prompt using Gemini.
        """
        if not self.model:
            return f"[Basic Expansion] {prompt}\n\n(Error: AI Unavailable. Please check your GEMINI_API_KEY in backend/.env)"

        try:
            system_instruction = (
                "You are an expert prompt engineer. Your task is to take a simple user prompt "
                "and expand it into a comprehensive 'Master Prompt'. "
                "The Master Prompt should include context, specific requirements, stylistic guidelines, "
                "and any necessary constraints to ensure the best possible output from an AI. "
                "IMPORTANT: Do not invent specific data values (like '5000 devices' or specific dates) unless the user provided them. "
                "Use placeholders or general terms if specific details are missing. "
                f"The output must be in {self.language}."
            )
            
            response = self.model.generate_content(f"{system_instruction}\n\nUser Prompt: {prompt}")
            return response.text
        except Exception as e:
            return f"Error generating Master Prompt: {str(e)}"

    def master_to_toon(self, master_prompt: str) -> str:
        """
        Convert a master prompt to TOON (Token-Oriented Object Notation) format using Gemini.
        """
        if not self.model:
            return "TOON format generation requires AI. Please check your API Key."

        try:
            toon_guide = """
            STRICT TOON SYNTAX RULES:
            1. Length Marker: Arrays must have a length marker, e.g., `users[3]`.
            2. Field Names: For arrays of objects, define fields once in curly braces, e.g., `users[3]{id,name,email}`.
            3. Data Rows: Array items must be CSV-like rows matching the field order. No quotes around values unless necessary.
            4. Nested Objects: Use YAML-like indentation (2 spaces).
            5. Key-Value: Simple keys are `key: value`.

            EXAMPLE INPUT (JSON):
            {
              "users": [
                {"id": 1, "name": "Sarah", "role": "Admin"},
                {"id": 2, "name": "Mike", "role": "Editor"}
              ],
              "meta": {"ver": "1.0"}
            }

            EXAMPLE OUTPUT (TOON):
            users[2]{id,name,role}:
              1,Sarah,Admin
              2,Mike,Editor
            meta:
              ver: "1.0"

            Template to follow for this task:
            task:
              description: <summary>
              type: <type>
              complexity: <level>
            objective:
              purpose: <goal>
              success_criteria[N]: <comma_separated_list>
              impact: <impact>
              target_audience:
                knowledge_level: <level>
                expectations: <expectations>
            outcome:
              deliverables[N]{type,format}:
                <type>,<format>
              content_requirements[N]: <comma_separated_list>
              quality_standards[N]{criterion,requirement,priority}:
                <criterion>,<requirement>,<priority>
            narrow:
              scope:
                include[N]: <comma_separated_list>
                exclude[N]: <comma_separated_list>
              constraints:
                <key>: <value>
              assumptions[N]: <comma_separated_list>
            """

            system_instruction = (
                "You are an expert system architect. Convert the following Master Prompt into the TOON (Token-Oriented Object Notation) format. "
                "You must STRICTLY follow the provided syntax and template. "
                "Do NOT output JSON. Do NOT output Markdown code blocks. Output ONLY the raw TOON text. "
                f"The output must be in {self.language}. "
                f"Structure guide: {toon_guide}"
            )

            response = self.model.generate_content(f"{system_instruction}\n\nMaster Prompt: {master_prompt}")
            # Clean up potential markdown code blocks if the model ignores instructions
            text = response.text.strip()
            if text.startswith("```toon"):
                text = text[7:]
            elif text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            return text.strip()
        except Exception as e:
            return f"Error generating TOON format: {str(e)}"

    def process(self, prompt: str) -> str:
        """
        Main processing pipeline: Normal -> Master -> TOON
        Returns ONLY the TOON formatted text.
        """
        # Stage 1: Expand to master prompt (Internal only)
        master = self.expand_to_master(prompt)
        
        # Stage 2: Convert to TOON format
        toon = self.master_to_toon(master)
        
        return toon

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="TOON-Maker: Normal to Master to TOON Format Converter")
    parser.add_argument("prompt", type=str, help="Normal prompt to convert")
    parser.add_argument("--lang", type=str, choices=["en", "fr"], default="en", help="Language: en or fr")
    args = parser.parse_args()
    
    # Load env for standalone run
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), 'backend', '.env'))
    
    tm = ToonMaker(language=args.lang)
    print(tm.process(args.prompt))
