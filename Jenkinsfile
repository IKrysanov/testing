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
        environment {
            ALLURE_RESULTS_DIR = '/tmp/allure-results' // Общая директория для allure-results
        }
        stage('Run tests') {
            steps {
                catchError {
                    script {
                            sh 'mkdir -p ${ALLURE_RESULTS_DIR}'
                            docker.image('python-web-tests') { c ->
                                sh "pytest -v -s ${CMD_PARAMS} --alluredir=${ALLURE_RESULTS_DIR}"
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
