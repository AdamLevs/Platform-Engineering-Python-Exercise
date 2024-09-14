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
                source ${PYTHON_ENV}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                source ${PYTHON_ENV}/bin/activate
                python main.py
                '''
            }
        }
    }

    post {
        always {
            sh '''
            deactivate
            rm -rf ${PYTHON_ENV}
            '''
        }
    }
}
