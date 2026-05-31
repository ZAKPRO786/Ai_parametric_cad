import json
import requests


def parse_prompt(prompt: str):

    system_prompt = f"""
You are a CAD parameter extraction assistant.

Known shapes:

- box
- cylinder
- spacer
- pipe
- plate
- bracket
- gear
- cone
- mounting_plate
For known shapes return JSON parameters.

Examples:

{{
    "shape":"box",
    "length":100,
    "width":50,
    "height":20
}}

{{
    "shape":"cylinder",
    "radius":25,
    "height":100
}}

{{
    "shape":"spacer",
    "outer_radius":20,
    "inner_radius":10,
    "height":15
}}

{{
    "shape":"pipe",
    "outer_radius":20,
    "inner_radius":15,
    "height":100
}}

{{
    "shape":"plate",
    "length":100,
    "width":50,
    "thickness":5
}}

{{
    "shape":"bracket",
    "length":100,
    "width":50,
    "height":75,
    "thickness":5
}}

{{
    "shape":"gear",
    "teeth":24,
    "module":2,
    "thickness":10,
    "bore_radius":4
}}
{{
    "shape":"cone",
    "radius":50,
    "height":100
}}
{{
    "shape":"mounting_plate",
    "length":80,
    "width":40,
    "thickness":8,
    "hole_diameter":5
}}
For unknown mechanical parts return:

{{
    "shape":"custom",
    "part_name":"pulley",
    "cadquery_code":"result = cq.Workplane('XY').box(100,50,20)"
}}

Rules:
- Return ONLY JSON
- No markdown
- No explanations
- No code blocks
- For custom parts include:
  - shape
  - part_name
  - cadquery_code
If the user asks for:
- base plate with holes
- mounting plate
- plate with four corner holes
Valid CadQuery operations:

box()
circle()
rect()
extrude()
revolve()
loft()
sweep()
cut()
union()
intersect()
hole()
cutBlind()
fillet()
chamfer()
faces()
workplane()
pushPoints()

Never use:

cutAll()
cutCircle()
gear()
cone()
pulley()
flange()
bearing()
Return shape = "mounting_plate"

User request:

{prompt}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": system_prompt,
            "stream": False
        }
    )

    text = response.json()["response"].strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    result = json.loads(text)

    if isinstance(result, list):
        result = result[0]

    if (
        isinstance(result, dict)
        and "dimensions" in result
    ):
        result.update(
            result["dimensions"]
        )
        del result["dimensions"]

    if (
        result.get("shape") == "custom"
        and "part_name" not in result
    ):
        result["part_name"] = "custom_part"

    return result