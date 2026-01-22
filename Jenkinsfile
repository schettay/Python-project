
pipeline {
    agent any

    parameters {
        string(name: 'A', defaultValue: '10', description: 'First number')
        string(name: 'B', defaultValue: '20', description: 'Second number')
    }

    stages {
        stage('Addition') {
            steps {
                script {
                    def sum = params.A.toInteger() + params.B.toInteger()
                    echo "Sum = ${sum}"
                }
            }
        }
    }
}

