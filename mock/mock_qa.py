EXAMPLE_QA = {
    "绝缘子污闪有哪些常见诱因？": {
        "answer": "常见诱因包括长期污秽沉积、雨雾天气导致表面受潮、盐雾或工业粉尘环境，以及绝缘老化。",
        "evidence": "图谱路径：绝缘子污闪 -> 污秽沉积 -> 绝缘下降 -> 闪络风险",
    },
    "导线断股应如何制定处理优先级？": {
        "answer": "建议综合断股比例、所在区段负荷等级、近期气象风险和历史告警频次进行分级处置。",
        "evidence": "图谱路径：导线断股 -> 机械强度下降 -> 断线风险 -> 负荷影响评估",
    },
    "发现高风险缺陷后第一步做什么？": {
        "answer": "第一步应完成现场复核与风险隔离确认，再结合运行方式制定检修窗口。",
        "evidence": "图谱路径：高风险缺陷 -> 现场复核 -> 风险隔离 -> 检修决策",
    },
}


def mock_answer(question: str) -> dict:
    clean_q = question.strip()
    if clean_q in EXAMPLE_QA:
        result = EXAMPLE_QA[clean_q]
        return {"answer": result["answer"], "evidence": result["evidence"], "source": "mock_exact"}

    return {
        "answer": "当前为演示版问答系统。根据已知规则，建议先明确缺陷类型、风险等级和关联部件，再生成处置方案。",
        "evidence": "图谱路径：缺陷实体 -> 风险评估节点 -> 处置策略节点",
        "source": "mock_fallback",
    }
