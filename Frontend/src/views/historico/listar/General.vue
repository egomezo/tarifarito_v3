<template>
  <div class="createPost-container" style="height: 88vh;">
    <TablaHistorico :tablecolumns="columns" :tabledata="data" :tableexpand="expand" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import TablaHistorico from './TablaHistorico'
import { CONSTANTS } from '../constants/constants'

export default {
  name: 'HistoricoGeneral',
  directives: { elDragDialog },
  components: { TablaHistorico },
  data() {
    return {
      loading: true,
      showOnlyAdmin: false,
      columns: CONSTANTS.tableColumnsGeneral,
      expand: CONSTANTS.tableExpandGeneral,
      data: []
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'usuario', 'idusuario', 'dependencia'])
  },
  created() {
    this.initView()
  },
  methods: {
    initView() {
      if (this.roles[0] === 'administrador') {
        this.showOnlyAdmin = true
      }
    },
    clickAgregar() {
      this.$router.push({ path: `/upload/historico/info_general` })
    }
  }
}
</script>

<style lang="scss" scoped>
</style>

<style lang="scss">
</style>
