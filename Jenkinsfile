pipeline {
    agent {
        label "jnodes"
    }

    environment {
            // VERSION = sh(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
            // IMAGE_NAME = "scoreserver-wog1312:${VERSION}"
            DOCKER_IMAGE_NAME = "scoreserver-wog1312"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t scoreserver-wog1312 .'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh """ 
                    python3 -m venv .venv
                    source .venv/bin/activate
                    pip install -r requirements.txt
                    """
                }
                script {
                    sh """
                    source .venv/bin/activate
                    python3 tests/e2e.py
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    withCredentials([string(credentialsId: '509c311a-29a4-4653-b394-ff3f9f5bdd51', variable: 'TOKEN'), string(credentialsId: '8c732d85-e233-43f1-8c7b-2081dad5e5ad', variable: 'USER')]) {
                        sh "docker login -u ${USER} -p ${TOKEN}"
                    }
                }
                script {
                    withCredentials([string(credentialsId: '509c311a-29a4-4653-b394-ff3f9f5bdd51', variable: 'TOKEN'), string(credentialsId: '8c732d85-e233-43f1-8c7b-2081dad5e5ad', variable: 'USER')]) {
                        sh "docker push ${USER}/${DOCKER_IMAGE_NAME}"
                    }
                }
            }
        }
    }
}
