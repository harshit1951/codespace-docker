pipeline {
    agent any

    tools {
        maven "Maven_Version"
    }

    stages {
	stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }	    
    }

    post {
	always {
	    archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
        }
    }
}

