# Terraez

This repository provides a command-line tool for installing and configuring Terraform and Terragrunt. It allows you to select the desired versions of Terraform and Terragrunt and automatically installs them on your system. Additionally, it provides several commands for executing common Terragrunt operations.

### Prerequisites
Before using this tool, make sure you have the following prerequisites installed on your system:

Python (version 3.6 or later)
Typer (Python library)
requests (Python library)
inquirer (Python library)

### Installation
To use this tool, perform the following steps:

Clone this repository to your local machine.
```
git clone https://github.com/msnyman1991/terraez.git
```

Install the required Python libraries.
```
pip install typer requests inquirer
```

### Usage

#### Configure Terraform and Terragrunt
Use the following command to configure Terraform and Terragrunt:
```
python terraez.py configure
```
This command fetches the available versions of Terraform and Terragrunt from their respective GitHub repositories and prompts you to select the desired versions. It then installs the chosen versions on your system.

#### Execute Terragrunt Commands
The following commands allow you to execute common Terragrunt operations:

Plan: Generate and show an execution plan for Terragrunt.
```
python terraez.py tgp
```
Apply: Apply the changes described in the Terragrunt configuration.

```
python terraez.py tga [-d/--destroy]
```
Use the -d or --destroy option to destroy the infrastructure instead of applying changes.

Run All Apply: Apply Terragrunt configurations for all child modules.

```
python terraez.py tgra [-d/--destroy]
```
Use the -d or --destroy option to destroy the infrastructure instead of applying changes.
Run All Plan: Generate and show an execution plan for all child modules.

```
python terraez.py tgrp
```
Force Unlock: Release a Terragrunt state lock.

```
python terraez.py tgfu <id>
```
Replace <id> with the lock ID.
  
#### Wipe Terragrunt Cache
To wipe the Terragrunt cache, use the following command:

```
python terraez.py wipe_cache
```
  
This command prompts you to enter the path to your Terragrunt directory. It then finds and deletes the Terragrunt cache files in the specified directory.

Note: Be cautious when using this command, as it permanently deletes the Terragrunt cache files.

License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

Acknowledgements
This tool relies on the following open-source projects:

Typer
requests
inquirer
We thank the contributors of these projects for their valuable work.
