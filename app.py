import os
import json

from datetime import datetime
from mcp_orchestrator import run

import streamlit as st
import cadquery as cq

from llm.parser import parse_prompt
from cad.generator import generate_model
from utils.viewer import cadquery_to_plotly


st.set_page_config(
    page_title="AI Parametric CAD",
    layout="wide"
)

st.title("AI Parametric CAD Generator")

prompt = st.text_area(
    "Describe the model",
    placeholder="Create a box 100 mm long, 50 mm wide and 20 mm high"
)

if st.button("Generate Model"):

    if not prompt.strip():

        st.warning(
            "Please enter a CAD description."
        )

        st.stop()

    try:

        # Prompt -> JSON
        #params = parse_prompt(prompt)
        model, params, report = run(
            prompt
        )
        st.subheader(
            "Extracted Parameters"
        )

        st.json(params)

        st.write(
            f"Detected Shape: {params['shape']}"
        )

        features = params.get(
            "features",
            []
        )

        if features:

            st.subheader(
                "Detected Features"
            )

            st.json(features)

        # Generate CAD model
        #model = generate_model(params)

        # 3D Preview
        st.subheader(
            "3D Preview"
        )

        fig = cadquery_to_plotly(model)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Create folders
        os.makedirs(
            "outputs",
            exist_ok=True
        )

        os.makedirs(
            "history",
            exist_ok=True
        )

        filename = params["shape"]

        stl_path = (
            f"outputs/{filename}.stl"
        )

        step_path = (
            f"outputs/{filename}.step"
        )

        # Export STL
        cq.exporters.export(
            model,
            stl_path
        )

        # Export STEP
        cq.exporters.export(
            model,
            step_path
        )

        # Save generation history
        history_file = (
            "history/history.json"
        )

        record = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "parameters": params,
            "stl_file": stl_path,
            "step_file": step_path
        }

        if os.path.exists(
            history_file
        ):

            try:

                with open(
                    history_file,
                    "r"
                ) as f:

                    history = json.load(f)

            except Exception:

                history = []

        else:

            history = []

        history.append(record)

        with open(
            history_file,
            "w"
        ) as f:

            json.dump(
                history,
                f,
                indent=4
            )

        st.success(
            "Model generated successfully!"
        )

        col1, col2 = st.columns(2)

        with col1:

            with open(
                stl_path,
                "rb"
            ) as f:

                st.download_button(
                    label="Download STL",
                    data=f,
                    file_name=f"{filename}.stl",
                    mime="application/octet-stream"
                )

        with col2:

            with open(
                step_path,
                "rb"
            ) as f:

                st.download_button(
                    label="Download STEP",
                    data=f,
                    file_name=f"{filename}.step",
                    mime="application/octet-stream"
                )

    except Exception as e:

        st.error(
            f"Generation failed: {str(e)}"
        )

        if "params" in locals():

            st.subheader(
                "Last Parsed Parameters"
            )

            st.json(params)
            st.write(
                "Solid Count:",
                report["solid_count"]
            )