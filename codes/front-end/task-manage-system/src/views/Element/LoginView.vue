<template>

    <!-- 登录界面 -->
    <div class="login-container">
        <span calss="style-span" style="font-family:'华文彩云';font-weight:400;font-size:40px"> 任务管理系统</span>
        <form @submit.prevent="login">
          <div class="form-group">
            <label for="username">用户名</label>
            <input type="text" placeholder="请输入你的用户名" id="username" v-model="username" required />
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" placeholder="请输入你的密码" id="password" v-model="password" required />
          </div>
          <button type="submit">登录</button>
        </form>

      </div>

</template>

<script>
// 在需要发送 HTTP 请求的组件中引入 Axios
import axios from 'axios';
export default {
    /* 登陆界面 */
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // 构造登录请求的数据
      const requestData = {
        username: this.username,
        password: this.password
      };

      // 发送登录请求
      axios.post('/login', requestData)
        .then(response => {
          // 登录成功，根据后端返回的数据执行相应的操作
          console.log('Login successful:', response.data);

          // 导航到显示页面
          this.$router.push('/users');
        })

        .catch(error => {
          // 登录失败，处理错误情况
          console.error('Login failed:', error);

          // 导航到显示页面
          this.$router.push('/users');
        });
    }
  }
};

</script>

<style>


.login-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 3rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 0.5rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

</style>