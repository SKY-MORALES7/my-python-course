def student_scores(scores:list[int]) -> dict:
    if not scores:
        return {"Min": None , "Max": None, "Average": "None"}
    else:
        return{
            "Min": min(scores),
            "Max": max(scores),
            "Average": sum(scores)/len(scores)
        }
    
print(student_scores([80, 95, 70, 60, 100])) 
# print(student_scores()) 