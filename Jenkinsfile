pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'maven-img'
        DOCKER_TAG = 'v1'
	DOCKER_VOLUME = 'my-vol'
	DOCKER_CONTAINER = 'my-maven-app'
    }

    tools {
        maven "Maven_Version"
    }

    stages {
        stage('Build') { 
	   steps {
		script {
                    // Build the Docker image from the Dockerfile
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                 }
           }
        }

	stage('Making Volume') {
	   steps {
		script {
		   sh "docker volume create ${DOCKER_VOLUME}"	
		}
	   }	
	}

	stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container with the specified volume
                    sh "docker run --name ${CONTAINER_NAME} -d -p 8080:8080 -v ${DOCKER_VOLUME}:/app/target ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up Docker container after the job finishes
                sh "docker rm -f ${CONTAINER_NAME} || true"
                // Optionally, clean up Docker volume
                sh "docker volume rm ${DOCKER_VOLUME} || true"
            }
        }
    }
}

