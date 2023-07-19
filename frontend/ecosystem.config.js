module.exports = {
    apps: [
      {
        name: 'pskovshevron',
        port: '3000',
        exec_mode: 'cluster',
        instances: 'max',
        script: './.output/server/index.mjs'
      }
    ]
  }