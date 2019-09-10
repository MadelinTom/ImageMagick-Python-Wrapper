import subprocess
import sys
import json


"""
Wrap the ImageMagick convert & -resize command line tool with a sub process. This function accepts:

1) A JPEG image (path)
2) Output image size factor (100%/50%)
3) Filename for output file 
"""


def convert_wrapper(jpeg_path=None, output_size=None, output_file_name=None, json_file=None):

    if (sys.argv[1].endswith(".json")):
        # Load json file path
        json_file_path = str(sys.argv[1])

        # Load json file
        with open(json_file_path, 'r') as f:
            json_dict = json.loads(f.read())

            for item in json_dict['pictures']:

                bash = ["convert",str(item['jpeg_path']), " -resize ", str(item['output_size']), " ", str(item['output_file_name'])]
                
                # Use the subprocess module to communicate with ImageMagick
                subprocess.call(bash, shell=False)
        return

    else:
        # Load variables 
        jpeg_path = sys.argv[1]
        output_size = sys.argv[2]
        output_file_name = sys.argv[3]

        # If no json provided Load the command line with the variables passed through to the function
        bash = ["convert",str(jpeg_path), " -resize ", str(output_size), " ", str(output_file_name)]

        # Use the subprocess module to communicate with ImageMagick
        subprocess.call(bash, shell=False)


if __name__ == '__main__':
    try:
        convert_wrapper(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        convert_wrapper(sys.argv[1])