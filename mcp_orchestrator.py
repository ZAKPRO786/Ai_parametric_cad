from agents.planner_agent import plan
from agents.validation_agent import validate
from agents.cad_agent import build
from agents.geometry_agent import analyze

from llm.parser import parse_prompt


def run(prompt):

    route = plan(prompt)

    params = parse_prompt(
        prompt
    )

    validate(params)

    model = build(params)

    report = analyze(model)

    return (
        model,
        params,
        report
    )