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
                echo "Jenkins is working!"
                pwd
                ls -la
                '''
            }
        }
    }
}