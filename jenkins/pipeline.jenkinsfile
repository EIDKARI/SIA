pipeline {
    agent  {label 'slave_node1'}


    stages {
        stage('stage 1') {
            steps {
                // Get some code from a GitHub repository
                bat("""
                rmdir /s /q SIA
                git clone https://github.com/EIDKARI/SIA.git
                cd SIA
                call "run.bat"
                """)

            }

            post {
                success {
                   archiveArtifacts artifacts: 'SIA\\genfile\\jenkins_file.txt', fingerprint: true
                }
            }
        }
        stage('stage 2: when stage 1 is successfull') {
            steps {
            build job : 'keid-windows-batch-call-archive-manual-2nd-stage'
            }
        }
    }
}