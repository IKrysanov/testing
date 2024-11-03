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
        stage('Run tests') {
            steps {
                    script {
                        try {
                            docker.image('python-web-tests').inside {
                                sh "allure generate --clean --output result"
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
