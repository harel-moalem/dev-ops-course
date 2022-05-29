properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone")
    {
        git "https://github.com/harel-moalem/dev-ops-course.git"
    }
    stage("show files")
    {
        bat "dir"
    }
}
