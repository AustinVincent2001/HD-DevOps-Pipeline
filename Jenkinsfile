pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Installing dependencies'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                bat 'pytest'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Running pylint code analysis'
                bat 'pylint app.py || exit /b 0'
            }
        }
    }
}