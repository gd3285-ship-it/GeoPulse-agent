import json
import asyncio
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uuid

# הנה אנחנו קוראים למנוע האמיתי של יעל!
from engine import InsuranceGEOEngine 

app = FastAPI(title="GEO-Pulse API - Real Data")

# הגדרת הקטגוריה בדיוק כמו שיעל בנתה
INSURANCE_CONFIG = {
    "INS_CAR": {
        "name": "ביטוח רכב - אמינות", 
        "focus": "מהירות תשלום תביעות והעברת כספים"
    }
}

# שימי לב: המנוע של יעל צריך מפתח Cohere! 
# אם אין לך כרגע, תקבלי שגיאת ERROR בדפדפן - וזה מעולה, כי זה אומר שהמנוע ניסה לעבוד!
COHERE_API_KEY = "הכנס_כאן_מפתח"
 

class ScanRequest(BaseModel):
    target_brand: str

def run_scan_in_background(task_id: str, brand_name: str):
    print(f"התחלתי סריקת AI אמיתית עבור: {brand_name}")

@app.post("/scan/start")
async def start_scan(request: ScanRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    background_tasks.add_task(run_scan_in_background, task_id, request.target_brand)
    return {"taskId": task_id}

@app.get("/scan/stream/{task_id}")
async def stream_scan(task_id: str):
    
    # מדליקים את המנוע!
    engine_ai = InsuranceGEOEngine(api_key=COHERE_API_KEY)

    async def event_generator():
        try:
            # מריצים את הפונקציה האמיתית שיעל כתבה
            for event in engine_ai.run_full_audit(INSURANCE_CONFIG):
                # אורזים את הנתונים וזורקים אותם החוצה לדפדפן של גיטי
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
                await asyncio.sleep(0.1)
        except Exception as e:
            # אם יש שגיאה (כמו חוסר במפתח API), משדרים גם אותה
            error_msg = {"event": "ERROR", "data": {"message": str(e)}}
            yield f"data: {json.dumps(error_msg, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")