import io
import shutil
import tarfile
import tempfile
import uuid

import gradio as gr
import requests


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
    
    return {'zip_url': f'{zip_name}.zip'}

inputs = gr.Textbox(label="URL")

title = "Conversion Engine for Arxiv Latex Tar to Zip"
description = "Enter the URL of the Arxiv paper"

gr.Interface(convert_tar_to_zip, inputs, "json", title=title, description=description).launch()