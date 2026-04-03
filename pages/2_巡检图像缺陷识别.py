from io import BytesIO

import pandas as pd
import streamlit as st
from PIL import Image

from services.detect_service import detect_defects

st.set_page_config(page_title="巡检图像缺陷识别", page_icon="🖼️", layout="wide")
st.title("巡检图像缺陷识别")
st.caption("当前为 Mock 识别流程，后续可替换为 RT-DETR 实时推理接口。")

uploaded = st.file_uploader("上传巡检图像", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    if uploaded.type not in {"image/jpeg", "image/png"}:
        st.error("仅支持 JPG / JPEG / PNG 格式。")
        st.stop()

    image_bytes = uploaded.read()
    original_img = Image.open(BytesIO(image_bytes)).convert("RGB")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 原始图像")
        st.image(original_img, use_container_width=True)

    if st.button("执行缺陷识别", type="primary"):
        with st.spinner("正在执行 Mock 识别..."):
            result = detect_defects(image_bytes=image_bytes, use_mock=True)

        with col2:
            st.markdown("#### 检测结果可视化")
            st.image(result["annotated_image"], use_container_width=True)

        st.success(f"识别完成，共检测到 {result['count']} 处缺陷。")
        st.markdown("#### 识别结果表")
        st.dataframe(pd.DataFrame(result["detections"]), use_container_width=True, hide_index=True)
else:
    st.info("请先上传一张巡检图像以开始演示流程。")
