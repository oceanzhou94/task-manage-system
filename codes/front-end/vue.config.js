const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    host: 'localhost', // 更改为你想要的域名
    port: 8000, // 你想要的端口
    proxy: {
      '/api': {
        target: 'http://192.168.184.1:8000', // 后端服务器地址
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/tms/task/list'
        }
      }
    }
  }
})
