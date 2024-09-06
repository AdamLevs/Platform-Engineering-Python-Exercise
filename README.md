# Platform-Engineering-Python-Exercise

This CLI tool allows you to manage AWS services including EC2, S3, and Route53. It provides a command-line interface to create and manage EC2 instances, S3 buckets, and Route53 domains.

## Installation

Follow these instructions to set up the tool on your system.

### Prerequisites

- **Python 3.6 or later**: Ensure Python is installed on your system.
- **Pip**: The package installer for Python.

### Installation Steps

#### Windows

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/downloads/).
   - Run the installer and check the box to add Python to your PATH.

2. **Install Required Packages**:
   - Open Command Prompt or PowerShell.
   - Navigate to the directory containing `requirements.txt`.
   - Run the following command:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Tool**:
   - Navigate to the directory with your scripts.
   - Run the tool with:
     ```bash
     python main.py
     ```

#### Linux

1. **Install Python**:
   - Python is often pre-installed. You can check by running `python3 --version`. If not installed, you can install it using your package manager. For example:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Install Required Packages**:
   - Open a terminal.
   - Navigate to the directory containing `requirements.txt`.
   - Run the following command:
     ```bash
     pip3 install -r requirements.txt
     ```

3. **Run the Tool**:
   - Navigate to the directory with your scripts.
   - Run the tool with:
     ```bash
     python3 main.py
     ```

#### macOS

1. **Install Python**:
   - Python is often pre-installed. You can check by running `python3 --version`. If not installed, you can install it using Homebrew. First, install Homebrew from [brew.sh](https://brew.sh/), then:
     ```bash
     brew install python
     ```

2. **Install Required Packages**:
   - Open Terminal.
   - Navigate to the directory containing `requirements.txt`.
   - Run the following command:
     ```bash
     pip3 install -r requirements.txt
     ```

3. **Run the Tool**:
   - Navigate to the directory with your scripts.
   - Run the tool with:
     ```bash
     python3 main.py
     ```

## Usage

1. **Run the tool**:
   - Execute the script with Python.
   - Follow the on-screen prompts to choose and manage AWS services.

2. **Interact with AWS Services**:
   - Choose from the menu to manage EC2 instances, S3 buckets, or Route53 domains.
  

## Notes

- Ensure that your AWS credentials are configured correctly. You will be prompted to enter your AWS Access Key ID and Secret Access Key when running the tool.
- The tool uses boto3 to interact with AWS services. Ensure you have the necessary permissions for the operations you want to perform.
- the test.png is there to put it inside the s3 bucket for testing 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
