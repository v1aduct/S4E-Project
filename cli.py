import subprocess

def GetStdout(command):
    results = subprocess.run(
        command.split(),
        capture_output=True
    )
    if results.returncode != 0:
        return results.stderr
    return results.stdout
