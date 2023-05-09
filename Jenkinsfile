#!/usr/bin/env groovy

pipeline {
  agent { label 'executor-v2' }

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '30'))
  }

  triggers {
    cron(getDailyCronString())
  }

  stages {
    stage('Validate') {
      parallel {
        stage('Changelog') {
          steps { parseChangelog() }
        }
      }
    }
  }

  post {
    always {
      cleanupAndNotify(currentBuild.currentResult)
    }
  }
}
