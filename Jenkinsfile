pipeline {
    agent {
        docker {
            image 'python:3.9-slim-buster'
            args '-u root'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install poetry && poetry install --no-dev'
                sh 'docker build -t my_project .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}

