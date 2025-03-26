from google_vertex_init import *

def generate_ai_explanation(llm_model, test_name, result, unit, reference_range):
    if not USE_LLM or not llm_model:
        return "AI explanation is disabled. Please set GOOGLE_CLOUD_PROJECT and authenticate."
    try:
        prompt = f"Explain in simple terms what the lab test '{test_name}' measures. The result is '{result} {unit}', and the typical reference range is '{reference_range}'."
        response = llm_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating AI explanation (Vertex AI): {e}"

def generate_ai_recommendations(llm_model, analysis_results):
    if not USE_LLM or not llm_model or not analysis_results:
        return "AI recommendations are disabled or no data to analyze."
    prompt_text = "Based on the following lab report analysis, provide general wellness tips and suggest questions the user might ask their doctor. Avoid giving specific medical advice or diagnoses. "
    for result in analysis_results:
        prompt_text += f"{result['test']}: {result['result']} {result['unit']} ({result['status']}). "
        if result['status'] == 'high':
            prompt_text += f"This is higher than the normal range. "
        elif result['status'] == 'low':
            prompt_text += f"This is lower than the normal range. "

    try:
        response = llm_model.generate_content(prompt_text)
        return response.text.strip()
    except Exception as e:
        return f"Error generating AI recommendations (Vertex AI): {e}"