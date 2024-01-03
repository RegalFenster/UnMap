import ssl
import urllib.request
import zipfile
import os

# Constants
DOWNLOAD_URL = 'https://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=tableCode:240;sexCode:0&DataMartId=POP&Format=csv&c=2,3,10,18'
ZIP_FILE_PATH = 'data/data.zip'
EXTRACTION_DIR = 'data'
NEW_FILE_NAME = 'data.csv'

def download_file(url, destination):
    # Set up SSL context to allow legacy TLS versions
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT

    # Use urllib to open the URL and read the content
    response = urllib.request.urlopen(url, context=ctx)

    # Save the data to a local file
    with open(destination, 'wb') as file:
        file.write(response.read())

# Download the file
download_file(DOWNLOAD_URL, ZIP_FILE_PATH)

# Unzip the data
with zipfile.ZipFile(ZIP_FILE_PATH) as zip_file:
    # Specify the extraction directory
    zip_file.extractall(EXTRACTION_DIR)

    # Assume there is only one file in the zip archive
    extracted_file = zip_file.namelist()[0]

    # Get the file extension
    file_extension = os.path.splitext(extracted_file)[1]

    # Build the paths for the original and new files
    original_file_path = os.path.join(EXTRACTION_DIR, extracted_file)
    new_file_path = os.path.join(EXTRACTION_DIR, NEW_FILE_NAME)

    # Delete older file
    if os.path.exists(new_file_path):
        os.remove(new_file_path)

    # Rename the file
    os.rename(original_file_path, new_file_path)