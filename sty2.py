student = {"name": "Ada", "scores": [88, 92, 79]}


print(student['name'])

#  docstrings are the triple-quoted strings sitting right under the def line, before any actual code runs.

def add_student(name: str, scores: list[int]) -> dict:
    """create  a student record as a dictionary"""

    return {"name": name, "scores":scores}



def calculate_average(scores: list[int]) -> float:
    if not scores:
        return {"Average": None}
    else:
        return sum(scores)/len(scores)
    
def print_report(student:dict) -> None:

    avg =  calculate_average(student["scores"])
    print(f"Name: {student['name']}")
    print(f"Scores: {student['scores']}")
    print(f"Average: {avg:.2f}")

j = add_student("jacob", [1, 2, 3, 4,5])
print_report(j)


# home work

def remove_student(students: list[dict], name: str) -> list[str]:
    return [student for student in students if student['name'] != name]

def search_by_name(students: list[dict], name: str) -> dict | None:
    for student in students:
        if student["name"] == name:
            return student
    return None