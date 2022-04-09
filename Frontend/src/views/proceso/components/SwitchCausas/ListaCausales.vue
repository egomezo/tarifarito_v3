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
          <el-card v-for="causa in datacausal" :key="causa.idcausa" style="border: 0px solid blue; width: 100%; padding: 3%; margin-top: 3%;">
            <div slot="header" class="clearfix">
              <span style="color: #606266;"><b>{{ causa.nombrecausal }}</b></span>
              <div style="float: right;">
                <el-button size="mini" type="danger" icon="el-icon-delete" :disabled="!editar" @click="handleDelete(causa)" />
              </div>
              <div style="float: right; padding-right: 2%;">
                <el-button style="border: 1px solid #67C23A;" size="mini" type="success" icon="el-icon-edit" :disabled="!editar" @click="handleEdit(causa)"><b>Editar</b></el-button>
              </div>
            </div>
            <div class="text item">
              <span style="color: #606266;"><b>Fecha hechos: </b></span>{{ causa.f_hechos | formatDate }}
            </div>
            <div style="border-top: 1px solid #F2F6FC; padding-bottom: 3%;" />
            <div class="text item" style="width: 100%;">
              <span style="color: #606266;"><b>Descripción</b></span><br><br>
              <el-input
                v-model="causa.descripcion"
                type="textarea"
                style="width: 100%;"
                rows="4"
                readonly
              />
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

    <!-- Cuadro de dialogo para agregar / editar causal -->

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

    <!-- Modal de confirmacion para borrar una causal -->

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
import { getListCausal, createCausal, updateCausal, deleteCausal } from '@/api/procesosDIEG/causal'
import moment from 'moment'

export default {
  name: 'ListaCausales',
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
    datacausal: {
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
      delCausal: ''
    }
  },
  created() {
    this.model = {}
    this.x = window.matchMedia('(max-width: 800px)')
    this.getCausales()
  },
  methods: {
    handleClose() {
      this.$emit('closedrawer', false)
    },
    async getCausales() {
      await getListCausal().then((response) => {
        // console.log('this.listaCausal - > ', response)
        this.dataFormItem['idcausal'] = response
      })
    },
    handleEdit(data) {
      // console.log('Editar --> ', data)
      this.tituloModalItem = 'Editar causal'
      this.modalAction = 'Editar'
      this.dialogVisible = true
      data.f_hechos = new Date(moment(data.f_hechos).format('YYYY/MM/DD'))
      this.formItem = data
    },
    handleDelete(data) {
      // console.log('Eliminar --> ', data)
      this.delCausal = { idproceso: data.idproceso, idcausal: data.idcausal, fecha_registro: data.fecha_registro }
      this.mensajeModalDelete = `¿Realmente desea eliminar la causal <b>${data.nombrecausal}</b>?`
      this.deleteDialogVisible = true
    },
    handleAgregar() {
      // console.log('Agregar')
      this.tituloModalItem = 'Agregar causal'
      this.modalAction = 'Agregar'
      this.dialogVisible = true
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de [editar / agregar] etapa
      if (modal.action === 'Editar') {
        // console.log(modal)
        // Se realiza la acción de editar causal
        await updateCausal(modal.data).then(async(response) => {
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Causal actualizada con éxito',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
        }, (err) => {
          console.log(err)
        })
      } else if (modal.action === 'Agregar') {
        // console.log(modal)
        modal.data.idproceso = parseInt(this.idproceso)
        if (!modal.data.hasOwnProperty('descripcion')) {
          modal.data.descripcion = ''
        }
        await createCausal(modal.data).then(async(response) => {
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Causal agregada con éxito',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
        }, (err) => {
          console.log(err)
          this.$notify({
            title: 'Advertencia',
            message: 'No se pudo completar la operación!',
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
        await deleteCausal(this.delCausal).then(async(response) => {
          this.$notify({
            title: 'Información',
            message: 'Se ha eliminado la causal',
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

