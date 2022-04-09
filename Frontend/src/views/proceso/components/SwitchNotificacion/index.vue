<template>
  <el-col :md="24" style="border: 0px solid blue; padding-top: 10px;">
    <el-card>
      <el-row>
        <el-col :md="countNotificaciones > 0 ? 22 : 22">
          <span>{{ title }}</span>
        </el-col>
        <el-col :md="countNotificaciones > 0 ? 0 : 2">
          <el-switch v-show="countNotificaciones > 0 ? false : true" v-model="valSwitch" active-color="#13ce66" />
        </el-col>
        <el-col v-show="countNotificaciones > 0" :md="countNotificaciones > 0 ? 2 : 0">
          <div class="badge-tercero">
            <el-badge :value="countNotificaciones" class="item" type="success">
              <el-link icon="el-icon-message-solid" :underline="false" @click="dialogDrawer = true" />
            </el-badge>
          </div>
        </el-col>
      </el-row>
    </el-card>

    <!-- Cuadro de dialogo para agregar notificación -->

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

    <ListaNotificacion
      drawertitulo="Notificación electrónica"
      :dialogdrawer="dialogDrawer"
      :datanotificacion="notificaciones"
      :editar="editar"
      :idproceso="idproceso"
      @updateView="handleUpdateView"
      @closedrawer="handleClose"
    />
  </el-col>
</template>

<script>
import ModalAgregar from '@/components/ModalAgregar'
import { CONSTANTS } from './constants/constants'
import ListaNotificacion from './ListaNotificacion'
import { getNotificacionProceso, createNotificacion } from '@/api/procesosDIEG/notificacion'

export default {
  directives: { },
  components: { ModalAgregar, ListaNotificacion },
  props: {
    idproceso: {
      type: String,
      required: true
    },
    editar: {
      type: Boolean,
      required: true
    },
    title: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      abogadoEditar: this.editar,
      valSwitch: false,
      switchDisable: false,
      countNotificaciones: 0,
      dialogVisible: false,
      tituloModalItem: '',
      formItem: CONSTANTS.formItem,
      domItem: CONSTANTS.domItem,
      rulesFormItem: CONSTANTS.rulesFormItem,
      dataFormItem: CONSTANTS.dataFormItem,
      modalAction: '',
      dialogDrawer: false,
      notificaciones: []
    }
  },
  watch: {
    valSwitch: {
      deep: true,
      handler(val) {
        // console.log('valSwitch - > ', val)
        if (this.countNotificaciones > 0) {
          this.valSwitch = true
          this.switchDisable = true
        } else {
          this.switchDisable = false
          this.valSwitch = false
          if (!this.dialogDrawer) {
            this.dialogVisible = true
            this.modalAction = 'Agregar'
            this.tituloModalItem = 'Agregar notificación'
          }
        }
      }
    }
  },
  mounted() {
    this.initView()
  },
  methods: {
    async initView() {
      this.getNotificaciones()
    },
    handleUpdateView() {
      this.getNotificaciones()
    },
    async getNotificaciones() { // Actualiza la lista de notificaciones luego de agregar / editar
      await getNotificacionProceso(this.idproceso).then((response) => {
        // console.log('Notificaciones_PROCESO -> ', response)
        this.countNotificaciones = response.length
        if (response.length) {
          this.notificaciones = response
        } else {
          this.dialogDrawer = false
        }
      })
    },
    handleClose(resp) {
      // console.log('cerrar drawer ->> ', resp)
      this.dialogDrawer = resp
      // this.$destroy()
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de [editar / agregar] notificacion
      // console.log(modal)
      if (modal.action === 'Agregar') {
        // console.log(modal)
        modal.data.idproceso = parseInt(this.idproceso)
        const arrayEmails = []
        for (const key in modal.data) { // Creamos el objeto de email's
          if (key.substring(0, 5) === 'email') {
            arrayEmails.push({ prop: key, value: modal.data[key] })
            delete modal.data[key]
          }
        }
        modal.data['email'] = JSON.stringify(arrayEmails)
        await createNotificacion(modal.data).then(async(response) => {
          // console.log('RESPONSE AGREGAR -> ', response)
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Notificación agregada con éxito',
            type: 'success',
            duration: 2000
          })
        })
        this.getNotificaciones()
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
    }
  }
}
</script>
