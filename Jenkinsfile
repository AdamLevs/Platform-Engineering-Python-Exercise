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
                script {
                    sh '''
                    echo "Creating virtual environment..."
                    python3 -m venv ${PYTHON_ENV}
                    echo "Activating virtual environment..."
                    source ${PYTHON_ENV}/bin/activate
                    echo "Installing dependencies..."
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Script') {
            steps {
                script {
                    sh '''
                    echo "Activating virtual environment..."
                    source ${PYTHON_ENV}/bin/activate
                    echo "Running script..."
                    python main.py
                    '''
                }
            }
        }
    }

    post {
        always {
            sh '''
            echo "Deactivating and removing virtual environment..."
            deactivate || true
            rm -rf ${PYTHON_ENV}
            '''
        }
    }
}
