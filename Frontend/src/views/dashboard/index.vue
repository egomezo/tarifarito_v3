<template>
  <div class="dashboard-container">
    <component :is="currentRole" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminDashboard from './admin'
import abogadoDashboard from './abogado'
import defaultDashboard from './default'

export default {
  name: 'Dashboard',
  components: { adminDashboard, abogadoDashboard, defaultDashboard },
  data() {
    return {
      currentRole: 'defaultDashboard'
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  created() {
    if (this.roles.includes('administrador')) {
      this.currentRole = 'adminDashboard'
    } else if (this.roles.includes('abogado')) {
      this.currentRole = 'abogadoDashboard'
    } else {
      this.currentRole = 'defaultDashboard'
    }
  }
}
</script>
