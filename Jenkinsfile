pipeline {
    agent any
    triggers {
        // تشغيل كل 5 دقائق
        cron('H/5 * * * *')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t python-date-report .'
            }
        }

        stage('Run in Docker') {
            steps {
                bat 'docker run --rm -v %cd%:/app python-date-report'
            }
        }

        stage('Show Report') {
            steps {
                bat 'type report.log'
            }
        }
    }
}
