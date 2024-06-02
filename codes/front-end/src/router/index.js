import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Element/LoginView.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import( '../views/Element/RegisterView.vue')
  },
  {
    path: '/users',
    name: 'Users',
    component: () => import( '../views/Element/ShowTaskView.vue')
  }
]

const router = new VueRouter({
  mode: 'history', // 设置使用历史模式
  routes
})

export default router
