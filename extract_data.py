import re
from medical_data_source import MEDICAL_KNOWLEDGE

def extract_lab_data(report_text):
    extracted_data = []
    for line in report_text.splitlines():
        line = line.strip()
        if not line:
            continue
        for test_name_on_report, details in MEDICAL_KNOWLEDGE.items():
            if re.search(r"\b" + re.escape(test_name_on_report) + r"\b", line, re.IGNORECASE):
                match = re.search(r"([0-9.]+)\s*([a-zA-Z/]+)?\s*(.*)", line, re.IGNORECASE)
                if match:
                    result = match.group(1)
                    unit = match.group(2) if match.group(2) else ""
                    range_match = re.search(r"(\d+[\.-]?\d*)\s*[-–—]\s*(\d+[\.-]?\d*)", line)
                    reference_range = f"{range_match.group(1)}-{range_match.group(2)}" if range_match else "Not found"
                    extracted_data.append({
                        "test": details["standard_name"],
                        "result": result,
                        "unit": unit,
                        "raw_line": line,
                        "reference_range_raw": reference_range
                    })
                    break
    return extracted_data
