import typer
import subprocess

app = typer.Typer()

@app.command()
def main():
    terraform_version = typer.prompt("Enter Terraform version")
    terragrunt_version = typer.prompt("Enter Terragrunt version")

    print(f"Installing Terraform {terraform_version}")
    subprocess.run(f'curl -LO https://releases.hashicorp.com/terraform/{terraform_version}/terraform_{terraform_version}_darwin_amd64.zip;tar xvf terraform_{terraform_version}_darwin_amd64.zip; mv terraform /usr/local/bin/terraform1; rm -rf terraform_{terraform_version}_darwin_amd64.zip', shell=True)

    print(f"Installing Terragrunt {terragrunt_version}")
    subprocess.run(f'curl -LO https://github.com/gruntwork-io/terragrunt/releases/download/{terragrunt_version}/terragrunt_darwin_amd64; mv terragrunt_darwin_amd64 /usr/local/bin/terragrunt1; chmod u+x /usr/local/bin/terragrunt1', shell=True)

if __name__ == "__main__":
    typer.run(main)
ƒ