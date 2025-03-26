import streamlit as st
from vertexai.generative_models import GenerativeModel
import vertexai
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "test-vertex-key.json"

PROJECT_ID = "test-vertex-454907"
REGION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")  # Default region

if not PROJECT_ID:
    st.warning("Please set the GOOGLE_CLOUD_PROJECT environment variable to enable Google Vertex AI features.")
    USE_LLM = False
else:
    USE_LLM = True
    LLM_MODEL_NAME = "gemini-pro"  # Choose an appropriate Gemini model

def initialize_vertex_ai():
    if USE_LLM:
        vertexai.init(project=PROJECT_ID, location=REGION)
        return GenerativeModel("gemini-2.0-flash-001")
    return None

llm_model = initialize_vertex_ai()
