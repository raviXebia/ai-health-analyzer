# --- Medical Knowledge Base ---
MEDICAL_KNOWLEDGE = {
    "Glucose": {
        "standard_name": "Blood Glucose",
        "units": ["mg/dL", "mmol/L"],
        "reference_range_explanation": "Generally, a fasting blood glucose level between 70 and 99 mg/dL is considered normal.",
        "interpretation": {
            "high": "Your blood glucose level is higher than the normal range. This can sometimes indicate issues with how your body processes sugar. It's recommended to discuss this with your doctor for further evaluation and advice.",
            "low": "Your blood glucose level is lower than the normal range. This could indicate potential issues with blood sugar regulation. It's advisable to consult your doctor to determine the cause.",
            "normal": "Your blood glucose level is within the normal range."
        },
        "description": "Measures the amount of glucose (sugar) in your blood. It's a key indicator for diabetes and other metabolic disorders.",
        "recommendations": [
            "Consider a balanced diet with controlled carbohydrate intake.",
            "Regular physical activity may help regulate blood sugar levels.",
            "Follow any monitoring advice provided by your healthcare provider."
        ]
    },
    "Total Cholesterol": {
        "standard_name": "Total Cholesterol",
        "units": ["mg/dL"],
        "reference_range_explanation": "Generally, total cholesterol below 200 mg/dL is considered desirable.",
        "interpretation": {
            "high": "Your total cholesterol level is higher than desirable. High cholesterol can increase the risk of heart disease. It's recommended to discuss this with your doctor for lifestyle modifications or further testing.",
            "low": "Your total cholesterol level is lower than desirable, which is generally good but could sometimes indicate underlying conditions. Consult your doctor if you have concerns.",
            "normal": "Your total cholesterol level is within the desirable range."
        },
        "description": "Measures the total amount of cholesterol in your blood, including LDL ('bad') and HDL ('good') cholesterol.",
        "recommendations": [
            "A heart-healthy diet low in saturated and trans fats is often recommended.",
            "Increasing intake of soluble fiber may be beneficial.",
            "Maintaining a healthy weight and regular exercise are important.",
        ]
    },
    "WBC Count": {
        "standard_name": "White Blood Cell Count",
        "units": ["cells/mcL", "x10^9/L"],
        "reference_range_explanation": "The normal range for white blood cell count is typically between 4,500 and 11,000 cells/mcL.",
        "interpretation": {
            "high": "Your white blood cell count is higher than normal, which could indicate an infection or inflammation. It's important to consult your doctor to determine the underlying cause.",
            "low": "Your white blood cell count is lower than normal, which could make you more susceptible to infections. Consult your doctor for evaluation.",
            "normal": "Your white blood cell count is within the normal range."
        },
        "description": "Measures the number of white blood cells in your blood, which are part of the immune system and help fight infections.",
        "recommendations": [
            "Follow your doctor's advice regarding any potential infection or inflammation.",
            "Maintaining a healthy lifestyle supports your immune system.",
            "Avoid contact with sick individuals if your WBC count is low."
        ]
    },
    # Add more lab tests here
}
