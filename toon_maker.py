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
            TOON Format Structure:
            task:
              description: <summary>
              type: <type>
              complexity: <level>
            objective:
              purpose: <goal>
              success_criteria[N]: <list>
              impact: <impact>
              target_audience:
                knowledge_level: <level>
                expectations: <expectations>
            outcome:
              deliverables[N]:
                type: <type>
                format: <format>
              content_requirements[N]: <list>
              quality_standards[N]{criterion,requirement,priority}:
                <csv_rows>
            narrow:
              scope:
                include[N]: <list>
                exclude[N]: <list>
              constraints:
                <key>: <value>
              assumptions[N]: <list>
            """

            system_instruction = (
                "You are an expert system architect. Convert the following Master Prompt into the TOON (Token-Oriented Object Notation) format. "
                "Use the structure provided below. Keep it token-efficient. "
                f"The output must be in {self.language}. "
                f"Structure guide: {toon_guide}"
            )

            response = self.model.generate_content(f"{system_instruction}\n\nMaster Prompt: {master_prompt}")
            return response.text
        except Exception as e:
            return f"Error generating TOON format: {str(e)}"

    def process(self, prompt: str) -> str:
        """
        Main processing pipeline: Normal -> Master -> TOON
        """
        t = self.translations[self.language]
        
        # Stage 1: Expand to master prompt
        master = self.expand_to_master(prompt)
        
        # Stage 2: Convert to TOON format
        toon = self.master_to_toon(master)
        
        # Format final output
        output = f"""## {t['ORIGINAL_PROMPT']}
{prompt}

---

## {t['MASTER_PROMPT']}
{master}

---

## {t['TOON_FORMAT']}

```toon
{toon}
```"""
        
        return output

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
