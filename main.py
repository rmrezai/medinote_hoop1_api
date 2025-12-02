
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/medinote/ap")
async def process_input(request: Request):
    try:
        body = await request.body()
        text = body.decode("utf-8").strip()

        if text.startswith("HOOP ["):
            # Placeholder logic
            return {
                "ap_entries": [
                    "1. Psychiatric Decompensation\n- Likely bipolar or schizoaffective disorder.\n- Recommend quetiapine titration.\n- Consider transfer to inpatient psychiatry.\n- Maintain Foley with urology follow-up."
                ]
            }

        return JSONResponse(status_code=400, content={"error": "Input must start with HOOP ["})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Server error: {str(e)}"})
