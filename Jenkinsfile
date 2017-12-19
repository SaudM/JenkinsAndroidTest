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
            stage("build.Release"){
                sh "./gradlew assembleRelease"
            }
            stage('file.save') {
                    archiveArtifacts artifacts: 'app/build/outputs/apk/debug/*.apk', fingerprint: true
            }
        } catch (error) {

            throw error
        }
    }