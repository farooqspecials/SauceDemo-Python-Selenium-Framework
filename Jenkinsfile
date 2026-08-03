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

                    pytest \
                        --browser chrome \
                        --html=reports/chrome-report.html \
                        --self-contained-html
                '''
            }
        }

        /*
        stage('Run Firefox Tests') {
            steps {
                sh '''
                    . venv/bin/activate

                    pytest \
                        --browser firefox \
                        --html=reports/firefox-report.html \
                        --self-contained-html
                '''
            }
        }

        stage('Run Edge Tests') {
            steps {
                sh '''
                    . venv/bin/activate

                    pytest \
                        --browser edge \
                        --html=reports/edge-report.html \
                        --self-contained-html
                '''
            }
        }
        */

    }

    post {

        always {

            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true

            echo "Pipeline Finished"

        }

        success {
            echo "All tests passed."
        }

        failure {
            echo "Some tests failed."
        }
    }
}