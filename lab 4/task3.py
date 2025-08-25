def extract_student_info(student_dict):
    student = student_dict.get('student', {})
    name = student.get('name', {})
    details = student.get('details', {})
    full_name = f"{name.get('first', '')} {name.get('last', '')}".strip()
    branch = details.get('branch', '')
    sgpa = details.get('sgpa', None)
    return {
        'Full Name': full_name,
        'Branch': branch,
        'SGPA': sgpa
    }