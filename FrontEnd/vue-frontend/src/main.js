import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import ElementUI from 'element-ui';
import axios from 'axios';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI).use(router);

Vue.config.productionTip = false
Vue.prototype.$axios = axios;
axios.defaults.baseURL = "http://10.33.0.134:5000/"

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
