<template>
  <div>
    <el-drawer
      ref="drawer"
      :before-close="handleClose"
      :visible.sync="dialogdrawer"
      direction="rtl"
      :destroy-on-close="true"
      custom-class="demo-drawer"
    >
      <div style="background: #f7fbff; height: 100%;">
        <sticky class-name="sub-navbar">
          <el-row>
            <el-col :span="24" style="text-align: center;">
              <label style="font-size: x-large; color: white;">{{ drawertitulo }}</label>
            </el-col>
          </el-row>
        </sticky>

        <!-- Card donde se listan las causas -->

        <div style="border: 0px solid red; width: 100%; height: 75vh; overflow-y: scroll; padding: 0% 5% 5% 5%;">
          <el-card v-for="tercero in dataterceros" :key="tercero.idtercero" style="border: 0px solid blue; width: 100%; padding: 3%; margin-top: 3%;">
            <div slot="header" class="clearfix">
              <span style="color: #606266;"><b>{{ tercero.nombre }}</b></span>
              <div style="float: right;">
                <el-button size="mini" type="danger" icon="el-icon-delete" :disabled="!editar" @click="handleDelete(tercero)" />
              </div>
              <div style="float: right; padding-right: 2%;">
                <el-button style="border: 1px solid #67C23A;" size="mini" type="success" icon="el-icon-edit" :disabled="!editar" @click="handleEdit(tercero)"><b>Editar</b></el-button>
              </div>
            </div>
            <div class="text item">
              <span style="color: #606266;"><b>{{ tercero.persona }}</b></span>
            </div>
            <div class="text item">
              <span style="color: #606266;"><b>Documento: </b></span>{{ tercero.documento }}
            </div>
            <div class="text item">
              <span style="color: #606266;"><b>Dirección: </b></span>{{ tercero.direccion }}
            </div>
            <div class="text item">
              <span style="color: #606266;"><b>e-mail: </b></span>{{ tercero.email }}
            </div>
          </el-card>
        </div>

        <div style="text-align: center; padding-top: 2%;">
          <el-button
            style="border: 1px solid #67c23a"
            type="primary"
            icon="el-icon-circle-plus"
            round
            :disabled="!editar"
            @click="handleAgregar()"
          >Agregar</el-button>
        </div>

      </div>
    </el-drawer>

    <!-- Cuadro de dialogo para agregar / editar tercero -->

    <ModalAgregar
      :modaltitulo="tituloModalItem"
      :modalvisible="dialogVisible"
      :modalform="formItem"
      :domcomponents="domItem"
      :rulesform="rulesFormItem"
      :datamodal="dataFormItem"
      :action="modalAction"
      @confirmar="handleConfirmar"
    />

    <!-- Modal de confirmacion para borrar una tercero -->

    <ModalDelete
      titulo="Advertencia"
      :mensaje="mensajeModalDelete"
      :modalvisible="deleteDialogVisible"
      @confirmar="submitDelete"
    />

  </div>
</template>

<script>
import Sticky from '@/components/Sticky' // 粘性header组件
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import ModalAgregar from '@/components/ModalAgregar'
import ModalDelete from '@/components/ModalConfirm'
import { CONSTANTS } from './constants/constants'
import { createTercero, updateTercero, deleteTercero } from '@/api/procesosDIEG/terceros'

export default {
  name: 'ListaTerceros',
  directives: { elDragDialog },
  components: { Sticky, ModalAgregar, ModalDelete },
  props: {
    dialogdrawer: {
      type: Boolean,
      default: false
    },
    editar: {
      type: Boolean,
      default: false
    },
    idproceso: {
      type: String,
      default: ''
    },
    drawertitulo: {
      type: String,
      default: ''
    },
    recargarlista: {
      type: Boolean,
      default: false
    },
    dataterceros: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      drawervisible: false,
      dialogVisible: false,
      formItem: CONSTANTS.formItem,
      domItem: CONSTANTS.domItem,
      rulesFormItem: CONSTANTS.rulesFormItem,
      dataFormItem: CONSTANTS.dataFormItem,
      tituloModalItem: '',
      modalAction: '',
      mensajeModalDelete: '',
      deleteDialogVisible: false,
      delTercero: ''
    }
  },
  created() {
    this.model = {}
    this.x = window.matchMedia('(max-width: 800px)')
  },
  methods: {
    handleClose() {
      this.$emit('closedrawer', false)
    },
    handleEdit(data) {
      // console.log('Editar --> ', data)
      this.tituloModalItem = 'Editar tercero'
      this.modalAction = 'Editar'
      this.dialogVisible = true
      this.formItem = data
    },
    handleDelete(data) {
      // console.log('Eliminar --> ', data)
      this.delTercero = data.idtercero
      this.mensajeModalDelete = `¿Realmente desea eliminar el tercero <b>${data.nombre}</b>?`
      this.deleteDialogVisible = true
    },
    handleAgregar() {
      // console.log('Agregar')
      this.tituloModalItem = 'Agregar tercero'
      this.modalAction = 'Agregar'
      this.dialogVisible = true
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de [editar / agregar] terceros
      if (modal.action === 'Editar') {
        // console.log(modal)
        // Se realiza la acción de editar tercero
        modal.data.persona = this.dataFormItem.persona.find((persona) => persona.label === modal.data.persona).id
        await updateTercero(modal.data).then(async(response) => {
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Tercero actualizado con éxito',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
          this.textActionTercero = 'Agregar'
        }, (err) => {
          console.log(err)
        })
      } else if (modal.action === 'Agregar') {
        // console.log(modal)
        modal.data.idproceso = parseInt(this.idproceso)
        modal.data.persona = this.dataFormItem.persona.find((persona) => persona.label === modal.data.persona).id
        await createTercero(modal.data).then(async(response) => {
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Tercero agregado con éxito',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
        }, (err) => {
          console.log(err)
          this.$notify({
            title: 'Advertencia',
            message: 'Documento de usuario ya registrado!',
            position: 'bottom-right',
            type: 'warning',
            duration: 2000
          })
        })
        this.$emit('updateView', true)
      }
      this.dialogVisible = false
      this.formItem = {} // Se reinicia el modelo del modal (importante)
      this.$emit('updateView', true)
    },
    async submitDelete(response) {
      // console.log(response)
      if (response) {
        await deleteTercero(this.delTercero).then(async(response) => {
          this.$notify({
            title: 'Información',
            message: 'Se ha eliminado el tercero!',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
          this.$emit('updateView', true)
        })
      }
      this.deleteDialogVisible = false
    }
  }
}
</script>

<style lang="scss" scoped>
  /* width */
  ::-webkit-scrollbar {
    width: 1px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: #f1f1f1;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #888;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
</style>

<style>
  /* Pantallas superiores a 800px (PC) */
  @media screen and (min-width: 800px) {
    .demo-drawer {
      width: 45% !important;
    }
  }

  /* Pantallas inferiores a 800px (mobile) */
  @media screen and (max-width: 800px) {
    .demo-drawer {
      width: 100% !important;
    }
  }

  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 15px;
  }
</style>

