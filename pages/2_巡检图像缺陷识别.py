from io import BytesIO

import pandas as pd
import streamlit as st
from PIL import Image

from services.detect_service import detect_defects

st.set_page_config(page_title="巡检图像缺陷识别", page_icon="🖼️", layout="wide")

st.title("巡检图像缺陷识别")
st.caption("用于演示巡检图像上传、Mock 缺陷识别与结果展示流程。")

left, right = st.columns([1, 1])

with left:
    st.markdown("### 图像输入区")
    uploaded = st.file_uploader("上传巡检图像", type=["jpg", "jpeg", "png"])
    st.caption("支持格式：JPG / JPEG / PNG")

    image_bytes = None
    if uploaded is not None:
        if uploaded.type not in {"image/jpeg", "image/png"}:
            st.error("仅支持 JPG / JPEG / PNG 格式。")
            st.stop()

        image_bytes = uploaded.read()
        original_img = Image.open(BytesIO(image_bytes)).convert("RGB")
        st.markdown("#### 原图预览")
        st.image(original_img, use_container_width=True)

with right:
    st.markdown("### 识别输出区")
    st.write("点击按钮执行 Mock 检测，右侧将展示带框结果图。")
    run_btn = st.button("执行缺陷识别", type="primary", use_container_width=True)

    if run_btn and image_bytes is not None:
        with st.spinner("正在执行 Mock 识别..."):
            result = detect_defects(image_bytes=image_bytes, use_mock=True)
        st.markdown("#### 检测结果图")
        st.image(result["annotated_image"], use_container_width=True)
        st.success(f"识别完成，共检测到 {result['count']} 处缺陷。")
        st.session_state["detect_result"] = result
    elif run_btn and image_bytes is None:
        st.warning("请先上传图像后再执行识别。")

st.markdown("### 识别结果表格")
if "detect_result" in st.session_state:
    st.dataframe(pd.DataFrame(st.session_state["detect_result"]["detections"]), use_container_width=True, hide_index=True)
else:
    st.info("完成识别后将在此显示缺陷类别、置信度与边界框坐标。")

with st.expander("页面说明", expanded=False):
    st.write("本页仅优化展示层，不改变检测业务逻辑；后续可在服务层切换 RT-DETR 真实推理。")
