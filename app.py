import io
import json
import os
import shutil
import tarfile
import tempfile
import uuid
from io import BytesIO

import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles


def convert_tar_to_zip(arxiv_url):
    latex_source_url = (arxiv_url.replace('/abs/', '/src/'))
    
    # Fetch the latex source as .tar.gz file
    resp = requests.get(latex_source_url)
    print(resp.status_code)
    tar_file = resp.content
    with tarfile.open(fileobj=io.BytesIO(tar_file), mode='r:gz') as tar:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Extract the tar file to a temporary directory
            tar.extractall(temp_dir)

            # Create a zip file from the extracted tar file
            filename = str(uuid.uuid4())
            zip_name = f'{filename}'
            shutil.make_archive(filename, 'zip', temp_dir)
    
    return f'{zip_name}.zip'

app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.head("/")
@app.get("/")
def index() -> FileResponse:
    return FileResponse(path="static/index.html", media_type="text/html")


@app.get("/fetch_tar")
def t5(arxiv_url: str):
    zip_path = convert_tar_to_zip(arxiv_url)
    return FileResponse(path=zip_path, media_type="application/zip", filename=zip_path)
