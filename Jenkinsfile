pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install -r requirements.txt || { echo "Failed to install dependencies."; exit 1; }
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                python main.py || { echo "Script execution failed."; exit 1; }
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // אפשר להוסיף כאן פעולות ניקוי נוספות אם נדרשות
        }
    }
}
