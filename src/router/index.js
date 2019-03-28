import Vue from 'vue'
import Router from 'vue-router'

import Auth from '../components/pages/Auth'
import Movies from '../components/pages/Movies'

Vue.use(Router)

export default new Router({
    base: '/',
    mode: 'history',
    // 设置history就ok,具体history相关知识请查看路由实现原理
    routes: [{
            path: '/movies',
            name: 'Movies',
            component: Movies
        },
        {
            path: '/auth',
            name: 'Auth',
            component: Auth
        }
    ]
})