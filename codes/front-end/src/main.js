import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import router from './router';
import axios from 'axios';

Vue.use(ElementUI);

Vue.config.productionTip = false;

//
//localStorage.setItem('access_token','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtaW1hIiwiZXhwIjoxNzE3NTc0MzQ1fQ.AUveZm50ocFsR-boQdgdmOQGDb5zvLp5nyj-8S2tyLU')

// 添加请求拦截器
axios.interceptors.request.use(config => {
  // 从 localStorage 获取 token
  const token = sessionStorage.getItem('access_token');
  console.log('Token:', token);  // 检查 token 是否存在
  if (token) {
    // 在请求头中添加 token，使用小写的 bearer
    config.headers.Authorization = `bearer ${token}`;
  }
  console.log('Request Headers:', config.headers);  // 检查请求头
  return config;
}, error => {
  // 对请求错误做些什么
  return Promise.reject(error);
});

Vue.prototype.axios = axios;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');

