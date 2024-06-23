import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Element/LoginView.vue')
  },
  {
    path: '/users',
    name: 'Users',
    component: () => import('../views/Element/ShowTaskView.vue'),
    meta: { requiresAuth: true } // 需要身份验证的路由

  }
];

const router = new VueRouter({
  mode: 'history', // 设置使用历史模式
  routes
});

// 添加全局导航守卫
router.beforeEach((to, from, next) => {
  console.log('Router beforeEach triggered');
  const loggedIn = !!sessionStorage.getItem('access_token'); // 确保返回布尔值并反转
  console.log(`User logged in: ${loggedIn}`);
  console.log(`Navigating from ${from.path} to ${to.path}`);
  console.log(`Requires auth: ${to.matched.some(record => record.meta.requiresAuth)}`);

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    next('/login'); // 如果未认证，重定向到登录页面
  } else {
    next(); // 否则，继续导航
  }
});





export default router;

