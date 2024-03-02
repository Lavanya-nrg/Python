def result(score):
    return f"The student {'passed' if score >=70 else 'failed'}"

result(85) # 'The student passed'
result(60) # 'The student failed'
