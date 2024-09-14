pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv_py'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv ${PYTHON_ENV}
                if [ -f "${PYTHON_ENV}/bin/activate" ]; then
                    echo "Virtual environment created successfully."
                else
                    echo "Failed to create virtual environment."
                    exit 1
                fi
                source ${PYTHON_ENV}/bin/activate
                pip install -r requirements.txt || { echo "Failed to install dependencies."; exit 1; }
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                source ${PYTHON_ENV}/bin/activate
                python main.py || { echo "Script execution failed."; exit 1; }
                '''
            }
        }
    }

    post {
        always {
            sh '''
            if [ -d "${PYTHON_ENV}" ]; then
                deactivate || echo "Failed to deactivate environment."
                rm -rf ${PYTHON_ENV} || echo "Failed to remove virtual environment."
            fi
            '''
        }
    }
}
