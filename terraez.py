import typer
from typing_extensions import Annotated
import subprocess
import requests
import inquirer

app = typer.Typer()

## Install Terraform
@app.command()
def configure():
    tf_v = []
    tf_url = f"https://api.github.com/repos/hashicorp/terraform/releases"
    tv_url_response = requests.get(tf_url)

    if tv_url_response.status_code == 200:
        releases = tv_url_response.json()
        for release in releases:
            tf_v.append(release["name"])
    else:
        print("Error fetching releases:", tv_url_response.status_code)

    terraform_version_select = [
        inquirer.List('version',
                      message="Select a Terraform version",
                      choices=tf_v
                      ),
    ]

    selected_terraform_version = inquirer.prompt(terraform_version_select)
    terraform_version = selected_terraform_version['version'][1:]

    print(f"Installing Terraform {terraform_version}")
    subprocess.run(f'curl -LO https://releases.hashicorp.com/terraform/{terraform_version}/terraform_{terraform_version}_darwin_amd64.zip;tar xvf terraform_{terraform_version}_darwin_amd64.zip; mv terraform /usr/local/bin/terraform1; rm -rf terraform_{terraform_version}_darwin_amd64.zip', shell=True)

## Install Terragrunt
    tg_v = []

    tg_url = f"https://api.github.com/repos/gruntwork-io/terragrunt/releases"
    tg_url_response = requests.get(tg_url)

    if tg_url_response.status_code == 200:
        releases = tg_url_response.json()
        for release in releases:
            tg_v.append(release["name"])
    else:
        print("Error fetching releases:", tg_url_response.status_code)

    terragrunt_version_select = [
        inquirer.List('version',
                      message="Select a Terragrunt version",
                      choices=tg_v
                      ),
    ]

    selected_terragrunt_version = inquirer.prompt(terragrunt_version_select)
    terragrunt_version = selected_terragrunt_version['version']

    print(f"Installing Terragrunt {terragrunt_version}")
    subprocess.run(f'curl -LO https://github.com/gruntwork-io/terragrunt/releases/download/{terragrunt_version}/terragrunt_darwin_amd64; mv terragrunt_darwin_amd64 /usr/local/bin/terragrunt1; chmod u+x /usr/local/bin/terragrunt1', shell=True)

## Run Terragrunt commands
@app.command()
def tgp():
    subprocess.run(f'terragrunt plan', shell=True)

@app.command()
def tga(destroy: bool = typer.Option(False, "-d", "--destroy")):
    command = 'terragrunt apply'
    if destroy:
        command += ' --destroy'
    subprocess.run(command, shell=True)

@app.command()
def tgra(destroy: bool = typer.Option(False, "-d", "--destroy")):
    command = 'terragrunt run-all apply'
    if destroy:
        command += ' --destroy'
    subprocess.run(command, shell=True)

@app.command()
def tgrp():
    subprocess.run(f'terragrunt run-all plan', shell=True)

@app.command()
def tgfu(id: str = typer.Argument(...)):
    command = f'terragrunt force-unlock {id}'
    subprocess.run(command, shell=True)

## Wipe Terragrunt Cache
@app.command()
def wipe_cache():
    tg_dir = typer.prompt("Enter Your Terragrunt directory path")
    find_cache = subprocess.run(f'find {tg_dir} -type d -name ''.terragrunt-cache''', shell=True, capture_output=True, text=True)
    if find_cache.stdout.strip() == "":
        print(f"no Terragrunt cache files found to delete in {tg_dir}")
    elif find_cache.stdout.strip() > "" and tg_dir == ".":
        subprocess.run(f'find {tg_dir} -type d -name ''.terragrunt-cache'' -prune -exec rm -rf {{}} \;', shell=True)
        print(f"Terragrunt cache wiped in current directory")
    elif find_cache.stdout.strip() > "" and tg_dir != ".":
        subprocess.run(f'find {tg_dir} -type d -name ''.terragrunt-cache'' -prune -exec rm -rf {{}} \;', shell=True)
        print(f"Terragrunt cache wiped in {tg_dir}")
if __name__ == "__main__":
    app()
