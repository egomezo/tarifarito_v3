<template>
  <div class="dashboard-container">
    <component :is="currentView" />
  </div>
</template>

<script>
import viewCostoUnitario from './components/costo-unitario/index'
import viewd097 from './components/distribucion/d097'
import viewd015 from './components/distribucion/d015'
import viewTarifas from './components/tarifas'
import viewSensibilidad from './components/sensibilidad'
import viewHistorico from './components/historico/index'
import viewReportes from './components/reportes'

export default {
  name: 'MenuRevisor',
  components: {
    viewCostoUnitario,
    viewd097,
    viewd015,
    viewTarifas,
    viewSensibilidad,
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
    if (view === '/verificacion/costo-unitario') {
      this.currentView = 'viewCostoUnitario'
    } else if (view === '/verificacion/componentes/d097') {
      this.currentView = 'viewd097'
    } else if (view === '/verificacion/componentes/d015') {
      this.currentView = 'viewd015'
    } else if (view === '/verificar-tarifas/tarifas') {
      this.currentView = 'viewTarifas'
    } else if (view === '/analisis-sensibilidad/sensibilidad') {
      this.currentView = 'viewSensibilidad'
    } else if (view === '/historico-verificaciones/verificaciones') {
      this.currentView = 'viewHistorico'
    } else if (view === '/reportes-revisor/reportes') {
      this.currentView = 'viewReportes'
    }
  }
}
</script>
