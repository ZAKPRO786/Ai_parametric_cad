# AI Parametric CAD Generator

> Natural Language to Parametric CAD using Qwen 2.5, CadQuery, OpenCascade, and MCP-Inspired Multi-Agent Architecture.

## Overview

AI Parametric CAD Generator is an offline AI-powered engineering design system that converts natural language descriptions into manufacturable CAD models.

The system combines Large Language Models (LLMs), multi-agent orchestration, and parametric CAD generation to automate engineering workflows. Users can describe engineering components using plain English, and the system automatically generates valid CAD geometry with STEP and STL export support.

### Key Features

* Natural Language to CAD Generation
* Fully Offline Execution
* MCP-Inspired Multi-Agent Architecture
* Parametric CAD Modeling
* STEP Export Support
* STL Export Support
* Interactive 3D Visualization
* Geometry Validation
* Extensible Component Library

---

# System Architecture

<p align="center">
  <img src="assets/sysarch.png" width="900">
</p>

The architecture separates planning, validation, CAD generation, and geometry verification into specialized agents.

```text
User
 ↓
Streamlit UI
 ↓
MCP Orchestrator
 ↓
Planner Agent
 ↓
Validation Agent
 ↓
CAD Agent
 ↓
Geometry Agent
 ↓
CadQuery / OpenCascade
 ↓
STEP / STL Export
```

---

# CAD Generation Pipeline

<p align="center">
  <img src="assets/flow.png" width="900">
</p>

```text
Natural Language Prompt
          ↓
Qwen 2.5
          ↓
Structured JSON
          ↓
Validation Agent
          ↓
CAD Planning
          ↓
Feature Engine
          ↓
CadQuery Modeling
          ↓
Geometry Validation
          ↓
STEP / STL Export
```

---

# Technology Stack

| Layer                | Technology  |
| -------------------- | ----------- |
| AI Model             | Qwen 2.5    |
| Runtime              | Ollama      |
| UI Framework         | Streamlit   |
| CAD Framework        | CadQuery    |
| Geometry Kernel      | OpenCascade |
| Visualization        | Plotly      |
| Export Formats       | STEP, STL   |
| Programming Language | Python 3.11 |

---

# Supported Components

## Basic Components

* Box
* Cylinder
* Pipe
* Spacer
* Plate

## Intermediate Components

* Flange
* Shaft
* Pulley
* Mounting Plate

## Advanced Components

* Enclosure
* L-Bracket
* Clevis Bracket
* Globe Valve
* Tyre Mould

## Experimental Components

* Planetary Gear
* Engine Cylinder
* Impeller
* Spiral Staircase

---

# CAD Operations

| Category           | Operations                                       |
| ------------------ | ------------------------------------------------ |
| Primitives         | Box, Cylinder, Sphere, Cone                      |
| Boolean Operations | Union, Cut, Intersect, Fuse                      |
| Feature Operations | Fillet, Chamfer, Hole, Bolt Circle, Hole Pattern |
| Transformations    | Translate, Rotate, Mirror, Polar Array           |

---

# Generated Outputs

## Globe Valve

<p align="center">
  <img src="assets/cl.png" width="650">
</p>

Industrial globe valve generated using feature-based parametric modeling and solid fusion operations.

---

## Tyre Mould

<p align="center">
  <img src="assets/wheel.png" width="650">
</p>

Industrial tyre mould with tread lug pattern generation, bolt-hole arrays, and manufacturing-oriented geometry.

---

## Flange

<p align="center">
  <img src="assets/flang.png" width="650">
</p>

Parametric flange with automated bolt circle and hole pattern generation.

---

# Validation Results

| Test Case   | Solid Count | STEP Export | STL Export | Status |
| ----------- | ----------- | ----------- | ---------- | ------ |
| Box         | 1           | PASS        | PASS       | PASS   |
| Flange      | 1           | PASS        | PASS       | PASS   |
| Globe Valve | 1           | PASS        | PASS       | PASS   |
| Tyre Mould  | 1           | PASS        | PASS       | PASS   |

Target Validation:

```text
Solid Count = 1
```

---

# User Interface

<p align="center">
  <img src="assets/u1.png" width="900">
</p>
<p align="center">
  <img src="assets/u2.png" width="900">
</p>
<p align="center">
  <img src="assets/u3.png" width="900">
</p>

Streamlit-based interface for Natural Language to CAD generation and interactive visualization.

---
## Project Structure

The project follows a modular architecture that separates AI processing, CAD generation, validation, geometry analysis, and export operations.

