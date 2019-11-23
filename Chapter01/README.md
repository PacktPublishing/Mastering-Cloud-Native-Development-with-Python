Copyright (c) 2017-2020 Starwolf Ltd and Richard Freeman. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at http://www.apache.org/licenses/LICENSE-2.0 or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


# Setting Up your Local AWS and Python Environment

A lot can be done with the web interface in the AWS Management console. This is a good place to start and it can help you to understand what you are building, but most often it is not recommended for production deployments. This is because it is time consuming and prone to human error (as we have discussed earlier in this chapter). What is accepted as best practice is to deploy and manage your infrastructure using code and configuration automatically rather than manually. We will be using the AWS command line interface (CLI) with AWS CloudFormation, bash shell scripts, and Python3 throughout the book so let's set these up now.

## Installing Bash on Windows 10

Please skip this step if you are not using Windows.

Using Bash (Unix Shell) makes your life much easier when deploying and managing you serverless and container stacks. I think all analysts, data scientists, architects, administrators, database administrators, developers, DevOps and technical people should know some basic Bash and be able to run shell scripts, which are typically used on LINUX and UNIX (including macOS Terminal).

As an alternative to Bash, you can adapt the scripts to use MS-DOS or Powershell but this is not something I recommend, given that Bash can now run natively on Windows 10 as an application. There are many more online examples for Bash and this is the widely used on production servers.

Note that I have stripped off the `\r` or carriage returns in the code provided, as they are illegal in shell scripts. You can use something like [Notepad++](https://notepad-plus-plus.org/) on Windows if you want to view the carriage returns in your files properly. If you use traditional Windows Notepad the new lines may not be rendered at all, so use [Notepad++](https://notepad-plus-plus.org/), [Sublime](https://www.sublimetext.com/), [Atom](https://atom.io/) or other such editors.

A detailed guide on how to install [Linux Bash shell on Windows 10 can be found here](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/). The main steps are:
1. Go to **Control Panel > Programs > Turn Windows Features On Or Off**.
2. Choose the check box next to the **Windows Subsystem for Linux** option in the list, and then Choose **OK**.
3. Open the **Microsoft Store** and search for **Ubuntu**.
4. Select **Ubuntu 18.04 LTS** and chose on **Get** to install it
5. **Launch Ubuntu** and setup a root account username and password
The Windows `C:\` and other dives are already mounted, and you can access them with the following command in the terminal:

```bash
$ cd /mnt/c/
```

The final step is to create a new `sudo` superuser called `datawolf` so that we don't use the  default account. This can be done as follows:

```bash
# Create user, enter password and details
$ sudo adduser datawolf
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for datawolf
Enter the new value, or press ENTER for the default
        Full Name []: datawolf
        Room Number []: 31
        Work Phone []:
        Home Phone []:
        Other []: I love bigdata
Is the information correct? [Y/n] Y

# A user to sudo group
$ sudo usermod -aG sudo datawolf

# Switch to new account, enter the password
$ su datawolf
Password:
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

# Test you have sudo access
$ sudo ls -la /root
```

Well done! You now have full access to a Linux shell on Windows.

## Update Ubuntu, install Git and Python3
First let’s ensure that our Ubuntu system is up to date, by running the following commands

```bash
$ sudo apt-get update
$ sudo apt-get -y upgrade
```

Update fetches the list of available updates and upgrade install them.
We will be using a distributed version-control system called [Git](https://git-scm.com/) will be used later on in this bookto pull the source code for the book and push code changes, here are the commands to to install Git.

```bash
$ apt-get install git-core
$ git --version
```

The first command installs Git and the second one checks it is installed and shows the version.

The Lambda code throughout the book is written in Python 3.7. Pip is a tool for installing and managing Python packages. Other popular Python package and dependency managers are available, such as [Conda](https://conda.io/docs/index.html) or [Pipenv](https://pipenv.readthedocs.io/), but we will be using pip as it is the recommended tool for installing packages from the Python Package Index [PyPI](https://pypi.org/) and it is also the most widely supported.

```bash
$ sudo apt-get -y install python3.7
$ sudo apt-get -y install python3-pip
$ python3 --version
```
You Using these these commands, you should get will install and check that you have the Python3.7 setup correctly.

The dependent Python spackages required for running, testing and deploying the microservices and applications are listed in `requirements.txt` under each project folder, and can be installed using pip with the following arguments.

```bash
$ sudo pip3 install -r /path/to/requirements.txt
```

This will install the dependent libraries for the local development envionment such as [Boto3](https://boto3.amazonaws.com) which is the Python AWS Software Development Kit (SDK).

In some serverless projects there is also another file called `lambda-requirements.txt` which contains the 3rd party packages that are required by the Lambda when it is deployed. We have created this other `requirements.txt` file as the Boto3 package is already included when the Lambda is deployed to AWS, and the deployed Lambda does not need to test  related libraries such as `nose` or `locust` which would unnnecessarily increases the package size.


## Install and Setup AWS CLI
AWS Command Line Interface (CLI) is used to package and deploy your Lambda functions, as well as setup the infrastructure and security in a repeatable way. Here are the commands to install the AWS CLI:

```bash
$ sudo pip install awscli --upgrade
$ aws --version
```
The first command installs or upgrades the AWS CLI and the seconds on shows the installed version.

You have created a user called `newuser` earlier and have a `credentials.csv` with the AWS keys. Enter the access key and secret key them them by running `aws configure`.

```bash
$ aws configure --profile demo
AWS Access Key ID: <the Access key ID from the csv>
AWS Secret Access Key: <the Secret access key from the csv>
Default region name: <your AWS region such as eu-west-1>
Default output format: <optional>
```

When you run command aws configure you will be prompted to enter the AWS Access Key ID, AWS Secret Access Key which you will find in the credentials.csv. When prompted to enter the AWS region name refer to [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html). Generally, those in the USA can use `us-east-1` and those in Europe can use `eu-west-1`. When prompted to enter output format press enter without entering a value. 
Here I have used `-–profile demo` to create a profile called demo so that you can easily support many environments, if you omit this you will overwrite the default AWS credentials profile.More details on setting up the AWS CLI is available in the [AWS Docs](https://aws.amazon.com/cli/).


## Installing a Python Integrated Development Environment (IDE)

Optional but when you add more code, collaborate with other on more complex projects and services, text editors like *Vi*, *Atom* and *Sublime* or notebooks like *Jupyter* have their limits when building enterprise grade software.

This when you switch to an Integrated Development Environment (IDE) which offers features out of-the-box like:
* Build and debugging tools
* Language specific highlighting and auto-completion
* Source control
* Code formatting, refactoring, and navigation
* Code inspection and profilers
* Code testing
* Support virtual environments

I recommend [PyCharm](https://www.jetbrains.com/pycharm/) which I used personally for this book and for work. It is free in its community edition and has all the features that I need. Other Python developers and data scientists enjoy using [VSCode](https://code.visualstudio.com) (especially those from a .NET background), [PyDev](https://www.pydev.org) (those from Java world), or [Spyder](https://www.spyder-ide.org) (those in data science).
 

[//]: # (section end ######################)

