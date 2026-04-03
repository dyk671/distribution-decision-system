# Project overview
This repository contains a master's thesis demo system for distribution line defect recognition and auxiliary decision-making.

The project is intended for thesis interface demonstration rather than production deployment.
The priority is:
- clear structure
- clean UI
- stable local execution
- screenshot-friendly pages for thesis writing

# Technical stack
- Python
- Streamlit
- Multipage Streamlit app
- Mock data first

Future integration points should be reserved for:
- improved RT-DETR defect detection
- GraphRAG retrieval enhancement
- fine-tuned large language model
- Neo4j knowledge graph database

# Main system modules
The system should include these pages:
1. 首页
2. 巡检图像缺陷识别
3. 缺陷辅助决策
4. 人工问答
5. 知识图谱可视化

# Repository structure expectations
Use the following structure unless the repository already has a better equivalent:

- `app.py` as the main entry point
- `pages/` for Streamlit multipage files
- `mock/` for mock data and mock logic
- `services/` for business logic wrappers
- `models/` for future real model integration
- `assets/` for static resources
- `README.md` for run instructions
- `requirements.txt` for Python dependencies

# Development goals
The current phase is prototype implementation.
Use mock data first to complete the whole interaction flow.

The prototype should demonstrate:
- image upload and defect recognition result display
- defect event display and auxiliary decision result display
- natural language question answering
- graph visualization and node relation browsing
- system overview and navigation

# UI requirements
- Use Chinese for visible UI text
- Keep the interface simple, academic, and clean
- Avoid flashy animations or overly complex visual effects
- Make layouts suitable for direct screenshots in a master's thesis
- Keep page hierarchy clear and readable

# Functional requirements
## 首页
The home page must be a system overview page, not an empty welcome page.
It should include:
- system title
- brief project introduction
- module overview
- concise usage guidance
- summary information or overview cards

## 巡检图像缺陷识别
It should support:
- image upload
- image preview
- mock detection execution
- bounding box visualization
- defect result table display

## 缺陷辅助决策
It should support:
- defect event display
- knowledge path display
- risk level display
- auxiliary decision result display
- copy or export of results if practical

## 人工问答
It should support:
- natural language question input
- example questions
- answer display
- evidence or path display
- simple history display using session state

## 知识图谱可视化
It should support:
- mock graph node-edge visualization
- node search if practical
- node attribute display
- local relation browsing
- basic interaction such as zoom or drag if practical

# Mock-first rule
Do not block implementation waiting for real models.
If a real backend is unavailable, implement the full page flow using mock data.

Mock modules should be easy to replace later with real logic.

# Separation of responsibilities
Pages should not directly hardcode all business logic.
Prefer this layering:
- page files handle UI
- service files handle business calls
- mock files provide temporary outputs
- model files reserve future real interfaces

# Coding preferences
- Keep code simple and readable
- Prefer small functions over large monolithic files
- Avoid unnecessary abstraction
- Use clear file names and clear Chinese page titles
- Add comments only when they improve maintainability
- Do not introduce React, Vue, or other frontend frameworks

# Streamlit preferences
- Prefer standard Streamlit multipage behavior
- Use `st.session_state` when history or cross-page state is needed
- Keep layouts stable and easy to understand
- Avoid fragile hacks unless necessary

# Working style
When starting a task:
1. inspect the current repository structure
2. identify missing files or folders
3. propose a short implementation plan if the task is multi-step
4. implement in small, reviewable steps
5. keep the app runnable throughout development when possible

# Done criteria
A task is considered complete only when:
- the Streamlit app can run locally
- all required pages can be opened
- imports are valid
- the relevant mock workflow works without crashing
- the UI matches the thesis-demo purpose
- README is updated when run steps change

# Validation
Before finishing, verify:
- app startup works
- page navigation works
- uploaded images can be processed by the mock detection flow
- decision page can show mock results
- QA page can show mock answers
- graph page can show mock graph data
- no obvious import or path errors remain

# README expectations
The README should stay concise and include:
- project purpose
- environment setup
- install command
- run command
- brief description of each page
- note that the current version uses mock data first

# Future integration note
Preserve clear replacement points for:
- RT-DETR inference
- GraphRAG retrieval
- LLM inference
- Neo4j querying

Do not tightly couple mock logic to page rendering in ways that make later replacement difficult.
