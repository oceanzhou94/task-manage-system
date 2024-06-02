<template>
  <div class="registration-container">
    <h2 class="registration-title">用户注册</h2>
    <form @submit.prevent="registerUser" class="registration-form">
      <div class="form-group">
        <label for="username">用户名：</label>
        <input type="text" id="username" v-model="userData.username" required>
      </div>
      <div class="form-group">
        <label for="password">密码：</label>
        <input type="password" id="password" v-model="userData.password" required>
      </div>
      <div class="form-group">
        <label for="nickname">昵称：</label>
        <input type="text" id="nickname" v-model="userData.nickname" required>
      </div>
      <div class="form-group">
        <label for="gender">性别：</label>
        <select id="gender" v-model="userData.gender" required>
          <option value="男">男</option>
          <option value="女">女</option>
          <option value="保密">保密</option>
        </select>
      </div>
      <div class="form-group">
        <label for="telephone">电话：</label>
        <input type="text" id="telephone" v-model="userData.telephone" required>
      </div>
      <button type="submit" class="registration-button">注册</button>
    </form>
    <div v-if="registrationResult" class="registration-result">
      <p>{{ registrationResult }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userData: {
        username: '',
        password: '',
        nickname: '',
        gender: '',
        telephone: ''
      },
      registrationResult: ''
    };
  },
  methods: {
    registerUser() {
      axios.post('http://192.168.184.1:8000/tms/register', this.userData)
          .then(response => {
            this.registrationResult = response.data.message;
          })
          .catch(error => {
            this.registrationResult = '注册失败：' + error.response.data.message;
          });
    }
  }
};
</script>

<style scoped>
.registration-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.registration-title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
}

.registration-form .form-group {
  margin-right: 12px;
  margin-bottom: 15px;
}

.registration-form label {
  display: block;
  font-weight: bold;
}

.registration-form input[type="text"],
.registration-form input[type="password"],
.registration-form select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.registration-form button.registration-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.registration-form button.registration-button:hover {
  background-color: #0056b3;
}

.registration-result {
  margin-top: 20px;
  text-align: center;
  font-weight: bold;
}
</style>
