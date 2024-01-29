
"""
key: name action
value: {
    expression: regex exp for string selection
    objective: objective of a command
}
"""
rules: dict = {
    "id": {
        "open.application": {
            "expression": r"^((tolong)?\s?(buka|jalankan)|)\s?(aplikasi|app|program)?\s(\w+)",
            "objective": 5, # application name
        },
        "sent.whatsapp.contact": {
            "expression": r"^((kirim|whatsapp)?\s?((w(hats)?a(app)?|pesan)?|chat|japri))\s(w(hats)?a(pp)?)?\s?(ke)?\s?(\w+)",
            "objective": 11, # contact name
        }
    }
}