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
        print(args_list)
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
        if "file"     in args:
            # open the file on the path provided in the request and read it that is the text to be converted to speech
            try:
                with open(args["file"], 'rb') as f:
                    args["text"] = f.read().decode("utf-8")
                args.pop("file")
            except Exception as e:
                logging.error(f"Error reading file {args['file']}: {e}")
                return {"error": "Failed to read file"}




        print(args)  # Print the keys of the request JSON for debugging
        # Extract parameters from the request
        args_list = []
        for key, value in args.items():
            if value is not None:
                args_list.append(f"--{key}")
                args_list.append(f"{value}")

        logging.info(f"Calling TTS with args: {args_list}")
        print(f"Calling TTS with args: {args_list}")  # Print the keys of the request JSON for debugging
    else:
        args_list = {}

    try:
        file = await request.get('file', None)
        text = (await file.read()).decode("utf-8")
        args["text"] = text  # Only overwrite if file is uploaded
    except Exception:
        pass

    print(f"Calling TTS with args: {args_list}")  # Print the keys of the request JSON for debugging


    call_tts_inline("do_tts.py", args_list)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)