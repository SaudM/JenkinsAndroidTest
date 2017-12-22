node{
        try {
            stage("build.clone"){
                checkout scmgit
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

             stage("send.email"){
                emailext body: '这是一个测试邮件', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'test', to: 'maxiaohong@hundun.cn'
            }


        } catch (error) {
            throw error
        }
    }