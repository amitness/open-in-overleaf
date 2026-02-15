from io import BytesIO
import tarfile
import zipfile

import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles


def convert_tar_to_zip(arxiv_url: str) -> BytesIO:
    latex_source_url = arxiv_url.replace("/abs/", "/src/")
    resp = requests.get(latex_source_url)

    zip_buffer = BytesIO()
    with tarfile.open(fileobj=BytesIO(resp.content), mode="r:gz") as tar:
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
            for member in tar.getmembers():
                if member.isfile() and (f := tar.extractfile(member)):
                    zf.writestr(member.name, f.read())

    zip_buffer.seek(0)
    return zip_buffer


app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("static/index.html", media_type="text/html")


@app.get("/fetch_tar")
def fetch_arxiv_zip(arxiv_url: str):
    return StreamingResponse(
        convert_tar_to_zip(arxiv_url),
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=arxiv_source.zip"},
    )
