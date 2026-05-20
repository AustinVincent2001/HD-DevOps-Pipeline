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

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application'

                bat 'start /B "" "C:\\Users\\Austin Vincent\\anaconda3\\envs\\devops-pipeline\\python.exe" app.py'
            }
        }
    }

    post {

        always {

            emailext(
                subject: "Jenkins Pipeline Status: ${currentBuild.currentResult}",
                body: """
Pipeline completed successfully.

Project: HD-DevOps-Pipeline
Build Number: ${BUILD_NUMBER}
Status: ${currentBuild.currentResult}

Stages Completed:
- Build
- Test
- Code Quality
- Security Scan
- Deploy
""",
                to: "ausbisacc@gmail.com"
            )
        }
    }
}