import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import HomeView from '@/views/HomeView.vue'
import SystemUsersView from '@/views/SystemUsersView.vue'
import PendingUsersView from '@/views/PendingUsersView.vue'
const router=createRouter({history:createWebHistory(),routes:[{path:'/',redirect:'/home'},{path:'/login',component:LoginView,meta:{guest:true}},{path:'/register',component:RegisterView,meta:{guest:true}},{path:'/home',component:HomeView,meta:{auth:true}},{path:'/system/users',component:SystemUsersView,meta:{auth:true,admin:true}},{path:'/system/users/pending',component:PendingUsersView,meta:{auth:true,admin:true}},{path:'/:pathMatch(.*)*',redirect:'/home'}]})
router.beforeEach((to)=>{const auth=useAuthStore();if(to.meta.auth&&!auth.token)return'/login';if(to.meta.admin&&!auth.isAdmin)return auth.token?'/home':'/login';if(to.meta.guest&&auth.token)return'/home'})
export default router
