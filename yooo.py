import subprocess

def ping_server(host):
    safe_host = host.replace(";", "").replace("&", "")
    subprocess.run(f"ping -c 1 {safe_host}", shell=True)