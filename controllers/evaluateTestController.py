from fastapi import HTTPException
from scripts.evaluateTest import evaluate_test

async def evaluate_test_controller(request_data: dict):
    try:
        # Extract required data
        result = request_data.get("result")
        job_title = request_data.get("jobTitle")
        expirience = request_data.get("Experience")
        skill = request_data.get("skill")

        # Validate input
        # if not result or not isinstance(result, dict):
        #     raise HTTPException(status_code=400, detail="Invalid or missing 'result' (must be a list)")
        if not job_title or not isinstance(job_title, str):
            raise HTTPException(status_code=400, detail="Invalid or missing 'jobTitle'")

        # Call the script function to evaluate test results
        response = await evaluate_test(result, job_title ,expirience ,skill)
        return {"status": "success", "data": response}

    except HTTPException as e:
        raise e  # Rethrow known HTTP exceptions

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