```text
AI_PARAMETRIC_CAD/
│
├── app.py                      # Streamlit application entry point
├── mcp_orchestrator.py         # Multi-agent orchestration layer
├── requirements.txt
├── README.md
│
├── agents/
│   ├── planner_agent.py        # Intent analysis and routing
│   ├── validation_agent.py     # Schema and parameter validation
│   ├── cad_agent.py            # CAD planning and generation
│   └── geometry_agent.py       # Geometry verification
│
├── parser/
│   ├── extractor.py            # Parameter extraction
│   └── rules.py                # Engineering rules
│
├── llm/
│   ├── parser.py               # Qwen integration layer
│   └── __init__.py
│
├── models/
│   └── schemas.py              # Component schemas
│
├── cad/
│   ├── primitives.py           # Primitive geometry creation
│   ├── features.py             # Fillets, chamfers, holes, patterns
│   ├── generator.py            # CAD generation engine
│   ├── exporter.py             # STEP/STL export utilities
│   ├── execute.py              # CAD execution pipeline
│   └── custom_executor.py      # Dynamic CAD execution
│
├── utils/
│   └── viewer.py               # Visualization utilities
│
├── assets/
│   ├── sysarch.png             # System architecture diagram
│   ├── flow.png                # Data flow diagram
│   ├── flang.png               # Flange output
│   ├── wheel.png               # Tyre mould output
│   ├── cl.png                  # Globe valve output
│   └── ...
│
├── outputs/
│   ├── *.step                  # Generated STEP files
│   └── *.stl                   # Generated STL files
│
├── history/
│   └── history.json            # Prompt history
│
└── models_llm/
    └── qwen2.5-3B-SFT/         # Local Qwen model files
```

### Directory Responsibilities

| Directory | Purpose |
|------------|----------|
| agents | Multi-agent workflow for planning, validation, CAD generation, and geometry verification |
| parser | Extracts engineering parameters from natural language prompts |
| llm | Handles interaction with the Qwen model |
| models | Defines structured schemas used throughout the pipeline |
| cad | Core CAD generation, feature creation, and export operations |
| utils | Visualization and helper utilities |
| assets | Architecture diagrams, workflow diagrams, and generated outputs |
| outputs | Generated STEP and STL files |
| history | Stores prompt history and generation records |
| models_llm | Local AI model storage |

---

## Architecture Overview

```text
User Prompt
     │
     ▼
Streamlit UI
     │
     ▼
MCP Orchestrator
     │
 ┌───┼───────────────┐
 ▼   ▼               ▼
Planner Validation  CAD Agent
 Agent    Agent
     │
     ▼
Feature Engine
     │
     ▼
CadQuery + OpenCascade
     │
     ▼
Geometry Agent
     │
     ▼
STEP / STL Export
```

This modular architecture enables scalable Natural Language to CAD generation while maintaining separation of concerns between AI reasoning, validation, geometry creation, and export workflows.
# Installation

## Clone Repository

```bash
git clone https://github.com/ZAKPRO786/Ai_parametric_cad.git
cd ai_parametric_cad
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama:

https://ollama.com

Pull Qwen:

```bash
ollama pull qwen2.5:3b
```

Verify:

```bash
ollama list
```

---

# Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# Example Prompts

```text
Create a flange with six bolt holes.

Create a stepped shaft with a keyway.

Create a globe valve with a handwheel.

Create an industrial tyre mould with tread lugs.

Create a centered 100 x 60 x 20 mm block with four 8 mm vertical through-holes. Add only a 2 mm chamfer on the top outer perimeter
```

---

# Current Limitations

* Single-part generation only
* No assembly constraints
* No FEA integration
* No topology optimization
* No Image-to-CAD support
* Limited engineering reasoning

---

# Future Roadmap

* Model Context Protocol (MCP)
* LangGraph Integration
* CrewAI Integration
* Image-to-CAD Generation
* Retrieval-Augmented CAD (RAG-CAD)
* Assembly Generation
* FEA Integration
* Autonomous CAD Agents
* Generative Engineering Design

---

# Project Outcomes

* Natural Language to CAD Workflow
* Fully Offline AI Inference
* Parametric CAD Generation
* STEP/STL Export Support
* Industrial Component Generation
* Multi-Agent CAD Architecture

---

# Author

**Muhammed Zachariya**

B.Tech Computer Science and Engineering

AI Parametric CAD Generator – Natural Language to Parametric CAD using Qwen, CadQuery, and OpenCascade.
