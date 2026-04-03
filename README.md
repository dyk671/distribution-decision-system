# 配电线路缺陷识别与辅助决策系统（论文演示原型）

## 项目目的
本项目用于硕士论文界面展示，采用 **Python + Streamlit** 构建多页面原型系统。
当前版本以 **Mock 数据优先**，用于演示完整交互流程，而非生产部署。

## 功能页面
1. **首页**：系统总览、模块说明与关键统计。
2. **巡检图像缺陷识别**：上传图像、Mock 识别、检测框展示、结果表格。
3. **缺陷辅助决策**：缺陷事件、知识路径、风险提示、处置建议、结果导出。
4. **人工问答**：自然语言提问、示例问题、证据路径、会话历史。
5. **知识图谱可视化**：实体关系图、节点搜索、属性查看、局部关系浏览。

## 环境准备
- Python 3.10+
- 建议使用虚拟环境

## 安装依赖
```bash
pip install -r requirements.txt
```

## 启动方式
```bash
streamlit run app.py
```

启动后在浏览器中打开命令行提示的本地地址（默认一般为 `http://localhost:8501`）。

## 目录结构
```text
.
├─ app.py
├─ pages/
├─ mock/
├─ services/
├─ models/
├─ assets/
├─ README.md
└─ requirements.txt
```

## 后续真实能力接入位置
- RT-DETR 缺陷识别：`models/rtdetr_infer.py`
- GraphRAG 辅助决策：`models/graphrag_infer.py`
- 大语言模型问答：`models/llm_infer.py`
- Neo4j 图谱查询：`models/neo4j_query.py`

服务层已统一封装调用入口（`services/`），后续可在不改页面交互的情况下替换 Mock 逻辑。
