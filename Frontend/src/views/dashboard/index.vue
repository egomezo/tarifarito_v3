<template>
  <div class="dashboard-container">
    <component :is="currentRole" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminDashboard from './admin'
import userDashboard from './user'
import defaultDashboard from './default'

export default {
  name: 'Dashboard',
  components: { adminDashboard, userDashboard, defaultDashboard },
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
    } else if (this.roles.includes('user')) {
      this.currentRole = 'userDashboard'
    } else {
      this.currentRole = 'defaultDashboard'
    }
  }
}
</script>
