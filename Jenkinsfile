pipeline {
    agent {
        label 'jnodes'
    }

    // environment {
    //         VERSION = sh(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
    //         IMAGE_NAME = "wog1312:${VERSION}"
    //     }

    stages {
        stage('Build') {
            steps {
                script {
                    sh "docker build -t scoreserver-wog1312 ."
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh "docker-compose up -d"
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
                    python3 tests/e2e.py"
                    """
                }
            }
        }

        stage('Deply') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
