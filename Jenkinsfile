pipeline {
  agent any
    stages {
    stage("Build image") {
        steps {
        catchError {
             script {
                  docker.build("python-web-tests", "-f Dockerfile .")
               }
          }
       }
    }
    stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
    stage('Reports') {
        steps {
           allure([
             includeProperties: false,
             jdk: '',
             properties: [],
             reportBuildPolicy: 'ALWAYS',
             results: [[path: 'report']]
           ])
              }
         }
    }
}
