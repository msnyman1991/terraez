import typer
import subprocess
import requests
import inquirer

app = typer.Typer()

@app.command()
def configure():
    tf_v = []
    # tg_v = []

    url = f"https://api.github.com/repos/hashicorp/terraform/releases"
    response = requests.get(url)

    if response.status_code == 200:
        releases = response.json()
        for release in releases:
            tf_v.append(release["name"])
    else:
        print("Error fetching releases:", response.status_code)

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

    # print(f"Installing Terragrunt {terragrunt_version}")
    # subprocess.run(f'curl -LO https://github.com/gruntwork-io/terragrunt/releases/download/{terragrunt_version}/terragrunt_darwin_amd64; mv terragrunt_darwin_amd64 /usr/local/bin/terragrunt1; chmod u+x /usr/local/bin/terragrunt1', shell=True)

@app.command()
def auth():
    print(f"Hello There")

@app.command()
def wipe_cache():
    print(f"Hello There")
    subprocess.run(f'find . -type d -name ''.terragrunt-cache'' -prune -exec rm -rf {} +', shell=True)

if __name__ == "__main__":
    app()
