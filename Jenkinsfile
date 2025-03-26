pipeline {
    // The Basic Calculator projects requires Python 3.10. 
    // Using a docker image from docker hub (https://hub.docker.com/)
    agent { 
        docker { 
            image 'python:3.10.13-bullseye' 
            args '-u 0'
        }
    }

    // Your pipeline steps
    stages {
        // Step 1. Clone code from Github using the Git/Github Plugin
        // stage('Clone Project') {
        //     steps {
        //         git branch: 'main', url: 'https://github.com/nih4me/Basic-Calculator.git'
        //     }
        // }
        
        // Step 2. Install dependencies listed in the requirements.txt file
        // Pip is already installed in the the python image 
        stage('Install Dependancies') {
            steps {
                sh 'pip install --user -r requirements.txt'
            }
        }

        // Step 3. Code Quality
        stage('Code Quality') {
            steps {
                sh 'python -m flake8 . --count --select E --show-source --statistics'
            }
        }
        
        // Step 4. Run Tests using pytest
        stage('Testing') {
            steps {
                sh 'python -m pytest test.py'
            }
        }
    }
}
