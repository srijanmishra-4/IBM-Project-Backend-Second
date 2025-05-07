from utils.gemini import call_gemini_api
import json
import re

async def evaluate_test(result: list, job_title: str  , expirience : str , skill : list):


    try:
        prompt = f"""
        Evaluate the following result dataset based on the given job title. The dataset contains multiple-choice, skill-based questions along with the user's responses. Each record includes:

    
        - Question (for the given skill)
        - Options
        - Correct Answer
        - User’s Answer
        - Difficulty


        Your task is to analyze the user's performance and provide a structured evaluation in the following format:

        ### 1. Skill-wise Performance & Evaluation:
        - Assess the user’s performance for each skill.
        - Provide insights into strengths and weaknesses based on the correctness of answers and difficulty levels.

        ### 2. Overall Performance (One Sentence Summary):
        - Summarize the user's overall competency in a single sentence.

        ### 3. Areas of Improvement:
        - Identify key areas where the user needs improvement.
        - Be specific rather than generic, focusing on recurring mistakes or struggles in particular skills/difficulty levels.

        ### 4. Personalized Learning Path:
        - Provide a concise bullet-pointed learning path instead of a step-by-step guide.
        - Each bullet point should be brief yet informative, highlighting targeted learning areas.
        - Keep it clear and actionable, avoiding excessive detail while ensuring it remains useful.
        - Ensure the learning plan is personalized and not generic, aligning with the user's performance gaps.

        ### Important:
        - The evaluation must align with the given job title ('{job_title}') and its expected skill set.
        - Avoid generic feedback—make the insights job-relevant and performance-driven.

        #### User's Test Result Data:
        {result}

        #### User's Expirience:
        {expirience}

        #### User's Skills:
        {skill}

        #### JSON Response Format:
        {{
            "Skill-wise Performance": {{
                "Skill 1": "Evaluation for Skill 1",
                "Skill 2": "Evaluation for Skill 2"
            }},
            "Overall Performance Summary": "Summarized competency level",
            "Areas of Improvement": [
                "Specific improvement point 1",
                "Specific improvement point 2"
            ],
            "Personalized Learning Path": [
                "Targeted learning area 1",
                "Targeted learning area 2"
            ]
        }}
        """


        response = await call_gemini_api(prompt)

        cleaned_response = re.sub(r"```json\n(.*?)\n```", r"\1", response, flags=re.DOTALL).strip()

        try:
            evaluate_json = json.loads(cleaned_response)
        except json.JSONDecodeError:
            return {"error": "Invalid response format from Gemini API"}

    
        return evaluate_json


    except Exception as e:
        raise Exception(f"Error evaluating test: {str(e)}")
