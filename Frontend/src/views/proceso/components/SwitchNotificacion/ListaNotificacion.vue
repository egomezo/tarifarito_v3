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

        <!-- Card donde se listan las notificaciones -->

        <div style="border: 0px solid red; width: 100%; height: 75vh; overflow-y: scroll; padding: 0% 5% 5% 5%;">
          <el-card v-for="notificacion in datanotificacion" :key="notificacion.idtnotificacion" style="border: 0px solid blue; width: 100%; padding: 3%; margin-top: 3%;">
            <div slot="header" class="clearfix">
              <span style="color: #606266;"><b>{{ notificacion.radicado }}</b></span>
              <div style="float: right;">
                <el-button size="mini" type="danger" icon="el-icon-delete" :disabled="!editar" @click="handleDelete(notificacion)" />
              </div>
              <div style="float: right; padding-right: 2%;">
                <el-button style="border: 1px solid #67C23A;" size="mini" type="success" icon="el-icon-edit" :disabled="!editar" @click="handleEdit(notificacion)"><b>Editar</b></el-button>
              </div>
            </div>
            <div class="text item">
              <span style="color: #606266;"><b>Fecha autorización: </b></span>{{ notificacion.fechaAutorizacion | formatDate }}
            </div>
            <div style="border-top: 1px solid #F2F6FC; padding-bottom: 3%;" />
            <div v-for="(email, index) in JSON.parse(notificacion.correos)" :key="email.prop" class="text item">
              <span style="color: #606266;"><b>Correo{{ index + 1 }}: </b></span>{{ email.value }}
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

    <!-- Cuadro de dialogo para agregar / editar notificacion -->

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

    <!-- Modal de confirmacion para borrar una notificacion -->

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
import { createNotificacion, updateNotificacion, deleteNotificacion } from '@/api/procesosDIEG/notificacion'
import moment from 'moment'

export default {
  name: 'NotificacionProceso',
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
    datanotificacion: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      loadingNotificacion: true,
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
      delNotificaion: ''
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
      this.tituloModalItem = 'Editar notificación'
      this.modalAction = 'Editar'
      this.dialogVisible = true
      data.fechaAutorizacion = new Date(moment(data.fechaAutorizacion).format('YYYY/MM/DD'))
      const emails = JSON.parse(data.correos)
      this.formItem = data
      for (const iterator of emails) {
        // console.log(iterator)
        this.domItem.push({ // Agregamos el control (Input) al DOM
          type: 'email',
          prop: iterator.prop,
          placeholder: 'Ingrese un correo',
          show: true
        })
        // Se agrega la regla del input creado
        this.rulesFormItem[iterator.prop] = [{ type: 'email', required: true, message: 'Ingrese un correo electrónico válido', trigger: 'blur' }]
      }
    },
    handleDelete(data) {
      // console.log('Eliminar --> ', data)
      this.delNotificaion = data.idnotificacion
      this.mensajeModalDelete = `¿Realmente desea eliminar la notificación <b>${data.radicado}</b>?`
      this.deleteDialogVisible = true
    },
    handleAgregar() {
      // console.log('Agregar')
      this.tituloModalItem = 'Agregar notificación'
      this.modalAction = 'Agregar'
      this.dialogVisible = true
    },
    createArrayEmails(data) {
      const arrayEmails = []
      for (const key in data) { // Creamos el objeto de email's
        if (key.substring(0, 5) === 'email') {
          arrayEmails.push({ prop: key, value: data[key] })
          delete data[key]
        }
      }
      return JSON.stringify(arrayEmails)
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de [editar / agregar] etapa
      if (modal.action === 'Editar') {
        // console.log(modal)
        modal.data['email'] = this.createArrayEmails(modal.data)
        // Se realiza la acción de editar notificacion
        await updateNotificacion(modal.data).then(async(response) => {
          // console.log('RESPONSE EDITAR -> ', response)
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Notificación modificada con éxito',
            type: 'success',
            duration: 2000
          })
        })
      } else if (modal.action === 'Agregar') {
        // console.log(modal)
        modal.data.idproceso = parseInt(this.idproceso)
        modal.data['email'] = this.createArrayEmails(modal.data)
        await createNotificacion(modal.data).then(async(response) => {
          // console.log('RESPONSE AGREGAR -> ', response)
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Notificación agregada con éxito',
            type: 'success',
            duration: 2000
          })
        })
        this.$emit('updateView', true)
      }
      this.dialogVisible = false
      this.formItem = {} // Se reinicia el modelo del modal (importante)
      this.domItem.forEach(element => { // Permite reiniciar el arreglo de componentes DOM del modal
        if (element.type === 'email') {
          const posElement = this.domItem.indexOf(element)
          this.domItem.splice(posElement)
        }
      })
      for (const key in this.rulesFormItem) { // Permite reiniciar el objeto de reglas del DOM
        if (key.substring(0, 5) === 'email') {
          delete this.rulesFormItem[key]
        }
      }
      this.$emit('updateView', true)
    },
    async submitDelete(response) {
      // console.log(response)
      if (response) {
        await deleteNotificacion(this.delNotificaion).then(async(response) => {
          this.$notify({
            title: 'Información',
            message: 'Se ha eliminado la notificación',
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
