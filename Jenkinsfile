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
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v
                '''
            }
        }

        stage('Build Container') {
            steps {
                sh 'podman build -f Containerfile.app -t task-api .'
            }
        }

        stage('Deploy Container') {
            sh '''
            podman stop task-api-container || true
            podman rm task-api-container || true

            podman run -d \
                --name task-api-container \ 
                --network host \
                task-api
            '''
        }
    }
}