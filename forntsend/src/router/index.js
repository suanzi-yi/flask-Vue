/*
 * @Descripttion: 
 * @version: 1.0
 * @Author: suanzi
 * @Date: 2022-03-12 08:42:33
 * @LastEditors: suanzi
 * @LastEditTime: 2022-05-02 16:19:06
 * @FilePath: \forntsend\src\router\index.js
 */
import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Home from '@/components/Home'
import Register from '@/components/Register'
import Comment from '@/components/Comment'
import TestMidway from '@/components/TestMidway'
Vue.use(Router)

const router=new Router({
  routes: [
    {
      path:'/TestMidway',
      name: 'midway',
      component:TestMidway
    },
    {
      path: '/',
      redirect:'/login',
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path:'/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/comment',
      name: 'Comment',
      component: Comment
    }
  ]
})

// // 挂载路由导航守卫
// router.beforeEach((to, from, next) => {
//   // to 将要访问的路径
//   // from 代表从哪个路径跳转而来
//   // next 是一个函数，表示放行
//   //     next()  放行    next('/login')  强制跳转

//   if (to.path === '/login') return next()
//   if (to.path === '/register') return next()
//   // 获取user
//   const name = window.sessionStorage.getItem('name')
//   if (!name) return next('/login')
//   next()
// })


export default router