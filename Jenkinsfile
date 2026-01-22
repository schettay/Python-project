pipeline {
  agent any

  parameters {
    string(name: 'NUM1', defaultValue: '10', description: 'First number')
    string(name: 'NUM2', defaultValue: '20', description: 'Second number')
  }

  stages {
    stage('Prepare') {
      steps {
        // Ensure the script has correct line endings and is executable
        writeFile file: 'add.py', text: '''
#!/usr/bin/env python3
import sys
from decimal import Decimal
def add(a, b):
    return Decimal(a) + Decimal(b)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: add.py <num1> <num2>", file=sys.stderr)
        sys.exit(1)
    try:
        result = add(sys.argv[1], sys.argv[2])
        print(result)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
'''.strip()    // optional: you can commit add.py instead of writing it here

        sh '''
          set -e
          # normalize CRLF if file came from Windows (safe if not present)
          perl -pi -e 's/\\r$//' add.py
          chmod +x add.py
        '''
      }
    }

    stage('Call Python') {
      steps {
        script {
          // Run Python and capture stdout as the sum
          def sumOut = sh(
            script: "python3 add.py '${params.NUM1}' '${params.NUM2}'",
            returnStdout: true
          ).trim()

          echo "Sum = ${sumOut}"
          currentBuild.displayName = "#${env.BUILD_NUMBER} • Sum=${sumOut}"
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'add.py', onlyIfSuccessful: false
    }
  }
}

