#!/usr/bin/env groovy

pipeline {
  agent { label 'conjur-enterprise-common-agent' }

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '30'))
  }

  triggers {
    cron(getDailyCronString())
  }

  stages {
    stage('Get InfraPool Agent') {
      steps {
        script {
          INFRAPOOL_EXECUTORV2_AGENT_0 = getInfraPoolAgent.connected(type: "ExecutorV2", quantity: 1, duration: 1)[0]
        }
      }
    }
    stage('Validate') {
      parallel {
        stage('Changelog') {
          steps { parseChangelog(INFRAPOOL_EXECUTORV2_AGENT_0) }
        }
      }
    }
  }

  post {
    always {
      releaseInfraPoolAgent(".infrapool/release_agents")
    }
  }
}
