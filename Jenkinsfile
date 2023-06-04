pipeline {
    agent any
    environment { 
        VERSION = "${env.BUILD_ID}"
    }

    stages {
        stage ('Delete docker volumes'){
          steps {
              sh 'docker system prune -a --volumes -f'
          }
        }

        stage('Build docker image') {
            steps {
                sh 'docker build -t medamine77/frontend-react-js:${VERSION} ./frontend-react-js/'
                sh 'docker build -t medamine77/backend-flask:${VERSION} ./backend-flask/'
            }
        }
        
        stage('Push image to dockerhub') {
            steps {            
                sh 'docker image push medamine77/frontend-react-js:${VERSION}'
                sh 'docker image push medamine77/backend-flask:${VERSION}'
            }
        }
        
        stage('Deploy to Kubernetes with ansible') {
            steps {
                ansiblePlaybook extras: '--extra-vars "tag=${VERSION}" -vvvv', installation: 'ansible', inventory: 'inventory.yaml', playbook: 'ansible-playbook-fullstack.yaml'
            }
        }
    
    post {
        always {
            script {
                def status = currentBuild.currentResult.toString()
                slackSend channel: '#jenkins',
                          color: status == 'SUCCESS' ? 'good' : 'danger',
                          message: "Build <${env.BUILD_URL}|#${env.BUILD_NUMBER}> has finished with status *${status}*"
            }
        }
}
}
