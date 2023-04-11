import io
import shutil
import tarfile
import tempfile
import uuid

import gradio as gr
import requests


def convert_tar_to_zip(arxiv_url):
    latex_source_url = (arxiv_url.replace('/abs/', '/e-print/')
                        .replace('arxiv.org', 'export.arxiv.org'))
    
    # Fetch the latex source as .tar.gz file
    tar_file = requests.get(latex_source_url).content
    with tarfile.open(fileobj=io.BytesIO(tar_file)) as tar:
        with tempfile.TemporaryDirectory() as dir:
            # Extract the tar file to a temporary directory
            tar.extractall(dir)

            # Create a zip file from the extracted tar file
            filename = str(uuid.uuid4())
            zip_name = f'{filename}'
            shutil.make_archive(filename, 'zip', dir)
    
    return {'zip_url': f'{zip_name}.zip'}

inputs = gr.Textbox(label="URL")

title = "Conversion Engine for Arxiv Latex Tar to Zip"
description = "Enter the URL of the Arxiv paper"

gr.Interface(convert_tar_to_zip, inputs, "json", title=title, description=description).launch()