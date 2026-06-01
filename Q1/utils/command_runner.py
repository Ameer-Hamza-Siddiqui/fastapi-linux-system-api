import subprocess
from fastapi import HTTPException

def run_command(command: list):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            raise HTTPException(
                status_code=500,
                detail={
                    "error": "Command execution failed",
                    "message": result.stderr
                }
            )

        return {
            "command": " ".join(command),
            "output": result.stdout.strip()
        }

    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=408,
            detail="Command execution timed out"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )