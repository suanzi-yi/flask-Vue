/*
 * @Descripttion: 
 * @version: 1.0
 * @Author: suanzi
 * @Date: 2022-03-12 08:42:33
 * @LastEditors: suanzi
 * @LastEditTime: 2022-05-02 15:56:22
 * @FilePath: \forntsend\src\main.js
 */
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import './assets/css/global.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Moment from 'moment'

Vue.prototype.moment  =  Moment
Vue.config.productionTip = false
Vue.use(ElementUI)

import axios from 'axios'
// 配置请求的跟路径
// axios.defaults.baseURL = 'http://114.115.211.196:80/v1/sql/'
Vue.prototype.$http = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  // components: { App },
  // template: '<App/>'
  render:h=>h(App)
})
