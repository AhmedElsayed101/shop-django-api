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
    agent { docker { image 'maven:3.8.4-openjdk-11-slim' } }
    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
    }
}
