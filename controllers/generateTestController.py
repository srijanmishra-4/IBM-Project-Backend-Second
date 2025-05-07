from fastapi import HTTPException
from scripts.generateTest import generate_test

async def generate_test_Controller(request_data: dict):
    try:
        # Extract skills and difficulty from request body
        jobRole = request_data.get("jobRole")
        difficulty = request_data.get("difficulty")
        experience = request_data.get("experience")

        # Validate inputs
        if not difficulty or difficulty not in ["beginner", "intermediate", "advanced"]:
            raise HTTPException(status_code=400, detail="Invalid or missing 'difficulty'")

        # Call the script function to generate test questions
        response = await generate_test(jobRole, difficulty , experience)
        return {"status": "success", "data": response}

    except HTTPException as e:
        raise e  # Rethrow known HTTP exceptions

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
