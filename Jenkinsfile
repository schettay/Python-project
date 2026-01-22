pipeline {
  agent any
	stages {
		stage('Test') {
     			steps{
				echo 'Welcome to our first program'
			}
		}
		stage('Addition') {
			steps { 
				sh '''
				python3 add.py
				'''
			}
		}  
	}
}

