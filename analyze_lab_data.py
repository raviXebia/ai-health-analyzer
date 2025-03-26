from medical_data_source import MEDICAL_KNOWLEDGE
import re

def analyze_lab_data(extracted_data):
    analysis_results = []
    abnormal_count = 0
    for item in extracted_data:
        test_name = item["test"]
        result = float(item["result"]) if item["result"].replace('.', '', 1).isdigit() else None
        unit = item["unit"]
        status = "normal"

        if test_name in MEDICAL_KNOWLEDGE and result is not None:
            details = MEDICAL_KNOWLEDGE[test_name]
            interpretation = details["interpretation"].get("normal", "Interpretation not available.")
            recommendations = details.get("recommendations", [])
            reference_range_str = details.get("reference_range_explanation", "Reference range information not available.")

            range_parts = re.findall(r"(\d+[\.-]?\d*)", details["reference_range_explanation"])
            if len(range_parts) >= 2:
                lower_bound = float(range_parts[0])
                upper_bound = float(range_parts[1])
                if result < lower_bound:
                    interpretation = details["interpretation"].get("low", interpretation)
                    status = "low"
                    abnormal_count += 1
                elif result > upper_bound:
                    interpretation = details["interpretation"].get("high", interpretation)
                    status = "high"
                    abnormal_count += 1
            else:
                reference_range_str = "Reference range information incomplete."

            analysis_results.append({
                "test": test_name,
                "result": item["result"],
                "unit": unit,
                "raw_line": item["raw_line"],
                "interpretation": interpretation,
                "description": details.get("description", "Description not available."),
                "recommendations": recommendations,
                "reference_range": reference_range_str,
                "status": status
            })
        else:
            analysis_results.append({
                "test": test_name,
                "result": item["result"],
                "unit": unit,
                "raw_line": item["raw_line"],
                "interpretation": "Could not find detailed information for this test.",
                "description": "Description not available.",
                "recommendations": [],
                "reference_range": "Reference range information not available.",
                "status": "unknown"
            })
    return analysis_results, abnormal_count
