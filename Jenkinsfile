pipeline {
    agent any
    stages {
        stage('Build image') {
            steps {
                    script {
                        docker.build('python-web-tests', '-f Dockerfile .')
                    }
            }
        }
        stage('Create env') {
            steps {
                    script {
                        try {
                            docker.image('python-web-tests').inside {
                                sh "export URL_SERVICE=${URL_SERVICE}"
                            }
                        } catch (err) {
                            echo err.getMessage()
                        }
                    }
            }
        }
        stage('Run tests') {
            steps {
                    script {
                        try {
                            docker.image('python-web-tests').inside {
                                sh "pytest ${CMD_PARAMS}"
                            }
                        } catch (err) {
                            echo err.getMessage()
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
