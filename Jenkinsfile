pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version
                    git --version
                    google-chrome --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Chrome Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -m smoke --browser chrome
                '''
            }
        }
    }
}