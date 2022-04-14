pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '''#!/bin/bash
                    
                    chmod +x dev-create-env-file.sh
                    ./dev-create-env-file.sh -v 3.9 -a 1.0.0 -p 8000
                    docker-compose -f docker-compose.dev.yml --env-file dev.env up -d
                    docker-compose -f docker-compose.dev.yml --env-file dev.env exec backend /bin/bash
                    chmod +x dev-bring-server-up.sh
                    ./dev-bring-server-up.sh
                    python manage.py test
                '''
            }
        }
    }
}
