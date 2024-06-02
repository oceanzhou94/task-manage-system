<template>
  <!-- 登录界面 -->
  <div class="login-container">
    <span class="style-span" style="font-family:'华文彩云';font-weight:400;font-size:40px">任务管理系统</span>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">用户名</label>
        <input type="text" placeholder="请输入你的用户名" id="username" v-model="username" required />
        <span v-if="usernameError" class="error-message">{{ usernameError }}</span>
      </div>
      <div class="form-group">
        <label for="password">密码</label>
        <input type="password" placeholder="请输入你的密码" id="password" v-model="password" required />
        <span v-if="passwordError" class="error-message">{{ passwordError }}</span>
      </div>
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script>
// 在需要发送 HTTP 请求的组件中引入 Axios
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      usernameError: '',
      passwordError: ''
    };
  },
  methods: {
    login() {
      // 清空之前的错误消息
      this.usernameError = '';
      this.passwordError = '';

      // 构造登录请求的数据
      const requestData = new URLSearchParams();
      requestData.append('username', this.username);
      requestData.append('password', this.password);

      // 发送登录请求
      axios.post('http://192.168.184.1:8000/tms/login', requestData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
          .then(response => {
            // 登录成功，根据后端返回的数据执行相应的操作
            //console.log('Login successful:', response.data);

            // 判断后端返回的数据中的消息是否为 "登录成功"
            if (response.data.message === "登录成功") {
              // 假设后端返回的 token 在 response.data.token 中
              const token = response.data.token;

              // 保存 token 到 localStorage
              localStorage.setItem('userToken', token);

              // 导航到显示页面
              this.$router.push('/users');
            }else if(response.data.message === "用户名不存在"){
              // 使用 alert 提示用户名错误
                   alert('用户名输入不正确，请重新输入。');
            }else if(response.data.message === "用户密码错误") {
              //     // 使用 alert 提示密码错误
                   alert('密码输入不正确，请重新输入。');
                }
          })
          // .catch(error => {
            // 登录失败，处理错误情况
           // console.error('Login failed:', error);

            // 处理后端返回的错误信息
            // if (response && error.response.data) {
            //   console.log('错误返回数据:', error.response.data);
            //   if (error.response.data.message === "用户名不存在") {
            //     // 使用 alert 提示用户名错误
            //     alert('用户名输入不正确，请重新输入。');
            //   } else if (error.response.data.message === "用户密码错误") {
            //     // 使用 alert 提示密码错误
            //     alert('密码输入不正确，请重新输入。');
            //   }
            //
            // }
          //});
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

.error-message {
  color: red;
  font-size: 0.875rem;
  margin-top: 0.5rem;
}
</style>
