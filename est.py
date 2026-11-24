def estimate_tokens(text):
    return round(len(text.split()) * 1.3)

sentences = [
    # "rename all pngs",
    # "delete every log file older than a week",
    # "move all screenshots from downloads to the archive folder",
    "cat",
    "renaming",
    "unbelievable",
    "Antigravity",
    "Your own first name"
]

for s in sentences:
    print(s,"->", estimate_tokens(s))
