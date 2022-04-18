<template>
  <div class="dashboard-container">
    <component :is="currentView" />
  </div>
</template>

<script>
import viewHistorico from '../revisor/components/historico'
import viewReportes from '../revisor/components/reportes'

export default {
  name: 'MenuAprobador',
  components: {
    viewHistorico,
    viewReportes
  },
  data() {
    return {
      // currentView: 'defaultDashboard'
    }
  },
  created() {
    const route = this.$route // obtenemos los parametros de la URL
    const tempRoute = Object.assign({}, route) // creamos un objeto de la URL
    const view = tempRoute.fullPath // obtenemos la URL de la vista
    console.log(route)
    console.log(view)
    if (view === '/historico-verificaciones/verificaciones') {
      this.currentView = 'viewHistorico'
    } else if (view === '/reportes-revisor/reportes') {
      this.currentView = 'viewReportes'
    }
  }
}
</script>
