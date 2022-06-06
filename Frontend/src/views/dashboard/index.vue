<template>
  <div class="dashboard-container">
    <component :is="currentRole" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminDashboard from './admin'
import defaultDashboard from './default'

export default {
  name: 'Dashboard',
  components: { adminDashboard, defaultDashboard },
  data() {
    return {
      currentRole: ''
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  created() {
    if (this.roles.includes('administrador')) {
      // console.log('Dashboard ADMIN role :>> ', this.roles.includes('administrador'))
      this.currentRole = 'adminDashboard'
    } else {
      // console.log('Dashboard OTRO role :>> ', true)
      this.currentRole = 'defaultDashboard'
    }
  }
}
</script>
