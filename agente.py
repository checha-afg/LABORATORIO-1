import re

class AgenteGerencial:
    def __init__(self):
        # Base de conocimiento con temas clave
        self.base_conocimiento = {
            "estrategia": "Las decisiones estratégicas se centran en el largo plazo, como expansión de mercados, innovación o alianzas. Implican alto riesgo y requieren análisis de entorno.",
            "recursos": "La asignación de recursos debe priorizar actividades con mayor retorno de inversión y alineación a los objetivos estratégicos.",
            "riesgos": "La gestión de riesgos implica identificar amenazas, evaluar su impacto y establecer planes de mitigación para asegurar la continuidad del negocio.",
            "liderazgo": "Un buen liderazgo en la toma de decisiones busca equilibrar la lógica analítica con la motivación del equipo y la cultura organizacional.",
            "costos": "El análisis de costos no solo debe considerar lo financiero, sino también el impacto en la productividad, calidad y satisfacción del cliente.",
            "innovacion": "Las decisiones sobre innovación requieren evaluar viabilidad técnica, costos, impacto en clientes y ventaja competitiva en el mercado."
        }

    def es_pregunta_gerencial(self, pregunta: str) -> bool:
        """Detecta si la pregunta pertenece al ámbito de decisiones gerenciales"""
        palabras_clave = ["decisión", "gerencial", "estrategia", "empresa", "riesgo",
                          "recursos", "liderazgo", "costos", "proyecto", "inversión",
                          "objetivos", "planeación", "planificación", "negocio"]
        return any(palabra in pregunta.lower() for palabra in palabras_clave)

    def responder(self, pregunta: str) -> str:
        if not self.es_pregunta_gerencial(pregunta):
            return "Solo puedo responder preguntas relacionadas con la toma de decisiones gerenciales."

        for clave, respuesta in self.base_conocimiento.items():
            if re.search(clave, pregunta.lower()):
                return f"🔎 Análisis: {respuesta}"

        return "Para esa decisión específica recomiendo un análisis basado en datos, evaluación de riesgos y alineación con los objetivos estratégicos."


# Ejemplo de uso
if __name__ == "__main__":
    agente = AgenteGerencial()
    print("🤖 Agente Gerencial listo. Hazme preguntas sobre toma de decisiones.")

    while True:
        pregunta = input("\nTu pregunta: ")
        if pregunta.lower() in ["salir", "exit", "quit"]:
            print("👋 Cerrando el agente gerencial...")
            break
        respuesta = agente.responder(pregunta)
        print(respuesta)