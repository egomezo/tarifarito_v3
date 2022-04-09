<template>
  <el-dialog
    v-el-drag-dialog
    :visible.sync="modalvisible"
    :before-close="handleCancel"
    :width="x.matches ? '' : '40em'"
    :fullscreen="x.matches ? true : false"
    custom-class="dialog-class"
    :show-close="true"
    :destroy-on-close="true"
    :close-on-click-modal="true"
    :close-on-press-escape="true"
    append-to-body
  >
    <div class="createPost-container">
      <div v-show="x.matches" style="position: fixed; text-align: center; border: 0px solid red; width: 90%; z-index: 10; margin-top: 85vh;">
        <el-button type="danger" icon="el-icon-close" circle size="medium" @click="handleCancel" />
      </div>
      <el-card v-for="item in datacargos" :key="item.numero_cargo" style="margin-top: 1em;">
        <div slot="header" class="clearfix">
          <span><b>Cargo # </b>{{ item.numero_cargo }}</span>
        </div>
        <div class="text item" style="text-align: justify;">
          <p class="keepAll">
            {{ item.cargo }}
          </p>
          <el-alert
            title="Norma infringida"
            type="info"
            :description="item.norma"
            show-icon
            :closable="false"
            class="keepAll"
          />
        </div>
      </el-card>
    </div>
  </el-dialog>
</template>

<script>
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui

export default {
  name: 'ModalCargos',
  directives: { elDragDialog },
  components: {},
  props: {
    modalvisible: {
      type: Boolean,
      default: false
    },
    datacargos: {
      type: Array,
      default: null
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
      this.$emit('closeModalCargos', { response: false })
    }
  }
}
</script>

<style lang="scss">
.keepAll {
  word-break: keep-all;
}
// Pantallas superiores a 800px (PC)
@media screen and (min-width: 800px) {
  .dialog-class {
    border-radius: 10px;
    // margin-top: 4% !important;
  }

  .dialog-class .el-dialog__body {
    padding-top: 10px !important;
  }
}

// Pantallas inferiores a 800px (mobile)
@media screen and (max-width: 800px) {
  .dialog-class .el-dialog__body {
    padding: 0px 20px 10px 20px !important;
  }

  .dialog-class .el-dialog__header {
    display: none;
  }
}
</style>
