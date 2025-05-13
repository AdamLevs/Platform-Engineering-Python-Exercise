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

        stage('Setup Python Env') {
            steps {
                sh '''
                    python3 -m venv ${PYTHON_ENV}
                    . ${PYTHON_ENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run main.py with argparse') {
            steps {
                sh '''
                    . ${PYTHON_ENV}/bin/activate
                    python main.py --service cloudwatch --action log-test
                '''
            }
        }

        stage('Docker Build & Run') {
            steps {
                sh '''
                    docker build -t aws-cli-app .
                    docker run aws-cli-app --service cloudwatch --action docker-log
                '''
            }
        }
    }

    post {
        always {
            sh '''
                if [ -d "${PYTHON_ENV}" ]; then
                    rm -rf ${PYTHON_ENV}
                fi
            '''
        }
    }
}