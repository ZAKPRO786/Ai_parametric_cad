import json
import requests


def parse_prompt(prompt: str):
    prompt_lower = prompt.lower()

    # -------------------------
    # Aerospace Clevis
    # -------------------------

    if (
            "aerospace" in prompt_lower
            or "lightening cutout" in prompt_lower
            or "reinforcing rib" in prompt_lower
    ):
        return {
            "shape": "advanced_clevis_bracket",
            "features": []
        }

    # -------------------------
    # Basic Clevis
    # -------------------------

    if (
            "clevis" in prompt_lower
            or "fork bracket" in prompt_lower
            or "double lug" in prompt_lower
    ):
        return {
            "shape": "clevis_bracket",
            "features": []
        }

    # -------------------------
    # L Bracket
    # -------------------------

    if (
            "l bracket" in prompt_lower
            or "right angle bracket" in prompt_lower
            or "gusseted bracket" in prompt_lower
    ):
        return {
            "shape": "bracket",
            "length": 100,
            "width": 50,
            "height": 75,
            "thickness": 5,
            "features": []
        }
    if (
            "globe valve" in prompt_lower
            or "stainless steel valve" in prompt_lower
            or "threaded valve" in prompt_lower
    ):
        return {
            "shape": "globe_valve",
            "features": []
        }
    # -------------------------
    # Engine Cylinder
    # -------------------------

    if (
            "radial engine" in prompt_lower
            or "engine cylinder" in prompt_lower
            or "cooling fins" in prompt_lower
    ):
        return {
            "shape": "engine_cylinder",
            "features": []
        }

    # -------------------------
    # Planetary Gear
    # -------------------------

    if (
            "planetary gear stage" in prompt_lower
            or "planetary gear" in prompt_lower
    ):
        return {
            "shape": "planetary_gear",
            "features": []
        }

    # -------------------------
    # Spiral Staircase
    # -------------------------

    if (
            "spiral staircase" in prompt_lower
            or "helical handrail" in prompt_lower
    ):
        return {
            "shape": "spiral_staircase",
            "features": []
        }

    # -------------------------
    # Impeller
    # -------------------------

    if (
            "impeller" in prompt_lower
            or "backward curved blades" in prompt_lower
    ):
        return {
            "shape": "impeller",
            "features": []
        }
    if (
            "tyre mould" in prompt_lower
            or "tire mould" in prompt_lower
            or "tire mold" in prompt_lower
    ):
        return {
            "shape": "tyre_mould",
            "features": []
        }
    system_prompt = f"""
    You are a CAD parameter extraction assistant.

    Return ONLY valid JSON.

    Supported Shapes:

    - box
    - cylinder
    - spacer
    - pipe
    - plate
    - bracket
    - gear
    - cone
    - mounting_plate
    - flange
    - shaft
    - stepped_shaft
    - housing
    - enclosure
    - clevis_bracket
    - pulley
    - advanced_clevis_bracket
    - engine_cylinder
    - planetary_gear
    - spiral_staircase
    - impeller
    - globe_valve
    - tyre_mould
    Supported Features:

    - hole_pattern
    - bolt_circle
    - chamfer
    - fillet
    - shell
    - blind_hole
    - keyway
    - slot
    - standoff
    - gusset
    - rib

    Examples:

    {{
        "shape":"box",
        "length":100,
        "width":60,
        "height":20,
        "features":[
            {{
                "type":"hole_pattern",
                "count":4,
                "diameter":8
            }},
            {{
                "type":"chamfer",
                "size":2
            }}
        ]
    }}
   {{
    "shape":"bracket",
    "length":100,
    "width":50,
    "height":75,
    "thickness":5,
    "features":[
        {{
            "type":"hole_pattern",
            "count":4,
            "diameter":8
        }},
        {{
            "type":"gusset"
        }}
    ]
}}
    {{
    "shape":"tyre_mould",
    "features":[]
}}
    {{
        "shape":"flange",
        "outer_diameter":80,
        "thickness":10,
        "bore_diameter":30,
        "features":[
            {{
                "type":"bolt_circle",
                "count":6,
                "diameter":6,
                "pitch_circle":60
            }},
            {{
                "type":"fillet",
                "radius":2
            }}
        ]
    }}
  {{
    "shape":"globe_valve",
    "features":[]
}}

    {{
        "shape":"enclosure",
        "features":[
            {{
                "type":"shell",
                "thickness":3
            }},
            {{
                "type":"standoff"
            }}
        ]
    }}

    {{
        "shape":"stepped_shaft",
        "features":[
            {{
                "type":"keyway",
                "width":6,
                "depth":3
            }},
            {{
                "type":"chamfer",
                "size":1
            }}
        ]
    }}

    {{
        "shape":"clevis_bracket",
        "features":[
            {{
                "type":"rib"
            }},
            {{
                "type":"gusset"
            }},
            {{
                "type":"fillet",
                "radius":3
            }}
        ]
    }}
{{
    "shape":"advanced_clevis_bracket",
    "features":[
        {{
            "type":"rib"
        }},
        {{
            "type":"gusset"
        }},
        {{
            "type":"fillet",
            "radius":3
        }}
    ]
}}
{{
    "shape":"engine_cylinder",
    "features":[
        {{
            "type":"fillet",
            "radius":2
        }}
    ]
}}
{{
    "shape":"planetary_gear",
    "features":[]
}}
{{
    "shape":"spiral_staircase",
    "features":[]
}}
{{
    "shape":"impeller",
    "features":[]
}}
    IMPORTANT:

    For a box use:

    {{
        "shape":"box",
        "length":100,
        "width":60,
        "height":20
    }}

    Never use:

    {{
        "shape":"box",
        "size":[100,60,20]
    }}

    For features use:

    {{
        "type":"hole_pattern"
    }}

    Never use:

    {{
        "feature":"hole_pattern"
    }}
IMPORTANT SHAPE DISTINCTIONS

L bracket
→ bracket

Mounting bracket
→ bracket

Right angle bracket
→ bracket

Clevis bracket
→ clevis_bracket

Fork bracket
→ clevis_bracket

Double lug bracket
→ clevis_bracket

Aerospace clevis bracket
→ advanced_clevis_bracket

Bracket with lightening cutouts
→ advanced_clevis_bracket

Bracket with reinforcing ribs
→ advanced_clevis_bracket
tyre mould -> tyre_mould
tire mould -> tyre_mould
tire mold -> tyre_mould
    Rules:

    - Return ONLY JSON
    - No markdown
    - No code blocks
    - No explanations
    - Never generate CadQuery code
    - Never return custom
    - Use exact field names from examples
    Mapping Rules:

L bracket
→ bracket

right angle bracket
→ bracket

gusseted bracket
→ bracket

clevis bracket
→ clevis_bracket

fork bracket
→ clevis_bracket

double lug bracket
→ clevis_bracket

aerospace clevis bracket
→ advanced_clevis_bracket

lightening cutouts
→ advanced_clevis_bracket

reinforcing ribs
→ advanced_clevis_bracket

engine cylinder
→ engine_cylinder

cooling fins
→ engine_cylinder

planetary gear
→ planetary_gear

sun gear
→ planetary_gear

ring gear
→ planetary_gear

spiral staircase
→ spiral_staircase

helical handrail
→ spiral_staircase

impeller
→ impeller

backward curved blades
→ impeller

    User Request:

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
        text = (
            text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    if text.startswith("```"):
        text = (
            text.replace("```", "")
            .strip()
        )

    start = text.find("{")
    end = text.rfind("}") + 1

    if start != -1 and end != -1:
        text = text[start:end]

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
        isinstance(result, dict)
        and "features" not in result
    ):
        result["features"] = []
    # Convert size array to dimensions

    if (
            result.get("shape") == "box"
            and "size" in result
    ):

        size = result["size"]

        if len(size) >= 3:
            result["length"] = size[0]
            result["width"] = size[1]
            result["height"] = size[2]

    # Convert feature -> type

    if "features" in result:

        for feature in result["features"]:

            if (
                    "feature" in feature
                    and "type" not in feature
            ):
                feature["type"] = feature["feature"]

    # Convert hole_size -> diameter

    if "features" in result:

        for feature in result["features"]:

            if (
                    feature.get("type")
                    == "hole_pattern"
            ):

                if "hole_size" in feature:
                    feature["diameter"] = (
                        feature["hole_size"]
                    )

    # Convert chamfer format

    if "features" in result:

        for feature in result["features"]:

            if (
                    feature.get("type")
                    == "chamfer"
            ):

                if "length" in feature:
                    feature["size"] = (
                        feature["length"]
                    )

    return result