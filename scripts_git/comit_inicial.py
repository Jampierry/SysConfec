import subprocess
import os

def run(cmd):
    print(f"Executando: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

# Cria README.md se não existir
if not os.path.exists("README.md"):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# SysConfec\n")

run("git init")
run("git add README.md")
run('git commit -m "Comit Inicial"')
run("git branch -M main")
run("git remote add origin https://github.com/Jampierry/SysConfec.git")
run("git push -u origin main")
print("Commit inicial realizado e projeto enviado para o GitHub!") 