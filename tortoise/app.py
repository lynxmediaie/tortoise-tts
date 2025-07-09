import logging
import runpy
import subprocess
import sys

from fastapi import FastAPI, Request

app = FastAPI()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
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
    logging.info(f"Received request with args: {args}")

    # If the request contains files, we can handle them here
    files = await request.form()
    # Verify if there is just one file
    if 'file' in files:
        file = files['file']
        if file.filename:
            # Save the file to a temporary location
            temp_file_path = f"/tmp/{file.filename}"
            with open(temp_file_path, 'wb') as f:
                f.write(await file.read())
                # make the text arg the content of the file
            with open(temp_file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)
                args['text'] = text

    print(args)  # Print the keys of the request JSON for debugging
    # Extract parameters from the request
    args_list = [f"--{key}={value}" for key, value in args.items() if value is not None]
    logging.info(f"Calling TTS with args: {args_list}")
    print(f"Calling TTS with args: {args_list}")  # Print the keys of the request JSON for debugging

    call_tts_inline("do_tts.py", args_list)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)