import json
from typing import Any
from groq import Groq
from app.core.config import settings

class Ia_Service():
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)

    def generar_recomendacion(self, resultado: dict[str,any]) -> str:
        system_prompt = """
Eres un analista experto.
Analiza el JSON y devuelve recomendaciones claras en texto plano.

Reglas:
- No devuelvas JSON
- Responde en texto limpio y sin formatos
- Sé concreto y accionable
"""

        user_prompt = f"""
Analiza este JSON:

{json.dumps(resultado, ensure_ascii=False, indent=2)}
"""

        try:
            completion = self.client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.3,
                max_completion_tokens=1000,
                reasoning_effort="medium",
                reasoning_format="hidden",
                stream=False,
            )

            return completion.choices[0].message.content.strip()

        except Exception as e:
            return f"Error generando recomendación: {str(e)}"