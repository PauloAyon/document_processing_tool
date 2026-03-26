import json
import os
from datetime import datetime


def export_to_json(result: dict, output_dir: str = "output") -> str:
    """Export processing result to a JSON file."""
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{result['filename']}_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print(f"Results saved to: {filepath}")
    return filepath