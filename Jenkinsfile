pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
		    }
    stages {
        // stage('Pre') { 
        //     steps {
        //         sh 'ansible-playbook -v -i /home/jenkins/.jenkins/workspace/FlaskApp/inventory.yaml /home/jenkins/.jenkins/workspace/FlaskApp/playbook.yaml'
        //     }
        // }
        // stage('Test') { 
        //     steps {
        //         sh 'sudo pytest /home/jenkins/.jenkins/workspace/FlaskApp/'
        //     }
        // }
        stage('Building') {
            steps {
                sh 'sudo docker-compose build'
            }
        }
        stage('Deploying') {
            steps {
                sh '''
                    ssh -i /home/jenkins/.ssh/Estio-Training-NForester -o StrictHostKeyChecking=no jenkins@10.0.1.10
                    sudo su ubuntu
                    sudo touch /home/ubuntu/script.sh
                    cat <<EOT > /home/ubuntu/script.sh
                    #!/bin/bash

                    sudo docker-compose -f /home/ubuntu/APIPrimeAge/docker-compose.yaml up -d
                    EOT
                    sudo chown ubuntu /home/ubuntu/script.sh
                    sudo chmod 777 /home/ubuntu/script.sh
                    . /home/ubuntu/script.sh
                '''
            }
        }
    }
}
