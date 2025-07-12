import logging
import runpy
import subprocess
import sys

from fastapi import FastAPI, Request, UploadFile

app = FastAPI()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)  # Log to stdout
    ]
)


def call_tts_inline(script, args_list):
    # Backup real argv
    real_argv = sys.argv
    try:
        sys.argv = [script, *args_list]
        # This will execute your script’s __main__ block
        runpy.run_path(script, run_name="__main__")
    finally:
        sys.argv = real_argv

@app.post("/tts")
async def tts(request: Request):
    """
    Endpoint to perform text-to-speech synthesis.

    """
    args = await request.json()
    if args:
        logging.info(f"Received request with args: {args}")
        if "file" in args:
            # open the file on the path provided in the request and read it that is the text to be converted to speech
            try:
                with open(args["file"], 'rb') as f:
                    args["text"] = f.read().decode("utf-8")
                args.pop("file")
            except Exception as e:
                logging.error(f"Error reading file {args['file']}: {e}")
                return {"error": "Failed to read file"}

        args_list = []
        for key, value in args.items():
            if value is not None:
                args_list.append(f"--{key}")
                args_list.append(f"{value}")

    else:
        args_list = {}

    try:
        file = await request.get('file', None)
        text = (await file.read()).decode("utf-8")
        args["text"] = text  # Only overwrite if file is uploaded
    except Exception:
        pass

    call_tts_inline("do_tts.py", args_list)
    return {"status": "TTS processing started", "args": args_list}

@app.post("/read")
async def read_file():
    """
    Endpoint to read a file and return its content.

    Args:
        file (UploadFile): The file to be read.

    Returns:
        dict: A dictionary containing the file content.
    """
    args_list = [
        "--textfile", "./../1wav.txt",
    ]
    call_tts_inline("read.py", args_list)


@app.get("/add-voice/<voice>")
async def add_voice(file: UploadFile, voice: str):
    """
    Endpoint to add a new voice.

    Args:
        voice (str): The name of the voice.
        file (UploadFile): The audio file for the voice.

    Returns:
        dict: A status message indicating the result of the operation.
    """
    try:
        file_path = f"./voices/{voice}.wav"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        return {"status": "Voice added successfully", "voice": voice}
    except Exception as e:
        logging.error(f"Error adding voice {voice}: {e}")
        return {"error": "Failed to add voice"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)