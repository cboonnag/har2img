import json
import base64 
from haralyzer import HarParser
import glob
import os


def har2img():
    path = 'har_files'

    files = [os.path.basename(f) for f in glob.glob(path + "**/*.har", recursive=True)]

    for har in files:
        print(har)
        with open(path +"/"+ har, 'r') as f:
            har_parser = HarParser(json.loads(f.read()))
        har_name = os.path.splitext(har)
        img_count = 0
        
        try:
            os.mkdir(har_name[0])
        except:
            print("exist")
        for page in har_parser.pages:
            for entry in page.entries:
                img_count += 1 
                # Need to be careful accessing the text property, it will not exist for non text-based responses.
                try:
                    b64txt = entry['response']['content'].get('text', '')
                    png64_decode = base64.decodebytes(bytes(b64txt, encoding="raw_unicode_escape"))
                    image_result = open(har_name[0]+"/"+har_name[0]+"-"+str(img_count)+".png", 'wb') # create a writable image and write the decoding result
                    image_result.write(png64_decode)
                except:
                    pass

if __name__ == "__main__":
    har2img()