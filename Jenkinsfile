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
        } catch (error) {

            throw error
        }
    }
