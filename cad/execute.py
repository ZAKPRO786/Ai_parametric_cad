import cadquery as cq

def execute_cadquery(code):

    local_vars = {}

    exec(
        code,
        {"cq": cq},
        local_vars
    )

    return local_vars["result"]