import subprocess
import sys

def run(cmd):
    print(f"Executando: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

# Mensagem de commit padrão ou passada como argumento
mensagem_commit = "Commit de todos os arquivos do projeto SysConfec"
if len(sys.argv) > 1:
    mensagem_commit = " ".join(sys.argv[1:])

run("git add .")
run(f'git commit -m "{mensagem_commit}"')
run("git push origin main")
print("Projeto SysConfec atualizado no GitHub!") 