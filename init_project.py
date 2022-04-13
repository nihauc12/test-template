import re
from typing import Optional, Dict


def ask(question: str, pattern: Optional[str] = None, pattern_hint: Optional[str] = None) -> str:
    regex = re.compile(pattern) if pattern is not None else None
    while True:
        answer = input(question)
        if pattern is None:
            return answer
        regex_match = regex.match(answer)
        if bool(regex_match) is True:
            return answer
        if pattern_hint is not None:
            print(pattern_hint)


def replace_in_file(file_path: str, replacement_dict: Dict[str, str]):
    # Read in the file
    with open(file_path, "r") as file:
        data = file.read()

    # Replace the target string
    for k, v in replacement_dict.items():
        data = data.replace(k, v)

    # Write the file out again
    with open(file_path, "w") as file:
        file.write(data)


project_name = ask("What is your project name ?", "^[a-z-]{3,}$", "minimum 3 letters")
author = ask("What is the author name ?")
python_version = ask(
    "What python version will you use ?",
    "^([2-3])(\.([0-9]{1,2})+)?(.([0-9]{1,2})+)?$",
    "Valid version examples: '3', '3.1', '3.8.12'",
)

replace_in_file(
    "./pyproject.toml",
    {
        "{{REPO_NAME}}": project_name,
        "{{PYTHON_VERSION}}": python_version,
        "{{AUTHOR_NAME}}": author if author is not None else "c12dev",
    },
)

replace_in_file(
    "./.github/workflows/ci.yml",
    {
        "{{PYTHON_VERSION}}": python_version,
    },
)
