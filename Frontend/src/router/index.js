/* jshint esversion: 6 */
/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/* Router Modules */
import componentsRouter from './modules/components'
import chartsRouter from './modules/charts'
import tableRouter from './modules/table'
import nestedRouter from './modules/nested'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [{
        path: '/redirect',
        component: Layout,
        hidden: true,
        children: [{
            path: '/redirect/:path*',
            component: () =>
                import ('@/views/redirect/index')
        }]
    },
    {
        path: '/login',
        component: () =>
            import ('@/views/login/index'),
        hidden: true
    },
    {
        path: '/auth-redirect',
        component: () =>
            import ('@/views/login/auth-redirect'),
        hidden: true
    },
    {
        path: '/404',
        component: () =>
            import ('@/views/error-page/404'),
        hidden: true
    },
    {
        path: '/401',
        component: () =>
            import ('@/views/error-page/401'),
        hidden: true
    },
    {
        path: '/',
        component: Layout,
        redirect: '/dashboard',
        children: [{
            path: 'dashboard',
            component: () =>
                import ('@/views/dashboard/index'),
            name: 'Dashboard',
            meta: { title: 'Principal', icon: 'component', noCache: true }
        }]
    },

    // {
    //   path: '/prueba1',
    //   component: () => import('@/views/documentation/index'),
    //   name: 'Juan camilo',
    //   meta: { title: 'Prueba1', icon: 'documentation', noCache: true }
    // },
    // {
    //   path: '/prueba2',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'vista_prueba_2',
    //       component: () => import('@/views/dashboard/default/index'),
    //       name: 'prueba2',
    //       meta: { title: 'Prueba2', icon: 'dashboard', noCache: true }
    //     }
    //   ]
    // },
    // {
    //   path: '/prueba3',
    //   component: Layout,
    //   meta: { title: 'Prueba Sub Menus', icon: 'dashboard', affix: true },
    //   children: [
    //     {
    //       path: 'vista_prueba_3_hijo1',
    //       component: () => import('@/views/dashboard/index'),
    //       name: 'hijo1',
    //       meta: { title: 'hijo1', icon: 'dashboard', affix: true }
    //     },
    //     {
    //       path: 'vista_prueba_3_hijo2',
    //       component: () => import('@/views/documentation/index'),
    //       name: 'hijo2',
    //       meta: { title: 'hijo2', icon: 'dashboard', affix: true }
    //     }
    //   ]
    // },

    // {
    //   path: '/documentation',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/documentation/index'),
    //       name: 'Documentation',
    //       meta: { title: 'Documentation', icon: 'documentation', affix: true }
    //     }
    //   ]
    // },
    // {
    //   path: '/guide',
    //   component: Layout,
    //   redirect: '/guide/index',
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/guide/index'),
    //       name: 'Guide',
    //       meta: { title: 'Guide', icon: 'guide', noCache: true }
    //     }
    //   ]
    // },
    // {
    //   path: '/profile',
    //   component: Layout,
    //   redirect: '/profile/index',
    //   hidden: true,
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/profile/index'),
    //       name: 'Profile',
    //       meta: { title: 'Profile', icon: 'user', noCache: true }
    //     }
    //   ]
    // }
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [{
        path: '/permission',
        component: Layout,
        redirect: '/permission/role',
        alwaysShow: true, // will always show the root menu
        name: 'Permission',
        meta: {
            title: 'Permisos',
            icon: 'lock',
            roles: ['admin', 'editor'] // you can set roles in root nav
        },
        children: [
            // {
            //   path: 'page',
            //   component: () => import('@/views/permission/page'),
            //   name: 'PagePermission',
            //   meta: {
            //     title: 'Page Permission',
            //     roles: ['admin', 'juan', 'editor'] // or you can only set roles in sub nav
            //   }
            // },
            // {
            //   path: 'directive',
            //   component: () => import('@/views/permission/directive'),
            //   name: 'DirectivePermission',
            //   meta: {
            //     title: 'Directive Permission'
            //     // if do not set roles, means: this page does not require permission
            //   }
            // },
            {
                path: 'role',
                component: () =>
                    import ('@/views/permission/role'),
                name: 'RolePermission',
                meta: {
                    title: 'Roles',
                    roles: ['admin', 'editor']
                }
            }
        ]
    },
    // vistas gestor de datos
    {
        path: '/tolerancia',
        component: Layout,
        children: [{
            path: 'nivel-tolerancia',
            component: () =>
                import ('@/views/roles'),
            name: 'nivel-tolerancia',
            meta: { title: 'nivelTolerancia', icon: 'size', noCache: true, roles: ['gestor'] }
        }]
    },
    {
        path: '/indices',
        component: Layout,
        children: [{
            path: 'indices-dane',
            component: () =>
                import ('@/views/roles'),
            name: 'indices-dane',
            meta: { title: 'Índices DANE', icon: 'chart', noCache: true, roles: ['gestor'] }
        }]
    },
    {
        path: '/comercial',
        component: Layout,
        children: [{
            path: 'Info-comercial',
            component: () =>
                import ('@/views/roles'),
            name: 'Info-comercial',
            meta: { title: 'Información Comercial', icon: 'clipboard', noCache: false, roles: ['gestor'] }
        }]
    },
    {
        path: '/D097',
        component: Layout,
        redirect: '#', // cuando se seleccione esta opcion en la ruta se redirecciona a la vista principal
        name: 'D097',
        meta: { title: 'InformaciónD097', icon: 'clipboard', roles: ['gestor'] },
        children: [{
            path: 'modificar',
            component: () =>
                import ('@/views/roles'), // Parent router-view
            name: 'modificar',
            meta: { title: 'Modificar', icon: 'edit', roles: ['gestor'] },
            redirect: '#',
            children: [{
                    path: 'resolucion',
                    component: () =>
                        import ('@/views/roles'),
                    name: 'resolucion',
                    meta: { title: 'Resolución', icon: 'form', roles: ['gestor'] }
                },
                {
                    path: 'error',
                    component: () =>
                        import ('@/views/roles'),
                    name: 'error',
                    meta: { title: 'Error', icon: 'bug', roles: ['gestor'] }
                }
            ]
        }]
    },
    {
        path: '/perdidas',
        component: Layout,
        children: [{
            path: 'perdidas-stn',
            component: () =>
                import ('@/views/roles'),
            name: 'perdidas-stn',
            meta: { title: 'Pérdidas STN', icon: 'example', noCache: true, roles: ['gestor'] }
        }]
    },
    {
        path: '/infoADD',
        component: Layout,
        children: [{
            path: 'info-ADD',
            component: () =>
                import ('@/views/roles'),
            name: 'info-ADD',
            meta: { title: 'Información ADD', icon: 'clipboard', noCache: true, roles: ['gestor'] }
        }]
    },
    // vistas revisor
    {
        path: '/verificacion',
        component: Layout,
        // redirect: 'noRedirect',
        redirect: '#',
        name: 'verificacion',
        meta: {
            title: 'Verificación CU',
            icon: 'edit',
            roles: ['revisor']
        },
        children: [{
                path: 'costo-unitario',
                component: () =>
                    import ('@/views/roles'),
                name: 'costo-unitario',
                meta: { title: 'Costo Unitario', icon: 'example', noCache: true, roles: ['revisor'] }
            },
            // {
            //     path: 'componentes',
            //     component: () =>
            //         import ('@/views/roles'), // Parent router-view
            //     name: 'componentes',
            //     meta: { title: 'Componentes', icon: 'nested', roles: ['revisor'] },
            //     redirect: '#',
            //     children: [{
            //             path: 'd097',
            //             component: () =>
            //                 import ('@/views/roles'),
            //             name: 'd097',
            //             meta: { title: 'D - CREG 097', icon: 'clipboard', roles: ['revisor'] }
            //         },
            //         {
            //             path: 'd015',
            //             component: () =>
            //                 import ('@/views/roles'),
            //             name: 'd015',
            //             meta: { title: 'D - CREG 015', icon: 'clipboard', roles: ['revisor'] }
            //         }
            //     ]
            // }
        ]
    },
    {
        path: '/verificar-tarifas',
        component: Layout,
        children: [{
            path: 'tarifas',
            component: () =>
                import ('@/views/roles'),
            name: 'tarifas',
            meta: { title: 'Verificación Tarifas', icon: 'edit', noCache: true, roles: ['revisor'] }
        }]
    },
    {
        path: '/analisis-sensibilidad',
        component: Layout,
        children: [{
            path: 'sensibilidad',
            component: () =>
                import ('@/views/roles'),
            name: 'sensibilidad',
            meta: { title: 'Análisis de sensibilidad', icon: 'skill', noCache: true, roles: ['revisor'] }
        }]
    },
    {
        path: '/historico-verificaciones',
        component: Layout,
        children: [{
            path: 'verificaciones',
            component: () =>
                import ('@/views/roles'),
            name: 'verificaciones',
            meta: { title: 'Histórico Verificaciones', icon: 'tree-table', noCache: true, roles: ['admin', 'revisor', 'aprobador'] }
        }]
    },
    {
        path: '/reportes-revisor',
        component: Layout,
        children: [{
            path: 'reportes',
            component: () =>
                import ('@/views/roles'),
            name: 'reportes',
            meta: { title: 'Reportes', icon: 'form', noCache: true, roles: ['revisor', 'aprobador'] }
        }]
    },

    // {
    //   path: '/icon',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/icons/index'),
    //       name: 'Icons',
    //       meta: { title: 'Icons', icon: 'icon', noCache: true }
    //     }
    //   ]
    // },

    // /** when your routing map is too long, you can split it into small modules **/
    // componentsRouter,
    // chartsRouter,
    // nestedRouter,
    // tableRouter,

    // {
    //   path: '/example',
    //   component: Layout,
    //   redirect: '/example/list',
    //   name: 'Example',
    //   meta: {
    //     title: 'Example',
    //     icon: 'example'
    //   },
    //   children: [
    //     {
    //       path: 'create',
    //       component: () => import('@/views/example/create'),
    //       name: 'CreateArticle',
    //       meta: { title: 'Create Article', icon: 'edit' }
    //     },
    //     {
    //       path: 'edit/:id(\\d+)',
    //       component: () => import('@/views/example/edit'),
    //       name: 'EditArticle',
    //       meta: { title: 'Edit Article', noCache: true, activeMenu: '/example/list' },
    //       hidden: false
    //     },
    //     {
    //       path: 'list',
    //       component: () => import('@/views/example/list'),
    //       name: 'ArticleList',
    //       meta: { title: 'Article List', icon: 'list' }
    //     }
    //   ]
    // },

    // {
    //   path: '/tab',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/tab/index'),
    //       name: 'Tab',
    //       meta: { title: 'Tab', icon: 'tab' }
    //     }
    //   ]
    // },

    // {
    //   path: '/error',
    //   component: Layout,
    //   redirect: 'noRedirect',
    //   name: 'ErrorPages',
    //   meta: {
    //     title: 'Error Pages',
    //     icon: '404'
    //   },
    //   children: [
    //     {
    //       path: '401',
    //       component: () => import('@/views/error-page/401'),
    //       name: 'Page401',
    //       meta: { title: '401', noCache: true }
    //     },
    //     {
    //       path: '404',
    //       component: () => import('@/views/error-page/404'),
    //       name: 'Page404',
    //       meta: { title: '404', noCache: true }
    //     }
    //   ]
    // },

    // {
    //   path: '/error-log',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'log',
    //       component: () => import('@/views/error-log/index'),
    //       name: 'ErrorLog',
    //       meta: { title: 'Error Log', icon: 'bug' }
    //     }
    //   ]
    // },

    // {
    //   path: '/excel',
    //   component: Layout,
    //   redirect: '/excel/export-excel',
    //   name: 'Excel',
    //   meta: {
    //     title: 'Excel',
    //     icon: 'excel'
    //   },
    //   children: [
    //     {
    //       path: 'export-excel',
    //       component: () => import('@/views/excel/export-excel'),
    //       name: 'ExportExcel',
    //       meta: { title: 'Export Excel' }
    //     },
    //     {
    //       path: 'export-selected-excel',
    //       component: () => import('@/views/excel/select-excel'),
    //       name: 'SelectExcel',
    //       meta: { title: 'Export Selected' }
    //     },
    //     {
    //       path: 'export-merge-header',
    //       component: () => import('@/views/excel/merge-header'),
    //       name: 'MergeHeader',
    //       meta: { title: 'Merge Header' }
    //     },
    //     {
    //       path: 'upload-excel',
    //       component: () => import('@/views/excel/upload-excel'),
    //       name: 'UploadExcel',
    //       meta: { title: 'Upload Excel' }
    //     }
    //   ]
    // },

    // {
    //   path: '/zip',
    //   component: Layout,
    //   redirect: '/zip/download',
    //   alwaysShow: true,
    //   name: 'Zip',
    //   meta: { title: 'Zip', icon: 'zip' },
    //   children: [
    //     {
    //       path: 'download',
    //       component: () => import('@/views/zip/index'),
    //       name: 'ExportZip',
    //       meta: { title: 'Export Zip' }
    //     }
    //   ]
    // },

    // {
    //   path: '/pdf',
    //   component: Layout,
    //   redirect: '/pdf/index',
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/pdf/index'),
    //       name: 'PDF',
    //       meta: { title: 'PDF', icon: 'pdf' }
    //     }
    //   ]
    // },
    // {
    //   path: '/pdf/download',
    //   component: () => import('@/views/pdf/download'),
    //   hidden: true
    // },

    // {
    //   path: '/theme',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/theme/index'),
    //       name: 'Theme',
    //       meta: { title: 'Theme', icon: 'theme' }
    //     }
    //   ]
    // },

    // {
    //   path: '/clipboard',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'index',
    //       component: () => import('@/views/clipboard/index'),
    //       name: 'ClipboardDemo',
    //       meta: { title: 'Clipboard', icon: 'clipboard' }
    //     }
    //   ]
    // },

    // {
    //   path: 'external-link',
    //   component: Layout,
    //   children: [
    //     {
    //       path: 'https://github.com/PanJiaChen/vue-element-admin',
    //       meta: { title: 'External Link', icon: 'link' }
    //     }
    //   ]
    // },

    // 404 page must be placed at the end !!!
    { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
    // mode: 'history', // require service support
    scrollBehavior: () => ({ y: 0 }),
    routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234noRedirectissuecomment-357941465
export function resetRouter() {
    const newRouter = createRouter()
    router.matcher = newRouter.matcher // reset router
}

export default router