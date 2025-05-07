from utils.gemini import call_gemini_api
import json
import re

async def generate_test(job_role: str, difficulty: str ,experience : str ):
    try:
        # Format the prompt dynamically
        prompt = f"""
        Generate a list of only the most essential core skills required for the job role of "{job_role}".
        Rules for Skill Selection:  
        - Include only the **most fundamental and job-specific skills** required for the role.  
        - Do **NOT** include soft skills (e.g., communication, leadership, teamwork).  
        - Do **NOT** include tools or software (e.g., Excel, Git, Jira, SAP).  
        - Do **NOT** include methodologies or frameworks (e.g., Agile, Scrum, Six Sigma).  

        Generate 7 multiple-choice questions (MCQs) for each skill provided in the list.

        ### **Requirements:**  
        - Each skill must have **5 to 7 MCQs** covering **all key concepts** for a **fair evaluation**.  
        - The **difficulty level** must strictly match `{difficulty}` (**Beginner, Intermediate, or Advanced**).  
        - The **experience level** must be considered when generating questions:  
        - `{experience}` will indicate the candidate’s **years of experience** in the skill.  
        - Adjust **question complexity** and **depth** based on `{experience}` and `{difficulty}`.  
        - Each question must have **exactly four options**, with **only one correct answer**.  
        - Ensure **topic diversity** within each skill—**no duplicate questions**.  
        - **Return only valid JSON**, without any extra text, explanation, or formatting beyond the specified structure.  

        ### **Variables:**  
        - **job_role**: `{job_role}` (Job Role To Generate the Skills from)  
        - **difficulty**: `{difficulty}` (The difficulty level: Beginner, Intermediate, or Advanced)  
        - **experience**: `{experience}` (Candidate’s experience in years, e.g., 0-1, 2-4, 5+ years)  
        ### Strict JSON Response Format:
        {{
            Test_ID : DDMMYYYYXX (EG : 0505202501 , here XX represent a number adding to date to make it unique and date should be current date ) 
            Skills : [list of skills you generated]
            "Questions": [
                {{
                    "Question_ID" : 1001
                    "Question": "MCQ question related to Skill 1",
                    "Options": ["Option A", "Option B", "Option C", "Option D"],
                    "Answer": "Correct option",
                    "Difficulty": "{difficulty}"
                }},
                {{
                    "Question_ID" : 1002
                    "Question": "Next MCQ for Skill 1",
                    "Options": ["Option A", "Option B", "Option C", "Option D"],
                    "Answer": "Correct option",
                    "Difficulty": "{difficulty}"
                }},
                {{
                    "Question_ID" : 2001
                    "Question": "MCQ question related to Skill 2",
                    "Options": ["Option A", "Option B", "Option C", "Option D"],
                    "Answer": "Correct option",
                    "Difficulty": "{difficulty}"
                }}
            ]
        }}
        """

        # Call Gemini API to generate questions

        response = await call_gemini_api(prompt)
        
        cleaned_response = re.sub(r"```json\n(.*?)\n```", r"\1", response, flags=re.DOTALL).strip()

        try:
            test_json = json.loads(cleaned_response)
        except json.JSONDecodeError:
            return {"error": "Invalid response format from Gemini API"}

        return test_json    

    except Exception as e:
        raise Exception(f"Error generating test: {str(e)}")
