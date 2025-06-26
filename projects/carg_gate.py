def reasoning_gate(complexity, energy, intent):
    """
    Determines reasoning level and rationale based on complexity, energy, and intent.
    Returns:
    - str: Mode label
    - str: Path explanation
    - int: Simulated carbon cost
    """

    if energy < 0.3 and complexity > 0.7 and intent == "Critical":
        return (
            "R2 (Throttled: Deep logic blocked)",
            "High task complexity and critical intent detected, but low energy availability prevented step-by-step reasoning.",
            3,
        )

    if complexity < 0.3 and intent == "Casual":
        return (
            "R1 (Fast heuristic)",
            "Simple task and casual context — using efficient, minimal logic.",
            1,
        )

    if energy > 0.5 and complexity > 0.5:
        return (
            "R3 (Full deduction)",
            "Ample energy and a complex task justify deeper, step-by-step reasoning.",
            6,
        )

    return (
        "R2 (Moderate reasoning)",
        "Intermediate conditions triggered moderate reasoning depth.",
        3,
    )
