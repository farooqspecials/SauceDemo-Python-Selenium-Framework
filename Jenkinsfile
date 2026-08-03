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
                    echo "===== Environment ====="
                    python3 --version
                    pip3 --version
                    git --version
                    google-chrome --version
                    firefox --version
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
                    mkdir -p reports
                    pytest --browser chrome \
                    --html=reports/chrome-report.html \
                    --self-contained-html
                '''
            }
        }

        stage('Run Firefox Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --browser firefox \
                    --html=reports/firefox-report.html \
                    --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            echo 'Pipeline Finished'
        }

        success {
            echo 'All browser tests passed.'
        }

        failure {
            echo 'One or more browser tests failed.'
        }
    }
}