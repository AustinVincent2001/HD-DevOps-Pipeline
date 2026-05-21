pipeline {
    agent any

    stages {

        stage('Build') {
            steps {

                echo 'Installing project dependencies'

                bat '"C:\\Users\\Austin Vincent\\anaconda3\\envs\\devops-pipeline\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {

                echo 'Running automated tests'

                bat '"C:\\Users\\Austin Vincent\\anaconda3\\envs\\devops-pipeline\\python.exe" -m pytest'
            }
        }

        stage('Code Quality') {
            steps {

                echo 'Running pylint code analysis'

                bat '"C:\\Users\\Austin Vincent\\anaconda3\\envs\\devops-pipeline\\python.exe" -m pylint app.py || exit /b 0'
            }
        }

        stage('Security Scan') {
            steps {

                echo 'Running Bandit security scan'

                bat '"C:\\Users\\Austin Vincent\\anaconda3\\envs\\devops-pipeline\\python.exe" -m bandit -r . || exit /b 0'
            }
        }

        stage('Docker Build') {
            steps {

                echo 'Building Docker image'

                bat 'docker build -t flask-devops-app .'
            }
        }

        stage('Docker Deploy') {
            steps {

                echo 'Stopping old container if exists'

                bat 'docker stop flask-container || exit /b 0'

                bat 'docker rm flask-container || exit /b 0'

                echo 'Running new Docker container'

                bat 'docker run -d --name flask-container -p 5000:5000 flask-devops-app'
            }
        }
    }

    post {

        always {

            emailext(
                subject: "Jenkins Pipeline Status: ${currentBuild.currentResult}",
                body: """
Pipeline execution completed.

Project: HD-DevOps-Pipeline
Build Number: ${BUILD_NUMBER}
Status: ${currentBuild.currentResult}

Stages:
- Build
- Test
- Code Quality
- Security Scan
- Docker Build
- Docker Deploy
""",
                to: "ausbisacc@gmail.com"
            )
        }
    }
}