<template>
  <div class="container-all">
    <div class="container right-panel-active">
      <!-- 注册 -->
      <div class="container__form container--signup">
        <form @submit.prevent="registerUser" action="#" class="form" id="form1">
          <h2 class="form__title">注册</h2>
          <input type="text" placeholder="用户名" class="input" v-model="userData.username"
                 minlength="3" maxlength="15" pattern="[a-zA-Z0-9]+" @input="validateUsername('userData')" required/>
          <span v-if="registrationUsernameError" class="error-message">
            <i class="fas fa-exclamation-circle"></i>{{ registrationUsernameError }}
          </span>
          <input type="password" placeholder="密码" class="input" v-model="userData.password"
                 minlength="8" maxlength="20" pattern="(?=.*[a-zA-Z])(?=.*[0-9]).{8,20}" @input="validatePassword('userData')" required/>
          <span v-if="registrationPasswordError" class="error-message">{{ registrationPasswordError }}</span>
          <input type="password" placeholder="确认密码" class="input" v-model="confirmPassword" required/>
          <span v-if="passwordMismatchError" class="error-message">{{ passwordMismatchError }}</span>
          <input type="text" placeholder="昵称" class="input" v-model="userData.nickname" required/>
          <div class="form-group">
            <label for="gender">性别：</label>
            <select id="gender" v-model="userData.gender" required>
              <option value="男">男</option>
              <option value="女">女</option>
              <option value="保密">保密</option>
            </select>
          </div>
          <input type="text" placeholder="电话" class="input" v-model="userData.telephone" required/>
          <span v-if="showSuccessMessage" class="success-message">注册成功！</span>
          <button type="submit" class="btn">注册</button>
        </form>
      </div>

      <!-- 登录 -->
      <div id="app" class="container__form container--signin">
        <form action="#" class="form" id="form2" @submit.prevent="login">
          <h2 class="form__title">登录</h2>
          <input type="text" placeholder="用户名" class="input" v-model="username"
                 minlength="3" maxlength="15" pattern="[a-zA-Z0-9]+" @input="validateUsername('login')" required/>
          <span v-if="usernameError" class="error-message">
            <i class="fas fa-exclamation-circle"></i> {{ usernameError }}
          </span>
          <input type="password" placeholder="密码" class="input" v-model="password"
                 minlength="8" maxlength="20" pattern="(?=.*[a-zA-Z])(?=.*[0-9]).{8,20}" @input="validatePassword('login')" required/>
          <span v-if="passwordError" class="error-message">
            <i class="fas fa-exclamation-circle"></i>{{ passwordError }}
          </span>
          <button class="btn" type="submit">登录</button>
        </form>
      </div>

      <!-- 覆盖层 -->
      <div class="container__overlay">
        <div class="overlay">
          <div class="overlay__panel overlay--left">
            <button class="btn" id="signIn">登录</button>
          </div>
          <div class="overlay__panel overlay--right">
            <button class="btn" id="signUp">注册</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      usernameError: '',
      passwordError: '',
      registrationUsernameError: '',
      registrationPasswordError: '',
      passwordMismatchError: '',
      showSuccessMessage: false,
      userData: {
        username: '',
        password: '',
        nickname: '',
        gender: '',
        telephone: ''
      },
    };
  },
  mounted() {
    const signInBtn = document.getElementById("signIn");
    const signUpBtn = document.getElementById("signUp");
    const container = document.querySelector(".container");

    signInBtn.addEventListener("click", () => {
      container.classList.remove("right-panel-active");
    });

    signUpBtn.addEventListener("click", () => {
      container.classList.add("right-panel-active");
    });
  },
  methods: {

    validateUsername(form) {
      const usernamePattern = /^[a-zA-Z0-9]+$/;
      if (form === 'login') {
        if (this.username.length < 3 || this.username.length > 15 || !usernamePattern.test(this.username)) {
          this.usernameError = '用户名应为3到15个字符，只能包含字母和数字';
        } else {
          this.usernameError = '';
        }
      } else {
        if (this.userData.username.length < 3 || this.userData.username.length > 15 || !usernamePattern.test(this.userData.username)) {
          this.registrationUsernameError = '用户名应为3到15个字符，只能包含字母和数字';
        } else {
          this.registrationUsernameError = '';
        }
      }
    },
    validatePassword(form) {
      const passwordPattern = /^(?=.*[a-zA-Z])(?=.*[0-9]).{8,20}$/;
      if (form === 'login') {
        if (this.password.length < 8 || this.password.length > 20 || !passwordPattern.test(this.password)) {
          this.passwordError = '密码应为8到20个字符，必须包含至少一个字母和一个数字';
        } else {
          this.passwordError = '';
        }
      } else {
        if (this.userData.password.length < 8 || this.userData.password.length > 20 || !passwordPattern.test(this.userData.password)) {
          this.registrationPasswordError = '密码应为8到20个字符，必须包含至少一个字母和一个数字';
        } else {
          this.registrationPasswordError = '';
        }
      }
    },
    login() {
      this.validateUsername('login');
      this.validatePassword('login');

      if (this.usernameError || this.passwordError) {
        return;
      }

      const requestData = new URLSearchParams();
      requestData.append('username', this.username);
      requestData.append('password', this.password);

      axios.post('http://localhost:8000/tms/login', requestData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }).then(response => {
        console.log('Response data:', response.data); // 添加调试信息
        if (response.data.code === 200 && response.data.message === "登录成功") {
          const token = response.data.data.access_token;
          console.log("获取到的token是：" + token);
          sessionStorage.setItem('access_token', token);
          this.$router.push('/users'); // 登录成功后导航到受保护页面
        } else if (response.data.message === "用户名不存在") {
          /*alert('用户名输入不正确，请重新输入。');*/
          this.usernameError = '用户名输入不正确，请重新输入。';
        } else if (response.data.message === "用户密码错误") {
          /*alert('密码输入不正确，请重新输入。');*/
          this.passwordError = '密码输入不正确，请重新输入。';
        }
      }).catch(error => {
        console.error('Login request error:', error); // 添加错误处理
        alert('登录请求失败，请稍后重试。');
      });

    },
    validateConfirmPassword() {
      if (this.userData.password !== this.confirmPassword) {
        this.passwordMismatchError = '两次输入的密码不一致，请重新输入';
      } else {
        this.passwordMismatchError = '';
      }
    },
    registerUser() {
      this.validateUsername('register');
      this.validatePassword('register');
      this.validateConfirmPassword(); // 在注册方法中验证确认密码

      if (this.registrationUsernameError || this.registrationPasswordError) {
        return;
      }

      axios.post('http://localhost:8000/tms/register', this.userData)
          .then(response => {
            this.registrationResult = response.data.message;
            setTimeout(() => {
              this.showSuccessMessage = true;
            }, 1000);
          })
          .catch(error => {
            this.registrationResult = '注册失败：' + error.response.data.message;
          });
    }
  }
};
</script>

