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
      chmod +x add.py
      python3 add.py
    }
    }
  }
}
