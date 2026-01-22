pipeline {
  agent any
  stages {
    stage('Test') {
      echo 'welcome to our first sample program'
    }
    stage('Addition')
    {
      sh '''
      chmod +x add.py
      ./add.py
      '''
    }
  }
}
