<template>
  <el-dialog
    v-el-drag-dialog
    :visible.sync="modalvisible"
    :before-close="handleCancel"
    :width="x.matches ? '' : '75em'"
    :fullscreen="x.matches ? true : false"
    custom-class="dialog-class"
    :show-close="true"
    :destroy-on-close="true"
    :close-on-click-modal="true"
    :close-on-press-escape="true"
    append-to-body
  >
    <div v-loading="srcparam != undefined ? false : true" class="createPost-container pdf-container">
      <embed
        :src="`${srcparam}#page=1&zoom=5%`"
        :height="x.matches ? '100%' : '550vh'"
        width="100%"
      >
    </div>
  </el-dialog>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui

export default {
  name: 'ModalPdf',
  directives: { elDragDialog },
  components: { },
  props: {
    modalvisible: {
      type: Boolean,
      default: false
    },
    srcparam: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      x: '',
      loading: true
    }
  },
  created() {
    this.x = window.matchMedia('(max-width: 800px)')
  },
  methods: {
    handleCancel() {
      this.$emit('closeModalPdf', { response: false })
    }
  }
}
</script>

<style lang="scss">

// Pantallas superiores a 800px (PC)
@media screen and (min-width: 800px) {
  .dialog-class {
    border-radius: 10px;
    margin-top: 4% !important;
  }

  .dialog-class .el-dialog__body {
    padding-top: 10px !important;
  }

  .pdf-container {
    padding: 0px 13px 0px 13px;
  }
}

// Pantallas inferiores a 800px (mobile)
@media screen and (max-width: 800px) {
  .dialog-class .el-dialog__body {
    padding: 0 !important;
  }

  .dialog-class .el-dialog__header {
    display: none;
  }

  .pdf-container {
    border: 1px solid red;
    height: 100vh;
  }
}
</style>
