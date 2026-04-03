from mock.mock_detect import run_mock_detection
from models.rtdetr_infer import run_rtdetr_infer


def detect_defects(image_bytes: bytes, use_mock: bool = True) -> dict:
    if use_mock:
        return run_mock_detection(image_bytes)
    return run_rtdetr_infer(image_bytes)
