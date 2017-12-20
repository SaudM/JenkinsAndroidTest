node{
        try {
            stage("build.clone"){
                checkout scm
            }
            stage("build.clean"){
                sh "./gradlew clean"
            }
            stage("build.debug"){
                sh "./gradlew assemble"
            }
            stage('file.save') {
                    archiveArtifacts artifacts: 'app/build/outputs/apk/debug/*.apk', fingerprint: true
            }

            stage("upload.file"){
                sh "./seafile_upload_plus.py"
            }
        } catch (error) {
            throw error
        }
    }