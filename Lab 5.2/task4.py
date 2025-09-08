def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on education, experience, gender, and age.
    Returns a numeric score.
    """

    score = 0

    # Education scoring
    # Higher education gets more points
    if education.lower() == "phd":
        score += 30
    elif education.lower() == "masters":
        score += 25
    elif education.lower() == "bachelors":
        score += 20
    elif education.lower() == "highschool":
        score += 10
    else:
        score += 5  # For other or unknown education

    # Experience scoring
    # 2 points per year of experience, capped at 20 years
    exp_points = min(experience, 20) * 2
    score += exp_points

    # Gender scoring
    # No points added or subtracted for gender (should be neutral)
    # Uncommenting the following would be unfair:
    # if gender.lower() == "male":
    #     score += 5
    # elif gender.lower() == "female":
    #     score += 5

    # Age scoring
    # Prefer working-age adults (e.g., 22-60), but don't penalize harshly
    if 22 <= age <= 60:
        score += 10
    elif 18 <= age < 22 or 61 <= age <= 70:
        score += 5
    else:
        score += 0  # No extra points for very young or old

    return score

# Example usage:
applicants = [
    {"education": "PhD", "experience": 10, "gender": "female", "age": 35},
    {"education": "Bachelors", "experience": 5, "gender": "male", "age": 25},
    {"education": "HighSchool", "experience": 2, "gender": "nonbinary", "age": 19},
    {"education": "Masters", "experience": 25, "gender": "female", "age": 62},
]

for idx, applicant in enumerate(applicants, 1):
    score = score_applicant(
        applicant["education"],
        applicant["experience"],
        applicant["gender"],
        applicant["age"]
    )
    print(f"Applicant {idx}: Score = {score}")

# Analysis of Bias or Unfairness:
#
# - Education: Favors higher degrees, which may disadvantage those without access to advanced education.
# - Experience: Linear up to 20 years, which is reasonable, but may disadvantage younger applicants.
# - Gender: Neutral in this logic (no points added or subtracted).
# - Age: Favors typical working ages, but does not harshly penalize others.
#
# Overall, the logic is mostly fair except for the education component, which could be biased against those from less privileged backgrounds.
# To improve fairness, consider weighting experience and skills more than formal education, and ensure no points are given or subtracted for gender or age unless job-relevant