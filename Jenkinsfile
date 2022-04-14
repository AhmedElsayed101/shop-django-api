// pipeline {
//   agent any
//   stages {
//     stage('build') {
//       steps {
//         sh '''echo "hello world"
// '''
//               sh '''echo $PWD
// '''
//               sh '''ls -la
// '''
//       }
//     }

//   }
// }
pipeline {
    agent { docker { image 'python:3.9' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                bash 'python --version'
                echo '$PWD'
                bash 'echo $PWD'
            }
        }
    }
}
