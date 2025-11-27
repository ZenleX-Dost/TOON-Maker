"""
TOON-Maker: Normal to Master to TOON Format Converter
Supports English and French
Implements comprehensive prompt expansion and TOON format conversion
"""

from typing import Dict, Any, List
import re

class ToonMaker:
    def __init__(self, language: str = "en"):
        self.language = language
        self.translations = {
            "en": {
                "ORIGINAL_PROMPT": "ORIGINAL PROMPT",
                "MASTER_PROMPT": "MASTER PROMPT",
                "TOON_FORMAT": "TOON FORMAT",
            },
            "fr": {
                "ORIGINAL_PROMPT": "PROMPT ORIGINAL",
                "MASTER_PROMPT": "PROMPT MAÎTRE",
                "TOON_FORMAT": "FORMAT TOON",
            }
        }

    def expand_to_master(self, prompt: str) -> str:
        """
        Expand a simple prompt into a comprehensive master prompt.
        Adds context, structure, details, and quality criteria.
        """
        prompt_lower = prompt.lower()
        
        # Analyze prompt intent
        is_writing = any(word in prompt_lower for word in ['write', 'create', 'draft', 'compose', 'rédigez', 'écrire', 'créer'])
        is_analysis = any(word in prompt_lower for word in ['analyze', 'analyse', 'explain', 'expliquer', 'compare', 'comparer'])
        is_technical = any(word in prompt_lower for word in ['code', 'program', 'develop', 'build', 'coder', 'programmer', 'développer'])
        
        if self.language == "fr":
            return self._expand_to_master_fr(prompt, is_writing, is_analysis, is_technical)
        else:
            return self._expand_to_master_en(prompt, is_writing, is_analysis, is_technical)
    
    def _expand_to_master_en(self, prompt: str, is_writing: bool, is_analysis: bool, is_technical: bool) -> str:
        """Expand prompt to master format in English"""
        
        base_expansion = f"{prompt.strip()}"
        
        # Add context enrichment
        if is_writing:
            base_expansion += " The content should be well-structured, engaging, and appropriate for the target audience. Use clear language and maintain a consistent tone throughout."
        elif is_analysis:
            base_expansion += " Provide a thorough analysis with supporting evidence and examples. Present information objectively and draw clear conclusions based on the analysis."
        elif is_technical:
            base_expansion += " Follow best practices and coding standards. Include proper error handling, documentation, and ensure the solution is maintainable and scalable."
        else:
            base_expansion += " Ensure the response is comprehensive, well-organized, and addresses all aspects of the request clearly and effectively."
        
        # Add quality criteria
        base_expansion += " The output should demonstrate high quality through accuracy, clarity, and attention to detail."
        
        # Add format specification
        base_expansion += " Structure the response with clear sections and logical flow to enhance readability and comprehension."
        
        return base_expansion
    
    def _expand_to_master_fr(self, prompt: str, is_writing: bool, is_analysis: bool, is_technical: bool) -> str:
        """Expand prompt to master format in French"""
        
        base_expansion = f"{prompt.strip()}"
        
        # Add context enrichment
        if is_writing:
            base_expansion += " Le contenu doit être bien structuré, engageant et adapté au public cible. Utilisez un langage clair et maintenez un ton cohérent tout au long."
        elif is_analysis:
            base_expansion += " Fournissez une analyse approfondie avec des preuves et des exemples à l'appui. Présentez les informations objectivement et tirez des conclusions claires basées sur l'analyse."
        elif is_technical:
            base_expansion += " Suivez les meilleures pratiques et normes de codage. Incluez une gestion appropriée des erreurs, de la documentation et assurez-vous que la solution est maintenable et évolutive."
        else:
            base_expansion += " Assurez-vous que la réponse est complète, bien organisée et aborde tous les aspects de la demande de manière claire et efficace."
        
        # Add quality criteria
        base_expansion += " Le résultat doit démontrer une haute qualité par la précision, la clarté et l'attention aux détails."
        
        # Add format specification
        base_expansion += " Structurez la réponse avec des sections claires et un flux logique pour améliorer la lisibilité et la compréhension."
        
        return base_expansion

    def master_to_toon(self, master_prompt: str) -> str:
        """
        Convert a master prompt to TOON (Token-Oriented Object Notation) format.
        Implements the full TOON structure: Task, Objective, Outcome, Narrow
        """
        if self.language == "fr":
            return self._master_to_toon_fr(master_prompt)
        else:
            return self._master_to_toon_en(master_prompt)
    
    def _extract_task_info(self, prompt: str) -> Dict[str, str]:
        """Extract task-related information from prompt"""
        prompt_lower = prompt.lower()
        
        # Determine task type
        if any(word in prompt_lower for word in ['write', 'create', 'draft', 'compose', 'rédigez', 'écrire', 'créer']):
            task_type = "creation" if 'en' in self.language else "création"
        elif any(word in prompt_lower for word in ['analyze', 'analyse', 'explain', 'expliquer']):
            task_type = "analysis" if 'en' in self.language else "analyse"
        elif any(word in prompt_lower for word in ['code', 'program', 'develop', 'coder', 'programmer']):
            task_type = "development" if 'en' in self.language else "développement"
        elif any(word in prompt_lower for word in ['transform', 'convert', 'transformer', 'convertir']):
            task_type = "transformation" if 'en' in self.language else "transformation"
        else:
            task_type = "general" if 'en' in self.language else "général"
        
        # Determine complexity
        word_count = len(prompt.split())
        if word_count < 20:
            complexity = "simple"
        elif word_count < 50:
            complexity = "moderate" if 'en' in self.language else "modérée"
        else:
            complexity = "complex" if 'en' in self.language else "complexe"
        
        return {
            "type": task_type,
            "complexity": complexity
        }
    
    def _master_to_toon_en(self, master_prompt: str) -> str:
        """Convert master prompt to TOON format in English"""
        
        task_info = self._extract_task_info(master_prompt)
        
        # Extract first sentence as description
        sentences = master_prompt.split('.')
        description = sentences[0].strip() if sentences else master_prompt[:100]
        
        toon = f"""task:
  description: {description}
  type: {task_info['type']}
  complexity: {task_info['complexity']}

objective:
  purpose: Fulfill the user's request with high quality and comprehensive results
  success_criteria[3]: accuracy,completeness,clarity
  impact: Deliver value through well-crafted output that meets expectations
  target_audience:
    knowledge_level: general
    expectations: professional_quality

outcome:
  deliverables[1]:
    type: {task_info['type']}_output
    format: structured_and_clear
  content_requirements[3]: addresses_prompt,well_organized,high_quality
  quality_standards[4]{{criterion,requirement,priority}}:
    accuracy,factually_correct,high
    clarity,easy_to_understand,high
    completeness,comprehensive_coverage,high
    style,appropriate_tone,medium

narrow:
  scope:
    include[2]: primary_request,relevant_context
    exclude[2]: out_of_scope_topics,unnecessary_details
  constraints:
    format: as_specified_in_prompt
    quality: professional_standard
    relevance: directly_addresses_request
  assumptions[2]: user_wants_quality_output,standard_interpretations_apply"""
        
        return toon
    
    def _master_to_toon_fr(self, master_prompt: str) -> str:
        """Convert master prompt to TOON format in French"""
        
        task_info = self._extract_task_info(master_prompt)
        
        # Extract first sentence as description
        sentences = master_prompt.split('.')
        description = sentences[0].strip() if sentences else master_prompt[:100]
        
        toon = f"""task:
  description: {description}
  type: {task_info['type']}
  complexity: {task_info['complexity']}

objective:
  purpose: Répondre à la demande de l'utilisateur avec qualité et résultats complets
  success_criteria[3]: précision,exhaustivité,clarté
  impact: Fournir de la valeur grâce à un résultat bien conçu qui répond aux attentes
  target_audience:
    knowledge_level: général
    expectations: qualité_professionnelle

outcome:
  deliverables[1]:
    type: résultat_{task_info['type']}
    format: structuré_et_clair
  content_requirements[3]: répond_au_prompt,bien_organisé,haute_qualité
  quality_standards[4]{{criterion,requirement,priority}}:
    précision,factuellement_correct,haute
    clarté,facile_à_comprendre,haute
    exhaustivité,couverture_complète,haute
    style,ton_approprié,moyenne

narrow:
  scope:
    include[2]: demande_principale,contexte_pertinent
    exclude[2]: sujets_hors_sujet,détails_inutiles
  constraints:
    format: tel_que_spécifié_dans_le_prompt
    quality: standard_professionnel
    relevance: répond_directement_à_la_demande
  assumptions[2]: utilisateur_veut_qualité,interprétations_standard_applicables"""
        
        return toon

    def process(self, prompt: str) -> str:
        """
        Main processing pipeline: Normal -> Master -> TOON
        Returns formatted output with all three stages
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
    import sys
    import argparse
    parser = argparse.ArgumentParser(description="TOON-Maker: Normal to Master to TOON Format Converter")
    parser.add_argument("prompt", type=str, help="Normal prompt to convert")
    parser.add_argument("--lang", type=str, choices=["en", "fr"], default="en", help="Language: en or fr")
    args = parser.parse_args()
    tm = ToonMaker(language=args.lang)
    print(tm.process(args.prompt))
