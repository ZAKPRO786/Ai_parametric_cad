def analyze(model):

    solids = len(
        model.val().Solids()
    )

    return {
        "solid_count": solids
    }