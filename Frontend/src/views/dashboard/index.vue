<template>
  <div class="dashboard-container">
    <component :is="currentRole" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import adminDashboard from './admin'
import editorDashboard from './editor'
import defaultDashboard from './default'

export default {
  name: 'Dashboard',
  components: { adminDashboard, editorDashboard, defaultDashboard },
  data() {
    return {
      // currentRole: 'adminDashboard'
      currentRole: 'defaultDashboard'
    }
  },
  computed: {
    ...mapGetters([
      'roles'
    ])
  },
  created() {
    if (!this.roles.includes('admin')) {
      this.currentRole = 'defaultDashboard'
    }
  }
}
</script>
