# how to create command line utility
#

import argparse
import requests

def download_file(url, local_filename):
    if local_filename==None:
        local_filename=url.split('/')[-1]     # Then the file should automatically be generated
    # NOTE the streame true parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # if you have chunk encoded response uncomment if 
                # and sel shuk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename

parser =argparse.ArgumentParser()


# parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument('url',help="url of the file to download")
parser.add_argument('output',help="by which name do you want to save your file")


# parser.add_argument("-o",'--optional',help="Name of the file", default=None)

# parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output)

download_file(args.url, args.output)


# review this video

# we are using this program downoload any image usint the url of image
# synext
# D:\UserData\Work\development\programming\python\CodeWithHarry> python "#85 creating command line utility in python.py" https://imagej.net/images/AuPbSn40.jpg tem111.jpg
#               working directry or python file location       python for call interprater      file name       url         file name will you save image which name