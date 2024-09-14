pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv_py'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from SCM...'
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    timeout(time: 1, unit: 'MINUTES') { // Set timeout for this stage
                        echo 'Creating virtual environment...'
                        sh '''
                        python3 -m venv ${PYTHON_ENV} || { echo "Failed to create virtual environment"; exit 1; }
                        echo "Virtual environment created successfully"
                        source ${PYTHON_ENV}/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
                        echo "Virtual environment activated"
                        pip install -r requirements.txt || { echo "Failed to install requirements"; exit 1; }
                        echo "Requirements installed successfully"
                        '''
                    }
                }
            }
        }

        stage('Run Script') {
            steps {
                script {
                    timeout(time: 1, unit: 'MINUTES') { // Set timeout for this stage
                        echo 'Running Python script...'
                        sh '''
                        source ${PYTHON_ENV}/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
                        python main.py || { echo "Python script failed"; exit 1; }
                        echo "Python script ran successfully"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh '''
            deactivate || true
            rm -rf ${PYTHON_ENV} || { echo "Failed to remove virtual environment"; exit 1; }
            echo "Cleanup completed"
            '''
        }
        failure {
            echo 'Build failed. Cleaning up...'
            sh '''
            rm -rf ${PYTHON_ENV} || { echo "Failed to remove virtual environment"; exit 1; }
            echo "Cleanup completed"
            '''
        }
        aborted {
            echo 'Build aborted. Cleaning up...'
            sh '''
            rm -rf ${PYTHON_ENV} || { echo "Failed to remove virtual environment"; exit 1; }
            echo "Cleanup completed"
            '''
        }
    }
}
