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
				a=1
				b=2
                                echo $((a+b))
				'''
			}
		}  
	}
}

