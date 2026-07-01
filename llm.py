from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def generate_response(query, recommendations):
    """
    Generates an AI explanation for the retrieved SHL assessments.
    """

    assessment_text = ""

    for i, assessment in enumerate(recommendations, start=1):

        assessment_text += f"""
Assessment {i}

Name:
{assessment.get("name")}

Description:
{assessment.get("description")}

Job Levels:
{", ".join(assessment.get("job_levels", []))}

Duration:
{assessment.get("duration")}

Remote Testing:
{assessment.get("remote")}

URL:
{assessment.get("link")}

---------------------------------------
"""

    system_prompt = """
You are an expert SHL Assessment Recommendation Assistant.

Your responsibilities:

- Recommend ONLY from the provided assessments.
- Never invent assessment names.
- Explain why each assessment matches the hiring requirement.
- Mention important competencies or skills evaluated.
- Keep the response concise, professional, and easy to understand.
"""

    user_prompt = f"""
Recruiter Requirement:

{query}

Retrieved SHL Assessments:

{assessment_text}

Recommend the best assessments and explain why they are suitable.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3,
        max_tokens=700
    )

    return response.choices[0].message.content