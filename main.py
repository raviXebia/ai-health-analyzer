import streamlit as st
import pytesseract
from pdf2image import convert_from_bytes
from analyze_lab_data import analyze_lab_data
from extract_data import extract_lab_data
from ai_services import *
from google_vertex_init import *

st.title("Interactive Health Report Analyzer with AI")
st.subheader("Upload your lab report and get a simplified summary with AI-powered insights.")

report_file = st.file_uploader("Upload your lab report (PDF)", type=["pdf"])

if report_file is not None:
    try:
        pdf_bytes = report_file.read()
        images = convert_from_bytes(pdf_bytes, dpi=300)
        report_text = ""
        for img in images:
            report_text += pytesseract.image_to_string(img) + "\n"

        st.subheader("Extracted Text from PDF:")
        st.text_area("Raw Extracted Text", report_text, height=200)

        extracted_data = extract_lab_data(report_text)
        if extracted_data:
            analysis_results, abnormal_count = analyze_lab_data(extracted_data)

            st.subheader("Analysis Results:")
            if abnormal_count > 0:
                st.warning(f"Found {abnormal_count} parameters outside the typical reference range. AI-powered insights and general recommendations are provided below. It's crucial to discuss these results with your doctor.")
            else:
                st.success("All analyzed parameters appear to be within the typical reference range. AI-powered insights are provided below.")

            for result in analysis_results:
                with st.expander(f"**{result['test']}**: {result['result']} {result['unit']} ({result['status'].capitalize()})"):
                    st.markdown(f"* **Description:** {result['description']}")
                    st.markdown(f"* **Reference Range:** {result['reference_range']}")
                    st.markdown(f"* **Interpretation:** {result['interpretation']}")

                    if USE_LLM:
                        print(f"Calling generate_ai_explanation with: llm_model={llm_model}, test_name='{result['test']}', result='{result['result']}', unit='{result['unit']}', reference_range='{result['reference_range']}'")
                        ai_explanation = generate_ai_explanation(llm_model, result['test'], result['result'], result['unit'], result['reference_range'])
                        st.subheader("AI-Powered Explanation (Google Vertex AI):")
                        st.markdown(ai_explanation)
                    else:
                        st.info("AI explanation is disabled. Set OPENAI_API_KEY to enable.")

                    if result['recommendations']:
                        st.subheader("General Recommendations:")
                        for rec in result['recommendations']:
                            st.markdown(f"- {rec}")

            if analysis_results and abnormal_count > 0 and USE_LLM:
                st.subheader("AI-Generated General Wellness Tips and Questions for Your Doctor:")
                ai_recommendations = generate_ai_recommendations(analysis_results)
                st.markdown(ai_recommendations)
            elif abnormal_count > 0 and not USE_LLM:
                st.info("AI-powered general wellness tips are disabled. Set OPENAI_API_KEY to enable.")

        else:
            st.warning("No recognizable lab data found in the report.")

    except Exception as e:
        st.error(f"Error reading PDF or performing OCR: {e}")

st.markdown("---")
st.info("This tool provides a simplified interpretation and AI-powered insights from your lab report for informational purposes only. It is not a substitute for professional medical advice. Always consult with your doctor for diagnosis and treatment.")