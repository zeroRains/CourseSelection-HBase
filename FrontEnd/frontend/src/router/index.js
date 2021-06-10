import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/home'
  },
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },{
    path:'/home',
    name:'Home',
    component:()=>import("../views/Home/Home.vue"),
    children:[
      {
        path:'/person',
        name:'person',
        component:()=>import("../views/Home/Person/Info.vue"),
      },{
        path: '/person/change',
        name: 'change',
        component: () => import('../views/Home/Person/Change.vue')
      },
      {
        path: '/person/info',
        name: 'info',
        component: () => import('../views/Home/Person/Info.vue')
      },
      {
        path: '/person/score',
        name: 'score',
        component: () => import('../views/Home/Person/Score.vue')
      },
      {
        path:'/course',
        name:'course',
        component:()=>import("../views/Home/Course/Choose.vue"),
      },
      {
        path: '/course/choose',
        name: 'choose',
        component: () => import('../views/Home/Course/Choose.vue')
      },
      {
        path: '/course/check',
        name: 'check',
        component: () => import('../views/Home/Course/Check.vue')
      },
      {
        path: '/course/close',
        name: 'close',
        component: () => import('../views/Home/Course/Close.vue')
      },
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
