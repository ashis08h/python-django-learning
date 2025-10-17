import asyncio
import tempfile
import os
import subprocess
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Setup templates and static dirs
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Run subprocess safely in a background thread
async def run_subprocess(cmd):
    """Run a subprocess in a thread-safe way (compatible with Windows)."""
    loop = asyncio.get_event_loop()
    process = await loop.run_in_executor(None, lambda: subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        text=True
    ))

    try:
        stdout, stderr = await loop.run_in_executor(None, process.communicate)
        return stdout.strip(), stderr.strip()
    except Exception as e:
        process.kill()
        raise e


@app.post("/run")
async def run_code(request: Request):
    data = await request.json()
    code = data.get("code", "")
    language = data.get("language", "python")

    blocked_keywords = ["import os", "import sys", "open(", "exec(", "eval(", "subprocess", "socket", "shutil"]
    if language == "python" and any(k in code for k in blocked_keywords):
        return JSONResponse({"error": "Use of restricted operations detected."})

    ext = ".py" if language == "python" else ".js"

    with tempfile.NamedTemporaryFile(delete=False, suffix=ext, mode="w") as temp_file:
        temp_file.write(code)
        temp_path = temp_file.name

    try:
        cmd = f'python "{temp_path}"' if language == "python" else f'node "{temp_path}"'
        stdout, stderr = await run_subprocess(cmd)

        if stderr:
            return JSONResponse({"error": stderr})
        return JSONResponse({"output": stdout or "Code executed successfully, but produced no output."})

    except Exception as e:
        return JSONResponse({"error": str(e)})
    finally:
        os.remove(temp_path)
