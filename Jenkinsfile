pipeline {
    agent {
        label 'jnodes'
    }

    environment {
            VERSION = sh(script: 'git describe --tags --abbrev=0', returnStdout: true).trim()
        }

    stages {
        stage('Build') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Run') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Test') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Deply') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
