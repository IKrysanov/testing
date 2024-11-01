pipeline {
    agent {
        docker {
            image 'python:3.9' // используем образ с Python, можно заменить на необходимую версию
            args '-v /tmp:/tmp' // монтируем временную директорию для отчетов allure
        }
    }
    environment {
        PYTHONPATH = '.' // добавляем текущую директорию в PYTHONPATH
        ALLURE_RESULTS = '/tmp/allure-results' // директория для сохранения результатов allure
    }
    stages {
        stage('Install dependencies') {
            steps {
                script {
                    // Устанавливаем pytest и allure
                    sh 'pip install pytest allure-pytest'
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    // Создаем папку для результатов Allure, если она не существует
                    sh 'mkdir -p ${ALLURE_RESULTS}'

                    // Запускаем тесты с использованием pytest и сохраняем результаты allure
                    sh 'pytest your_test_file.py --alluredir=${ALLURE_RESULTS}'
                }
            }
        }
        stage('Allure Report') {
            steps {
                // Публикуем отчет Allure, если он установлен на Jenkins
                allure includeProperties: false, jdk: '', reportBuildPolicy: 'ALWAYS', results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }
    post {
        always {
            // Удаляем временные файлы после завершения работы
            cleanWs()
        }
    }
}
