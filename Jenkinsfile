pipeline {
    agent { docker { image 'ubuntu:20.04' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                echo "$PWD"
                sh '''#!/bin/bash
                    docker --version
                '''
                sh 'echo $PWD'
            }
        }
    }
}
