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

    post {
        success {
            emailext(
                subject: "✅ Python Date Report - Build #${BUILD_NUMBER} Successful",
                body: """
<h3>Build #${BUILD_NUMBER} - SUCCESS ✅</h3>
<p>Job: ${JOB_NAME}</p>
<p>Date: ${new Date()}</p>
<p>Report file attached below.</p>
<p>Check build logs at: <a href="${BUILD_URL}">${BUILD_URL}</a></p>
""",
                to: "mohamadassdi4@gmail.com",
                attachmentsPattern: "report.log",
                mimeType: 'text/html'
            )
        }

        failure {
            emailext(
                subject: "❌ Python Date Report - Build #${BUILD_NUMBER} Failed",
                body: """
<h3>Build #${BUILD_NUMBER} - FAILED ❌</h3>
<p>Job: ${JOB_NAME}</p>
<p>Check build logs at: <a href="${BUILD_URL}">${BUILD_URL}</a></p>
""",
                to: "mohamadassdi4@gmail.com",
                mimeType: 'text/html'
            )
        }
    }
}
