import Vue from 'vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import App from './App.vue'
import router from './router'

Vue.use(ElementUI);


Vue.config.productionTip = false

//路由配置
import axios from 'axios';

// 添加请求拦截器
axios.interceptors.request.use(config => {
  // 从 localStorage 获取 token
  const token = localStorage.getItem('userToken');
  if (token) {
    // 在请求头中添加 token
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  // 对请求错误做些什么
  return Promise.reject(error);
});

Vue.prototype.axios = axios;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
