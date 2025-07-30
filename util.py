#!/usr/bin/python3

import subprocess

def processText(input):
    if 'http' in str(input):
        subprocess.run(f"wget {input} -O input.jpeg", shell=True)

    process = subprocess.run("sh classify.sh input.jpeg", stdout=subprocess.PIPE, shell=True)
    result = process.stdout.decode('utf-8')
    result = result[result.rfind("imagenet") + 9:]
    return result
