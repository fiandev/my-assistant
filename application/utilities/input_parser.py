import re
from application.constants.rules import rules
from application.constants.conjunctions import temporal_conjuction
from application.helpers.string import str_to_list

"""
example output:
[
    {
        'prompt': str,
        'action_name': str,
        'objective': str,
    },
]
"""
def input_parser (input: str, lang: str = "id") -> list:
    temporal_conjuctions = str_to_list(temporal_conjuction[lang])
    
    for conjunction in temporal_conjuctions:
        input = input.replace(conjunction, "|")
    
    """
    iteration prompts to get the context of user input
    """
    prompts: list = str_to_list(input, separator="|")
    actions: list = []
    
    for prompt in prompts:
        for action_name in rules[lang]:
            action = rules[lang][action_name]
            match = re.match(action["expression"], prompt)
            if match:
                actions.append({
                    "prompt": prompt,
                    "action_name": action_name,
                    "objective": match.group(action["objective"]),
                })
    
    return actions