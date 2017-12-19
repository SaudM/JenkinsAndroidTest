node{
        try {
            stage("build.clone"){
                checkout scm
            }
            stage("build.clean"){
                sh "./gradlew clean"
            }
            stage("build.debug"){
                sh "./gradlew assembleDebug"
            }
            stage('file.save') {
                    archiveArtifacts artifacts: 'app/build/outputs/apk/debug/*.apk', fingerprint: true
            }

            stage("upload.file"){

                sh "./seafile_upload_plus.py fe10fc73-c32c-43d8-9ea0-364dd175a7cf $WORKSPACE/app/build/outputs/apk/debug/$(find $WORKSPACE/app/build/outputs/apk/ -name 'app*')"
            }
        } catch (error) {
            throw error
        }
    }