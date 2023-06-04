pipeline {
    agent any

    stages {
        stage('Clone git') {
            steps {
                git branch: 'main', url: 'https://github.com/R24Amine/aws-bootcamp-cruddur-2023'
                
            }
        }
        
        stage ('Delete docker volumes'){
          steps  {
            sh 'docker system prune -a --volumes -f'
          }
        }

        stage ('npm package'){
          steps  {
            sh 'cd frontend-react-js'
            sh 'npm i'
          }
        }
        
        stage('Start containers') {
          steps {
            sh 'docker-compose up -d'
            sh 'docker-compose ps'
          }
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
