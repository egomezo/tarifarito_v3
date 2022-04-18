<template>
  <div>
    <component :is="currentView" />
  </div>
</template>

<script>
import viewTolerancia from './components/tolerancia'
import viewIndicesDane from './components/indicesDane'
import viewInfoComercial from './components/infoComercial'
import viewResolucion from './components/infoD097/resolucion'
import viewError from './components/infoD097/error'
import viewPerdidas from './components/perdidasSTN'
import viewInfoADD from './components/infoADD'
import {
  getNToleranciaList
} from '@/api/tarifarito/gestor/nTolerancia'

export default {
  name: 'MenuGestor',
  components: {
    viewTolerancia,
    viewIndicesDane,
    viewInfoComercial,
    viewResolucion,
    viewError,
    viewPerdidas,
    viewInfoADD
  },
  data() {
    // this.getListNTolerancia()
    return {
      // currentView: 'defaultDashboard'
      listLoading: true
    }
  },
  created() {
    const route = this.$route // obtenemos los parametros de la URL
    const tempRoute = Object.assign({}, route) // creamos un objeto de la URL
    const view = tempRoute.fullPath // obtenemos la URL de la vista
    // console.log(view)

    if (view === '/tolerancia/nivel-tolerancia') {
      this.currentView = 'viewTolerancia'
    } else if (view === '/indices/indices-dane') {
      this.currentView = 'viewIndicesDane'
    } else if (view === '/comercial/Info-comercial') {
      this.currentView = 'viewInfoComercial'
    } else if (view === '/D097/modificar/resolucion') {
      this.currentView = 'viewResolucion'
    } else if (view === '/D097/modificar/error') {
      this.currentView = 'viewError'
    } else if (view === '/perdidas/perdidas-stn') {
      this.currentView = 'viewPerdidas'
    } else if (view === '/infoADD/info-ADD') {
      this.currentView = 'viewInfoADD'
    }
  },
  methods: {
    async getListNTolerancia() {
      this.listLoading = true
      await getNToleranciaList().then(response => {
        this.list = response
        console.log(this.list)
      })
    }
  }
}
</script>
