pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
      echo 'welcome to our first sample program'
      }
    }
    stage('Addition')
    {
      steps {
      sh '''
      chmod +x add.py
      ./add.py
      '''
    }
    }
  }
}
