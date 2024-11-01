pipeline {
    agent any
    stages {
        stage('Build image') {
            steps {
                catchError {
                    script {
                        docker.build('python-web-tests', '-f Dockerfile .')
                    }
                }
            }
        }
        agent {
            docker {
                args '-v /var/lib/jenkins/workspace/Testing/allure-results:/allure-results'
            }
        }
        stage('Run tests') {
            steps {
                catchError {
                    script {
                            docker.image('python-web-tests') {
                                sh "pytest ${CMD_PARAMS}"
                            }
                    }
                }
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
