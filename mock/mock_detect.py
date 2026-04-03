from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from typing import Any

from PIL import Image, ImageDraw


@dataclass
class Detection:
    defect_type: str
    confidence: float
    bbox: tuple[int, int, int, int]


def run_mock_detection(image_bytes: bytes) -> dict[str, Any]:
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    width, height = image.size

    detections = [
        Detection("绝缘子污闪", 0.93, (int(width * 0.12), int(height * 0.2), int(width * 0.34), int(height * 0.55))),
        Detection("导线断股", 0.88, (int(width * 0.52), int(height * 0.28), int(width * 0.82), int(height * 0.62))),
    ]

    drawn = image.copy()
    draw = ImageDraw.Draw(drawn)
    for det in detections:
        draw.rectangle(det.bbox, outline=(255, 80, 80), width=4)
        draw.text((det.bbox[0], max(0, det.bbox[1] - 18)), f"{det.defect_type} {det.confidence:.2f}", fill=(255, 80, 80))

    table_rows = [
        {
            "缺陷类别": det.defect_type,
            "置信度": round(det.confidence, 3),
            "边界框坐标": str(det.bbox),
        }
        for det in detections
    ]

    return {
        "original_image": image,
        "annotated_image": drawn,
        "detections": table_rows,
        "count": len(table_rows),
    }
