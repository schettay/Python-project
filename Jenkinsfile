pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'welcome to our first sample program'
      }
    }

    stage('Addition') {
      steps {
        // Ensure Unix line endings (safe if none), then run the script
        sh '''
          set -e
          sed -i 's/\r$//' add.py      # remove CRLF if the file came from Windows
          chmod +x add.py              # make it executable
          ./add.py                     # or: python3 add.py
        '''
      }
    }
  }
}

