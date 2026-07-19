def is_simple_question(question):

    question = question.lower()

    keywords = [
        "how many",
        "count",
        "average",
        "mean",
        "max",
        "maximum",
        "min",
        "minimum",
        "highest",
        "lowest",
        "sum",
        "missing",
        "duplicate",
        "rows",
        "columns",
        "unique"
    ]

    return any(word in question for word in keywords)