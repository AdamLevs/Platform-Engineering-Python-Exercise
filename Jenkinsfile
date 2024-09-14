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
                    // Create and activate virtual environment, then install dependencies
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

        stage('Run main.py') {
            steps {
                script {
                    // Run the main.py script
                    sh '''
                        source ${PYTHON_ENV}/bin/activate
                        python main.py || { echo "Failed to run main.py"; exit 1; }
                        echo "main.py executed successfully"
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Cleaning up..."
                sh '''
                    if [ -d "${PYTHON_ENV}" ]; then
                        rm -rf ${PYTHON_ENV}
                    fi
                '''
            }
        }
        failure {
            echo "Build failed. Check the logs for details."
        }
    }
}
