import subprocess
import json

def crawl(url):

    result = subprocess.run(
        ["katana","-u", url, "-d", "1"],
        capture_output=True,
        text=True
    )
    if result.returncode !=0:
        return 500
    
    count = 0

    for line in result.stdout.splitlines():
        count+=1

    return [result.stdout, count]

print(crawl("https://www.york.ac.uk/teaching/cws/wws/webpage1.html")[0])