<style>
:root {
  /* 颜色 */
  --white: #e9e9e9;
  --gray: #333;
  --blue: #0367a6;
  --lightblue: #008997;

  /* 圆角 */
  --button-radius: 0.7rem;

  /* 尺寸 */
  --max-width: 758px;
  --max-height: 420px;

  font-size: 16px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
  Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.error-message {
  font-size: 0.8rem; /* 调整字体大小为 0.8rem，根据需要进行调整 */
  color: #ff0000; /* 设置警告符号和错误信息的颜色 */
}

.error-message i {
  margin-right: 5px; /* 调整警告符号与文本之间的间距，根据需要进行调整 */
}

.success-message {
  font-size: 12px;
  color: green;
  margin-top: 5px;
}

.container-all {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  height: 100vh; /* 使用视口高度撑开容器 */
  margin-top: -70px; /* 往上移动 50px，根据需要调整 */
}

.container.right-panel-active {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  background-color: var(--white);
  //background: url("https://res.cloudinary.com/dbhnlktrv/image/upload/v1599997626/background_oeuhe7.jpg");
  /* 决定背景图像的位置是在视口内固定，或者随着包含它的区块滚动。 */
  /* https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-attachment */
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  display: grid;
  //height: 100vh;
  place-items: center;
}

.form__title {
  font-weight: 300;
  margin: 0;
  margin-bottom: 1.25rem;
}

.link {
  color: var(--gray);
  font-size: 0.9rem;
  margin: 1.5rem 0;
  text-decoration: none;
}

.container {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  background-color: var(--white);
  border-radius: var(--button-radius);
  box-shadow: 0 0.9rem 1.7rem rgba(0, 0, 0, 0.25),
  0 0.7rem 0.7rem rgba(0, 0, 0, 0.22);
  height: var(--max-height);
  max-width: var(--max-width);
  overflow: hidden;
  position: relative;
  width: 100%;
}

.container__form {
  height: 100%;
  position: absolute;
  top: 0;
  transition: all 0.6s ease-in-out;
}

.container--signin {
  left: 0;
  width: 50%;
  z-index: 2;
}

.container.right-panel-active .container--signin {
  transform: translateX(100%);
}

.container--signup {
  left: 0;
  opacity: 0;
  width: 50%;
  z-index: 1;
}

.container.right-panel-active .container--signup {
  animation: show 0.6s;
  opacity: 1;
  transform: translateX(100%);
  z-index: 5;
}

.container__overlay {
  height: 100%;
  left: 50%;
  overflow: hidden;
  position: absolute;
  top: 0;
  transition: transform 0.6s ease-in-out;
  width: 50%;
  z-index: 100;
}

.container.right-panel-active .container__overlay {
  transform: translateX(-100%);
}

.overlay {
  background-color: var(--lightblue);
  background: url("https://res.cloudinary.com/dbhnlktrv/image/upload/v1599997626/background_oeuhe7.jpg");
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  left: -100%;
  position: relative;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
  width: 200%;
}

.container.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay__panel {
  align-items: center;
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: center;
  position: absolute;
  text-align: center;
  top: 0;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
  width: 50%;
}

.overlay--left {
  transform: translateX(-20%);
}

.container.right-panel-active .overlay--left {
  transform: translateX(0);
}

.overlay--right {
  right: 0;
  transform: translateX(0);
}

.container.right-panel-active .overlay--right {
  transform: translateX(20%);
}

.btn {
  background-color: var(--blue);
  background-image: linear-gradient(90deg, var(--blue) 0%, var(--lightblue) 74%);
  border-radius: 20px;
  border: 1px solid var(--blue);
  color: var(--white);
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.form > .btn {
  margin-top: 1.5rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}

.form {
  background-color: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 3rem;
  height: 100%;
  text-align: center;
}

#form2 {
  margin-top: -70px;
}

.input {
  background-color: #fff;
  border: none;
  padding: 0.6rem 0.9rem; /* 调整上下内边距为 0.6rem，左右保持 0.9rem */
  margin: 0.3rem 0; /* 调整上下外边距为 0.3rem，左右保持 0 */
  width: 100%;
  border-radius: 10px; /* 圆角设置 */
}

@keyframes show {
  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }
  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}
</style>
